from tkinter import *
import sqlite3 
from tkinter import messagebox
root = Tk()
root.config(bg = "Light Grey")
frame = LabelFrame(root,text = "FACEBOOK",font = 90 ,fg = "White", padx=5, pady=5)
frame.pack(padx=10,pady=10)
frame.config(bg = "blue")
root.title("Facebook Regestration")
con=sqlite3.connect("Facebook.db")
c=con.cursor()
# c.execute("""CREATE TABLE address(
#     first_name text,
#     last_name text,
#     address text,
#     password text,
#     city text,
#     father_name text,
#     age integer,
#     zip_code
# )""")
# print("tabel created sucessfully")
def submit():
    con=sqlite3.connect("Facebook.db")
    c=con.cursor()
    c.execute("INSERT INTO address VALUES(:f_name,:l_name,:address,:age,:password, :father_name,:city,:zip_code)",{
    'f_name':f_name.get(),
    'l_name':l_name.get(),
    'address':address.get(),
    'age':age.get(),
    'password':password.get(),
    'father_name':father_name.get(),
    'city':city.get(),
    'zip_code':zip_code.get()
    })
    messagebox.showinfo("Adresses","Inserted Sucessfully")
    con.commit()
    con.close()  
def query():
    conn = sqlite3.connect("Facebook.db")  
    c = conn.cursor()
    c.execute("SELECT *, oid FROM address")
    records = c.fetchall()
    print(records)

    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[8]) + "\n"
    
    query_label = Label(frame, text = print_record)
    query_label.grid(row=9, column = 3, columnspan=2)
def delete():
    conn = sqlite3.connect("Facebook.db")
    c = conn.cursor()
    c.execute("DELETE from address WHERE oid = " + delete_box.get())
    print("DELETED SUCESSFULLY")
    delete_box.delete(0,END)
    conn.commit()
    conn.close()

