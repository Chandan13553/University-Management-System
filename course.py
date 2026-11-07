from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import box
from university import myuni
console = Console()
class Course:
    def __init__(self):
        self.courses = []
        self.course_assigned = []
        self.student_enroll = []
    def create_course(self,course_name,course_code,credit_hour,max_students):  
        if credit_hour <= 0:
            console.print("[bold yellow]Credit hour must be greater than zero.[/bold yellow]")  
            return 
        if max_students <= 0:
            console.print("[bold yellow]Maximum number of students must be greater than zero.[/bold yellow]") 
            return
        if not course_name.strip():
            console.print("[bold yellow]Course name can't be empty.[/bold yellow]")
            return
        for ch in self.courses:
            if ch[0].strip() == course_name.strip():
                console.print(f"[bold yellow]Course with name {course_name} already exists.[/bold yellow]")
                return
            if ch[1] == course_code:
                console.print(f"[bold yellow]Course with course code {course_code} already exists.[/bold yellow]")
                return
        self._course_name = course_name.strip()
        self._course_code = course_code.strip()
        self._credit_hour = credit_hour
        self._max_students = max_students
        self.courses.append([course_name,course_code,credit_hour,max_students])
        myuni._courses.append([course_name,course_code,credit_hour,max_students])
        self.course_assigned.append([])
        self.student_enroll.append([])
        
        console.print(f"[bold green]Course {self._course_name} created successfully.[/bold green]")
   
    def total_enrolled(self):
        total = 0
        i = 0
        for ch in self.student_enroll:
            total += len(ch)  
            i += 1  
        return total
    def available_seats(self):
        total_seats = 0
        i = 0
        for ch in self.courses:
            total_seats += ch[3]
            i += 1 
        return total_seats - self.total_enrolled() 
    def full_courses(self):
        full = 0
        i = 0
        for ch in self.courses:
            if len(self.student_enroll[i]) == ch[3]:
                full += 1
            i += 1
        return full        
    def unassigned_courses(self):
        i = 0
        for ch in self.course_assigned:
            if ch != []:
                i += 1
        return len(self.courses) - i        
    def display(self,course_id):
        table = Table(
                    box=None,
                    show_header=False
                )
        table.add_column("Subject",style="sky_blue1")
        table.add_column("Information",style="sky_blue1")
        i = 0
        for ch in self.courses:
            if ch[1] == course_id.strip():
                break
            i += 1
        try:
            table.add_row("Course Name",f"{self.courses[i][0]}")
            table.add_row("Course Code",f"{self.courses[i][1]}")
            table.add_row("Credit Hours",f"{self.courses[i][2]}")
            table.add_row("Capacity",f"{self.courses[i][3]}")
            table.add_row("Enrolled students",f"{len(self.student_enroll[i])}")
          
            if self.course_assigned[i] != []:
                table.add_row("Professor",f"{self.course_assigned[i][0][0]}")
                
            else:
                table.add_row("No professor is assigned for this course","")
            panel = Panel(
                        table,
                        title="COURSE INFORMATION",
                        style="bold",
                        border_style="bold green",
                        box=box.ROUNDED,
                        padding=(1, 2)
                        )
            console.print(panel)    
        except IndexError:
            console.print("[bold red]Course not found.[/bold red]")      
    def total_information(self):
        table = Table(
                    box=None,
                    show_header=False
                    )
        table.add_column("Subject",style="sky_blue1")
        table.add_column("Information",style="sky_blue1")
        table.add_row("Total Enrollments",f"{self.total_enrolled()}")
        table.add_row("Available seats",f"{self.available_seats()}")
        table.add_row("Full Courses",f"{self.full_courses()}")
        table.add_row("Unassigned Courses",f"{self.unassigned_courses()}")
        panel = Panel(
                    table,
                    title="COURSE STATISTICS",
                    style="bold",
                    border_style="bold green",
                    box=box.ROUNDED,
                    padding=(1, 2)
                    )
        console.print(panel) 
        


c = Course()

#cours = Course("Data Structure and Algorithms","ENCT 401",3,96)
#cours.display()


      

