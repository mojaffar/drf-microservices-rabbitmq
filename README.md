# DRF Microservices RabbitMQ Example

This project demonstrates a microservices architecture using Django REST Framework, Celery, and RabbitMQ.

## Services
- **order_service**: Handles order-related APIs and tasks.
- **notification_service**: Handles notifications, listens to RabbitMQ.
- **RabbitMQ**: Message broker for async communication.

## Development Quickstart

1. **Build and run all services:**
   ```bash
   sudo docker-compose up --build
   ```
   - Order service: http://localhost:8000
   - Notification service: http://localhost:8001
   - RabbitMQ UI: http://localhost:15673 (user: guest, pass: guest)

2. **Stop all services:**
   ```bash
   sudo docker-compose down
   ```

## Project Structure
- `order_service/` and `notification_service/` each have their own `requirements.txt`, `Dockerfile`, and Django project.
- `docker-compose.yml` orchestrates all services.

## Git Best Practices
- Sensitive files and build artifacts are ignored via `.gitignore` and `.dockerignore`.
- Do not commit `.env` or database files.

---

**Ready to push to git!**
