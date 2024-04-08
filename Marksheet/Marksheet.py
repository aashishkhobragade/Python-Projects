import tkinter as tk
from tkinter import messagebox
import math
from fpdf import FPDF
#Main Window Control Section
master = tk.Tk()
master.title("Marksheet Calculator")
master.geometry("1200x800")

#SOME CODE SHOULD BE COMMENTED 
# title_bar = tk.Frame(master, bg="white", height=30, relief="raised", bd=1)
# title_bar.pack(fill="x")


#Color Control Section
bgcolor = "#2C7865"
bgcolor2="#FF9800"
fgcolor = "white"
fgcolor2 = "black"



#Function Control Center
def calculate_total():
  try:
    # Get marks from text fields and convert to integers
    mark1 = int(subject1entry.get()) 
    mark2 = int(subject2entry.get())
    mark3 = int(subject3entry.get())
    mark4 = int(subject4entry.get())
    mark5 = int(subject5entry.get())
    mark6 = int(subject6entry.get())


    #Credit Calculation
    credit1 = round((mark1/10) * 3)
    credit2 = round((mark2/10) * 4)
    credit3 = round((mark3/10) * 3)
    credit4 = round((mark4/10) * 4)
    credit5 = round((mark5/10) * 4)
    credit6 = round((mark6/10) * 4)

    #total Credits

    total_credit = credit1+credit2+credit3+credit4+credit5+credit6
    # Calculate total marks
    total = mark1 + mark2 + mark3 + mark4 + mark5+ mark6

    SGPA = (total_credit / 20 )

    # Update total marks label
    totalmarks.config(text=f"Total Marks: {total} / 600")
    calCreditans.config(text=f"{total_credit}")

    #Setting the credits to there subjects
    obcredit1.config(text=f"{credit1}")
    obcredit2.config(text=f"{credit2}")
    obcredit3.config(text=f"{credit3}")
    obcredit4.config(text=f"{credit4}")
    obcredit5.config(text=f"{credit5}")
    obcredit6.config(text=f"{credit6}")
    

    calGPA.config(text=f"{SGPA}")



  except ValueError:
    # Handle invalid input (non-numeric characters)
    totalmarks.config(text="Invalid Input! Please enter numbers only.")
    calCreditans.config(text=f"Invalid Data")



#Created a function which extract entred data to create a PDF 
def export_to_pdf():
    name = name_entry.get()
    roll_number = roll_number_entry.get()
    registration_number = registration_number_entry.get()

    # Gather subject marks
    marks = {
        "Mathematics IV": subject1entry.get(),
        "Analysis of Algorithm": subject2entry.get(),
        "Microprocessor": subject3entry.get(),
        "Operating System": subject4entry.get(),
        "Database Management": subject5entry.get(),
        "Python SBLC": subject6entry.get(),
    }

    data = [
        {"Subject": "Mathematics IV", "Marks": subject1entry.get(), "Credit": obcredit1.cget("text")},
        {"Subject": "Analysis of Algorithm", "Marks": subject2entry.get(), "Credit": obcredit2.cget("text")},
        {"Subject": "Microprocessor", "Marks": subject3entry.get(), "Credit": obcredit3.cget("text")},
        {"Subject": "Operating System", "Marks": subject4entry.get(), "Credit": obcredit4.cget("text")},
        {"Subject": "Database Management", "Marks": subject5entry.get(), "Credit": obcredit5.cget("text")},
        {"Subject": "Python SBLC", "Marks": subject6entry.get(), "Credit": obcredit6.cget("text")},
        # Add more dictionaries as needed
    ]

    # Calculate total credits
    total_credits = sum(int(entry["Credit"]) for entry in data)

    # Calculate SGPA (assuming SGPA calculation logic)
    sgpa = total_credits / 20

    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", "B", size=20)
    pdf.cell(200, 10, txt="DATTA MEGHE COLLEGE OF ENGINEERING", ln=True, align="C")
    pdf.set_font("Arial", "B", size=15)
    pdf.cell(200, 10, txt="MARKSHEET", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f" Name                : {name}", ln=True, align="L")
    pdf.cell(200, 10, txt=f" Roll Number         : {roll_number}", ln=True, align="L")
    pdf.cell(200, 10, txt=f" Registration Number : {registration_number}", ln=True, align="L")
    pdf.cell(200, 10, txt="", ln=True, align="L")  # Add some space

    # Table header
    header = ["Subject", "Marks", "Credits"]
    col_widths = [100, 40, 50]
    for i in range(len(header)):
        pdf.cell(col_widths[i], 10, header[i], 1, 0, "C")
    pdf.ln()

    # Table data
    for entry in data:
        pdf.cell(col_widths[0], 10, entry["Subject"], 1, 0, "C")
        pdf.cell(col_widths[1], 10, entry["Marks"], 1, 0, "C")
        pdf.cell(col_widths[2], 10, entry["Credit"], 1, 0, "C")
        pdf.ln()

    # Total credits (bold)
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(200, 10, txt=f"Total Credits: {total_credits}", ln=True, align="L")

    # SGPA (bold)
    pdf.cell(200, 10, txt=f"SGPA: {sgpa}", ln=True, align="L")

    pdf_output = f"{name}.pdf"
    pdf.output(pdf_output)
    messagebox.showinfo("PDF Exported", f"PDF file '{pdf_output}' generated successfully!")





