# Data Bank

Data Bank is a single-user application built with Django that allows users to create and manage personal data for individuals. The application provides functionalities to store and organize information such as name, age, education, phone number, email address, and a photo for each person. Users can also delete data as needed.

## Features

- **User Authentication:** Users can create an account and securely authenticate themselves to access the application.
- **Create Data:** Users can create entries for individuals by providing their name, age, education, phone number, email address, and uploading a photo.
- **View Data:** Users can view the stored data of individuals, including all the information provided during creation.
- **Update Data:** Users can update the information of individuals if needed.
- **Delete Data:** Users have the ability to delete individual entries from the database.
- **SQLite3 Database:** The application uses SQLite3 as its database management system, providing a lightweight and efficient solution for storing data.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/anandmohanam/databank.git
cd data-bank
Run migrations:
python manage.py makemigrate
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver
