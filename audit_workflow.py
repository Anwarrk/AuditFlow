from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from rich.align import Align

from findings import create_finding

console = Console()


def show_decision_tree():

    tree = """

        Planning 

        Review and confirm the planning requirements
        before starting the audit engagement.

                       START
                         |
                         ↓
 
               Audit Subject Defined?
                   /            \\
                  YES            NO
                   |              |
                   ↓              ↓

          Audit Objective      Record Finding
              Defined?
             /       \\
            YES       NO
             |         |
             ↓         ↓

       Audit Scope    Record Finding
         Defined?
         /      \\
        YES      NO
         |        |
         ↓        ↓

    Ready for   Record Finding
    Fieldwork ✓   



"""

    console.print(
        Panel(
            Align.center(tree),
            title="Audit Process",
            border_style="green"
        )
    )

    sleep(2)


def planning_workflow():

    show_decision_tree()

    input(
        "\nPress ENTER to begin Planning..."
    )

    sleep(1)

    # Step 1

    subject = Confirm.ask(
        "\nIs the audit subject defined?"
    )

    if not subject:

        create_finding(
            title="Missing Audit Subject",
            severity="Medium",
            description="The audit subject has not been defined."
        )

        console.print(
            "\n[red]Planning stopped: Audit subject missing ⚠[/red]"
        )

        return False

    console.print(
        "[green]Audit subject validated ✓[/green]"
    )

    # Step 2

    objective = Confirm.ask(
        "\nIs the audit objective defined?"
    )

    if not objective:

        create_finding(
            title="Missing Audit Objective",
            severity="Medium",
            description="The audit objective has not been defined."
        )

        console.print(
            "\n[yellow]Planning stopped: Audit objective missing ⚠[/yellow]"
        )

        return False

    console.print(
        "[green]Audit objective validated ✓[/green]"
    )

    # Step 3

    scope = Confirm.ask(
        "\nIs the audit scope defined?"
    )

    if not scope:

        create_finding(
            title="Missing Audit Scope",
            severity="Medium",
            description="The audit scope has not been defined."
        )

        console.print(
            "\n[yellow]Planning stopped: Audit scope missing ⚠[/yellow]"
        )

        return False

    console.print(
        "[green]Audit scope validated ✓[/green]"
    )

    console.print(
        Panel(
            "Planning Completed Successfully ✓",
            title="Completed",
            border_style="green"
        )
    )

    return True