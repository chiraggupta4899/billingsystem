from tkinter import *
def add_customer():
    pass
def view_customer():
    pass
def update_customer():
    pass
def view_price():
    pass
def create_bill():
    pass
root=Tk()
lms=1300
bms=750
root.minsize(lms,bms)
root.maxsize(lms,bms)
root.configure(background='lightblue')
frame1 = Frame(root, width=100, height=750, background="bisque")
frame2 = Frame(root, width=900, height =750, background="lightblue")
frame1.pack(expand = True,fill = BOTH ,side= LEFT)
frame2.pack(expand = True,fill = BOTH ,side= LEFT)
addcustomer=Button(frame1,text="Add Customer",command=add_customer)
addcustomer.place(x=100,y=50)
viewcustomer=Button(frame1,text="View Customers",command=view_customer)
viewcustomer.place(x=100,y=100)
updatecustomer=Button(frame1,text="Update Customer Details",command=update_customer)
updatecustomer.place(x=100,y=150)
viewprice=Button(frame1,text="Price List",command=view_price)
viewprice.place(x=100,y=200)
createbill=Button(frame1,text="Create Bill",command=create_bill)
createbill.place(x=100,y=250)
root.mainloop()
