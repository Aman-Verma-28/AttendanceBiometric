# AttendanceBiometric

This project is a simple implementation of a biometric attendance system using the fingerprint sensor.

## Getting Started

### Installing

To install the project, you need to clone the repository and install the required packages.

```bash
git clone https://github.com/Aman-Verma-28/AttendanceBiometric.git
cd AttendanceBiometric/Biometric
pip install -r backendrequirements.txt
```

### Configuration

The following environment variables can be set to configure the application:

| Variable | Description | Default |
|---|---|---|
| `DJANGO_SECRET_KEY` | Django secret key for cryptographic signing | Insecure default (change in production) |
| `DJANGO_DEBUG` | Enable/disable debug mode | `True` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of allowed hosts | Empty |

### Running the project

To run the project, you need to run the backend and the frontend separately.

#### Backend

To run the backend, you need to run the following command from the `Biometric/` directory:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### Frontend

The frontend will be the admin panel of the Django project. You can access it by going to the following URL:

```
http://localhost:8000/admin
```

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/entry/` | List all active attendance records |
| `GET` | `/entry/?token=<token>` | Get attendance records for a specific user |
| `POST` | `/entry/` | Record a new entry (requires `token` and `item_token` in body) |
| `POST` | `/exit/` | Record an exit (requires `token` in body) |
