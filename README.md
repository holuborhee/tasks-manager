# Tasks Manager

Create and Manage your tasks.

## Features

* [x] CRUD for tasks on the backend
* [x] Add, Edit, and Delete using AJAX on the frontend
* [x] Fetch and Display with Jquery and Tailwind on the Client Side
* [x] Search by task title
* [x] Filter by Assigned User
* [x] Sort my priority
* [ ] drag-and-drop functionality to change the status of tasks
* [ ] User Authentication and Authorization
* [ ] Validation on Client Side and Server side

## Prerequisites

Before you can run this project, you need to make sure you have the following software installed on your machine:

- Python (version 3.12.4)
- pip (Python package manager)
- virtualenv (Python virtual environment manager)

## Getting Started

1. Clone this repository to your local machine using the following command: `git clone https://github.com/holuborhee/tasks-manager.git`
2. Create a virtual environment for this project using the following command: `cd your-repo virtualenv venv`
3. Activate the virtual environment using the following command:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

4. Install the required Python packages using the following command: `pip install -r requirements.txt`

6. Apply the database migrations using the following command: `python manage.py migrate`

7. Create a superuser account using the following command: `python manage.py createsuperuser`

Follow the prompts to enter your desired username, email address, and password.

8. Start the Django development server using the following command: `python manage.py runserver`

9. Open your web browser and go to `http://127.0.0.1:8000/` to view the project.

10. To create more users, you can visit `http://127.0.0.1:8000/admin` and login with the username and password you created on **Step 7**
