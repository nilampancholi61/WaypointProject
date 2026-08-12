# Waypoint Project

Waypoint is a Django web application built around the Waypoint domain engine developed during Weeks 7 and 8.

## Setup

Create and activate the virtual environment:

python3 -m venv env
source env/bin/activate

## Install Requirements

pip install -r requirements.txt

## Database

python manage.py migrate

## Run the Development Server

python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

## Domain Engine

The Week 7 and Week 8 domain code is available in the waypoint_core/ package.

Test the package with:

python -c "import waypoint_core"

## Django MVT

Django follows the Model-View-Template (MVT) architecture:

- Model: Represents application data.
- View: Contains application logic that responds to requests.
- Template: Controls how information is displayed.# Waypoint
