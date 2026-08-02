from time import sleep

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from rich.rule import Rule
from rich.table import Table

from findings import create_finding


console = Console()


def show_fieldwork_intro():

    console.print()

    console.print(
        Panel(
            Align.center(
                "[bold cyan]Phase 2[/bold cyan]\n\n"
                "[bold white]Fieldwork & Documentation[/bold white]\n\n"
                "Assess security controls, collect audit evidence,\n"
                "evaluate control effectiveness, and document results."
            ),
            title="Audit Process",
            border_style="blue"
        )
    )

    input(
        "\nPress ENTER to begin Fieldwork & Documentation..."
    )


def show_progress(current, total):

    completed = "█" * current
    remaining = "░" * (total - current)
    percentage = int((current / total) * 100)

    console.print()

    console.print(
        Panel.fit(
            Align.center(
                "[bold cyan]Fieldwork Progress[/bold cyan]\n\n"
                f"[green]{completed}[/green]"
                f"[dim]{remaining}[/dim]\n\n"
                f"[bold]{percentage}% Completed[/bold]"
            ),
            border_style="cyan"
        )
    )


def show_activity(number, total, title):

    console.print()

    console.print(
        Rule(
            f"[bold cyan]Activity {number} / {total}[/bold cyan]"
        )
    )

    console.print(
        Panel.fit(
            f"[bold green]{title}[/bold green]",
            border_style="green"
        )
    )


def show_evidence_checklist():

    table = Table(
        show_header=True,
        header_style="bold cyan",
        expand=False
    )

    table.add_column(
        "Evidence Requirement",
        min_width=24
    )

    table.add_column(
        "Status",
        justify="center",
        min_width=8
    )

    table.add_row(
        "Relevant",
        "[green]✓[/green]"
    )

    table.add_row(
        "Valid",
        "[green]✓[/green]"
    )

    table.add_row(
        "Properly Documented",
        "[green]✓[/green]"
    )

    console.print()

    console.print(
        Panel.fit(
            table,
            title="Evidence Validation Checklist",
            border_style="cyan"
        )
    )

    console.print(
        Panel(
            "[bold yellow]Evidence Note[/bold yellow]\n\n"
            "Evidence should be current and properly documented.\n\n"
            "[white]Examples:[/white]\n"
            "• Relevant to the control being assessed\n"
            "• Dated or time-stamped\n"
            "• Approved or authorized, where applicable",
            border_style="yellow"
        )
    )


def show_phase_completion():

    console.print()

    console.print(
        Panel(
            Align.center(
                "[bold green]"
                "Fieldwork & Documentation Completed ✓"
                "[/bold green]\n\n"
                "Security controls have been assessed,\n"
        "audit evidence has been evaluated,\n"
        "and audit results have been documented.\n\n"
            ),
            title="Phase 2 Completed",
            border_style="green"
        )
    )


def fieldwork_workflow():

    total_activities = 4

    show_fieldwork_intro()

    # Activity 1: Assess Security Control
    show_progress(
        1,
        total_activities
    )

    show_activity(
        1,
        total_activities,
        "Assess Security Control"
    )

    control_assessed = Confirm.ask(
        "\nHas the selected security control been assessed?"
    )

    if not control_assessed:

        create_finding(
            title="Security Control Not Assessed",
            severity="High",
            description=(
                "The selected security control has not been assessed."
            )
        )

        console.print(
            "\n[red]"
            "Fieldwork stopped: "
            "Control assessment is incomplete."
            "[/red]"
        )

        return False

    console.print(
        "[green]Security Control Assessed ✓[/green]"
    )

    sleep(1)

    # Activity 2: Collect Audit Evidence
    show_progress(
        2,
        total_activities
    )

    show_activity(
        2,
        total_activities,
        "Collect Audit Evidence"
    )

    show_evidence_checklist()

    evidence_collected = Confirm.ask(
        "\nHas supporting audit evidence been collected?"
    )

    if not evidence_collected:

        create_finding(
            title="Supporting Audit Evidence Missing",
            severity="High",
            description=(
                "Supporting audit evidence has not been collected "
                "for the selected security control."
            )
        )

        console.print(
            "\n[red]"
            "Fieldwork stopped: "
            "Supporting audit evidence is missing."
            "[/red]"
        )

        return False

    console.print(
        "[green]Supporting Audit Evidence Collected ✓[/green]"
    )

    sleep(1)

    # Activity 3: Evaluate Control
    show_progress(
        3,
        total_activities
    )

    show_activity(
        3,
        total_activities,
        "Evaluate Control"
    )

    evidence_acceptable = Confirm.ask(
        "\nIs the evidence relevant, valid, and properly documented?"
    )

    if not evidence_acceptable:

        create_finding(
            title="Audit Evidence Quality Issue",
            severity="Medium",
            description=(
                "The collected audit evidence is not relevant, valid, "
                "or properly documented."
            )
        )

        console.print(
            "\n[yellow]"
            "Evidence quality issue identified and documented."
            "[/yellow]"
        )

    control_effective = Confirm.ask(
        "\nDoes the security control meet its intended objective?"
    )

    if not control_effective:

        create_finding(
            title="Control Weakness Identified",
            severity="High",
            description=(
                "The evaluated security control does not meet "
                "its intended objective."
            )
        )

        console.print(
            "\n[yellow]"
            "Control weakness identified and documented."
            "[/yellow]"
        )

    else:

        console.print(
            "[green]Control Meets Its Intended Objective ✓[/green]"
        )

    sleep(1)

    # Activity 4: Document Results & Findings
    show_progress(
        4,
        total_activities
    )

    show_activity(
        4,
        total_activities,
        "Document Results & Findings"
    )

    results_documented = Confirm.ask(
        "\nHave the audit results and findings been documented?"
    )

    if not results_documented:

        create_finding(
            title="Audit Results Not Documented",
            severity="Medium",
            description=(
                "The audit results and identified findings "
                "have not been documented."
            )
        )

        console.print(
            "\n[yellow]"
            "Fieldwork stopped: "
            "Audit results and findings are not documented."
            "[/yellow]"
        )

        return False

    console.print(
        "[green]Audit Results and Findings Documented ✓[/green]"
    )

    sleep(1)

    show_phase_completion()

    return True

