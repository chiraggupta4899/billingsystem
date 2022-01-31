from tkinter import *
def add_employee():
    pass
def view_employee():
    pass
def update_employee():
    pass
def view_customer():
    pass
def view_stock():
    pass
def update_stock():
    pass
def update_price():
    pass
root=Tk()
root.title("Owner Side")
lms=1300
bms=750
root.minsize(lms,bms)
root.maxsize(lms,bms)
root.configure(background='lightblue')
frame1 = Frame(root, width=100, height=750, background="bisque")
frame2 = Frame(root, width=900, height =750, background="lightblue")
frame1.pack(expand = True,fill = BOTH ,side= LEFT)
frame2.pack(expand = True,fill = BOTH ,side= LEFT)
addemployee=Button(frame1,text="Add Employee",command=add_employee)
addemployee.place(x=100,y=50)
viewemployee=Button(frame1,text="View Employee",command=view_employee)
viewemployee.place(x=100,y=100)
updateemployee=Button(frame1,text="Update Employee Details",command=update_employee)
updateemployee.place(x=100,y=150)
viewcustomer=Button(frame1,text="View Customers",command=view_customer)
viewcustomer.place(x=100,y=200)
viewstock=Button(frame1,text="View Stock",command=view_stock)
viewstock.place(x=100,y=250)
updatestock=Button(frame1,text="Update Stock",command=update_stock)
updatestock.place(x=100,y=300)
updateprice=Button(frame1,text="Update Price",command=update_price)
updateprice.place(x=100,y=350)
root.mainloop()
