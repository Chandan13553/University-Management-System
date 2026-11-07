from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import box
from student import s
from professor import p
from course import c
console = Console()
class SearchRecord:
    def search_record(self):
        table = Table(
                    show_header=False,
                    box=None 
                    )
        table.add_column("Option",style="yellow")
        table.add_column("Operation",style="white")
        table.add_row("1","Search Student")
        table.add_row("2","Search Professor")
        table.add_row("3","Search Course")
        table.add_row("4","Exit\n")
        panel = Panel(
                   table,
                   title="SEARCH RECORDS",
                   style="bold",
                   border_style="bold green",
                   box=box.ROUNDED,
                   padding=(1, 2)
                   ) 
        console.print(panel)
        while True:
            try:
                choice = int(console.input("[bold cyan]Enter your choice: [/bold cyan]"))
            except ValueError:
                console.input("[bold yellow]Please enter a valid numeric choice.[/bold yellow]")
                continue
            match choice:
                case 1:
                    sid = console.input("[bold cyan]Enter Student ID : [/bold cyan]")
                    s.display(sid)
                case 2:
                    pid = console.input("[bold cyan]Enter Professor ID : [/bold cyan]")
                    p.display(pid)
                case 3:
                    course_code = console.input("[bold cyan]Enter Course code : [/bold cyan]")
                    c.display(course_code)  
                case 4:
                    break
                case _:
                    console.input("[bold red]Invalid Choice[/bold red]") 
            key = console.input("[bold cyan]\nDo you want to continue to searching records(y/n) ? : [/bold cyan]") 
            if key.strip().lower() == 'y':
                continue
            else:
                break    
                         


search = SearchRecord()    