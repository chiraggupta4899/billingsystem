from tkinter import *
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
root.mainloop()
