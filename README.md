# 🧪 BDD Experiments with Behave and Allure 3

This project is a hands-on sandbox for Behavior-Driven Development (BDD) using [Behave](https://behave.readthedocs.io/en/stable/) and Allure Report 3. It provides a collaborative testing framework with visual reporting and Python virtual environment isolation.

## 📦 Requirements

### 💻 System Prerequisites
- Python 3.7+
- Git
- VS Code
- Java Runtime (JRE or JDK) – required for Allure
- Allure 3 CLI (see below)

## ⚙️ Setup Instructions

### 🔁 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/bdd-experiments.git
cd bdd-experiments
```

### 🐍 2. Set Up a Virtual Environment

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows (Git Bash):
```bash
py -m venv .venv
source .venv/Scripts/activate
```

### 📦 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 📊 4. Install Allure 3 CLI

macOS (Homebrew):
```bash
brew install allure
```

Windows (Scoop):
```powershell
scoop install allure
```

Manual (all platforms):
Download from https://github.com/allure-framework/allure3/releases and add to PATH.

### 🧪 5. Run Tests and Generate Reports
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results/ features/
allure serve allure-results/
```

## 💻 Working in VS Code

### ✅ Recommended Extensions
- Python (by Microsoft)
- Behave VSC
- GitLens

### 🧭 Setup Interpreter
- Open Command Palette: `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows)
- Select: `Python: Select Interpreter`
- Choose: `.venv/bin/python` (macOS) or `.venv\Scripts\python.exe` (Windows)

## 🗂️ Project Structure
```
bdd-experiments/
├── features/
│   ├── steps/
│   │   └── example_steps.py
│   └── example.feature
├── .venv/                  # Not committed
├── allure-results/         # Allure results
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
/allure-results/
```
