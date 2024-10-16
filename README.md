# Django Password Generator 🔐

A simple web-based password generator built using Django and HTMX. This tool allows users to generate secure, random passwords of custom length with a simple, dynamic user interface.


<img src="assets/1.png" alt="drawing" style="width:450px;"/>

<img src="assets/2.png" alt="drawing" style="width:450px;"/>

<img src="assets/4.png" alt="drawing" style="width:450px;"/>

<img src="assets/3.png" alt="drawing" style="width:450px;"/>

## Features 🌟
- Generate random, secure passwords using letters, digits, and special characters.
- Specify custom password types and lengths.
- Dynamic frontend using HTMX for smooth, real-time interactions without full page reloads.
- Easy to install and use locally.


## Installation 🛠️

### Prerequisites
- Python 3.x
- Django 4.x
- A virtual environment (recommended)

### 1. Clone the repository
```bash
git clone https://github.com/code-freq/password-generator.git
cd password-generator
```
### 2. Create a virtual environment
```bash
python -m venv .venv
```
### 3. Activate the virtual environment
- **On Windows:**
    ```bash
    .venv\Scripts\activate
    ```
- **On macOS/Linux:**
    ```bash
    source .venv/bin/activate
    ```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run database migrations
```bash
python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```

Now, open your browser and visit http://127.0.0.1:8000/ to use the password generator!

## Usage 💻

1. Open the app in your browser.
2. Input the desired password length *(default is 8, minimum is 4, and maximum is 128 characters)*.
3. Select password type using checkboxes.
4. Click the "Generate Password" button.
5. Your password will appear instantly, without any page refresh, thanks to HTMX.

## Project Structure 🏗️

```
password-generator/
│
└── passwordgen/              # Main Django project folder
    ├── generator/            # Application (App) folder
    │   ├── migrations/       # Database migrations
    │   ├── templates/        # HTML templates
    │   ├── admin.py          # Django Admin setup
    │   ├── apps.py           # Application configuration
    │   ├── __init__.py       # Python package initializer
    │   ├── models.py         # Database models
    │   ├── tests.py          # Tests
    │   ├── urls.py           # App URLs
    │   └── views.py          # Views (business logic)
    ├── passwordgen/          # Main project configuration
    │   ├── __init__.py       # Python package initializer
    │   ├── asgi.py           # ASGI configuration
    │   ├── settings.py       # Project settings
    │   ├── urls.py           # Main URL configurations
    │   └── wsgi.py           # WSGI configuration
    ├── db.sqlite3            # SQLite database (used for development)
    └── manage.py             # Django management commands

```

## Technologies Used 🚀

- **Django:** Backend framework for handling requests and serving the password generator.
- **HTMX:** JavaScript library to provide dynamic functionality (generating passwords without page reloads).
- **HTML/CSS:** Simple and clean frontend design for ease of use.


## Contributing 🤝

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## Contact 📧

If you have any questions or suggestions, feel free to reach out:

*code.freq7@gmail.com*

GitHub: code-freq
