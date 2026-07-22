# AuditFlow 🔍

AuditFlow is an interactive audit workflow assistant that automates audit workflow navigation, guides auditors through audit phases, and supports audit documentation.

## Overview

AuditFlow provides a structured way to follow the Information Security Audit Process through an interactive command-line interface.

The assistant helps auditors initialize audit sessions, select audit frameworks, validate planning requirements, and generate audit findings when requirements are not satisfied.

## Audit Process

AuditFlow follows three main audit phases:

1. Planning
2. Fieldwork & Documentation
3. Reporting & Follow-Up

Currently, AuditFlow focuses on the Planning phase and provides a foundation for expanding the remaining audit phases.

## Features

- Interactive command-line audit assistant
- Auditor session initialization
- Organization and framework selection
- Support for audit frameworks:
  - ISO 27001
  - NCA ECC
- Audit process visualization
- Planning phase assessment workflow
- Decision-based validation
- Finding creation for unmet requirements
- Audit planning summary generation

## Technologies

- Python
- Rich Library (Terminal UI)

## Project Structure

```
AuditFlow/
│
├── main.py
│   └── Main application interface
│
├── audit_workflow.py
│   └── Audit workflow and planning assessment logic
│
├── audit_phases.py
│   └── Information about remaining audit phases
│
├── findings.py
│   └── Finding creation and management
│
├── README.md
│   └── Project documentation
│
└── .gitignore
    └── Git configuration
```

## Installation

### Clone the repository

```bash
git clone <repository-url>
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
4. Review the audit process
5. Complete the planning assessment
6. View the audit summary

## Workflow Example

```
Audit Session
      |
      ↓
Planning Phase
      |
      ↓
Scope Validation
      |
      ↓
Objectives Validation
      |
      ↓
Stakeholders Validation
      |
      ↓
Planning Summary
```

## Future Improvements

- Add Fieldwork & Documentation workflow execution
- Add control assessment features
- Support additional audit frameworks

## License

This project is created for learning and demonstration purposes.
