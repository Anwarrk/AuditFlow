from datetime import datetime
from time import sleep

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from rich.table import Table

from findings import create_finding



console = Console()


def show_reporting_workflow():

    workflow = """    
┌──────────────────┐        ┌──────────────────┐       ┌──────────────────────┐
│   Draft Report   │ ─────► │  Auditee Review  │ ─────►│ Final Audit Report   │  ─────► ◇ Outstanding Findings? ◇
└──────────────────┘        └──────────────────┘       └──────────────────────┘
                                                                                             │
                                                                               ┌─────────────┴─────────────┐
                                                                               │                           │
                                                                               ▼                           ▼
                                                              ┌──────────────────────────┐       ┌──────────────────┐
                                                              │ Corrective Action Plan   │       │  Audit Closed ✓  │
                                                              │          (CAP)           │       └──────────────────┘
                                                              └────────────┬─────────────┘
                                                                           │
                                                                           ▼
                                                              ┌──────────────────────────┐
                                                              │     Follow-Up Review     │
                                                              └────────────┬─────────────┘
                                                                           │
                                                                           ▼
                                                              ┌──────────────────────────┐
                                                              │     Pending Follow-Up    │
                                                              └──────────────────────────┘
"""

    console.print()

    console.print(
        Panel(
            Align.center(
                "[bold magenta]Phase 3[/bold magenta]\n\n"
                "[bold white]Reporting & Follow-Up[/bold white]\n\n"
                "Finalize the audit report and track corrective actions\n"
                "for outstanding findings, where required.\n\n"
                f"{workflow}"
            ),
            title="Reporting & Follow-Up Workflow",
            border_style="magenta"
        )
    )


def get_follow_up_date():

    while True:

        follow_up_date = console.input(
            "\n[bold cyan]Enter follow-up review date "
            "(YYYY-MM-DD): [/bold cyan]"
        ).strip()

        try:

            parsed_date = datetime.strptime(
                follow_up_date,
                "%Y-%m-%d"
            )

            if parsed_date.date() <= datetime.now().date():

                console.print(
                    "[red]"
                    "Follow-up date must be after today's date."
                    "[/red]"
                )

                continue

            return parsed_date.strftime("%d %b %Y")

        except ValueError:

            console.print(
                "[red]"
                "Invalid date format. Please use YYYY-MM-DD."
                "[/red]"
            )


def show_follow_up_summary(
    organization,
    framework,
    follow_up_date
):

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
        "Organization",
        organization
    )

    table.add_row(
        "Framework",
        framework
    )

    table.add_row(
        "Final Report",
        "[green]Issued ✓[/green]"
    )

    table.add_row(
        "Corrective Action Plan",
        "Agreed"
    )

    table.add_row(
        "Follow-Up Review Date",
        follow_up_date
    )

    table.add_row(
        "Reporting Status",
        "[green]Completed ✓[/green]"
    )

    table.add_row(
        "Finding Status",
        "[yellow]Open — Pending Follow-Up[/yellow]"
    )

    console.print()

    console.print(
        Panel(
            table,
            title="Follow-Up Schedule",
            border_style="yellow"
        )
    )


def show_closed_summary(
    organization,
    framework
):

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
        "Organization",
        organization
    )

    table.add_row(
        "Framework",
        framework
    )

    table.add_row(
        "Final Report",
        "[green]Issued ✓[/green]"
    )

    table.add_row(
        "Outstanding Findings",
        "[green]None[/green]"
    )

    table.add_row(
        "Audit Status",
        "[bold green]Closed ✓[/bold green]"
    )

    console.print()

    console.print(
        Panel(
            table,
            title="Reporting Summary",
            border_style="green"
        )
    )


def reporting_workflow(
    organization="Organization",
    framework="Selected Framework"
):

    show_reporting_workflow()

    input(
        "\nPress ENTER to begin Reporting & Follow-Up..."
    )

    draft_reviewed = Confirm.ask(
        "\nHas the draft report been reviewed with the auditee?"
    )

    if not draft_reviewed:

        create_finding(
            title="Draft Report Review Not Completed",
            severity="Medium",
            description=(
                "The draft audit report has not been reviewed "
                "with the auditee before finalization."
            )
        )

        console.print(
            "\n[red]"
            "Reporting stopped: "
            "The draft report must be reviewed with the auditee."
            "[/red]"
        )

        return {
            "completed": False,
            "follow_up_required": False,
            "follow_up_date": None,
            "audit_status": "Incomplete"
        }

    console.print(
        "[green]Draft Report Reviewed with Auditee ✓ [/green]"
    )

    report_approved = Confirm.ask(
        "\nHas the final audit report been approved?"
    )

    if not report_approved:

        create_finding(
            title="Final Audit Report Not Approved",
            severity="High",
            description=(
                "The final audit report has not been approved "
                "for issuance."
            )
        )

        console.print(
            "\n[red]"
            "Reporting stopped: "
            "The final audit report must be approved before issuance."
            "[/red]"
        )

        return {
            "completed": False,
            "follow_up_required": False,
            "follow_up_date": None,
            "audit_status": "Incomplete"
        }

    console.print(
        "\n[bold green]"
        "Final Audit Report Approved and Issued ✓"
        "[/bold green]"
    )

    sleep(1)

    outstanding_findings = Confirm.ask(
        "\nAre there outstanding findings requiring corrective action?"
    )

    if not outstanding_findings:

        console.print(
            "\n[green]"
            "No Outstanding Findings Requiring Action ✓"
            "[/green]"
        )

        show_closed_summary(
            organization,
            framework
        )

        return {
            "completed": True,
            "follow_up_required": False,
            "follow_up_date": None,
            "audit_status": "Closed"
        }

    console.print(
        Panel.fit(
            "[bold yellow]Corrective Action Plan (CAP)[/bold yellow]",
            title="Follow-Up Required",
            border_style="yellow"
        )
    )

    cap_agreed = Confirm.ask(
        "\nHas a corrective action plan been agreed with the auditee?"
    )

    if not cap_agreed:

        create_finding(
            title="Corrective Action Plan Not Agreed",
            severity="High",
            description=(
                "Outstanding findings require a corrective action plan, "
                "but no plan has been agreed with the auditee."
            )
        )

        console.print(
            "\n[red]"
            "Reporting stopped: "
            "A corrective action plan is required."
            "[/red]"
        )

        return {
            "completed": False,
            "follow_up_required": True,
            "follow_up_date": None,
            "audit_status": "Incomplete"
        }

    console.print(
        "[green]Corrective Action Plan Agreed ✓ [/green]"
    )

    follow_up_date = get_follow_up_date()

    show_follow_up_summary(
        organization,
        framework,
        follow_up_date
    )

    console.print(
        "\n[yellow]"
        "Outstanding findings will remain open "
        "until the follow-up review is completed."
        "[/yellow]"
    )

    return {
        "completed": True,
        "follow_up_required": True,
        "follow_up_date": follow_up_date,
        "audit_status": "Pending Follow-Up"
    }