def update():
    con = sqlite3.connect("Facebook.db")
    c = con.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE address SET
    first_name = :first,
    last_name = :last,
    address = :address,
    age = :age,
    password = :password,
    father_name = :father_name,
    city = :city,
    zip_code = :zip_code
    WHERE oid  = :oid""",
    {'first': f_name_editor.get(),
    'last': l_name_editor.get(),
    'address': address_editor.get(),
    'age':age_editor.get(),
    'password':password_editor.get(),
    'father_name':father_name_editor.get(),
    'city':city_editor.get(),
    'zip_code': zip_code_editor.get(),
    'oid' : record_id
        
    }
    )
    con.commit()
    con.close()
    editor.destroy()

def edit():

    global editor
    editor = Toplevel()
    editor.config(bg = "Light Blue")
    editor.title("Update Data")
    editor.geometry("300x400")
    conn = sqlite3.connect("Facebook.db")
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM address WHERE oid= " + record_id)
    records = c.fetchall()
    
    global f_name_editor
    global l_name_editor
    global address_editor
    global age_editor
    global password_editor
    global father_name_editor
    global city_editor
    global zip_code_editor

    f_name_editor = Entry(editor, width = 30)
    f_name_editor.grid(row = 0, column = 1, padx = 20, pady =(10,0))
    l_name_editor = Entry(editor, width = 30)
    l_name_editor.grid(row = 1, column = 1)
    address_editor = Entry(editor, width = 30)
    address_editor.grid(row = 2, column = 1)
    age_editor = Entry(editor, width = 30)
    age_editor.grid(row = 3, column = 1)
    password_editor = Entry(editor, width = 30)
    password_editor.grid(row = 4, column = 1)
    city_editor = Entry(editor, width = 30)
    city_editor.grid(row = 5, column = 1)
    father_name_editor = Entry(editor, width = 30)
    father_name_editor.grid(row = 6, column = 1)
    zip_code_editor = Entry(editor, width = 30)
    zip_code_editor.grid(row = 7, column = 1)
    f_name_label= Label(editor, text = "First Name", bg = "Sky blue")
    f_name_label.grid(row = 0, column = 0)
    l_name_label= Label(editor, text = "Last Name", bg = "Sky blue")
    l_name_label.grid(row = 1, column = 0)
    address_label= Label(editor, text = "Address", bg = "Sky blue")
    address_label.grid(row = 2, column = 0)
    age_label= Label(editor, text = "Age", bg = "Sky blue")
    age_label.grid(row = 3, column = 0)
    password_label= Label(editor, text = "Password", bg = "Sky blue")
    password_label.grid(row = 4, column = 0)
    city_label= Label(editor, text = "City", bg = "Sky blue")
    city_label.grid(row = 5, column = 0)
    father_name_label= Label(editor, text = "Father Name", bg = "Sky blue")
    father_name_label.grid(row = 6, column = 0)
    zip_code_label= Label(editor, text = "Zip Code", bg = "Sky blue")
    zip_code_label.grid(row = 7, column = 0)

    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        age_editor.insert(0,record[3])
        password_editor.insert(0,record[4])
        city_editor.insert(0,record[5])
        father_name_editor.insert(0,record[6])
        zip_code_editor.insert(0,record[7])
    
    edit_btn = Button(editor, text = "Save", bg = "Light grey",command= update)
    edit_btn.grid(row = 8, column=0, columnspan=2, pady = 10, padx = 10, ipadx=125)


# my_text = Label(frame, text = "FACE BOOK", font = 90, bg = "Blue", fg = "white")
# my_text.grid(row = 0,column = 6)

f_name=Entry(frame,width=30)
f_name.grid(row=0,column=4,padx=20)

l_name=Entry(frame,width=30)
l_name.grid(row=1,column=4)

address=Entry(frame,width=30)
address.grid(row=2,column=4)

age=Entry(frame,width=30)
age.grid(row=3,column=4)

password=Entry(frame,width=30)
password.grid(row=4,column=4)

city=Entry(frame,width=30)
city.grid(row=5,column=4)

father_name=Entry(frame,width=30)
father_name.grid(row=6,column=4)

zip_code=Entry(frame,width=30)
zip_code.grid(row=7,column=4)

f_name_label=Label(frame,text="First Name", bg = "blue", fg = "White", font = 30)
f_name_label.grid(row=0,column=3)

l_name_label=Label(frame,text="Last Name", bg = "blue", fg = "White",font = 30)
l_name_label.grid(row=1,column=3)

address_label=Label(frame,text="Address", bg = "blue", fg = "White",font = 30)
address_label.grid(row=2,column=3)


age_label=Label(frame,width=30,text ="Age", bg = "blue", fg = "White",font = 30)
age_label.grid(row=3,column=3)

password_label=Label(frame,width=30, text = "Password", bg = "blue", fg = "White",font = 30)
password_label.grid(row=4,column=3)

city_label=Label(frame,text="City", bg = "blue", fg = "White",font = 30)
city_label.grid(row=5,column=3)


father_name_label=Label(frame,width=30, text = "Father Name", bg = "blue", fg = "White",font = 30)
father_name_label.grid(row=6,column=3)

zip_code_label=Label(frame,text="Zipcode", bg = "blue", fg = "White",font = 30)
zip_code_label.grid(row=7,column=3)

Select_label = Label(frame,text = "Type ID", bg = "blue", fg = "White",font = 30)
Select_label.grid(row=12, column=3)

delete_box = Entry(frame, width = 30)
delete_box.grid(row = 12, column=4, pady = 5)


submit_btn=Button(frame,text="dd records", bg = "sky blue", fg = "White",font = 40,command=submit)
submit_btn.grid(row=8,column=3,columnspan=2,pady=10,padx=10,ipadx=100)

query_btn = Button(frame, text = "Show records", bg = "sky blue", fg = "White",font = 40, command = query)
query_btn.grid(row = 11, column = 3, columnspan=2, pady=10, padx=10, ipadx= 120)

delete_btn = Button(frame,text = "Delete", bg = "sky blue", fg = "White",font = 40, command=delete)
delete_btn.grid(row = 13 , column = 3, columnspan=2, pady=10, padx=10, ipadx=120)

edit_btn = Button(frame, text = "Update", bg = "sky blue", fg = "White",font = 40, command=edit)
edit_btn.grid(row=14, column=3, columnspan=2, padx=10, pady =10, ipadx = 120)
    

con.commit()
con.close()









root.mainloop()