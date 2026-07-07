# 🛒 LCF MarketPlace

> A modern, modular, and scalable e-commerce marketplace project built with Django and Django REST Framework.

## 🌟 About The Project

LCF MarketPlace is a dynamic web application designed to connect buyers and sellers. Users can browse various product categories, search for specific items, and seamlessly post their own products for sale. The project focuses on a clean user interface (Dark Mode), robust backend architecture, and a scalable containerized database design utilizing PostgreSQL.

## 🚀 Key Features (Currently Implemented)

- **Custom Authentication & JWT** — Robust custom user model (`account.User`) handling avatars, roles, and profiles, fully secured with JWT authentication for API endpoints.
- **RESTful API Architecture** — Powered by Django REST Framework (DRF) with clean serializers and endpoint routing for frontend/mobile integration.
- **Full Containerization** — Fully dockerized development environment ensuring consistency across all platforms.
- **Modular Architecture** — Divided into distinct, maintainable apps (`account`, `base`, `lcfshop`).
- **Dynamic Sidebar & Categories** — Uses Django context processors to inject category data globally across all templates without redundant queries.
- **Smart Search** — Real-time search functionality integrated directly into the navigation bar.
- **Flash Messaging** — Django Messages framework for immediate user feedback (success/error alerts).
- **Responsive UI** — Built with Bootstrap 5, featuring a dark theme, OwlCarousel sliders, and FontAwesome icons.

## 🛠️ Built With

| Category         | Technology                                            |
| ---------------- | ----------------------------------------------------- |
| Backend          | Django 6.0.3, Python 3.x, Django REST Framework (DRF) |
| Authentication   | JWT (JSON Web Tokens)                                 |
| Containerization | Docker & Docker Compose                               |
| Database         | PostgreSQL (persistent via Docker volumes)            |
| Frontend         | HTML5, CSS3, Bootstrap 5, jQuery                      |
| Architecture     | MVT (Model-View-Template) & REST API                  |

---

## ⚙️ Local Setup & Installation

You can run this project locally using either **Docker** (recommended) or the **traditional setup**.

### Option 1: The Docker Way (Recommended 🚀)

Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd lcfshop
   ```

2. **Build and run the containers:**
   This command automatically pulls the Python and PostgreSQL images, sets up the network, and starts the servers.

   ```bash
   docker-compose up --build
   ```

3. **Run migrations & create a superuser:**
   Open a new terminal window and execute these commands inside the running web container:

   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   ```

4. **Access the project:**
   - App: [http://localhost:8001/](http://localhost:8001/)
   - Django Admin Panel: [http://localhost:8001/admin/](http://localhost:8001/admin/)
   - DRF API Root: [http://localhost:8001/api/](http://localhost:8001/api/)

### Option 2: Traditional Setup (Without Docker 🛠️)

Prerequisites: Python 3.10+ and a local PostgreSQL server running.

1. **Create and activate a virtual environment:**

   ```bash
   python -m venv env

   # On Windows:
   env\Scripts\activate

   # On macOS/Linux:
   source env/bin/activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the database:**
   Update the `DATABASES` settings in `settings.py` to point to your local `127.0.0.1` PostgreSQL server instead of the Docker host.

4. **Run migrations & start the server:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

5. **Access the project:**
   - App: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📁 Project Structure

```
├── env/                  # Python virtual environment (local backup)
├── base/                 # Core application for products, comments, categories
├── account/              # Application for user authentication and profiles
├── lcfshop/              # Main Django project settings directory
├── templates/            # Global HTML templates
├── static/                # Static files (CSS, JS, images)
├── Dockerfile             # Blueprint for the web container
└── docker-compose.yml     # Multi-container orchestrator (web & DB)
```

## 🎯 Current Features

- Displaying a list of products on the homepage (`/`)
- Product search by name, category, and seller
- Product detail view with comments (`/product/<uuid:id>/`)
- Liking comments and adding new comments
- Posting new ads (`/post_ad/`)
- Editing and deleting ads (restricted to owner or admin)
- User authentication (signup, login, logout)
- Browsable API endpoints for all core marketplace data via DRF

## 🗺️ Future Features / Roadmap

- [ ] Real-time chat room for buyers & sellers
- [ ] Advanced admin dashboard
- [ ] Seller profile page with ratings
- [ ] Dynamic shopping cart & order tracking
- [ ] Notification system

## 💡 Important Notes

- **Data Persistence:** Database records are securely stored inside a named Docker volume (`postgres_data`). Stopping or rebuilding containers will not wipe your data.
- **Media Files:** For file uploads (product images, avatars), ensure `MEDIA_ROOT` and `MEDIA_URL` are properly configured:
  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```
