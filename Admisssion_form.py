#Author: Shazia Shaikh
#Admission Form

from tkinter import *

from tkinter import ttk

root = Tk()
root.title("Admission Form")
root.geometry("700x1090")

FirstName = StringVar()
MiddleName = StringVar()
LastName = StringVar()
Gender = StringVar()
DATE_BIRTH = StringVar()
DATE_BIRTH1 = StringVar()
BloodGroup = StringVar()
Religion = StringVar()
Caste = StringVar()
Nationality = StringVar()
AdhaarNo = IntVar()
Community = StringVar()
LanguageKnown = StringVar()
MotherTongue = StringVar()
Res_Address = StringVar()
Cor_Address = StringVar()
ContactNo = IntVar()
PermanentAddress = StringVar()


def submit():
    root1 = Tk()
    root1.title("Admin Form")
    root1.geometry("600x700")

    a1 = FirstName.get()
    a2 = MiddleName.get()
    a3 = LastName.get()
    a4 = var.get()
    a5 = DATE_BIRTH.get()
    a6 = DATE_BIRTH1.get()
    a7 = BloodGroup.get()
    a8 = Religion.get()
    a9 = Caste.get()
    a10 = Nationality.get()
    a11 = AdhaarNo.get()
    a12 = var1.get()
    a13 = LanguageKnown.get()
    a14 = MotherTongue.get()
    a15 = Res_Address.get()
    a16 = Cor_Address.get()
    a17 = ContactNo.get()


    p1 = Label(root1)
    p1.place(x=10, y=20)
    value1 = "First Name Is :" + str(a1)
    p1.config(text=value1)

    p2 = Label(root1)
    p2.place(x=10, y=50)
    value2 = "Middle Name Is :" + str(a2)
    p2.config(text=value2)

    p3 = Label(root1)
    p3.place(x=10, y=80)
    value3 = "Last Name Is :" + str(a3)
    p3.config(text=value3)

    p4 = Label(root1)
    p4.place(x=10, y=110)
    value4 = "Gender Is :" + str(a4)
    p4.config(text=value4)

    p5 = Label(root1)
    p5.place(x=10, y=140)
    value5 = "Date Of Birth Is :" + str(a5)
    p5.config(text=value5)

    p6 = Label(root1)
    p6.place(x=10, y=170)
    value6 = "Date Of Birth In Words Is :" + str(a6)
    p6.config(text=value6)

    p7 = Label(root1)
    p7.place(x=10, y=200)
    value7 = "Blood Group Is :" + str(a7)
    p7.config(text=value7)

    p8 = Label(root1)
    p8.place(x=10, y=230)
    value8 = "Religion Is :" + str(a8)
    p8.config(text=value8)

    p9 = Label(root1)
    p9.place(x=10, y=260)
    value9 = "Caste Is :" + str(a9)
    p9.config(text=value9)

    p10 = Label(root1)
    p10.place(x=10, y=290)
    value10 = "Nationality Is :" + str(a10)
    p10.config(text=value10)

    p11 = Label(root1)
    p11.place(x=10, y=320)
    value11 = "Adhaar No. Is :" + str(a11)
    p11.config(text=value11)

    p12 = Label(root1)
    p12.place(x=10, y=350)
    value12 = "Community :" + str(a12)
    p12.config(text=value12)

    p13 = Label(root1)
    p13.place(x=10, y=380)
    value13 = "Language Known :" + str(a13)
    p13.config(text=value13)

    p14 = Label(root1)
    p14.place(x=10, y=410)
    value14 = "Mother Tongue Is :" + str(a14)
    p14.config(text=value14)

    p15 = Label(root1)
    p15.place(x=10, y=440)
    value15 = "Residential Address :" + str(a15)
    p15.config(text=value15)

    p16 = Label(root1)
    p16.place(x=10, y=470)
    value16 = "Correspondance Address :" + str(a16)
    p16.config(text=value16)

    p17 = Label(root1)
    p17.place(x=10, y=500)
    value17 = "Contact Number :" + str(a17)
    p17.config(text=value17)

    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")
    e6.delete(0, "end")
    e7.delete(0, "end")
    e8.delete(0, "end")
    e9.delete(0, "end")
    e10.delete(0, "end")
    e11.delete(0, "end")
    e12.delete(0, "end")
    e13.delete(0, "end")
    e14.delete(0, "end")
    e15.delete(0, "end")

    root1.mainloop()


