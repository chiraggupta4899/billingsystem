from tkinter import *
import re
def del_error_window():
    screen.destroy()
def addcustomersql():
    global er
    er=[1,1,1,1]
    cust_name=ccname.get()
    cust_phone=cphone.get()
    cust_add=cadd.get()
    cust_bal=int(cbal.get())
    if cust_name.replace(" ","").isalpha():
        er[0]=0
    else:
        er[0]=1
    pattern=re.compile("(0|91)?[6-9][0-9]{9}")
    if pattern.match(cust_phone):
        er[1]=0
    else:
        er[1]=1
    if len(cust_add)!=0:
        er[2]=0
    else:
        er[2]=1
    if int(cust_bal)>=0:
        er[3]=0
    else:
        er[3]=1
    if sum(er)==0:
        print(cust_name,cust_phone,cust_add,cust_bal)
        print("success")
        clr_frame2()
    else:
        error_window()
    

def error_window():
    global screen
    screen = Toplevel(root)
    screen.title("Wrong Input!!")
    for i in range(4):
        if er[i]==1:
            if i==0:
                er0=Label(screen,text="Enter Valid Name!",fg="red")
                er0.pack()
            if i==1:
                er1=Label(screen,text="Enter Valid Phone Number!",fg="red")
                er1.pack()
            if i==2:
                er2=Label(screen,text="Enter Valid Address!",fg="red")
                er2.pack()
            if i==3:
                er3=Label(screen,text="Enter Valid Balance!",fg="red")
                er3.pack()
    ok=Button(screen,text="OK",command=del_error_window)
    ok.pack()
    
def clr_frame2():
    for x in frame2.winfo_children():
        x.destroy()
def add_customer():
    clr_frame2()
    titleoftask= Label(frame2,text ="",font=("Arial",20))
    titleoftask.config(text="Enter details of Customer")
    titleoftask.place(x=350,y=50)
    namelabel= Label(frame2,text ="Name:",font=("Arial",20))
    namelabel.place(x=100,y=150)
    global ccname
    ccname= Entry(frame2,width=40)
    ccname.place(x=250,y=150)
    phonelabel= Label(frame2,text ="Phone:",font=("Arial",20))
    phonelabel.place(x=100,y=200)
    global cphone
    cphone= Entry(frame2,width=40)
    cphone.place(x=250,y=200)
    addresslabel= Label(frame2,text ="Address:",font=("Arial",20))
    addresslabel.place(x=100,y=250)
    global cadd
    cadd= Entry(frame2,width=40)
    cadd.place(x=250,y=250)
    balancelabel= Label(frame2,text ="Balance:",font=("Arial",20))
    balancelabel.place(x=100,y=300)
    global cbal
    cbal= Entry(frame2,width=40)
    cbal.insert(0,0)
    cbal.place(x=250,y=300)
    submit=Button(frame2,text="Submit",command=addcustomersql)
    submit.place(x=350,y=500)
 
def view_customer():
    pass
def update_customer():
    pass
def view_price():
    pass
def create_bill():
    pass
root=Tk()
root.title("Employee Side")
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
