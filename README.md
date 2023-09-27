# cashier

## Description

This is a simple cashier application that can be used to calculate the total price of items in a shopping cart. It is written in Python 3.7.3 and uses the [PyQt5](https://pypi.org/project/PyQt5/) library for the GUI.

## Installation
```bash
pip install -r requirements.txt
```

## Running the application
```bash
python manage.py runserver
```
## To Run Docker
```bash
docker build -t cashier-app .
```

```bash
docker run -v C:\cashier_data:/app/db_volume -p 8000:8000 cashier-app
```