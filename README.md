
# eOY Directory Services

## Project Overview
eOY Directory Services is an enterprise-grade, AI-powered directory management solution designed to enhance traditional Active Directory capabilities. It allows for streamlined management of users, groups, and roles, with integrated AI-powered anomaly detection, role recommendations, and compliance management features to improve organizational security and efficiency.

## Features
- **User Management**: Secure, scalable management of user accounts, roles, and permissions.
- **Group Management**: Create and manage user groups with flexible policies and role assignments.
- **Role Recommendation**: AI-powered role suggestions based on user activities and access patterns.
- **Anomaly Detection**: Real-time anomaly detection to identify suspicious user activities.
- **Compliance Management**: Automated compliance reporting to meet regulatory standards.
- **Scalability**: Designed for scalability to handle large enterprise environments.

## Architecture

The system is composed of the following components:

1. **Backend (API)**:
   - Built using Flask, providing RESTful APIs for user management, group management, anomaly detection, and more.
   
2. **Frontend**:
   - Built with modern JavaScript frameworks to provide a user-friendly interface for administrators and users to interact with the directory services.

3. **Database**:
   - Stores user data, logs, group information, and role assignments.
   
4. **AI Integration**:
   - Leveraging machine learning models for anomaly detection and role recommendations.

5. **Docker**:
   - The project is containerized with Docker for easy deployment and scalability.

## Project Structure

Here is the general structure of the project:


## Installation and Setup

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mishesbone/eoy_directory_services_app.git
   ```

2. Navigate to the backend directory:
  
   cd eoy_directory_services_app/backend


3. Create a virtual environment:
   
   python -m venv ad_env


4. Activate the virtual environment:
   - On Windows:
   
     .\ad_env\Scripts\activate

   - On macOS/Linux:
   
     source ad_env/bin/activate
   

5. Install the required dependencies:

   pip install -r requirements.txt


6. Run the backend server:
   
   python main.py
  
### Frontend Setup

1. Navigate to the frontend directory:

   cd ../frontend
  

2. Install Node.js dependencies:
  
   npm install


3. Start the frontend:
   
   npm start
 

## Running with Docker

To deploy the entire application using Docker, follow these steps:

1. Make sure Docker is installed on your machine.

2. From the root directory, run:
  
   docker-compose up --build


3. Access the application:
   - Backend API: `http://localhost:5000`
   - Frontend UI: `http://localhost:3000`

## Usage

Once the system is set up, you can use it for:

- Managing user accounts and permissions.
- Organizing users into groups and managing roles.
- Receiving AI-powered role recommendations based on user behavior.
- Detecting anomalies in user activities.
- Ensuring compliance with relevant security regulations.

## Contributing

We welcome contributions to improve eOY Directory Services. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Commit your changes.
5. Push your changes to your fork.
6. Create a pull request for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact:
- **Name**: Fwangshak Sabar Mishwatts
- **Email**: itsmishesbone@gmail.com


### Key Sections of the README:

- **Project Overview**: Provides a brief description of what the project does.
- **Features**: Lists the core features of the eOY Directory Services.
- **Architecture**: Describes the different components of the project.
- **Project Structure**: Provides a high-level view of the project's directory layout.
- **Installation and Setup**: Details the steps to set up both the backend and frontend.
- **Docker Setup**: Explains how to run the entire project with Docker.
- **Usage**: Describes how to interact with the deployed system.
- **Contributing**: Outlines the steps for contributing to the project.
- **License**: Indicates the licensing of the project (you can update the license type if needed).
- **Contact**: Provides contact information for further inquiries.

