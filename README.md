# Avionics Status Board

## Overview
The **Avionics Status Board** is a web-based platform designed for avionics technicians and leads to manage and track the status of work on aircraft. The system enables users to assign tasks, update progress, manage permissions, and document turnovers efficiently.

## Features
- **User Authentication**: Custom user model with role-based access (Leads & Avionics Techs).
- **Work Management**: View, assign, and track work status for aircraft.
- **Software Status Tracking**: Separate software work table with status updates.
- **Turnovers**: Leads can perform turnovers for shift handovers.
- **Permissions & Roles**:
  - Leads: Can assign work, approve users, manage roles, perform turnovers, update/archive/delete work.
  - Avionics Technicians: Can comment, update work status, and sign off completed tasks.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Frontend**: React, Material UI
- **Database**: PostgreSQL
- **Authentication**: Django Guardian for role-based permissions

## Entity-Relationship Diagram (ERD)
![ERD](docs/erd.png)

## Wireframes
![Wireframe](docs/wireframe.png)

## Installation & Setup

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/rSchleckser/avionics-status-board.git
   cd avionics-status-board
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
(Frontend setup instructions to be added once React development begins)

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login/` | User login |
| POST | `/api/auth/signup/` | User registration |
| POST | `/api/auth/logout/` | User logout |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/users/` | Get all users |
| GET | `/api/users/{id}/` | Get user details |
| PATCH | `/api/users/{id}/` | Update user |

### Work Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/work/` | List all work items |
| POST | `/api/work/` | Create a work item |
| PATCH | `/api/work/{id}/` | Update a work item |
| DELETE | `/api/work/{id}/` | Delete a work item |

## Contribution Guidelines
- Fork the repository and create a feature branch.
- Follow PEP 8 coding standards.
- Submit a pull request with a detailed description of changes.

## License
MIT License

## Contact
For any inquiries, contact rickyschleckser@gmail.com.

