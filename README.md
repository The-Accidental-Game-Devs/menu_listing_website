# Menu Listing Website

---

## Description

This project is an open-source website built with **Django and Bootstrap**, designed to be flexible and user-friendly. It provides all the core features you need to manage your online menu listing efficiently.

---

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)
- [Contact](#contact)

---

## Features

### Customer-Facing Features

These features enhance the Browse experience for your customers:

-   [🚧 In Progress] **Special Item Display**: Prominently showcase unique or popular dishes directly on the homepage, making it easy for customers to spot your specialties.
-   [🚧 In Progress] **Intuitive Menu Browse**: Customers can effortlessly search and filter menu items by category, making their Browse experience seamless and helping them quickly find what they're looking for.

### Admin & Staff Features

These features empower administrators and staff to manage the menu efficiently:

-   [🚧 In Progress] **Comprehensive Item Management**: Add, edit, delete, view, and search menu items. Staff can also categorize items for better organization and customer navigation.
-   [🚧 In Progress] **Streamlined Category Management**: Create, update, delete, view, and search menu categories with ease. This helps keep your menu structured and simple for both management and your customers.

---

### Requirements

* **Python**: 3.13.3 or higher (or compatible with Django's latest versions)
* **Pip**: Ensure you have a recent version of pip installed.

---

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/The-Accidental-Game-Devs/menu_listing_website.git
    ```
2.  **Navigate to the project directory**:
    ```bash
    cd menu_listing_website
    ```
3.  **Create a Python virtual environment (recommended)**:
    ```bash
    python -m venv .venv # For Windows
    python3 -m venv .venv  # For Linux/macOS
    ```
4.  **Activate the virtual environment**:
    ```bash
    source .venv/bin/activate # For Linux/macOS
    .venv\Scripts\activate # For Windows
    ```
5.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
6.  **Create a `.env` file**:
    This file will store your environment variables, including sensitive data like your `SECRET_KEY`.
    ```bash
    nano .env  # For Linux/macOS, or use any text editor
    ```
7.  **Add your Django `SECRET_KEY`**:
    Paste the following line into your `.env` file. **Replace `YourStrongUniqueSecretKey` with a truly unique and complex key.**
    ```bash
    SECRET_KEY='YourStrongUniqueSecretKey'
    ```
    You can generate a strong key using Python:
    ```bash
    python -c "import secrets; print(secrets.token_urlsafe())"
    ```
    **Important**: Never commit your `.env` file or actual `SECRET_KEY` to version control!
8.  **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```
9.  **Create a superuser (for admin access)**:
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to enter your desired username, email, and password.
10. **Run the development server locally**:
    ```bash
    python manage.py runserver
    ```
    You can now access the website at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

---

## License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.

---

## Contact

For support, please reach out to [aung.lin.thant.address@gmail.com](mailto:aung.lin.thant.address@gmail.com).

---

**Note**: This project is under active development, and some features are still being built. Check the status in the features section for up-to-date progress.