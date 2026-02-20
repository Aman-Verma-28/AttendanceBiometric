# AttendanceBiometric

A barcode-based attendance tracking system built with Django and Django REST Framework. Users and items are assigned unique barcodes on registration, enabling quick entry/exit logging through simple API calls.

## Tech Stack

- **Backend:** Django 5.0, Django REST Framework
- **Database:** SQLite
- **Auth:** Django admin + djangorestframework-simplejwt (JWT)
- **Barcode Generation:** python-barcode with Pillow

## Project Structure

```
AttendanceBiometric/
├── Biometric/
│   ├── AttandanceBiometric/   # Django project settings & URL config
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── UserManagement/        # Core app: models, views, admin
│   │   ├── models.py          # UserRegistraion, UserAttendance, Item
│   │   ├── views.py           # EntryView, ExitView API endpoints
│   │   └── admin.py
│   ├── manage.py
│   └── db.sqlite3
├── backendrequirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/Aman-Verma-28/AttendanceBiometric.git
cd AttendanceBiometric
pip install -r backendrequirements.txt
```

### Running the Server

```bash
cd Biometric
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   # create an admin account
python manage.py runserver
```

The development server starts at `http://localhost:8000`.

### Admin Panel

Manage users and items through the Django admin interface:

```
http://localhost:8000/admin
```

Log in with the superuser credentials you created above.

## API Endpoints

### Entry — `POST /entry/`

Record a user's entry for a given item.

**Request body:**

```json
{
  "token": "<user_token>",
  "item_token": "<item_token>"
}
```

### Entry — `GET /entry/`

Retrieve attendance records. Omit `token` to list all active entries, or provide it to filter by user.

**Request body (optional):**

```json
{
  "token": "<user_token>"
}
```

### Exit — `POST /exit/`

Record a user's exit and mark the attendance as inactive.

**Request body:**

```json
{
  "token": "<user_token>"
}
```

## Models

| Model | Description |
|---|---|
| **UserRegistraion** | Stores user info (name, contact, address, role) and auto-generates a unique barcode on save. |
| **Item** | Represents an item that users interact with; also auto-generates a barcode. |
| **UserAttendance** | Links a user to an item with entry/exit timestamps and an active flag. |

## License

This project is open source and available under the [MIT License](LICENSE).

