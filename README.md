# Backend Systems Reference

This is my personal reference repo for essential backend and infrastructure skills that go **beyond CRUD**.  
It includes concise notes, patterns, and code snippets for quickly setting up and managing production-ready web systems.

---

## Structure

Each folder contains practical examples, configs, and notes.

```

/
├── deployment/            # SSH, systemd, Nginx, Gunicorn/Uvicorn, HTTPS
├── docker/                # Dockerfiles, Compose, image optimization
├── caching/               # TTL patterns, Redis, cache strategies
├── background-tasks/      # Celery, FastAPI BackgroundTasks, retries
├── logging-monitoring/    # Logging, Prometheus, Grafana, health checks
├── security/              # OAuth2, rate limiting, secure headers
├── api-gateways/          # Nginx as reverse proxy, load balancing
├── env-configs/           # .env, Pydantic Settings, secret management
├── database-ops/          # Pooling, migrations, backups
├── ci-cd/                 # GitHub Actions, pipelines, deployments
└── snippets/              # Misc helpers and reusable patterns

```

---

## Why This Exists

I built this to:
- Quickly revisit the “how do I set this up again?” tasks
- Avoid Googling the same infrastructure setup 10 times
- Have a reliable launchpad for any backend project

---

## Usage

You can:
- Clone this and use as your own boilerplate
- Copy snippets into new backend projects
- Expand each section as you learn more


---

## Topics Covered (WIP)

- Deployment (Uvicorn + Nginx + HTTPS)
- Docker
- Redis caching patterns
- FastAPI background jobs
- OAuth2 + JWT scopes
- GitHub Actions CI
- Prometheus + Grafana basics
- Structured logging
- Rate limiting logic

---

> Feel free to fork, copy, or adapt for your own backend journey.
