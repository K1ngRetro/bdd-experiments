# 🧪 BDD Experiments with Behave and Allure

This project is a hands-on sandbox for Behavior-Driven Development (BDD) using [Behave](https://behave.readthedocs.io/en/stable/) and [Allure Reports](https://docs.qameta.io/allure/). It provides a collaborative testing framework with visual reporting and Python virtual environment isolation.

## 📦 Requirements

### 💻 System Prerequisites
- Python 3.7+
- Git
- VS Code
- Git Bash (for Windows)
- Java Runtime (JRE or JDK) – required for Allure
- Allure CLI (see below)

## ⚙️ Setup Instructions

### 🔁 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/bdd-experiments.git
cd bdd-experiments
```

### 🐍 2. Set Up a Virtual Environment
```bash
python -m venv .venv
source .venv/Scripts/activate      # Windows
# or
source .venv/bin/activate          # macOS/Linux
```

### 📦 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 📊 4. Install Allure CLI

#### Option A: Scoop (Windows)
```bash
scoop install allure
```

#### Option B: Manually
Download from https://github.com/allure-framework/allure2/releases and add to PATH.

### 🧪 5. Run Tests and Generate Reports
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/
allure serve reports/
```

## 💻 Working in VS Code

### ✅ Recommended Extensions
- Python (by Microsoft)
- Behave VSC
- GitLens

### 🧭 Setup Interpreter
- Open Command Palette: `Ctrl+Shift+P`
- Select: `Python: Select Interpreter`
- Choose: `.venv/Scripts/python.exe`

## 🗂️ Project Structure
```
bdd-experiments/
├── features/
│   ├── steps/
│   │   └── example_steps.py
│   └── example.feature
├── .venv/                  # Not committed
├── reports/                # Allure results
├── .gitignore
├── requirements.txt
├── setup.sh
└── README.md
```

## 🚫 .gitignore
```
.venv/
__pycache__/
*.pyc
/reports/
```