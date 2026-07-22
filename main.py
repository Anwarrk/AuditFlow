from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.align import Align

from audit_workflow import planning_workflow


console = Console()


def banner():

    console.print(
        Panel(
            Align.center(
                "[bold cyan]            AuditFlow 🔍[/bold cyan]\n\n"
                "[white]Interactive Audit Workflow Assistant[/white]"
            ),
            border_style="cyan",
            expand=False
        )
    )


def show_audit_process():

    process = """

       ┌──────────────┐         ┌──────────────────────┐         ┌──────────────────────┐
       │   Planning   │  --->   │   Fieldwork &        │  --->   │   Reporting &        │
       │              │         │   Documentation      │         │   Follow-Up          │
       └──────────────┘         └──────────────────────┘         └──────────────────────┘

"""

    console.print(
        Panel(
            Align.center(process),
            title=" Audit Process ",
            border_style="blue"
        )
    )


def show_session(auditor, organization, framework):

    console.print(
        Panel(
            f"""
[bold cyan]Welcome, Auditor[/bold cyan] [bold green]{auditor}[/bold green]!


[white]Organization:[/white] {organization}

[white]Framework:[/white] {framework}


[green]Audit session initialized successfully ✓[/green]
""",
            title="Audit Session",
            border_style="green"
        )
    )


def show_completion(auditor, framework):

    console.print(
        Panel(
            f"""
[bold green]Planning Assessment Completed ✓[/bold green]


Auditor   : {auditor}

Framework : {framework}


Next Audit Phases:

1. Fieldwork & Documentation
   • Evidence Collection
   • Control Testing


2. Reporting & Follow-Up
   • Findings Documentation
   • Corrective Actions Tracking


Thank you for using AuditFlow.
Have a productive day!
""",
            title="Planning Summary",
            border_style="green"
        )
    )


def start_audit():

    console.clear()

    console.print(
        "\n[bold green]Initialize Audit Session[/bold green]\n"
    )


    auditor = input("Auditor Name : ")

    organization = input("Organization : ")


    console.print(
        "\n[bold cyan]Audit Framework[/bold cyan]\n"
    )

    console.print("[1] ISO 27001")
    console.print("[2] NCA ECC")


    framework_choice = input("\nChoose : ")


    if framework_choice == "1":

        framework = "ISO 27001"


    elif framework_choice == "2":

        framework = "NCA ECC"


    else:

        framework = "Unknown"



    console.clear()


    show_session(
        auditor,
        organization,
        framework
    )


    console.print()


    show_audit_process()



    input(
        "\nPress ENTER to start audit execution..."
    )


    console.clear()


    result = planning_workflow()



    if result:

        console.print()

        show_completion(
            auditor,
            framework
        )


        input(
            "\nPress ENTER to return to main menu..."
        )



def main():

    while True:

        console.clear()

        banner()


        console.print()

        console.print(
            "[cyan][1][/cyan] Start Audit"
        )

        console.print(
            "[red][2][/red] Exit\n"
        )


        choice = input(
            "Select option: "
        )


        if choice == "1":

            start_audit()



        elif choice == "2":

            console.print(
                "\n[bold green]Thank you for using AuditFlow.[/bold green]"
            )

            break



        else:

            console.print(
                "\n[red]Invalid option[/red]"
            )

            sleep(1)



if __name__ == "__main__":

    main()