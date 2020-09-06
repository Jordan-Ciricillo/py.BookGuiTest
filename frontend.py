from tkinter import *
import backend

#Clear the list box first, then populate it
def populate_list_view():
    listy.delete(0, END)
    for item in backend.view_all():
        listy.insert(END, item)

#Call the backend function for searching and repopulate the table
def search_entry():
    listy.delete(0, END)
    for item in backend.search_func(title_value.get(), author_val.get(), isbn_val.get(), year_val.get()):
        listy.insert(END, item)

#insert a record
def insert_rec():
    backend.add_entry(title_value.get(), author_val.get(), isbn_val.get(), year_val.get())
    listy.delete(0, END)
    listy.insert(END,(title_value.get(), author_val.get(), isbn_val.get(), year_val.get()))

#because it's bound, it takes the event parameter
#get ID for row to pass to delete function on the backend
# populate fields for changing
def get_selected_item(event):
    global selection
    try:
        index = listy.curselection()[0]
        selection = listy.get(index)
        a1.delete(0,END)
        a1.insert(END, selection[1]) #title
        b1.delete(0,END)
        b1.insert(END, selection[4]) #Year
        c1.delete(0,END)
        c1.insert(END, selection[2]) #Author
        d1.delete(0,END)
        d1.insert(END, selection[3]) #ISBN
    except IndexError:
        pass

    return(selection)

#pass item index and delete record. 
def delete_record():
    backend.delete_entry(selection[0])
   # repopulate table
    populate_list_view()


def update_record():
    backend.update_entry(selection[0], title_value.get(), author_val.get(), isbn_val.get(), year_val.get())
    #print(selection[0], title_value.get(), author_val.get(), isbn_val.get(), year_val.get())
    # repopulate table
    populate_list_view() 

mainW = Tk()

mainW.title("Practice Book Database")

#Create a database and connection
#connection = sqlite3.c


#Title label 
a1=Label(mainW,text="Title", width=10)
a1.grid(row=0,column=0) 

#Text entry for title
title_value=StringVar()  #
a1=Entry(mainW,textvariable=title_value,width=15 )  
a1.grid(row=0,column=1)


#Year label
b1=Label(mainW, text= "Year", width=10)
b1.grid(row=1, column=0)

#Text entry for year
year_val=StringVar()  #
b1=Entry(mainW,textvariable=year_val,width=15)  
b1.grid(row=1,column=1)


#Author label
c1=Label(mainW, text= "Author", width=10)
c1.grid(row=0, column=2)

#Text entry for Author
author_val=StringVar()  #
c1=Entry(mainW,textvariable=author_val, width=15)  
c1.grid(row=0,column=3)


#ISBN label
d1=Label(mainW, text= "ISBN", width=10)
d1.grid(row=1, column=2)

#Text entry for ISBN
isbn_val=StringVar()  #
d1=Entry(mainW,textvariable=isbn_val,width=15)  
d1.grid(row=1,column=3)



#View all button
view_all_btn=Button(mainW,text="View All",command=populate_list_view, width=15)
view_all_btn.grid(row=2,column=3)

#Search Button
search_Btn=Button(mainW,text="Search",command=search_entry, width=15)
search_Btn.grid(row=3,column=3)

#Add Entry
add_btn=Button(mainW,text="Add Entry",command=insert_rec, width=15)
add_btn.grid(row=4,column=3)

#Update Entry
update_btn=Button(mainW,text="Update",command=update_record, width=15)
update_btn.grid(row=5,column=3)

#Delete Record
delete_btn=Button(mainW,text="Delete",command=delete_record, width=15)
delete_btn.grid(row=6,column=3)

#Exit Program
exit_btn=Button(mainW,text="Close",command=mainW.destroy, width=15)
exit_btn.grid(row=7,column=3)

#Make a list box to store the records, make sure it spans properly 
listy=Listbox(mainW, height=10, width=40)
listy.grid(row=2, columnspan=2,rowspan=6, padx=5)

#Scrolly bar
scrolly=Scrollbar(mainW)
scrolly.grid(row=2, column=2, rowspan=6)

#Tie the list and scroll bar together
listy.configure(yscrollcommand=scrolly.set)
scrolly.configure(command=listy.yview)

#bind the list to a function
listy.bind('<<ListboxSelect>>',get_selected_item)

mainW.mainloop()