#Container for entering marks
container1 = tk.Frame(master, bg=bgcolor, width=600, height=400)
container1.pack(side="left", fill="both", expand=True)

name = tk.Label(container1,text="Datta Meghe College of Engineering",font=("Arial",30),bg=bgcolor,pady=20 ,fg=fgcolor)
name.pack(anchor="center")
name2 = tk.Label(container1,text="Department of Artificial Intelligence & Data Science",font=("Arial",18),bg=bgcolor,pady=0 ,fg=fgcolor)
name2.pack(anchor="center")


name_label = tk.Label(container1, text="Name:", font=("Arial", 12), bg=bgcolor,fg=fgcolor)
name_label.pack(anchor="w", pady=10, padx=50)

name_entry = tk.Entry(container1, width=30)
name_entry.pack(anchor="w", padx=50)




roll_number_label = tk.Label(container1, text="Roll Number:", font=("Arial", 12), bg=bgcolor,fg=fgcolor)
roll_number_label.pack(anchor="w", pady=10, padx=50)

roll_number_entry = tk.Entry(container1, width=30)
roll_number_entry.pack(anchor="w", padx=50)




registration_number_label = tk.Label(container1, text="Registration Number:", font=("Arial", 12), bg=bgcolor,fg=fgcolor)
registration_number_label.pack(anchor="w", pady=10, padx=50)

registration_number_entry = tk.Entry(container1, width=30)
registration_number_entry.pack(anchor="w", padx=50)






subjects = tk.Frame(container1, bg=bgcolor, width=300, height=200)
subjects.pack(side="bottom", fill="both", expand=True, pady=30, padx=50)
#Main Heading
heading = tk.Label(subjects, text="Enter Marks Here :", font=("Arial", 15), bg=bgcolor, fg=fgcolor)
heading.grid(column=1, row=1)


#Subject 1 
num1 = tk.Label(subjects,text="1.",bg=bgcolor, fg=fgcolor)
num1.grid(column=1, row=2 , padx=0,pady=10,sticky='w')
subject1 = tk.Label(subjects, text="Mathematics IV :", bg=bgcolor, fg=fgcolor)
subject1.grid(column=2, row=2 , padx=10,pady=10,sticky='w')
subject1entry = tk.Entry(subjects,width=10)
subject1entry.grid(column=3, row=2 , padx=10,pady=10,sticky='w')


#Subject 2
num2 = tk.Label(subjects,text="2.",bg=bgcolor, fg=fgcolor)
num2.grid(column=1, row=3 , padx=0,pady=10,sticky='w')
subject2 = tk.Label(subjects, text="Analysis of Algorithm :", bg=bgcolor, fg=fgcolor)
subject2.grid(column=2, row=3 , padx=10,pady=10,sticky='w')
subject2entry = tk.Entry(subjects,width=10)
subject2entry.grid(column=3, row=3 , padx=10,pady=10,sticky='w')


