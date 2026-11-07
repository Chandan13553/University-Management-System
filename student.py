from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import box
from person import person
from course import c
from university import myuni
class InvalidMarks(Exception):
    pass

console = Console()
class student(person):
    def __init__(self):
        self.student_courses = []
        self._student = []
        self._student_grades = []
        self._student_marks = []
    def register_student(self,name,age,gender,studentid):
        if age < 18:
            console.print("[bold yellow]Student below age 18 are not elidgible.[/bold yellow]")
            return
        for ch in self._student:
            if ch[3] == studentid.strip():
                console.print("[bold yellow]Student with this Student ID already exists.[/bold yellow]")
                return
        if not name.strip():
            console.print("[bold red]Student Name can't be empty.[/bold red]")
            return
        super().__init__(name,age,gender)
        self._studentid = studentid.strip()
        myuni._students.append([self._name,self._age,self._gender,self._studentid])
        self._student.append([self._name,self._age,self._gender,self._studentid])
        self.student_courses.append([])
        self._student_grades.append([])
        self._student_marks.append([])

        console.print(f"[bold green]Student {self._student[-1][0]} has been registered successfully.[/bold green]")
        

    def enroll_course(self,stuid,course_id):        
        i = 0
        for ch in self._student:
            if ch[3] == stuid.strip():
                break
            i += 1
        if i == len(self._student):
            print("Student not found.")
            return    
        for ch in self.student_courses[i]:
            if ch[1] == course_id.strip():
                console.print(f"[bold yellow]{self._student[i][0]} is already enrolled in this course.[/bold yellow]")
                return         
        j = 0
        for ch in c.courses:
            if ch[1] == course_id.strip():
                break
            j += 1
        if j == len(c.courses):
            console.print("[bold red]Course not found.[/bold red]")
            return     
        if c.courses[j][3] - len(c.student_enroll[j]) <= 0:
            console.print(f"[bold magenta]Course capacity is reached,{self._student[i][0]} can't be enrolled.[/bold magenta]")
            return
        self.student_courses[i].append(ch)
        c.student_enroll[j].append(self._student[i])
        console.print(f"[bold green]{self._student[i][0]} is successfully enrolled in Course {ch[0]}.[/bold green]")          
           
    def remove_course_student(self,stuid,course_id):
        i = 0
        for ch in self._student:
            if ch[3] == stuid.strip():
                break
            i += 1
        if i == len(self._student):
            console.print("[bold red]Student not found.[/bold red]")
            return   
        j = 0    
        k = 0
        l = 0
        for ch in c.courses:
            if ch[1] == course_id:
                break
            l = l+1
        if l == len(c.courses):
            console.print("[bold red]Course not found![/bold red]")   
            return
      
        for m in range(len(self.student_courses[i])):    #[[[courses],[courses]],[]]
            if self.student_courses[i][m][1] == course_id.strip():
                
                    self._student_grades[i].remove(self._student_grades[i][m])
                    self._student_marks[i].remove(self._student_marks[i][m])
                    self.student_courses[i].remove(self.student_courses[i][m])
                    c.student_enroll[j].remove(self._student[i])  
                    console.print(f"[bold green]Course {ch[0]} is successfully removed.[/bold green]")
                    break
            
            if m == len(self.student_courses[i]) - 1:
                console.print(f"[bold yellow]{self._student[i][0]} was not enrolled in this course.[/bold yellow]") 
                return 
         
    def marks_to_grade(self,mark):
        if mark < 40:
            return 0
        elif mark >= 40 and mark < 50:
            return 2.3
        elif mark >= 50 and mark < 60:
            return 2.7
        elif mark >= 60 and mark < 70:
            return 3.0
        elif mark >= 70 and mark < 80:
            return 3.3
        elif mark >= 80 and mark < 90:
            return 3.7
        else:
            return 4.0
        
                
    def record_marks(self,stu_id):
        i = 0
        for ch in self._student:
            if ch[3] == stu_id.strip():
                break
            i += 1
        if i == len(self._student):
            console.print("[bold red]Student not found.[/bold red]")
            return    
        console.print(f"[sky_blue1]\nName : {self._student[i][0]}[/sky_blue1]")
        console.print(f"[sky_blue1]Age : {self._student[i][1]}[/sky_blue1]")
        console.print(f"[sky_blue1]Gender : {self._student[i][2]}[/sky_blue1]")
        if  self._student_grades[i] != []:
            mark_choice = console.input(f"[bright_cyan]The marks of {self._student[i][0]} is already recorded.\nDo you want to replace it(y/n) ? : [/bright_cyan]")
            if mark_choice.strip() == 'y' or mark_choice.strip() == 'Y':
                 self._student_grades[i].clear()
            else:
                return     
        for j in range(len(self.student_courses[i])):
                     while(True):
                        try:
                            mark = float(console.input(f"[bright_cyan]Enter mark obtained in {self.student_courses[i][j][0]} : [/bright_cyan]"))
                            if mark < 0 or mark > 100:
                                raise InvalidMarks("Marks must be between 0 - 100!")
                            self._student_grades[i].append(self.marks_to_grade(mark))
                            self._student_marks[i].append(mark)
                            break
                        except ValueError:
                            console.print("[bold red]Marks must be numeric![/bold red]")
                        except InvalidMarks as e:
                            console.print(f"[bold red]{e}[/bold red]")                
        console.print("[bold green]Marks has been recorded.[/bold green]")     

    def student_stat(self,stuid):
        table = Table(
            show_header=False,
            box=None
        )
        table.add_column("Subject",style="sky_blue1")
        table.add_column("Information",style="sky_blue1")
        i = 0
        for ch in self._student:
            if ch[3] == stuid.strip():
                break
            i += 1 
        if i == len(self._student):
            console.print("[bold red]Student not found![/bold red]")
            return    
        total_subs = 0
        total_credit = 0 
        try:
            for j in range(len(self._student_grades[i])):
                total_credit += self._student_grades[i][j]*self.student_courses[i][j][2]
                total_subs += self.student_courses[i][j][2]
                if self._student_grades[i][j] == 0:
                    GPA = 0
                    break
                else:
                    GPA = float(total_credit/total_subs)
            table.add_row("Name",f"{self._student[i][0]}") 
            table.add_row("Age",f"{self._student[i][1]}") 
            table.add_row("Gender",f"{self._student[i][2]}")
            table.add_row("Studenr ID",f"{self._student[i][3]}")        
            for k in range(len(self._student_marks[i])):
                table.add_row(f"{self.student_courses[i][k][0]}",f"{self._student_marks[i][k]}") 
            table.add_row("GPA",f"{GPA:.2f}")      
            panel = Panel(
            table,
            title="STUDENT INFORMATION",
            style="bold",
            border_style="bold green",
            box=box.ROUNDED,
            padding=(1, 2)
            ) 
            console.print(panel) 
        except ZeroDivisionError:
            if not self.student_courses[i]:
                console.print(f"[bold yellow]{self._student[i][0]} has not enrolled in any course so GPA can't be calculated.[/bold yellow]") 
            else:
                console.print("[bold red]Marks of the courses are not provided.[/bold red]")            

    def display(self,stuid):
        table = Table(
            show_header=False,
            box=None
            )
        table.add_column("Subject",style="sky_blue1")
        table.add_column("Information",style="sky_blue1")
        i = 0
        for ch in self._student:
            if ch[3] == stuid.strip():
                break
            i += 1
        if i == len(self._student):
            console.print("[bold red]Student not found![/bold red]") 
            return   
        table.add_row("Name",f"{self._student[i][0]}") 
        table.add_row("Age",f"{self._student[i][1]}") 
        table.add_row("Gender",f"{self._student[i][2]}")
        table.add_row("Studenr ID",f"{self._student[i][3]}") 
        table.add_row("COurses",f"{', '.join(ch[0] for ch in self.student_courses[i])}")
        panel = Panel(
            table,
            title="STUDENT INFORMATION",
            style="bold",
            border_style="bold green",
            box=box.ROUNDED,
            padding=(1, 2)
            )
        console.print(panel)   
       


s = student()      

