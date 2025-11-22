# To-Do List App

Minimalistik va qulay To-Do List web-ilovasi. Django yordamida qurilgan bo‘lib, foydalanuvchilarga vazifalarni yaratish, tahrirlash va o‘chirish imkoniyatini beradi.

![Status](https://img.shields.io/badge/STATUS-ACTIVE-success)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-3.x%2F4.x-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## ⭐ Features

- Vazifalarni qo‘shish
- Vazifalarni tahrirlash
- Vazifalarni o‘chirish
- 24 soatlik vaqt formati
- Bootstrap UI
- Toza va sodda CRUD amaliyotlari

---

## 📂 Project Structure

to-do-list-app1/
│── app/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ │ ├── home.html
│ │ └── create_post.html
│── manage.py


---


---

## 🧩 Installation

### 1. Repository’ni yuklab oling

git clone https://github.com/username/to-do-list-app1.git
cd to-do-list-app1

2. Virtual environment yaratish

python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

3. Kutubxonalarni o‘rnatish

pip install django

4. Migratsiya qilish

python manage.py migrate

5. Serverni ishga tushirish

python manage.py runserver

