import numpy as np
from sklearn.ensemble import IsolationForest
from sqlalchemy.orm import Session
from backend.api.models.user import User

class AnomalyDetectionService:
    def __init__(self):
        # Initialize the Isolation Forest model for anomaly detection
        self.model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
        self.trained = False

    def train_model(self, data: np.ndarray):
        """
        Train the Isolation Forest model on user activity data.

        Args:
            data (np.ndarray): A 2D array where rows represent user activity features.
        """
        self.model.fit(data)
        self.trained = True

    def detect_anomalies(self, data: np.ndarray):
        """
        Detect anomalies in the provided data.

        Args:
            data (np.ndarray): A 2D array of user activity features.

        Returns:
            np.ndarray: An array of anomaly scores (-1 indicates anomaly).
        """
        if not self.trained:
            raise ValueError("The model has not been trained yet.")
        return self.model.predict(data)

    def get_user_activity_data(self, db: Session):
        """
        Extract user activity data from the database for training.

        Args:
            db (Session): SQLAlchemy session object.

        Returns:
            np.ndarray: A 2D array of user activity features.
        """
        users = db.query(User).all()
        # Example: Convert user data into numerical features
        data = [
            [
                user.id,
                len(user.username),
                int(user.is_active),
                int(user.is_admin),
            ]
            for user in users
        ]
        return np.array(data)

    def train_from_db(self, db: Session):
        """
        Train the model using data extracted from the database.

        Args:
            db (Session): SQLAlchemy session object.
        """
        data = self.get_user_activity_data(db)
        self.train_model(data)
