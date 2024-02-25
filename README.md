# AttendanceBiometric

This project is a simple implementation of a biometric attendance system using the fingerprint sensor.

## Getting Started

### Installing

To install the project, you need to clone the repository and install the required packages.

```bash
git clone https://github.com/Aman-Verma-28/AttendanceBiometric.git
cd AttendanceBiometric
pip install -r backendrequirements.txt
```

### Running the project

To run the project, you need to run the backend and the frontend separately.

#### Backend

To run the backend, you need to run the following command:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### Frontend

The fronted will be the admin panel of the Django project. You can access it by going to the following URL:

```
http://localhost:8000/admin
```

