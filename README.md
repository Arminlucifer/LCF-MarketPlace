# 🛒 LCF MarketPlace

> A modern, modular, and scalable e-commerce marketplace built with Django.

## 🌟 About The Project
LCF MarketPlace is a dynamic web application designed to connect buyers and sellers. Users can browse various product categories, search for specific items, and seamlessly post their own products for sale. The project focuses on a clean user interface (Dark Mode), robust backend architecture, and a scalable database design.

### 🚀 Key Features (Currently Implemented)
 Custom Authentication System: Implemented a robust Custom User Model (`account.User`) handling avatars, roles, and profiles.
 *Modular Architecture: The project is divided into distinct, maintainable applications (`account`, `base`, `lcfshop`).
 *Dynamic Sidebar & Categories: Utilized Django Context Processors to inject category data globally across all templates without redundant queries.
 *Smart Search: Real-time search functionality integrated directly into the navigation bar.
 *Flash Messaging: Integrated Django Messages framework to provide users with immediate feedback (success/error alerts).
 *Responsive UI: Built with Bootstrap 5, featuring an elegant dark theme, OwlCarousel for sliders, and FontAwesome icons.

## 🛠️ Built With
 *Backend: Django 6.0.3, Python 3.x
 *Database: PostgreSQL (Ready for production scaling)
 *Frontend: HTML5, CSS3, Bootstrap 5, jQuery
 *Architecture: MVT (Model-View-Template)

## ⚙️ Local Setup & Installation

Follow these steps to get the project running on your local machine.

### Prerequisites
 Python 3.10+
* PostgreSQL server running locally


## Activate the virtual environment:

env\Scripts\activate

## Run migrations:
python manage.py makemigrations
python manage.py migrate

## Create a superuser (Optional but recommended):
python manage.py createsuperuser

## Run the development server:
python manage.py runserver

The project should now be accessible at http://127.0.0.1:8000/.

-------------

## Project Structure
env/: Python virtual environment.
lcf_marketplace/: Main Django project settings directory.
base/: Core application for products, comments, etc.
account/: Application for user authentication and management.
templates/: HTML templates.
static/: Static files (CSS, JS, Images).



##Current Features
Displaying a list of products on the homepage (/).
Product search by name, category, and seller.
Product detail view with comments (/product/<uuid:id>/).
Liking comments.
Adding a new comment
Posting new ads (/post_ad/).
Editing and deleting ads (for owner or admin).
User authentication (signup and login).



###Future Features / Roadmap
Real-time Chat Room
Advanced Admin Panel
Seller Profile Page
Shopping Cart
Notification System
And more…

-------------------------
Important Notes
For file uploads (product images, etc.), ensure MEDIA_ROOT and MEDIA_URL settings in settings.py are correctly configured.
To utilize authentication features, the urls.py and views.py for the account application should be fully implemented.

Refer to the Django documentation and relevant code sections for more detailed information
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
