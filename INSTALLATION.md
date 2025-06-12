# Installation Guide for Menu Listing Website

This document provides step-by-step instructions to get the Menu Listing Website project up and running on your local machine for development purposes.

---

## Table of Contents

- [Requirements](#requirements)
- [Installation Steps](#installation-steps)
- [Accessing the Website](#accessing-the-website)

---

## Requirements

To run this project, you'll need:

* **Python**: 3.13.3 or higher (or compatible with Django's latest versions).
* **Pip**: Ensure you have a recent version of pip installed.

---

## Installation Steps

1.  **Clone the repository**:
    Start by cloning the project's repository to your local machine:
    ```bash
    git clone [https://github.com/The-Accidental-Game-Devs/menu_listing_website.git](https://github.com/The-Accidental-Game-Devs/menu_listing_website.git)
    ```

2.  **Navigate to the project directory**:
    Change your current directory to the newly cloned project folder:
    ```bash
    cd menu_listing_website
    ```

3.  **Create a Python virtual environment (recommended)**:
    It's best practice to use a virtual environment to manage project dependencies separately from your system's Python packages.
    ```bash
    python -m venv .venv # For Windows
    python3 -m venv .venv  # For Linux/macOS
    ```

4.  **Activate the virtual environment**:
    Activate the virtual environment to ensure all packages are installed within it:
    ```bash
    source .venv/bin/activate # For Linux/macOS
    .venv\Scripts\activate # For Windows
    ```

5.  **Install dependencies**:
    Install all required Python packages listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

6.  **Create a `.env` file**:
    This file will store your environment variables, including sensitive data like your Django `SECRET_KEY`. Create it in the project root:
    ```bash
    nano .env  # For Linux/macOS, or use any text editor like VS Code
    ```

7.  **Add your Django `SECRET_KEY`**:
    Paste the following line into your `.env` file. **Replace `YourStrongUniqueSecretKey` with a truly unique and complex key.** This key is critical for security.
    ```bash
    SECRET_KEY='YourStrongUniqueSecretKey'
    ```
    You can generate a strong key using Python:
    ```bash
    python -c "import secrets; print(secrets.token_urlsafe())"
    ```
    **Important**: Never commit your `.env` file or actual `SECRET_KEY` to version control! Add `.env` to your `.gitignore` file if it's not already there.

8.  **Apply database migrations**:
    Set up the database schema by applying Django's migrations:
    ```bash
    python manage.py migrate
    ```

9.  **Create a superuser (for admin access)**:
    You'll need a superuser account to access the Django administration panel and manage your menu.
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to enter your desired username, email address, and password.

---

## Accessing the Website

After completing the installation steps, you can run the server locally:

```bash
python manage.py runserver
```