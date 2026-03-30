# 🏦 BankLite Web + API Application (Repo 7)

## 📌 Overview

This project is part of my learning journey into **Software Testing and QA Automation**.

After building foundational projects in Python, OOP, and basic application logic, this repository introduces a more realistic application structure with:

- Web interface (Flask + HTML)
- REST-style API layer
- Service (business logic) layer
- Storage abstraction

This project is intentionally designed as a **testing playground**, where both **manual testing and automation testing** can be applied.

---

## 🎯 Learning Objectives

This repository focuses on bridging the gap between:

👉 *“writing code”* → *“testing real applications like a QA engineer”*

Key objectives:

- Understand layered application architecture
- Learn how Web UI and APIs behave differently
- Practice manual testing on real user flows
- Prepare for automation testing (UI + API)
- Identify bugs across multiple layers
- Build confidence in real-world testing scenarios

---


## 🏗️ Architecture

```
Browser (Frontend JS)
        ↓
API Layer (Backend)
        ↓
Service Layer
        ↓
Database-style Storage

```

---

## 🔍 Features

- User login
- Account balance view
- Deposit / Withdraw
- Transfer between accounts
- Transaction history
- REST API for all major operations

---

## 🧪 Testing Focus (Very Important)

This repository is **NOT just a development project**.

It is primarily designed for:

### 1. Manual Testing
- Functional testing (login, deposit, transfer)
- Negative scenarios (invalid input, insufficient balance)
- Boundary testing
- UI validation
- Bug reporting

### 2. API Testing
- Test endpoints using:
  - Postman
  - curl
  - pytest + requests (later)
- Validate:
  - request/response
  - status codes
  - data correctness
  - error handling

### 3. Future Automation (Next Step)

This repo will be used for:

#### 🔹 UI Automation
- Playwright
- End-to-end user journeys

#### 🔹 API Automation
- pytest + requests
- Data-driven testing
- Integration-level validation

---

## 🚀 Why This Project Matters

This project simulates a **real-world QA environment**, where:

- UI and API coexist
- Business logic is shared
- Bugs can occur at multiple layers
- Test coverage must be planned

It helps me transition from:

👉 *“learning Python”*  
➡️ *“thinking like a QA engineer”*

---

## ⚠️ Current Limitations (Intentional for Learning)

- In-memory storage (data resets on restart)
- No real database
- Basic authentication
- Minimal validation in some areas

These limitations are intentional to:

- Keep the system simple
- Focus on testing concepts
- Allow easy bug discovery

---

## 🔮 Future Improvements

This project will evolve into:

- API automation framework (pytest-based)
- UI automation suite (Playwright / Selenium)
- Better validation and error handling
- Possible database integration
- Advanced logging and reporting

---

## ▶️ How to Run

```
python run.py
```

Then open:

```
http://127.0.0.1:5000
```

---

## 💬 Final Note

This repository represents a key transition point in my journey:

> From building applications → to testing them like a professional QA engineer.

The next step is to **apply structured testing and automation on top of this system**.
