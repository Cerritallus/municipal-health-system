# Municipal Health & Triage Management System (MHTMS)

## Overview

The Municipal Health & Triage Management System (MHTMS) is a secure enterprise-grade healthcare web application developed using the Django Framework. The system digitizes patient intake, triage prioritization, and clinical workflow management for municipal health clinics.

The system supports role-based workflows for nurses, doctors, and administrators while implementing enterprise security controls such as Anti-IDOR protection, JWT authentication, brute-force prevention, honeypot traps, and audit logging.

---

# Core Features

## Patient Management

* Patient registration system
* UUID-based patient records
* Medical history preservation
* Secure CRUD operations

## Triage Management

* Nurse vital sign encoding
* Rule-based triage engine
* Automatic severity classification:

  * LOW
  * MEDIUM
  * HIGH
  * CRITICAL

## Doctor Dashboard

* Real-time patient queue
* Priority-based triage highlighting
* Bulk discharge functionality
* Patient detail workflow

## Security Features

* JWT Authentication
* Anti-IDOR object protection
* Role-Based Access Control (RBAC)
* Django Axes brute-force protection
* Honeypot anti-bot protection
* Python audit logging
* DEBUG=False enforcement

## API System

* Public masked health statistics API
* HIPAA-style field masking
* Doctor-only protected medical endpoints

---

# Technology Stack

## Backend

* Django 6
* Django REST Framework
* PostgreSQL
* JWT Authentication

## Frontend

* Bootstrap 5
* Django Templates

## Security

* django-axes
* honeypot middleware
* Bandit
* pip-audit

## Deployment

* Railway
* Cloudinary
* Gunicorn
* WhiteNoise

---

# User Roles

## Nurse

* Register patients
* Encode triage vitals
* Manage patient intake queue

## Doctor

* Review patient queue
* View triage details
* Bulk discharge patients

## Administrator

* System oversight
* User management
* Full dashboard access

---

# API Endpoints

## Public Endpoints

### GET /api/public/stats/

Returns aggregated health statistics.

### GET /api/public/patients/

Returns masked patient records.

---

## Protected Endpoints

### POST /api/token/

JWT login endpoint.

### GET /api/doctor/triage/

Protected doctor-only endpoint returning full triage records.

---

# Security Architecture

The system implements multiple enterprise security layers:

* UUID-based Anti-IDOR protection
* JWT-secured APIs
* CSRF protection
* Brute-force login prevention
* Audit logging
* HIPAA-style data masking
* Production-safe deployment configuration

---

# Deployment Instructions

## Local Setup

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Create admin user:

python manage.py createsuperuser

Run server:

python manage.py runserver

---

# Railway Deployment

1. Push project to GitHub
2. Create Railway project
3. Connect GitHub repository
4. Add PostgreSQL plugin
5. Configure environment variables
6. Deploy application
7. Run migrations in Railway shell

---

# Environment Variables

SECRET_KEY=
DEBUG=False
DATABASE_URL=
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=

---

# Security Compliance

The system passed:

* Bandit SAST scans
* pip-audit dependency scans
* Django check --deploy validation

---

# Researchers / Developers

Municipal Health & Triage Management System Development Team
EVSU Main Campus
2026
