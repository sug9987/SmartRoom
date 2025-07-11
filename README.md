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

 8. 📸 Screenshots
    Landing Page
   <img width="1916" height="972" alt="image" src="https://github.com/user-attachments/assets/79b2184c-9136-454c-8bae-a66cd3ffc5b1" />
   
   <img width="1722" height="659" alt="image" src="https://github.com/user-attachments/assets/f2413ee7-4774-41ef-a7a4-e2094dc4ebec" />
   
   <img width="1890" height="697" alt="image" src="https://github.com/user-attachments/assets/14475434-1dad-473e-b6a4-b749d34dfbdf" />
   
   <img width="1884" height="874" alt="image" src="https://github.com/user-attachments/assets/ca27520f-c3c2-45e2-a7ae-856995f06786" />


Login Page
<img width="1910" height="964" alt="image" src="https://github.com/user-attachments/assets/d2e634e2-24b8-4ee5-aaf5-42f8e2c6adc2" />


Registration Page
<img width="1017" height="887" alt="image" src="https://github.com/user-attachments/assets/e2d0cace-0c1e-494a-b4d0-7e5d0a843fcf" />


User Dashboard / Booking Form
<img width="1909" height="604" alt="image" src="https://github.com/user-attachments/assets/5e8037e1-2fcf-4186-a829-fc02b074f067" />

<img width="1872" height="969" alt="image" src="https://github.com/user-attachments/assets/8602324d-f18a-43b6-91b3-be7a2ed36710" />



Admin Dashboard
<img width="1918" height="969" alt="image" src="https://github.com/user-attachments/assets/a31069db-be39-46f4-96a0-3928f1c19afc" />

<img width="1856" height="813" alt="image" src="https://github.com/user-attachments/assets/2897004e-22f4-4be7-a1f2-df1e92dbede2" />

<img width="1887" height="391" alt="image" src="https://github.com/user-attachments/assets/1f3f70d0-933a-4cd7-b471-508f493877b1" />

<img width="907" height="854" alt="image" src="https://github.com/user-attachments/assets/c665e362-4374-4128-b0c8-cd2f810449d9" />

<img width="784" height="332" alt="image" src="https://github.com/user-attachments/assets/5e12a42a-a760-4bb8-b944-dada6efd65d4" />





Room Booking Confirmation / Booking List
<img width="1910" height="973" alt="image" src="https://github.com/user-attachments/assets/4bd38c71-9450-4bd3-9c27-0edfec065541" />

<img width="1919" height="552" alt="image" src="https://github.com/user-attachments/assets/9a3914bd-a9e3-4c85-98b0-a3181184725b" />



