from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()

finding_counter = 0
findings = []


def create_finding(title, severity, description):

    global finding_counter

    finding_counter += 1

    finding_id = f"AF-{finding_counter:03d}"

    severity_colors = {
        "High": "red",
        "Medium": "yellow",
        "Low": "cyan"
    }

    color = severity_colors.get(severity, "white")

    finding = {
        "id": finding_id,
        "title": title,
        "severity": severity,
        "status": "Open",
        "description": description
    }

    findings.append(finding)

    console.print(
        Panel(
            f"""
[bold red]Audit Finding Recorded[/bold red]

[bold]Finding ID :[/bold] {finding_id}

[bold]Title      :[/bold] {title}

[bold]Severity   :[/bold] [{color}]{severity}[/{color}]

[bold]Status     :[/bold] [red]Open[/red]

[bold]Description[/bold]

{description}
""",
            title="Audit Finding",
            border_style=color
        )
    )

    return finding_id


def get_findings():

    return findings.copy()


def get_findings_count():

    return len(findings)


def has_open_findings():

    return any(
        finding["status"] == "Open"
        for finding in findings
    )


def get_findings_summary():

    summary = {
        "total": len(findings),
        "high": 0,
        "medium": 0,
        "low": 0,
        "open": 0
    }

    for finding in findings:

        severity = finding["severity"].lower()

        if severity in summary:
            summary[severity] += 1

        if finding["status"] == "Open":
            summary["open"] += 1

    return summary


def show_findings_summary():

    summary = get_findings_summary()

    if summary["total"] == 0:

        console.print(
            Panel(
                "[green]No audit findings were recorded.[/green]",
                title="Findings Summary",
                border_style="green"
            )
        )

        return

    table = Table(
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column(
        "Finding ID",
        style="bold"
    )

    table.add_column(
        "Title"
    )

    table.add_column(
        "Severity",
        justify="center"
    )

    table.add_column(
        "Status",
        justify="center"
    )

    for finding in findings:

        severity = finding["severity"]

        severity_colors = {
            "High": "red",
            "Medium": "yellow",
            "Low": "cyan"
        }

        color = severity_colors.get(
            severity,
            "white"
        )

        table.add_row(
            finding["id"],
            finding["title"],
            f"[{color}]{severity}[/{color}]",
            "[red]Open[/red]"
        )

    console.print(
        Panel(
            table,
            title=(
                f"Audit Findings Summary "
                f"({summary['total']} Total)"
            ),
            border_style="red"
        )
    )

    console.print(
        Panel.fit(
            f"""
[bold red]High:[/bold red] {summary["high"]}

[bold yellow]Medium:[/bold yellow] {summary["medium"]}

[bold cyan]Low:[/bold cyan] {summary["low"]}

[bold white]Open:[/bold white] {summary["open"]}
""",
            title="Finding Counts",
            border_style="cyan"
        )
    )


def reset_findings():

    global finding_counter

    finding_counter = 0
    findings.clear()