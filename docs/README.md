
# eoy Directory Services

## Overview
eOY Directory Services is an enterprise-grade, AI-powered directory management solution, providing enhanced capabilities over traditional Active Directory. This service is designed to help organizations streamline user, group, and role management, and integrates AI-powered anomaly detection and role recommendations for optimal security and user experience.

## Features
- **User Management**: Secure, scalable, and customizable management of user accounts and access permissions.
- **Group Management**: Create and manage user groups with flexible policies and role assignments.
- **Role Recommendation**: AI-driven recommendations to suggest user roles based on behavior and access patterns.
- **Anomaly Detection**: Detect anomalous activities in real-time to enhance security.
- **Compliance Management**: Ensure compliance with data protection regulations and internal policies.
- **AI-Powered Insights**: Leveraging machine learning algorithms for better security, access management, and workflow automation.

## Architecture
The project consists of the following components:
- **Backend**: Provides API endpoints, services for user and group management, anomaly detection, role recommendations, and more.
- **Frontend**: User interface built using modern web technologies for interaction with the directory services.
- **Docker**: The project uses Docker for containerization, making it easy to deploy in various environments.
- **Database**: Stores user data, logs, group information, and role assignments.
  
The project leverages technologies like Python, Flask, Node.js, and Docker for seamless performance.

## Installation

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mishesbone/eoy_directory_services_app.git
   ```

2. Navigate to the backend directory:
   ```bash
   cd eoy_directory_services_app/backend
   ```

3. Set up a virtual environment:
   ```bash
   python -m venv ad_env
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\ad_env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source ad_env/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the backend:
   ```bash
   python main.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Run the frontend:
   ```bash
   npm start
   ```

## Docker Deployment

To deploy the project using Docker, you can use the following steps:

1. Ensure Docker is installed on your system.
2. From the root directory, run:
   ```bash
   docker-compose up --build
   ```
   This will build and start the backend and frontend containers.

## Usage

Once the system is set up, you can use the following:

- Access the backend API at `http://localhost:5000`.
- Use the frontend UI at `http://localhost:3000` for user and group management.

## Contributing

If you'd like to contribute to this project, please fork the repository, create a new branch, and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact:
- **Name**: Fwangshak Sabar Mishwatts
- **Email**: itsmishesbone@gmail.com
```

### Key Sections:

1. **Overview**: Describes the project in a concise way.
2. **Features**: Lists the key functionalities of the project.
3. **Architecture**: Gives a high-level explanation of the system structure.
4. **Installation**: Provides the steps to set up the backend and frontend.
5. **Docker Deployment**: Details on running the project with Docker.
6. **Usage**: How to interact with the application after setup.
7. **Contributing**: Instructions for developers who want to contribute to the project.
8. **License**: Indicates the licensing of the project (you can change the license as per your preference).
9. **Contact**: Information for reaching out for support or inquiries.

