from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import box
from person import person
from course import c
from university import myuni
console = Console()
class Professor(person):
    def __init__(self):
        self._course_assigned = []
        self._professor = []
    def register_professor(self,name,age,gender,prof_id,department):
        if age < 30:
            console.print("[bold yellow]Professors below age 30 are not elidgible.[/bold yellow]")
            return
        for ch in self._professor:
            if ch[3] == prof_id:
                console.print("[bold yellow]Professor with this Professor ID already exists.[/bold yellow]")
                return
        if not name.strip():
            console.print("[bold red]Professor Name can't be empty.[/bold red]")
            return
        for ch in self._professor:
            if ch[3] == prof_id:
                console.print(f"[bold yellow]Professor with ID {prof_id} already exists.[/bold yellow]")
                return
        super().__init__(name,age,gender)
        self._prof_id = prof_id.strip()
        self._department = department.strip()
        myuni._professors.append([self._name,self._age,self._gender,self._prof_id,self._department])
        self._professor.append([name,age,gender,prof_id,department])
        self._course_assigned.append([])
        
        console.print(f"[bold green]Professor {self._name} has been registered successfully.[/bold green]")
    def assign_course(self,professor_id,course_id):
        i = 0
        for ch in self._professor:
            if ch[3] == professor_id.strip():
                break
            i += 1
        if i == len(self._professor):
            console.print("[bold red]Professor not found.[/bold red]")  
            return
        for ch in self._course_assigned[i]:
            if ch[1] == course_id.strip():
                console.print(f"[bold yellow]{self._course_assigned[i][0]} is already assigned to {self._professor[i][0]}[/bold yellow]")
                return
        j = 0
        for ch in c.courses:
            if ch[1] == course_id.strip():
                self._course_assigned[i].append(ch)
                c.course_assigned[j].append(self._professor[i])
                console.print(f"[bold green]Course {ch[0]} is successfully assigned to {self._professor[i][0]}.[/bold green]")
                break
            j += 1
        if j == len(c.courses):
            console.print("[bold red]Course not found.[/bold red]")  
            return  
    def remove_course_professor(self,professor_id,course_id):
        i = 0
        for ch in self._professor:
            if ch[3] == professor_id.strip():
                break
            i += 1
        if i == len(self._professor):
                console.print("[bold red]Professor not found.[/bold red]")  
                return        
        j = 0 
        l = 0 
        for ch in c.courses:
            if ch[1] == course_id:
                break
            j = j+1
        if j == len(c.courses):
            console.print("[bold red]Course not found![/bold red]")   
            return
        for m in range(len(self._course_assigned[i])):    #[[[courses],[courses]],[]]
                    if self._course_assigned[i][m][1] == course_id.strip():   
                        self._course_assigned[i].remove(self._course_assigned[i][m])
                        c.course_assigned[j].remove(self._professor[i])  
                        console.print(f"[bold green]Course {ch[0]} is successfully removed.[/bold green]")
                        return
                    
                    
        console.print(f"[bold yellow]{self._professor[i][0]} was not enrolled in this course.[/bold yellow]")            
    def display(self,profid):
            table = Table(
                    show_header=False,
                    box=None
                    )
            table.add_column("Subject",style="sky_blue1")
            table.add_column("Information",style="sky_blue1")
            i = 0
            for ch in self._professor:
                if ch[3] == profid.strip():
                    break
                i += 1
            try:
                table.add_row("Name",f"{self._professor[i][0]}")
                table.add_row("Age",f"{self._professor[i][1]}")
                table.add_row("Gender",f"{self._professor[i][2]}")
                table.add_row("Courses assigned",f"{', '.join(ch[0] for ch in self._course_assigned[i])}")
                panel = Panel(
                            table,
                            title="PROFESSOR INFORMATION",
                            style="bold",
                            border_style="bold green",
                            box=box.ROUNDED,
                            padding=(1, 2)
                            )
                console.print(panel)   
            except IndexError:
                console.print("[bold red]Professor not found.[/bold red]")


p = Professor()
#p = Professor("Chandan",26,"Male","BCTAB","Computer Science") 
#p.assign_course("Data Structure and Algorithms") 
#p.display() 
#p.remove_course("Data Structure and Algorithms")         

