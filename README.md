# Cinema API Project

This project is a REST API developed with Django and Django REST Framework to manage a database of movies, authors, and spectators. It integrates external data via The Movie Database (TMDb) API and is fully containerized with Docker.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation and Launch

1.  **Clone the repository**

    ```bash
    git clone https://github.com/dimitri-hoareau/cinema_project
    cd cinema-project
    ```

2.  **Environment Configuration**

    Create a `.env` file in the project root, based on the `.env.example` file (if you have one, otherwise create it directly). This file must contain the necessary variables for the database and the TMDb API.

    ```
    # .env
    # Django secret key (do not use this value in production)
    SECRET_KEY=django-insecure-veaskmpqo^ly%h$a@_j2b5gy5t6=0ysa(h^-ple%t&2u+wc(q7

    # Debug mode
    DEBUG=True

    # PostgreSQL Database
    POSTGRES_DB=cinema_db
    POSTGRES_USER=cinema_user
    POSTGRES_PASSWORD=cinema_password
    DB_HOST=db
    DB_PORT=5432

    # API Key for The Movie Database (TMDb)
    # IMPORTANT: Replace with your own API key
    TMDB_API_KEY=YOUR_TMDB_API_KEY_HERE
    ```

3.  **Launch the application with Docker Compose**

    Use the following command to build the images and start the containers.

    ```bash
    docker-compose up --build
    ```

    The API will be accessible at `http://localhost:8000`. The `entrypoint.sh` script will ensure that migrations are applied and a superuser (`admin` / `admin`) is created on the first launch.

4.  **Import data from TMDb**

    To populate the database with popular movies, run the custom import command.

    ```bash
    docker-compose exec backend python manage.py import_movies
    ```

---

## API Endpoint Description

The base URL for all endpoints is `http://localhost:8000/api/`.

### Authentication (JWT)

- **`POST /api/auth/login/`**: Obtain JWT tokens.
  - **Body**: `{ "username": "your_username", "password": "your_password" }`
- **`POST /api/auth/token/refresh/`**: Refresh an access token.
  - **Body**: `{ "refresh": "your_refresh_token" }`
- **`POST /api/auth/register/`**: Create a new Spectator account.
  - **Permissions**: Open to all.
- **`POST /api/auth/logout/`**: Log out (adds the refresh token to the blacklist).
  - **Permissions**: Authenticated user.
  - **Body**: `{ "refresh": "your_refresh_token" }`

### Authors (`/authors/`)

- **`GET api/authors/`**: List all authors.
  - **Permissions**: Read-only for all.
  - **Filters (Query Params)**:
    - `?source=tmdb`: Returns only authors imported from TMDb.
    - `?source=admin`: Returns only manually created authors.
- **`GET api/authors/{id}/`**: Retrieve details for an author.
  - **Permissions**: Read-only for all.
- **`PUT/PATCH api/authors/{id}/`**: Update an author.
  - **Permissions**: Administrator or authenticated user (to be defined according to your rules).
- **`DELETE api/authors/{id}/`**: Delete an author (only if they have no associated movies).
  - **Permissions**: Administrator or authenticated user.
- **`POST api/authors/{id}/rate/`**: Rate an author.
  - **Permissions**: Authenticated spectator.
  - **Body**: `{ "score": 5 }` (score from 1 to 5).

### Films (`/films/`)

- **`GET api/films/`**: List all films.
  - **Permissions**: Read-only for all.
  - **Filters (Query Params)**:
    - `?status=released`: Filter by status (values: `released`, `project`, `archived`).
    - `?source=tmdb`: Filter by creation source (`tmdb` or `admin`).
- **`GET api/films/{id}/`**: Retrieve details for a film.
  - **Permissions**: Read-only for all.
- **`PUT/PATCH api/films/{id}/`**: Update a film.
  - **Permissions**: Administrator or authenticated user.
- **`POST api/films/{id}/archive/`**: Archive a film.
  - **Permissions**: Administrator or authenticated user.
- **`POST api/films/{id}/rate/`**: Rate a film.
  - **Permissions**: Authenticated spectator.
  - **Body**: `{ "score": 4 }`
- **`POST api/films/{id}/add_favorite/`**: Add a film to favorites.
  - **Permissions**: Authenticated spectator.
- **`POST api/films/{id}/remove_favorite/`**: Remove a film from favorites.
  - **Permissions**: Authenticated spectator.

### Favorites (`/favorites/`)

- **`GET /api/spectator/favorites/`**: List the favorite films of the authenticated spectator.
  - **Permissions**: Authenticated spectator.

---

## Administration Interface

The Django administration interface is available at `http://localhost:8000/admin/`.

- **Login**: `admin`
- **Password**: `admin`

Note: The entrypoint.sh script automatically creates this superuser for development convenience. This user should not be created automatically in a production environment.
