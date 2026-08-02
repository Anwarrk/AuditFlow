from datetime import datetime
from time import sleep

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from audit_workflow import planning_workflow
from audit_process_2 import fieldwork_workflow
from audit_process_3 import reporting_workflow
from findings import reset_findings


console = Console()


def banner():

    console.print(
        Panel(
            Align.center(
                "[bold cyan]AuditFlow 🔍[/bold cyan]\n\n"
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
            title="Audit Process",
            border_style="blue"
        )
    )


def show_session(
    auditor,
    organization,
    framework,
    session_id,
    date
):

    console.print(
        Panel(
            f"""
[bold cyan]Welcome, Auditor[/bold cyan] [bold green]{auditor}[/bold green]!

[white]Session ID:[/white] {session_id}

[white]Date:[/white] {date}

[white]Organization:[/white] {organization}

[white]Framework:[/white] {framework}

[green]Audit session initialized successfully ✓[/green]
""",
            title="Audit Session",
            border_style="green"
        )
    )


def show_completion(
    auditor,
    organization,
    framework,
    session_id,
    date,
    reporting_result
):

    follow_up_required = reporting_result["follow_up_required"]
    follow_up_date = reporting_result["follow_up_date"]

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 2)
    )

    table.add_column(
        "Field",
        style="bold cyan"
    )

    table.add_column(
        "Value",
        style="white"
    )

    table.add_row(
        "Session ID",
        session_id
    )

    table.add_row(
        "Audit Date",
        date
    )

    table.add_row(
        "Auditor",
        auditor
    )

    table.add_row(
        "Organization",
        organization
    )

    table.add_row(
        "Framework",
        framework
    )

    table.add_row(
        "",
        ""
    )

    table.add_row(
        "Planning",
        "[green]Completed ✓[/green]"
    )

    table.add_row(
        "Fieldwork & Documentation",
        "[green]Completed ✓[/green]"
    )

    table.add_row(
        "Reporting & Follow-Up",
        "[green]Completed ✓[/green]"
    )

    table.add_row(
        "",
        ""
    )

    table.add_row(
        "Final Report",
        "[green]Issued ✓[/green]"
    )

    if follow_up_required:

        table.add_row(
            "Audit Status",
            "[yellow]Pending Follow-Up[/yellow]"
        )

        table.add_row(
            "Finding Status",
            "[yellow]Open — Pending Follow-Up[/yellow]"
        )

        table.add_row(
            "Follow-Up Date",
            follow_up_date
        )

        border_style = "yellow"

    else:

        table.add_row(
            "Audit Status",
            "[bold green]Closed ✓[/bold green]"
        )

        table.add_row(
            "Outstanding Findings",
            "[green]None[/green]"
        )

        border_style = "green"

    console.print()

    console.print(
        Panel(
            table,
            title="Audit Session Summary",
            border_style=border_style
        )
    )

    console.print(
        Panel(
            Align.center(
                "[bold cyan]Thank you for using AuditFlow.[/bold cyan]\n\n"
                "[white]We wish you a successful audit.[/white]"
            ),
            border_style="cyan"
        )
    )


def select_framework():

    while True:

        console.print(
            "\n[bold cyan]Audit Framework[/bold cyan]\n"
        )

        console.print("[1] ISO 27001")
        console.print("[2] NCA ECC")

        framework_choice = input(
            "\nChoose : "
        ).strip()

        if framework_choice == "1":

            return "ISO 27001"

        if framework_choice == "2":

            return "NCA ECC"

        console.print(
            "\n[red]Invalid framework selection. Try again.[/red]"
        )


def start_audit():

    reset_findings()

    console.clear()

    console.print(
        "\n[bold green]Initialize Audit Session[/bold green]\n"
    )

    auditor = input(
        "Auditor Name : "
    ).strip()

    organization = input(
        "Organization : "
    ).strip()

    framework = select_framework()

    now = datetime.now()

    session_id = now.strftime(
        "AF-%Y%m%d-%H%M%S"
    )

    date = now.strftime(
        "%d %b %Y"
    )

    console.clear()

    show_session(
        auditor,
        organization,
        framework,
        session_id,
        date
    )

    console.print()

    show_audit_process()

    input(
        "\nPress ENTER to continue to Planning..."
    )

    console.clear()

    planning_result = planning_workflow()

    if not planning_result:
        input(
            "\nPress ENTER to return to main menu..."
        )

        return

    input(
        "\nPress ENTER to continue to "
        "Fieldwork & Documentation..."
    )

    console.clear()

    fieldwork_result = fieldwork_workflow()

    if not fieldwork_result:

        input(
            "\nPress ENTER to return to main menu..."
        )

        return

    input(
        "\nPress ENTER to continue to "
        "Reporting & Follow-Up..."
    )

    console.clear()

    reporting_result = reporting_workflow(
        organization=organization,
        framework=framework
    )

    if not reporting_result["completed"]:

        input(
            "\nPress ENTER to return to main menu..."
        )

        return

    show_completion(
        auditor,
        organization,
        framework,
        session_id,
        date,
        reporting_result
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
        ).strip()

        if choice == "1":

            start_audit()

        elif choice == "2":

            console.print(
                "\n[bold green]"
                "Thank you for using AuditFlow."
                "[/bold green]"
            )

            break

        else:

            console.print(
                "\n[red]Invalid option[/red]"
            )

            sleep(1)


if __name__ == "__main__":

    main()