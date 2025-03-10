# Django Task Manager

A simple Django-based task manager application that demonstrates CRUD operations, admin integration, and basic REST API setup for future expansion.

## Features

- Create, read, update, and delete tasks.
- Built with Django's class-based generic views.
- Admin panel integration.
- Configured for VS Code with debugging and task running.
- Future enhancements: User authentication, REST API, and deployment instructions.

## Installation

### Prerequisites

- Python 3.x
- MacPorts (for managing Python installations on macOS)
- Virtualenv

### Steps

1. **Clone the repository:**

   git clone https://github.com/yugeshmkumar/django-task-manager
   cd django-task-manager

2. **Set Up a Virtual Environment:**

   python3 -m venv venv
   source venv/bin/activate

3. **Install Dependencies:**

   pip install django

4. **Apply Migrations:**

   python manage.py migrate

5. **Create a Superuser:**

   python manage.py createsuperuser

6. **Run the Development Server:**

   python manage.py runserver

7. **Access the Application:**

   Visit http://127.0.0.1:8000/ for the main page.
   Visit http://127.0.0.1:8000/admin for the admin interface.

## VS Code Setup
The project is configured to work well with VS Code:

- launch.json is set up for debugging with Django.
- tasks.json is provided for running migrations.
- settings.json ensures that VS Code uses your virtual environment's Python interpreter and auto-formats your code on save.

## For additional VS Code extensions, consider installing:

- GitLens
- Bracket Pair Colorizer

## Contributing
Feel free to fork this repository and submit pull requests for improvements or additional features.

## License
MIT License

