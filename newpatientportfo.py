from tkinter import *

window=Tk()
window.title("Patient Registration")
window.configure(background = "gray")
window.geometry("500x500")

def create_new():
    file_name = patient_entry.get()
    new_file = open(file_name*".txt","a")
    new_file.write(new_entry.get(1.0,END))
    new_file.close()



registration_title = Label(window,text="New Patient Portfolio",background = "gray",font = ("Times New Roman","18","bold"))
registration_title.grid(row=1, column=1, rowspan=1)

patient_label = Label(window, text="Full name:",background="gray",font=("Times New Romans", "12","bold"))
patient_entry= Entry(window,width=25)
patient_label.grid(row=2,column=1,sticky="E",pady=(10,0))
patient_entry.grid(row=2,column=2,sticky="W",pady=(10,0))

patient_label = Label(window, text="Date of Birth:",background="gray",font=("Times New Romans", "12","bold"))
patient_entry= Entry(window,width=25)
patient_label.grid(row=4,column=1,sticky="E",pady=(10,0))
patient_entry.grid(row=4,column=2,sticky="W",pady=(10,0))

patient_label = Label(window, text="Gender:",background="gray",font=("Times New Romans", "12","bold"))
patient_entry= Entry(window,width=25)
patient_label.grid(row=5,column=1,sticky="E",pady=(10,0))
patient_entry.grid(row=5,column=2,sticky="W",pady=(10,0))

patient_label = Label(window, text="Phone Number:",background="gray",font=("Times New Romans", "12","bold"))
patient_entry= Entry(window,width=25)
patient_label.grid(row=6,column=1,sticky="E",pady=(10,0))
patient_entry.grid(row=6,column=2,sticky="W",pady=(10,0))

patient_label = Label(window, text="Address:",background="gray",font=("Times New Romans", "12","bold"))
patient_entry= Entry(window,width=25)
patient_label.grid(row=7,column=1,sticky="E",pady=(10,0))
patient_entry.grid(row=7,column=2,sticky="W",pady=(10,0))

patient_label = Label(window, text="Email:",background="gray",font=("Times New Romans", "12","bold"))
patient_entry= Entry(window,width=25)
patient_label.grid(row=8,column=1,sticky="E",pady=(10,0))
patient_entry.grid(row=8,column=2,sticky="W",pady=(10,0))

patient_label = Label(window, text="Social Security:",background="gray",font=("Times New Romans", "12","bold"))
patient_entry= Entry(window,width=25)
patient_label.grid(row=9,column=1,sticky="E",pady=(10,0))
patient_entry.grid(row=9,column=2,sticky="W",pady=(10,0))

patient_label = Label(window, text="Primary Insurance:",background="gray",font=("Times New Romans", "12","bold"))
patient_entry= Entry(window,width=25)
patient_label.grid(row=10,column=1,sticky="E",pady=(10,0))
patient_entry.grid(row=10,column=2,sticky="W",pady=(10,0))


new_entry_label = Label(window,text="Reason for Visit:",background = "gray",font = ("Times New Roman","12","bold"))
registration_title = Label(window,text="New Patient Porfolio",background = "gray",font = ("Times New Roman","16","bold"))
new_entry_label.grid(row=12,column=1,sticky="E",pady=(10,0))
new_entry = Text(window,width=30,height= 5)
new_entry.grid(row=12,column=2,columnspan=4,sticky="NSEW",pady=(10,0))

new_submit = Button(window,text="Submit",width=10,command= create_new)
new_submit.grid(row=13,column=2,sticky="W",pady=(10,0))





                       
window.mainloop()



