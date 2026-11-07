from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import box
console = Console()
class University:
    def __init__(self):
        self._students = []
        self._professors = []
        self._courses = []
    def display(self):
        table = Table(
            box=None,
            show_header=False
        )
        table.add_column("Subject",style="sky_blue1")
        table.add_column("Information",style="sky_blue1")
        table.add_row("Total students",f"{len(self._students)}")
        table.add_row("Total Professors",f"{len(self._professors)}")
        table.add_row("Total Courses",f"{len(self._courses)}")
        panel = Panel(
            table,
            title="UNIVERSITY STATISTICS",
            style="bold",
            border_style="bold green",
            box=box.ROUNDED,
            padding=(1, 2)
            )
        console.print(panel)
       
        
           
        




myuni = University()            
        