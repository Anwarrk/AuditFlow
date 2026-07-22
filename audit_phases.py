from rich.console import Console
from rich.panel import Panel


console = Console()



def show_remaining_phases():


    console.print(

        Panel(

"""
Next Audit Phases:

1. Fieldwork & Documentation

- Evidence Collection
- Control Testing


2. Reporting & Follow-Up

- Findings Documentation
- Corrective Actions Tracking

""",

        title="Audit Lifecycle",

        border_style="blue"

        )

    )