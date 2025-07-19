# 🌍 Tourist Hub

> A web platform where tourists and guides connect, share travel experiences, and explore destinations together.

---

## 📌 Overview

**Tourist Hub** is a Django-based web application that enables tourists to discover local guides, read travel blogs, and share personal journeys. Guides can showcase their profiles and connect with travelers for opportunities.

---

## 💻 Tech Stack

| Layer           | Technology                         |
|----------------|-------------------------------------|
| Language        | Python 3.x, HTML, CSS, JavaScript  |
| Backend         | Django (MVC Architecture)          |
| Frontend        | Django Templates, Bootstrap        |
| Database        | SQLite (for development)           |
| Version Control | Git & GitHub                       |
| Deployment      | Heroku / Any WSGI-compatible host  |

---

## 📁 Project Structure

```
tourist-hub/
├── accounts/          # User registration, login, profile
├── guide/             # Guide-specific views and models
├── blog/              # Blog creation and display
├── home/              # Landing page and general views
├── arts/              # Art showcase section
├── media/             # Uploaded images and files
├── static/            # CSS, JS, images
├── templates/         # HTML templates
├── db.sqlite3         # SQLite database (default)
├── manage.py          # Django project manager
└── requirements.txt   # Dependency list
```

---

## 🚀 Features

- Role-based login for **Tourists** and **Guides**
- Create and view **Travel Blogs**
- Upload and explore **Artworks**
- Search and filter guides
- Profile management
- Secure authentication system
- Admin dashboard for superuser

---

## ⚙️ Setup Instructions

### Clone the repository

```bash
git clone https://github.com/SerialGuy/tourist-hub.git
cd tourist-hub
```

### Create a virtual environment

```bash
python -m venv venv
# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a superuser (admin login)

```bash
python manage.py createsuperuser
```

### Run the development server

```bash
python manage.py runserver
```

Access the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Usage Guide

- Tourists can:
  - Register and log in
  - Browse and search for guides
  - Read and create blog posts
  - View artwork shared by others

- Guides can:
  - Create a guide profile
  - Manage their listings
  - Post blogs and share media

- Admin can:
  - Access [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
  - Use superuser credentials to manage all models

---

## ☁️ Deployment (Heroku Example)

If you want to deploy on Heroku:

```bash
heroku login
heroku create tourist-hub-app
git push heroku main
heroku run python manage.py migrate
heroku open
```

---

## 📝 License

This project is licensed under the MIT License - feel free to modify and use for your own projects.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📫 Contact

For any queries, contact: **[SerialGuy](https://github.com/SerialGuy)**