#Subject 3
num3 = tk.Label(subjects,text="3.",bg=bgcolor, fg=fgcolor)
num3.grid(column=1, row=4 , padx=0,pady=10,sticky='w')
subject3 = tk.Label(subjects, text="Microprocessor :", bg=bgcolor, fg=fgcolor)
subject3.grid(column=2, row=4 , padx=10,pady=10,sticky='w')
subject3entry = tk.Entry(subjects,width=10)
subject3entry.grid(column=3, row=4 , padx=10,pady=10,sticky='w')


#Subject 4
num4 = tk.Label(subjects,text="4.",bg=bgcolor, fg=fgcolor)
num4.grid(column=1, row=5 , padx=0,pady=10,sticky='w')
subject4 = tk.Label(subjects, text="Operaying System :", bg=bgcolor, fg=fgcolor)
subject4.grid(column=2, row=5 , padx=10,pady=10,sticky='w')
subject4entry = tk.Entry(subjects,width=10)
subject4entry.grid(column=3, row=5 , padx=10,pady=10,sticky='w')



#Subject 5
num5 = tk.Label(subjects,text="5.",bg=bgcolor, fg=fgcolor)
num5.grid(column=1, row=6 , padx=0,pady=10,sticky='w')
subject5 = tk.Label(subjects, text="Database Management :", bg=bgcolor, fg=fgcolor)
subject5.grid(column=2, row=6 , padx=10,pady=10,sticky='w')
subject5entry = tk.Entry(subjects,width=10)
subject5entry.grid(column=3, row=6 , padx=10,pady=10,sticky='w')


#Subject 6
num6 = tk.Label(subjects,text="6.",bg=bgcolor, fg=fgcolor)
num6.grid(column=1, row=7 , padx=0,pady=10,sticky='w')
subject6 = tk.Label(subjects, text="Python SBLC :", bg=bgcolor, fg=fgcolor)
subject6.grid(column=2, row=7 , padx=10,pady=10,sticky='w')
subject6entry = tk.Entry(subjects,width=10)
subject6entry.grid(column=3, row=7 , padx=10,pady=10,sticky='w')


calculate_button = tk.Button(subjects, text="Calculate",bg="red",command=calculate_total)
calculate_button.grid(row=9, column=0, columnspan=8,pady=30)

totalmarks = tk.Label(subjects,text="Total Marks : 000/600",font=("Arial",18),bg=bgcolor,pady=10 ,fg=fgcolor)
totalmarks.grid(row=10,column=2,pady=0)



#to display the GPA and FINAL Result

container2 = tk.Frame(master, bg=bgcolor2, width=300, height=400)
container2.pack(side="right", fill="both", expand=True)


headingres = tk.Label(container2,text="Calculated Result",font=("Arial",18),bg=bgcolor2,pady=40 ,fg=fgcolor2)
headingres.pack(anchor="center")



#Result calculated window
resultContainer = tk.Frame(container2, bg=bgcolor2, width=300, height=300)
resultContainer.pack(side="bottom", fill="both", expand=True, padx=45)
calCredit = tk.Label(resultContainer,text="Total Credit",font=("Arial",18),bg=bgcolor2,pady=20 ,fg=fgcolor2)
calCredit.pack(anchor="w")
calCreditans = tk.Label(resultContainer,text="0.00",font=("Arial",18),bg=bgcolor2,pady=10 ,fg=fgcolor2)
calCreditans.pack(anchor="w")
GPA = tk.Label(resultContainer,text="SGPA",font=("Arial",18),bg=bgcolor2,pady=20 ,fg=fgcolor2)
GPA.pack(anchor="w")
calGPA = tk.Label(resultContainer,text="0.00",font=("Arial",18),bg=bgcolor2,pady=10 ,fg=fgcolor2)
calGPA.pack(anchor="w")
export_button = tk.Button(resultContainer, text="Export to PDF", command= export_to_pdf)
export_button.pack(anchor="center")




