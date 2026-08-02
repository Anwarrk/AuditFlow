# AuditFlow 🔍

AuditFlow is an interactive command-line assistant that automates the Information Security Audit workflow, guiding auditors through Planning, Fieldwork & Documentation, and Reporting & Follow-Up.

## Overview

The application simulates real-world information security audit activities across Planning, Fieldwork & Documentation, and Reporting & Follow-Up using an interactive Rich terminal interface.

It helps auditors initialize audit sessions, select audit frameworks, validate planning requirements, document findings, and manage follow-up activities throughout the audit lifecycle.


<img width="319" height="157" alt="image" src="https://github.com/user-attachments/assets/60802d5c-0ab0-44df-9fe7-95898dd408f9" />


## Audit Process

AuditFlow follows three main audit phases:

1. Planning
2. Fieldwork & Documentation
3. Reporting & Follow-Up


## Features

- Interactive audit workflow assistant
- Interactive audit workflow visualization
- Audit session initialization
- Organization and audit framework selection
- Support for ISO 27001 and NCA ECC
- Planning workflow with decision validation
- Fieldwork & Documentation workflow
- Reporting & Follow-Up workflow
- Corrective Action Plan (CAP) tracking
- Follow-up review scheduling
- Audit finding generation
- Rich terminal user interface

## Technologies

- Python
- Rich (Terminal UI)
  
## Project Structure

```
AuditFlow/
│
├── main.py
├── audit_workflow.py
├── audit_process_2.py
├── audit_process_3.py
├── findings.py
├── README.md
└── .gitignore

```

## Installation

### Clone the repository

```bash
git clone https://github.com/Anwarrk/AuditFlow.git
```

### Navigate to the project directory

```bash
cd AuditFlow
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install rich
```

## Usage

Run the application:

```bash
python main.py
```

Then follow the interactive workflow:

1. Start a new audit session
2. Enter auditor and organization information
3. Select an audit framework
4. Complete the Planning phase
5. Perform Fieldwork & Documentation
6. Complete Reporting & Follow-Up
7. Review the audit session summary

## Audit Workflow

```
Audit Session
      │
      ▼
   Planning
      │
      ▼
Fieldwork & Documentation
      │
      ▼
Reporting & Follow-Up
      │
      ▼
Audit Summary
```

## Future Improvements

- Export audit reports to PDF or Word
- Save and resume audit sessions
- Support additional audit frameworks
- Generate professional audit reports automatically
- Dashboard and audit analytics

## License

This project is created for learning and demonstration purposes.
