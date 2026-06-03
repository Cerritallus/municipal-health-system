# Municipal Health & Triage Management System (MHTMS)

## Overview
A secure enterprise-grade healthcare triage system for municipal clinics.

## Features

### Patient Management
- Patient registration
- Secure medical records (UUID-based)

### Triage System
- Nurse input for vitals
- Automatic priority classification (LOW, MEDIUM, HIGH, CRITICAL)

### Doctor Dashboard
- Patient queue management
- Bulk discharge functionality
- Critical patient highlighting

### Security
- Anti-IDOR protection
- Django Axes brute-force prevention
- Honeypot bot detection
- Audit logging system
- JWT authentication
- HIPAA-style API masking

### API System
- Public health statistics API
- Masked patient API
- Doctor-only full medical API

## Tech Stack
- Django 5
- Django REST Framework
- PostgreSQL (Railway)
- Cloudinary
- Bootstrap 5
- JWT Authentication

## Deployment
Hosted on Railway with PostgreSQL and Cloudinary integration.

## Security Compliance
- DEBUG=False enforced
- Secure middleware enabled
- Dependency scanning (pip-audit)
- Static analysis (Bandit)

## Admin Access
- Role-based system (Admin / Doctor / Nurse)