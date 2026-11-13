# 🔧 AutoService Management System

A web app for running a car service centre: customers, vehicles, appointments,
repair orders, services, spare parts and invoices in one place.

Built as a team coursework project for the **Fundamentals of Information
Systems** module at **Kaunas University of Technology (KTU)**.

**Status:** in development (UI prototype screens are in place)

## Roles

- **Klientas** (customer): registers vehicles, books visits, sees and pays invoices
- **Vadybininkas** (service manager): manages visits, orders, services, parts, invoices and staff
- **Meistras** (mechanic): works on assigned orders and updates parts usage

## Tech stack

- Python 3.13, Django 6.1
- SQLite for local development
- Tailwind CSS + IBM Carbon styles (via `django-tailwind`)
- uv for dependencies, pytest, ruff and ty for checks

## Project structure

```text
autoservisu_sistema/   Django project settings and root URLs
apps/                  Django apps: accounts, billing, inventory, main, orders, services, vehicles
templates/             All HTML templates (base, partials, one folder per app)
theme/                 Tailwind / Carbon styles and static JS
```

## Setup

You need **Python 3.13+**, **[uv](https://docs.astral.sh/uv/)** and **Node.js** (for Tailwind).

```bash
git clone https://github.com/MartynasMatDev/Autoservisu_Sistema.git
cd Autoservisu_Sistema

uv sync
uv run python manage.py migrate
uv run python manage.py seed_demo
uv run python manage.py tailwind install
uv run python manage.py tailwind build
```

Run the app:

```bash
uv run python manage.py runserver
```

Then open http://127.0.0.1:8000/.

`seed_demo` creates sample data and demo users, all with password `pass`:
`user1`, `user2` (customers), `vadybininkas`, `meistras`, `meistras2`,
`meistras3`, `admin` (superuser).

## Before committing

Run all checks (pytest, ruff, ty):

```bash
./test.sh      # Linux / macOS
.\test.ps1     # Windows
```

Work on a separate branch and open a pull request into `master`.
