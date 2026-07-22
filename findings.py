from rich.console import Console
from rich.panel import Panel


console = Console()


finding_counter = 0



def create_finding(title, severity, description):


    global finding_counter


    finding_counter += 1



    console.print(

        Panel(

            f"""
[bold red]Finding Created ⚠[/bold red]


ID       : {finding_counter}

Title    : {title}

Severity : {severity}

Status   : Open


Description:
{description}

""",

            title="Audit Finding",

            border_style="red"

        )

    )


    return finding_counter