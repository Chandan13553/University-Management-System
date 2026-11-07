from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import box
from student import s
from professor import p
from course import c
from university import myuni
from searchrecord import search
from storage import save_data
from storage import load_university_data
console = Console()

load_university_data(s, p, c, myuni)

while True:
    print("\n")
    table = Table(
        show_header=False,
        box=None
             )
    table.add_column("Option",style="yellow")
    table.add_column("Operation",style="white")
    table.add_row("01","Register student")
    table.add_row("02","Register Professor")
    table.add_row("03","Create Course")
    table.add_row("04","Assign Professor to Course")
    table.add_row("05","Enroll Student in Course")
    table.add_row("06","Remove Student from Course")
    table.add_row("07","Remove Professor from Course")
    table.add_row("08","Record Student Marks")
    table.add_row("09","Display Student Information")
    table.add_row("10","Display Professor Information")
    table.add_row("11","Display Course Information")
    table.add_row("12","Search Records")
    table.add_row("13","Display University Statistics")
    table.add_row("14","Display Grades of Student")
    table.add_row("15","Exit")

    panel = Panel(
        table,
        title="UNIVERSITY MANAGEMENT SYSTEM",
        style="bold",
        border_style="sky_blue1",
        box=box.ROUNDED,
        padding=(1, 2)
        )
    console.print(panel)
    print("\n")
    while(True):
        try:
            choice =  int(console.input("[bright_cyan]\nEnter your choice : [/bright_cyan]"))
            break
        except ValueError:
            console.print("[bold red]Please enter a valid choice![/bold red]")
            continue
             
    match choice:
        case 1:
            try:
                name = console.input("[bright_cyan]Enter student's name : [/bright_cyan]")
                age = int(console.input("[bright_cyan]Enter age of the student : [/bright_cyan]"))
                gender = console.input("[bright_cyan]Enter gender : [/bright_cyan]")
                stuid = console.input("[bright_cyan]Enter student ID : [/bright_cyan]")
                s.register_student(name,age,gender,stuid)
            except ValueError:
                 console.print("[bold red]Please enter appropriate data.[/bold red]")    
        case 2:
            try:
                name = console.input("[bright_cyan]Enter professor's name : [/bright_cyan]")
                age = int(console.input("[bright_cyan]Enter age of the professor : [/bright_cyan]"))
                gender = console.input("[bright_cyan]Enter gender : [/bright_cyan]")
                profid = console.input("[bright_cyan]Enter professor ID : [/bright_cyan]")  
                dep = console.input("[bright_cyan]Enter Department : [/bright_cyan]")
                p.register_professor(name,age,gender,profid,dep)
            except ValueError:
                 console.print("[bold red]Please enter appropriate data.[/bold red]")    
        case 3:
            try:
                name = console.input("[bright_cyan]Enter name of the course : [/bright_cyan]")
                code = console.input("[bright_cyan]Enter course code : [/bright_cyan]")
                credit = int(console.input("[bright_cyan]Enter credit hour : [/bright_cyan]"))
                maxs = int(console.input("[bright_cyan]Enter maximum number of students : [/bright_cyan]"))
                c.create_course(name,code,credit,maxs)
            except ValueError:
                console.print("[bold red]Please enter appropriate data.[/bold red]")    
        case 4:
            try:
                pid = console.input("[bright_cyan]Enter ID of professor whom course is to be assigned : [/bright_cyan]")
                cid = console.input("[bright_cyan]Enter course ID : [/bright_cyan]")
                p.assign_course(pid,cid) 
            except ValueError:
                console.print("[bold red]Please enter appropriate data.[/bold red]")
        case 5:
            sid = console.input("[bright_cyan]Enter ID of student : [/bright_cyan]")
            cid = console.input("[bright_cyan]Enter course ID : [/bright_cyan]")
            s.enroll_course(sid,cid)
        case 6:
            sid = console.input("[bright_cyan]Enter ID of student : [/bright_cyan]")
            cid = console.input("[bright_cyan]Enter course ID : [/bright_cyan]")
            s.remove_course_student(sid,cid)
        case 7:
            pid = console.input("[bright_cyan]Enter ID of professor : [/bright_cyan]")
            cid = console.input("[bright_cyan]Enter course ID : [/bright_cyan]")
            p.remove_course_professor(pid,cid)
        case 8:
            sid = console.input("[bright_cyan]Enter student ID : [/bright_cyan]")
            s.record_marks(sid)    
        case 9:
            sid = console.input("[bright_cyan]Enter student ID : [/bright_cyan]")
            s.display(sid)
        case 10:
            pid = console.input("[bright_cyan]Enter professor ID : [/bright_cyan]")
            p.display(pid) 
        case 11:
            ccode = console.input("[bright_cyan]Enter course code : [/bright_cyan]")
            c.display(ccode)
        case 12:
            search.search_record()
        case 13:
            myuni.display()
            c.total_information()
        case 14:
            sid = console.input("[bright_cyan]Enter Student ID : [/bright_cyan]")
            s.student_stat(sid) 
        case 15:
            break              
        case _:
            console.print("[bold red]Invalid Choice[/bold red]")

    key = console.input("[bright_cyan]\nDo you want to continue(y/n) ? : [/bright_cyan]") 
    if key.strip().lower() == 'y':
        continue
    else:
        break
             
         

data = {
    "students": s._student,
    "professors": p._professor,
    "courses": c.courses,
    "student_courses": s.student_courses,
    "student_marks" : s._student_marks,
    "student_grades": s._student_grades,
    "professor_courses": p._course_assigned,
    "course_students": c.student_enroll
}
save_data(data)

