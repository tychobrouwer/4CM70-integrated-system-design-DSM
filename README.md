## Integrated System Design — DSM (Simple README)

This repository contains materials and ESL (Embedded System Language) files used for the Integrated System Design course.

## Requirements

- Python 1.12
- graphviz

## Repository structure

- esl/
- dsm.ipynb
- README.md
- requirements.txt

## Initialize the development environment (Unix-like: macOS / Linux / WSL / Git Bash)

Use a virtual environment and install dependencies from `requirements.txt`.

```zsh
# create a virtual environment
python3.12 -m venv .venv

# activate it
source .venv/bin/activate

# upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt
```

## Initialize the development environment (Windows)

PowerShell (recommended):

```powershell
# create venv
python -m venv .venv

# run in PowerShell to allow script execution if needed:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# activate
.\.venv\Scripts\Activate.ps1

# upgrade pip and install
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Command Prompt (cmd.exe):

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Git Bash / WSL users can use the Unix-like instructions above (use `source .venv/bin/activate`).