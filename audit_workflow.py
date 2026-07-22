from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from rich.align import Align

from findings import create_finding


console = Console()



def show_decision_tree():


    tree = """

              PLANNING PHASE

                   START
                     |
                     ↓

              Validate Scope
                     |
                     ↓

            Validate Objectives
                     |
                     ↓

          Validate Stakeholders
                     |
                     ↓

           Planning Completed


       If validation fails:
          Create Finding

"""


    console.print(
        Panel(
            Align.center(tree),
            title="Planning Assessment Flow 🌳",
            border_style="green"
        )
    )


    sleep(2)



def planning_workflow():


    show_decision_tree()



    console.print(
        "\n[bold cyan]PLANNING PHASE[/bold cyan]"
    )


    sleep(1)



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
            "\n[red]Planning stopped: Scope missing ⚠[/red]"
        )


        return False



    console.print(
        "[green]Audit scope confirmed ✓[/green]"
    )




    objectives = Confirm.ask(
        "\nAre audit objectives defined?"
    )



    if not objectives:


        create_finding(
            title="Missing Audit Objectives",
            severity="Medium",
            description="Audit objectives are not documented."
        )


        console.print(
            "\n[yellow]Planning stopped: Objectives missing ⚠[/yellow]"
        )


        return False




    console.print(
        "[green]Audit objectives confirmed ✓[/green]"
    )




    stakeholders = Confirm.ask(
        "\nAre stakeholders identified?"
    )



    if not stakeholders:


        create_finding(
            title="Missing Stakeholder Identification",
            severity="Low",
            description="Audit stakeholders have not been identified."
        )


        console.print(
            "\n[yellow]Planning stopped: Stakeholders missing ⚠[/yellow]"
        )


        return False




    console.print(
        "[green]Stakeholders confirmed ✓[/green]"
    )




    console.print(

        Panel(
            "Planning Assessment Completed ✓",
            title="Completed",
            border_style="green"
        )

    )


    return True