#Credit Calculation Window

creditContainer = tk.Frame(container2, bg=bgcolor2, width=300, height=400)
creditContainer.pack(side="bottom", fill="both", expand=True,padx=45)

subjectcode = tk.Label(creditContainer,text="Sr. No.",bg=bgcolor2,fg=fgcolor2)
subjectcode.grid(column=1,row=1,pady=10,padx=25)
code1 = tk.Label(creditContainer,text="1.",bg=bgcolor2,fg=fgcolor2)
code1.grid(column=1,row=2,pady=10,padx=25)
code2 = tk.Label(creditContainer,text="2.",bg=bgcolor2,fg=fgcolor2)
code2.grid(column=1,row=3,pady=10,padx=25)
code3 = tk.Label(creditContainer,text="3.",bg=bgcolor2,fg=fgcolor2)
code3.grid(column=1,row=4,pady=10,padx=25)
code4 = tk.Label(creditContainer,text="4.",bg=bgcolor2,fg=fgcolor2)
code4.grid(column=1,row=5,pady=10,padx=25)
code5 = tk.Label(creditContainer,text="5.",bg=bgcolor2,fg=fgcolor2)
code5.grid(column=1,row=6,pady=10,padx=25)
code6 = tk.Label(creditContainer,text="6.",bg=bgcolor2,fg=fgcolor2)
code6.grid(column=1,row=7,pady=10,padx=25)

titlecredit = tk.Label(creditContainer,text="Subject Credit",bg=bgcolor2,fg=fgcolor2)
titlecredit.grid(column=2,row=1,pady=10,padx=15)
credit1 = tk.Label(creditContainer,text="3",bg=bgcolor2,fg=fgcolor2)
credit1.grid(column=2,row=2,pady=10,padx=25)
credit2 = tk.Label(creditContainer,text="4",bg=bgcolor2,fg=fgcolor2)
credit2.grid(column=2,row=3,pady=10,padx=25)
credit3 = tk.Label(creditContainer,text="3",bg=bgcolor2,fg=fgcolor2)
credit3.grid(column=2,row=4,pady=10,padx=25)
credit4 = tk.Label(creditContainer,text="4",bg=bgcolor2,fg=fgcolor2)
credit4.grid(column=2,row=5,pady=10,padx=25)
credit5 = tk.Label(creditContainer,text="4",bg=bgcolor2,fg=fgcolor2)
credit5.grid(column=2,row=6,pady=10,padx=25)
credit6 = tk.Label(creditContainer,text="4",bg=bgcolor2,fg=fgcolor2)
credit6.grid(column=2,row=7,pady=10,padx=25)

ObtainedCredit = tk.Label(creditContainer,text="Obtained Credit",bg=bgcolor2,fg=fgcolor2)
ObtainedCredit.grid(column=3,row=1,pady=10,padx=15)
obcredit1 = tk.Label(creditContainer,text="_",bg=bgcolor2,fg=fgcolor2)
obcredit1.grid(column=3,row=2,pady=10,padx=25)
obcredit2 = tk.Label(creditContainer,text="_",bg=bgcolor2,fg=fgcolor2)
obcredit2.grid(column=3,row=3,pady=10,padx=25)
obcredit3 = tk.Label(creditContainer,text="_",bg=bgcolor2,fg=fgcolor2)
obcredit3.grid(column=3,row=4,pady=10,padx=25)
obcredit4 = tk.Label(creditContainer,text="_",bg=bgcolor2,fg=fgcolor2)
obcredit4.grid(column=3,row=5,pady=10,padx=25)
obcredit5 = tk.Label(creditContainer,text="_",bg=bgcolor2,fg=fgcolor2)
obcredit5.grid(column=3,row=6,pady=10,padx=25)
obcredit6 = tk.Label(creditContainer,text="_",bg=bgcolor2,fg=fgcolor2)
obcredit6.grid(column=3,row=7,pady=10,padx=25)

master.resizable(False,False)
master.mainloop()


# Created by Ashish Vilas Khobragade 
# 2024 , 8 APRIL 
