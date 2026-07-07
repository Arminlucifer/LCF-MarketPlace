# 🛒 LCF MarketPlace

> A modern, modular, and scalable e-commerce marketplace project built with Django and Django REST Framework.

## 🌟 About The Project

LCF MarketPlace is a dynamic web application designed to connect buyers and sellers. Users can browse various product categories, search for specific items, and seamlessly post their own products for sale. The project focuses on a clean user interface (Dark Mode), robust backend architecture, and a scalable containerized database design utilizing PostgreSQL.

### 🚀 Key Features (Currently Implemented)

- **Custom Authentication System:** Implemented a robust Custom User Model (`account.User`) handling avatars, roles, and profiles.
- **RESTful API Architecture:** Powered by **Django REST Framework (DRF)** with clean serializers and endpoint routing for frontend/mobile integration.
- **Full Containerization:** Fully dockerized development environment ensuring "it works on my machine" consistency across all platforms.
- **Modular Architecture:** The project is divided into distinct, maintainable applications (`account`, `base`, `lcfshop`).
- **Dynamic Sidebar & Categories:** Utilized Django Context Processors to inject category data globally across all templates without redundant queries.
- **Smart Search:** Real-time search functionality integrated directly into the navigation bar.
- **Flash Messaging:** Integrated Django Messages framework to provide users with immediate feedback (success/error alerts).
- **Responsive UI:** Built with Bootstrap 5, featuring an elegant dark theme, OwlCarousel for sliders, and FontAwesome icons.

## 🛠️ Built With

- **Backend:** Django 6.0.3, Python 3.x, Django REST Framework (DRF)
- **Containerization:** Docker & Docker Compose
- **Database:** PostgreSQL (Persistent via Docker Volumes)
- **Frontend:** HTML5, CSS3, Bootstrap 5, jQuery
- **Architecture:** MVT (Model-View-Template) & REST API

---

## ⚙️ Local Setup & Installation

You can run this project locally using either **Docker** (Recommended) or the **Traditional Setup**.

### Option 1: The Docker Way (Recommended 🚀)

Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd lcfshop
   Build and run the containers:
   This command automatically pulls the Python and PostgreSQL images, sets up the network, and starts the servers.
   ```

Bash
docker-compose up --build
Run migrations & create a superuser:
Open a new terminal window and execute these commands inside the running web container:

Bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
The project will be accessible at: http://localhost:8001/

The Django Admin Panel is at: http://localhost:8001/admin/

The DRF API Root is available at: http://localhost:8001/api/

Option 2: Traditional Setup (Without Docker 🛠️)
Prerequisites: Python 3.10+ and a local PostgreSQL server running.

Create and activate a virtual environment:

Bash
python -m venv env

# On Windows:

env\Scripts\activate

# On macOS/Linux:

source env/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Configure Database:
Update the DATABASES settings in settings.py to point to your local 127.0.0.1 PostgreSQL server instead of the Docker host.

Run migrations & Start server:

Bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
The project will be accessible at: http://127.0.0.1:8000/

📁 Project Structure
Plaintext
├── env/ # Python virtual environment (Local backup)
├── base/ # Core application for products, comments, categories
├── account/ # Application for user authentication and profiles
├── lcfshop/ # Main Django project settings directory
├── templates/ # Global HTML templates
├── static/ # Static files (CSS, JS, Images)
├── Dockerfile # Blueprint for the web container
└── docker-compose.yml # Multi-container orchestrator (Web & DB)
🎯 Current Features
Displaying a list of products on the homepage (/).

Product search by name, category, and seller.

Product detail view with comments (/product/<uuid:id>/).

Liking comments and adding new comments.

Posting new ads (/post_ad/).

Editing and deleting ads (restricted to owner or admin).

User authentication (signup, login, logout).

Browsable API endpoints for all core marketplace data via DRF.

🗺️ Future Features / Roadmap
[ ] Real-time Chat Room for Buyers & Sellers

[ ] Advanced Admin Dashboard

[ ] Seller Profile Page with Ratings

[ ] Dynamic Shopping Cart & Order Tracking

[ ] JWT Authentication for API Endpoints

[ ] Notification System

💡 Important Notes
Data Persistence: Database records are securely stored inside a named Docker volume (postgres_data). Stopping or rebuilding containers will not wipe your data.

Media Files: For file uploads (product images, avatars), ensure MEDIA_ROOT and MEDIA_URL are properly configured.

Python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
