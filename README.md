# Caloriq

**Your daily nutrition dashboard.**

Caloriq is a full-stack web application that helps you understand, track and manage your daily calorie, protein and weight progress. Set your goal, log what you eat, and see at a glance how close you are to your targets.

![Status](https://img.shields.io/badge/status-v1.0%20released-brightgreen)
![Backend](https://img.shields.io/badge/backend-Python-blue)
![Frontend](https://img.shields.io/badge/frontend-HTML%20%7C%20CSS%20%7C%20JS-orange)
![Database](https://img.shields.io/badge/database-SQLite-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

<!-- TODO: add a dashboard screenshot here -->
<!-- ![Caloriq dashboard](docs/images/dashboard.png) -->

**Live demo:** _coming soon_ <!-- TODO: add link once deployed -->

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Overview](#api-overview)
- [How Targets Are Calculated](#how-targets-are-calculated)
- [Testing](#testing)
- [Roadmap](#roadmap)
- [Team](#team)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [License](#license)

---

## Overview

Many people eat through the day without knowing how many calories or how much protein they've actually had. Caloriq answers two simple questions:

1. **What should I aim for?** From your age, gender, height, weight, activity level and goal, Caloriq estimates your BMR, TDEE, daily calorie target and daily protein target.
2. **What have I consumed?** Log your meals and Caloriq keeps a live running total of calories consumed, calories remaining and protein eaten.

Caloriq is built for anyone who wants to **lose weight, maintain weight, gain muscle**, or just be more aware of what they eat.

## Features

### Available in v1.0

- **User login**: individual accounts with hashed passwords and protected data
- **Daily dashboard**: target, consumed and remaining calories at a glance
- **Food tracking (CRUD)**: add, view, edit and delete food entries; totals update automatically
- **Protein tracking**: daily protein consumed against your target
- **Goal progress bars**: visual progress for calories and protein
- **Weight tracking**: record your weight and see starting weight, current weight and change
- **Weight history chart**: track your progress over time
- **Weekly trends chart**: see how your intake changes across the week
- **Export & reports**: download your data as CSV or PDF
- **Input validation**: clear error messages instead of crashes

### In progress

- **Landing page with account creation**: a combined "Create your account / Log in" front page so new users can sign up and get started quickly

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript, [Chart.js](https://www.chartjs.org/) |
| Backend | Python (REST API) <!-- TODO: state Flask or FastAPI --> |
| Database | SQLite |
| Version control | Git & GitHub |

## Architecture

```
┌──────────────────────┐
│         USER         │
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│       FRONTEND       │
│  HTML / CSS / JS     │
└──────────┬───────────┘
           │  HTTP (JSON)
┌──────────▼───────────┐
│       BACKEND        │
│   Python REST API    │
└──────────┬───────────┘
           │  SQL
┌──────────▼───────────┐
│       DATABASE       │
│        SQLite        │
└──────────────────────┘
```

## Project Structure

<!-- TODO: update to match the actual repo layout -->

```
caloriq/
├── backend/
│   ├── app.py
│   ├── routes/
│   ├── models/
│   ├── services/        # nutrition calculations
│   └── database/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── tests/
├── docs/
├── requirements.txt
├── LICENSE
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- Git
- A modern web browser

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/caloriq.git
cd caloriq

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Running the application

```bash
# Start the backend
python backend/app.py
```

Then open `frontend/index.html` in your browser, or visit the address the backend prints in the terminal.

<!-- TODO: confirm the run command, port, and whether the backend serves the frontend -->

## API Overview

<!-- TODO: replace with your real endpoints. Example shape below. -->

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/login` | Log in |
| `POST` | `/auth/logout` | Log out |
| `GET` | `/foods` | List today's food entries |
| `POST` | `/foods` | Add a food entry |
| `PUT` | `/foods/{id}` | Edit a food entry |
| `DELETE` | `/foods/{id}` | Delete a food entry |
| `GET` | `/weight` | Get weight history |
| `POST` | `/weight` | Save current weight |

Full API documentation lives in [`docs/api.md`](docs/api.md).

## How Targets Are Calculated

<!-- TODO: confirm these match your implementation -->

- **BMR** (Basal Metabolic Rate): estimated from age, gender, height and weight
- **TDEE** (Total Daily Energy Expenditure): BMR adjusted for activity level
- **Calorie target**: TDEE adjusted for your goal (lose, maintain or gain)
- **Protein target**: an estimated minimum based on body weight and goal

Targets are estimates. The target is a user-defined goal, not an absolute medical limit.

## Testing

```bash
pytest
```

Tests cover nutrition calculations, input validation, food CRUD, daily totals, API endpoints, and authentication/authorization.

## Roadmap

- [x] Backend API and database
- [x] Authentication and protected user data
- [x] Dashboard and food tracking (CRUD)
- [x] Weight tracking and history chart
- [x] Weekly trends chart
- [x] CSV / PDF export
- [ ] Landing page with account creation and login
- [ ] Deployment and live demo
- [ ] Meal planning, favourite foods and custom foods
- [ ] Nutrition API / food database integration
- [ ] Barcode scanning
- [ ] Water and exercise tracking
- [ ] Dark mode
- [ ] Mobile app
- [ ] AI nutrition assistant

## Team

| Developer | Role |
|---|---|
| **Mthokozisi Vundla** | Backend, API, database, authentication |
| **Katleho** | Frontend, UI/UX, dashboard |

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push the branch: `git push origin feature/your-feature`
5. Open a pull request

## Disclaimer

Caloriq's calorie and protein calculations are estimates for educational and tracking purposes only. They are not medical advice or a substitute for professional nutritional or medical guidance.

## License

Released under the [MIT License](LICENSE).
