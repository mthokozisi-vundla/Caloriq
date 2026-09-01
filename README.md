# Caloriq
# 🍎 Calorie Tracker

A full-stack web application designed to help users understand, track, and manage their daily calorie and macronutrient intake.

The application allows users to enter their personal information and goals, receive estimated daily calorie and protein targets, record the food they consume, and monitor their progress throughout the day.

---

## 📌 Project Status

**Version:** 1.0
**Status:** Planning / Development
**Developer:** Mthokozisi Vundla
**Project Type:** Full-Stack Web Application

---

# 📖 Table of Contents

* [Project Overview](#-project-overview)
* [Problem Statement](#-problem-statement)
* [Project Goal](#-project-goal)
* [Target Users](#-target-users)
* [Core Features](#-core-features)
* [How It Works](#-how-it-works)
* [User Flow](#-user-flow)
* [Technology Stack](#-technology-stack)
* [Project Architecture](#-project-architecture)
* [Project Structure](#-project-structure)
* [Database](#-database)
* [Calculations](#-calculations)
* [Validation](#-validation)
* [Authentication](#-authentication)
* [CRUD Functionality](#-crud-functionality)
* [Testing](#-testing)
* [Development Roadmap](#-development-roadmap)
* [Future Features](#-future-features)
* [Installation](#-installation)
* [Running the Application](#-running-the-application)
* [Git Workflow](#-git-workflow)
* [Project Documentation](#-project-documentation)
* [Disclaimer](#-disclaimer)
* [License](#-license)

---

# 🎯 Project Overview

Calorie Tracker is a personal nutrition management application.

The application is designed around two main questions:

### 1. What should I aim for?

The application uses information such as:

* Age
* Gender
* Height
* Weight
* Activity level
* Goal

to estimate:

* BMR
* TDEE
* Daily calorie target
* Daily protein target

### 2. What have I consumed?

The user records the food they consume throughout the day.

The application then automatically calculates:

* Total calories consumed
* Calories remaining
* Protein consumed
* Carbohydrates consumed
* Fat consumed

This allows the user to compare their actual intake against their daily targets.

---

# ❗ Problem Statement

Many people consume food throughout the day without knowing how many calories or macronutrients they are actually consuming.

This can make it difficult to manage food intake when trying to:

* Lose weight
* Maintain weight
* Gain muscle
* Improve nutritional awareness

For example, a user may choose a daily target of:

```text
2,000 kcal
```

but have no convenient way of knowing how close they are to that target.

Calorie Tracker addresses this problem by allowing the user to record their food and automatically maintain a running daily total.

---

# 🎯 Project Goal

The goal of this project is to create a functional full-stack nutrition tracking application while developing practical software-development skills.

The project will be developed progressively.

The initial focus is on creating a working Version 1 before introducing more advanced features.

---

# 👥 Target Users

The initial users are:

* Individuals trying to lose weight
* Individuals trying to maintain their weight
* Individuals trying to gain muscle
* Individuals who want greater awareness of their daily food intake

The application is initially being developed for personal use but will be designed to support multiple users.

---

# ✨ Core Features

## 👤 User Accounts

Users will be able to:

* Register
* Log in
* Log out
* View their profile
* Update their information

---

## 🧍 User Profile

Users can provide:

* Name
* Email
* Password
* Age
* Gender
* Height
* Weight
* Activity level
* Goal

---

## 🎯 Goals

Users can select a goal such as:

* Lose weight
* Maintain weight
* Gain muscle/weight

The selected goal will be used when determining the user's estimated calorie target.

---

# 🧮 Nutrition Calculator

The application will calculate estimated nutritional targets.

The calculator will use information such as:

```text
Age
Gender
Height
Weight
Activity Level
Goal
```

The application will calculate:

### BMR

Basal Metabolic Rate.

### TDEE

Total Daily Energy Expenditure.

### Daily Calorie Target

An estimated calorie target based on the user's goal.

### Daily Protein Target

An estimated minimum daily protein target.

---

# 🍽️ Food Tracking

Users will be able to record the food they consume.

Each food entry may contain:

```text
Food name
Quantity
Calories
Protein
Carbohydrates
Fat
Date
Time
```

Example:

```text
Food: Eggs
Quantity: 3
Calories: 210 kcal
Protein: 18 g
Carbohydrates: 1 g
Fat: 15 g
```

---

# 📊 Daily Dashboard

The dashboard will provide an overview of the user's current day.

Example:

```text
Daily Target
2,000 kcal

Consumed
1,650 kcal

Remaining
350 kcal
```

The dashboard will also display:

```text
Protein
120 / 150 g

Carbohydrates
180 / 250 g

Fat
55 / 70 g
```

The user's food entries will also be displayed.

---

# 🔔 Calorie Target Notification

The application will monitor the user's daily calorie intake.

When the user reaches their selected calorie target, the application will display a notification.

Example:

> You've reached your daily calorie target of 2,000 kcal.

If the user exceeds the target:

> You've exceeded your daily calorie target by 250 kcal.

The target is treated as a user-defined goal rather than an absolute medical limit.

---

# 🔄 User Flow

The basic application flow will be:

```text
                 START
                   │
                   ▼
               Register
                   │
                   ▼
                 Login
                   │
                   ▼
            Complete Profile
                   │
                   ▼
             Select Goal
                   │
                   ▼
        Calculate Nutrition Targets
                   │
                   ▼
               Dashboard
                   │
             ┌─────┴─────┐
             ▼           ▼
         Add Food    View Progress
             │           │
             ▼           │
        Update Totals ◄──┘
             │
             ▼
      Reach Calorie Target?
             │
        ┌────┴────┐
       YES        NO
        │          │
        ▼          ▼
   Notification   Continue
```

---

# 🛠️ Technology Stack

The technology stack will be introduced progressively.

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask or FastAPI

The final framework will be selected during backend development.

## Database

Initial database:

* SQLite

Potential future database:

* PostgreSQL

## Version Control

* Git
* GitHub

## Testing

* Python testing tools
* API testing tools

## Deployment

A suitable cloud hosting platform will be selected once the application is production-ready.

---

# 🏗️ Project Architecture

The application will follow a basic full-stack architecture:

```text
┌───────────────────────┐
│        USER           │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│       FRONTEND        │
│   HTML / CSS / JS     │
└───────────┬───────────┘
            │
            │ HTTP Requests
            ▼
┌───────────────────────┐
│       BACKEND         │
│        Python         │
│      REST API         │
└───────────┬───────────┘
            │
            │ Database Queries
            ▼
┌───────────────────────┐
│       DATABASE        │
│        SQLite         │
└───────────────────────┘
```

---

# 📁 Project Structure

The project will eventually follow a structure similar to:

```text
calorie-tracker/
│
├── backend/
│   ├── app.py
│   ├── routes/
│   ├── models/
│   ├── services/
│   └── database/
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── profile.html
│   ├── css/
│   └── js/
│
├── tests/
│
├── docs/
│   ├── requirements.md
│   ├── database-design.md
│   ├── architecture.md
│   └── api.md
│
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```

The structure may change as the application develops.

---

# 🗄️ Database

The initial application will use SQLite.

The database will eventually contain information such as:

## Users

```text
users
-------------------------
id
name
email
password_hash
age
gender
height
weight
activity_level
goal
calorie_target
protein_target
created_at
```

## Food Entries

```text
food_entries
-------------------------
id
user_id
food_name
quantity
calories
protein
carbohydrates
fat
date
created_at
```

The `user_id` will associate each food entry with its owner.

---

# 🧮 Calculations

The application will contain functions responsible for nutritional calculations.

Potential functions include:

```text
calculate_bmr()
calculate_tdee()
calculate_calorie_target()
calculate_protein_target()
calculate_daily_calories()
calculate_daily_protein()
calculate_daily_carbohydrates()
calculate_daily_fat()
```

The formulas and assumptions used by the application will be documented in the project.

---

# ✅ Input Validation

The application will validate user input before processing or storing it.

Examples include:

### Age

Must be a valid positive value.

### Height

Must be a valid positive numerical value.

### Weight

Must be a valid positive numerical value.

### Calories

Cannot be negative.

### Macronutrients

Protein, carbohydrates and fat cannot be negative.

### Email

Must follow a valid email format.

### Required fields

Important fields cannot be left empty.

Invalid input should result in a clear error message rather than causing the application to crash.

---

# 🔐 Authentication

Users will eventually have individual accounts.

Authentication will include:

* Registration
* Login
* Logout
* Password hashing
* Session/token management
* Authorization

Users should only be able to access and modify their own information and food records.

Passwords will never be stored as plain text.

---

# 🔄 CRUD Functionality

Food tracking will demonstrate CRUD operations.

## Create

Add a food entry.

```text
CREATE → Add Food
```

## Read

View food entries.

```text
READ → View Food
```

## Update

Edit a food entry.

```text
UPDATE → Edit Food
```

## Delete

Remove a food entry.

```text
DELETE → Delete Food
```

After an entry is modified or deleted, the daily totals should automatically update.

---

# 🧪 Testing

Testing will be introduced throughout development.

Tests will eventually cover:

* BMR calculations
* TDEE calculations
* Calorie targets
* Protein targets
* Input validation
* Food creation
* Food retrieval
* Food updates
* Food deletion
* Daily totals
* API endpoints
* Authentication
* Authorization

The objective is to ensure that individual components work correctly before the entire system is integrated.

---

# 🚀 Development Roadmap

## Phase 1 — Planning

* [x] Define project idea
* [x] Define problem
* [x] Define target users
* [x] Define Version 1 scope
* [x] Create README
* [ ] Create detailed requirements
* [ ] Create user stories
* [ ] Design application flow
* [ ] Design database

---

## Phase 2 — Python Foundation

* [ ] Create project environment
* [ ] Create basic Python structure
* [ ] Implement functions
* [ ] Implement calculations
* [ ] Implement validation
* [ ] Implement food tracking logic
* [ ] Test core Python functionality

---

## Phase 3 — Database

* [ ] Create SQLite database
* [ ] Create users table
* [ ] Create food entries table
* [ ] Establish relationships
* [ ] Implement database operations
* [ ] Test database functionality

---

## Phase 4 — Backend

* [ ] Select Flask/FastAPI
* [ ] Create backend application
* [ ] Create routes
* [ ] Create API endpoints
* [ ] Connect backend to database
* [ ] Implement CRUD operations
* [ ] Implement error handling
* [ ] Test API

---

## Phase 5 — Authentication

* [ ] Registration
* [ ] Password hashing
* [ ] Login
* [ ] Logout
* [ ] Authentication
* [ ] Authorization
* [ ] Protect user data

---

## Phase 6 — Frontend

* [ ] Create landing page
* [ ] Create registration page
* [ ] Create login page
* [ ] Create profile page
* [ ] Create calculator interface
* [ ] Create dashboard
* [ ] Create food-entry interface
* [ ] Create food history
* [ ] Style application
* [ ] Add JavaScript functionality

---

## Phase 7 — Full-Stack Integration

* [ ] Connect frontend to API
* [ ] Send user information
* [ ] Retrieve user information
* [ ] Add food through frontend
* [ ] Retrieve food entries
* [ ] Edit food
* [ ] Delete food
* [ ] Display daily totals
* [ ] Display calorie progress
* [ ] Implement notifications

---

## Phase 8 — Testing & Improvements

* [ ] Unit testing
* [ ] API testing
* [ ] Validation testing
* [ ] Authentication testing
* [ ] Error handling
* [ ] Security review
* [ ] Fix bugs
* [ ] Improve UI/UX
* [ ] Improve performance

---

## Phase 9 — Deployment

* [ ] Prepare production configuration
* [ ] Configure environment variables
* [ ] Prepare production database
* [ ] Deploy backend
* [ ] Deploy frontend
* [ ] Test live application
* [ ] Fix deployment issues
* [ ] Add live application link to README

---

## Phase 10 — Portfolio

* [ ] Clean GitHub repository
* [ ] Improve README
* [ ] Add screenshots
* [ ] Add architecture diagram
* [ ] Document API
* [ ] Document database
* [ ] Add testing information
* [ ] Add live demo
* [ ] Add project to CV
* [ ] Add project to portfolio

---

# 🔮 Future Features

Features that may be considered after Version 1:

* Weight tracking
* Weight-loss progress
* Weekly statistics
* Monthly statistics
* Progress charts
* Meal planning
* Custom foods
* Favourite foods
* Food database
* Nutrition API integration
* Barcode scanning
* Water tracking
* Exercise tracking
* Calories burned
* Data export
* Mobile application
* Dark mode
* AI nutrition assistant

These features are intentionally outside the initial Version 1 scope.

---

# 💻 Installation

## 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

## 2. Navigate into the project

```bash
cd calorie-tracker
```

## 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

The exact command will depend on the backend framework selected.

For example, a Flask application may eventually be started with:

```bash
python backend/app.py
```

Development instructions will be updated as the project develops.

---

# 🌿 Git Workflow

The project will use Git for version control.

Recommended workflow:

```text
main
 │
 ├── feature/user-authentication
 ├── feature/calorie-calculator
 ├── feature/food-tracking
 ├── feature/dashboard
 └── feature/database
```

For individual development, feature branches can still be used to keep changes organized.

Example:

```bash
git checkout -b feature/calorie-calculator
```

After completing the feature:

```bash
git add .
git commit -m "Add calorie calculation functionality"
git push origin feature/calorie-calculator
```

---

# 📚 Project Documentation

Additional documentation will be stored inside the `docs/` directory.

Planned documentation includes:

### `requirements.md`

Detailed functional and non-functional requirements.

### `database-design.md`

Database tables, relationships and design decisions.

### `architecture.md`

Application architecture and how the components communicate.

### `api.md`

API endpoints, request formats and responses.

---

# ⚠️ Disclaimer

The calorie and protein calculations provided by this application are estimates intended for educational and tracking purposes.

They should not be considered medical advice or a substitute for professional nutritional or medical guidance.

---

# 📄 License

This project will be licensed under the MIT License once the repository is ready for public release.

---

# 👨🏾‍💻 Developer

**Mthokozisi Vundla**

This project is being developed as a personal software-development and portfolio project with the goal of building practical experience in Python, backend development, databases, frontend development and full-stack application development.
