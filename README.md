SmartRoom – Meeting Room Booking System

 1. 📘 Project Title & Description  
SmartRoom is a web-based application that enables efficient booking of meeting rooms. It prevents scheduling conflicts, offers user and admin dashboards, and ensures a smooth room reservation experience.

 2. 👥 Team Details  
Team Name: CodeCrafters  
Members:  
- Sumit Gupta – sumitgupta2436@gmail.com
- Affifa Shaikh – afifamdshaikh123@gmail.com

 3. 🛠️ Tech Stack  
- Languages: Python, HTML, CSS  
- Frameworks: Django, Bootstrap  
- Database: MySQL  
- Tools: Git, GitHub, VS Code

 4. 🧾 Project Description  
SmartRoom provides functionalities like user registration, login, room availability check, conflict-free booking, and an admin panel for managing rooms and bookings. It is designed for simplicity and efficiency in organizational settings.

 5. ⚙️ Setup Instructions  
 Clone the repository
bash
git clone https://github.com/sug9987/SmartRoom.git
cd SmartRoom

 Create a virtual environment and install dependencies
bash
python -m venv env
env\Scripts\activate  # On Windows
pip install -r requirements.txt

 MySQL Configuration:
1. Install MySQL and create a database:
sql
CREATE DATABASE smartroom_db;

2. Update your `settings.py`:
python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smartroom_db',
        'USER': 'root’, # your username
        'PASSWORD': 'root', # your password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

3. Run the migrations and start the server:
bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Access the app at: `http://127.0.0.1:8000/`



 6. 🚀 Usage Guide
 ➤ Admin Login
 Username: `admin`
 Password: `admin124`
 ➤ Sample User Login
 Username: `Affifa`
 Password: `Sumit123`
 ➤ Features:
 User login/register and room booking.
 Admin can add new rooms and view all bookings.
 Users can check room availability.
 Simple and conflict-free booking system.

 7. 🧩 API Endpoints / Architecture
/                  - Landing page  
/login/            - User login  
/logout/           - User logout  
/register/         - Register a new user  
/book-room/        - Booking form for users  
/add-room/         - Admin can add a new room  
/admin-dashboard/  - Admin dashboard and control panel  

 8. 📸 Screenshots (Optional)
