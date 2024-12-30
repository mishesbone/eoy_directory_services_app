from sklearn.cluster import KMeans
import numpy as np
from sqlalchemy.orm import Session
from backend.api.models.user import User
from backend.api.models.role import Role

class RoleRecommendationService:
    def __init__(self, n_clusters: int = 3):
        """
        Initialize the RoleRecommendationService.

        Args:
            n_clusters (int): Number of clusters for the K-Means algorithm.
        """
        self.n_clusters = n_clusters
        self.model = KMeans(n_clusters=n_clusters, random_state=42)
        self.trained = False

    def train_model(self, data: np.ndarray):
        """
        Train the K-Means model on user data.

        Args:
            data (np.ndarray): A 2D array of user activity and skill features.
        """
        self.model.fit(data)
        self.trained = True

    def recommend_roles(self, data: np.ndarray):
        """
        Recommend roles for users based on their data.

        Args:
            data (np.ndarray): A 2D array of user features.

        Returns:
            list: List of cluster labels (role groups) for each user.
        """
        if not self.trained:
            raise ValueError("The model has not been trained yet.")
        return self.model.predict(data)

    def get_user_feature_data(self, db: Session):
        """
        Extract user feature data from the database.

        Args:
            db (Session): SQLAlchemy session object.

        Returns:
            np.ndarray: A 2D array of user features for clustering.
        """
        users = db.query(User).all()
        # Example: Convert user attributes to numerical features
        data = [
            [
                len(user.username),  # Length of username
                int(user.is_active),  # Active status
                user.login_count,  # Number of logins
                user.task_completion_rate,  # Task completion rate
            ]
            for user in users
        ]
        return np.array(data)

    def map_roles_to_clusters(self, db: Session):
        """
        Map clusters to roles in the database.

        Args:
            db (Session): SQLAlchemy session object.
        """
        roles = db.query(Role).all()
        cluster_roles = {i: role.name for i, role in enumerate(roles)}
        return cluster_roles

    def train_from_db(self, db: Session):
        """
        Train the model using data extracted from the database.

        Args:
            db (Session): SQLAlchemy session object.
        """
        data = self.get_user_feature_data(db)
        self.train_model(data)

    def assign_roles(self, db: Session):
        """
        Assign recommended roles to users in the database.

        Args:
            db (Session): SQLAlchemy session object.
        """
        user_data = self.get_user_feature_data(db)
        cluster_labels = self.recommend_roles(user_data)
        cluster_roles = self.map_roles_to_clusters(db)

        users = db.query(User).all()
        for user, cluster in zip(users, cluster_labels):
            user.recommended_role = cluster_roles.get(cluster, "Unassigned")
            db.add(user)
        db.commit()