l1 = Label(root, text="First Name :")
l1.place(x=10, y=20)

e1 = Entry(root, width=25, textvariable=FirstName)
e1.place(x=10, y=40)

l2 = Label(root, text="Middle Name :")
l2.place(x=170, y=20)

e2 = Entry(root, width=25, textvariable=MiddleName)
e2.place(x=170, y=40)

l3 = Label(root, text="Last Name :")
l3.place(x=330, y=20)

e3 = Entry(root, width=25, textvariable=LastName)
e3.place(x=330, y=40)

l4 = Label(root, text="Gender :")
l4.place(x=10, y=80)

var = StringVar()

c1 = ttk.Radiobutton(root, text="Male", variable=var, value="Male")
c1.place(x=10, y=100)

c2 = ttk.Radiobutton(root, text="Female", variable=var, value="Female")
c2.place(x=60, y=100)

l5 = Label(root, text="Date of Birth :")
l5.place(x=150, y=80)

e4 = Entry(root, width=20, textvariable=DATE_BIRTH)
e4.place(x=150, y=100)

l6 = Label(root, text="DATE_BIRTH in Words :")
l6.place(x=300, y=80)

e5 = Entry(root, width=30, textvariable=DATE_BIRTH1)
e5.place(x=300, y=100)

l7 = Label(root, text="Blood Group :")
l7.place(x=10, y=130)

e6 = Entry(root, width=20, textvariable=BloodGroup)
e6.place(x=10, y=150)

l8 = Label(root, text="Religion :")
l8.place(x=150, y=130)

e7 = Entry(root, width=20, textvariable=Religion)
e7.place(x=150, y=150)

l9 = Label(root, text="Caste :")
l9.place(x=300, y=130)

e8 = Entry(root, width=20, textvariable=Caste)
e8.place(x=300, y=150)

l10 = Label(root, text="Nationality :")
l10.place(x=430, y=130)

e9 = Entry(root, width=20, textvariable=Nationality)
e9.place(x=430, y=150)

l11 = Label(root, text="Adhaar no. :")
l11.place(x=10, y=190)

e10 = Entry(root, width=40, textvariable=AdhaarNo)
e10.place(x=90, y=190)

l12 = Label(root, text="Community :")
l12.place(x=10, y=220)

var1 = StringVar()

r1 = Radiobutton(root, text="SC/ST", variable=var1, value="SC/ST")
r1.place(x=100, y=220)

r2 = Radiobutton(root, text="OBC", variable=var1, value="OBC")
r2.place(x=160, y=220)

r3 = Radiobutton(root, text="GEN", variable=var1, value="GEN")
r3.place(x=220, y=220)

r4 = Radiobutton(root, text="OTHERS", variable=var1, value="OTHERS")
r4.place(x=280, y=220)

l13 = Label(root, text="Language Known :")
l13.place(x=10, y=260)

e11 = Entry(root, width=60, textvariable=LanguageKnown)
e11.place(x=10, y=285)

l14 = Label(root, text="Mother Tongue:")
l14.place(x=430, y=260)

e12 = Entry(root, width=30, textvariable=MotherTongue)
e12.place(x=430, y=285)

l15 = Label(root, text="Residential Address :")
l15.place(x=10, y=320)

e13 = Entry(root, width=70, textvariable=Res_Address)
e13.place(x=160, y=320)

l16 = Label(root, text="Correspondance Address :")
l16.place(x=10, y=350)

e14 = Entry(root, width=70, textvariable=Cor_Address)
e14.place(x=160, y=350)

l17 = Label(root, text="Contact No.:")
l17.place(x=10, y=380)

e15 = Entry(root, width=30, textvariable=ContactNo)
e15.place(x=10, y=405)

l18 = Label(root, text="Declaration : I hereby declare that all statements made in theapplication \
are true,complete and correct to the best of my knowledge and belief.")
l18.place(x=10, y=440)

b1 = Button(root, text="submit", command=submit)
b1.place(x=10, y=470)

root.mainloop()