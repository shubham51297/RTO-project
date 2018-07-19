from tkinter import *
import json

#fine class called by the main menu
class finec:

    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("FINE")
        top.geometry("530x350")
        self.label1 = Label(top,text="FINE", font='Helvetica 18 bold')
        self.b1 = Button(top,text="ADD A FINE", width=25, bg='#2ECC71', font='bold',command=self.enter)
        self.b2 = Button(top,text="SEARCH AND PAY", width=25, bg='#2ECC71', font='bold',command=self.sea)
        self.b3 = Button(top,text="GO BACK", width=25, bg='#E74C3C', font='bold',command=self.dis)
        self.label1.grid(row=0,column=0,pady=10,padx=50)
        self.b1.grid(row=6,column=0,pady=10,padx=50)
        self.b2.grid(row=12,column=0,pady=10,padx=50)
        self.b3.grid(row=18,column=0,pady=30,padx=50)
    def dis(self):
        self.top.destroy()
    def enter(self):
        inputDialog = freg(self.top)
        root.wait_window(inputDialog.top)
    def sea(self):
        inputDialog = deletefine(self.top)
        root.wait_window(inputDialog.top)

#vehicle class called by the main menu
class vehicle :
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("VEHICLE REGISTRATION")
        top.geometry("530x350")
        self.label1 = Label(top,text="VEHICLE REGISTRATION", font='Helvetica 18 bold')
        self.b1 = Button(top,text="NEW REGISTRATION", width=25, bg='#2ECC71', font='bold',command=self.enter)
        self.b2 = Button(top,text="SEARCH AND MODIFY", width=25, bg='#2ECC71', font='bold',command=self.modifyit)
        self.b3 = Button(top,text="DELETE RECORD", width=25, bg='#2ECC71', font='bold',command=self.dele)
        self.b4 = Button(top,text="GO BACK", width=25, bg='#E74C3C', font='bold',command=self.dis)
        self.label1.grid(row=0, column=0, pady=10, padx=50)
        self.b1.grid(row=6, column=0, pady=10, padx=50)
        self.b2.grid(row=12, column=0, pady=10, padx=50)
        self.b3.grid(row=18, column=0, pady=10, padx=50)
        self.b4.grid(row=24, column=0, pady=30, padx=50)

    def dis(self):
        self.top.destroy()

    def enter(self):
        inputDialog = vlreg(self.top)
        root.wait_window(inputDialog.top)
    def dele(self):
        inputDialog = deletevehicle(self.top)
        root.wait_window(inputDialog.top)
    def modifyit(self):
        inputDialog = modi(self.top)
        root.wait_window(inputDialog.top)



#driving class called by the main menu
class driving :
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("DRIVING LICENCE")
        top.geometry("530x350")
        self.label1 = Label(top,text="DRIVING LICENCE", font='Helvetica 18 bold')
        self.b1 = Button(top,text="NEW REGISTRATION", width=25, bg='#2ECC71', font='bold',command=self.enter)
        self.b2 = Button(top,text="SEARCH AND MODIFY", width=25, bg='#2ECC71', font='bold',command=self.modi)
        self.b3 = Button(top,text="DELETE RECORD", width=25, bg='#2ECC71', font='bold',command=self.dele)
        self.b4 = Button(top,text="GO BACK", width=25, bg='#E74C3C', font='bold',command=self.dis)
        self.label1.grid(row=0, column=0, pady=10, padx=50)
        self.b1.grid(row=6, column=0, pady=10, padx=50)
        self.b2.grid(row=12, column=0, pady=10, padx=50)
        self.b3.grid(row=18, column=0, pady=10, padx=50)
        self.b4.grid(row=24, column=0, pady=30, padx=50)

    def dis(self):
        self.top.destroy()

    def enter(self):
        inputDialog = dlreg(self.top)
        root.wait_window(inputDialog.top)
    def dele(self):
        inputDialog = deletedl(self.top)
        root.wait_window(inputDialog.top)
    def modi(self):
        inputDialog = modifydl(self.top)
        root.wait_window(inputDialog.top)



#driving licence entry class called by the driving class
class dlreg :
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("DRIVING LICENCE")
        top.geometry("630x450")
        f = open("dl.json", "r")
        dic = json.load(f)
        listkey = list(dic.keys())
        listkey.sort(reverse=True)
        f.close()
        self.label1 = Label(top, text="ENTER THE DETAILS", font='Helvetica 18 bold')
        self.label1.grid(row=0, column=0, pady=8, padx=5)
        self.dlnol = Label(top,text="DL number",font='Helvetica 12 bold')
        self.dlnol.grid(row=1,column=0,padx=5,pady=8)
        self.dlno=Entry(top)
        self.dlno.grid(row=1,column=1,pady=8)
        self.dlnol = Label(top, text="Last number "+listkey[0], font='Helvetica 12 bold')
        self.dlnol.grid(row=1, column=2, padx=5, pady=8)
        self.fnamel = Label(top,text= "First name", font='Helvetica 12 bold')
        self.fnamel.grid(row=3, column=0, padx=5, pady=8)
        self.fname = Entry(top)
        self.fname.grid(row=3, column=1, pady=8)
        self.lnamel = Label(top,text= "last name", font='Helvetica 12 bold')
        self.lnamel.grid(row=5, column=0, padx=5, pady=8)
        self.lname = Entry(top)
        self.lname.grid(row=5, column=1, pady=8)
        self.dobl = Label(top,text ="D.O.B(dd-mm-yyyy) : ", font='Helvetica 12 bold')
        self.dobl.grid(row=7, column=0, padx=5, pady=8)
        self.dob = Entry(top)
        self.dob.grid(row=7, column=1, pady=8)
        self.addrl = Label(top, text="Address :  ", font='Helvetica 12 bold')
        self.addrl.grid(row=9, column=0, padx=5, pady=8)
        self.addr = Entry(top)
        self.addr.grid(row=9, column=1, pady=8)
        self.vdatel = Label(top, text="Validity date(dd-mm-yyyy) : ", font='Helvetica 12 bold')
        self.vdatel.grid(row=11, column=0, padx=5, pady=8)
        self.vdate = Entry(top)
        self.vdate.grid(row=11, column=1, pady=8)
        self.ltypel = Label(top,text= "Licence type ", font='Helvetica 12 bold')
        self.ltypel.grid(row=13, column=0, padx=5, pady=8)
        self.ltype = Entry(top)
        self.ltype.grid(row=13, column=1, pady=8)
        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.grid(row=14,columnspan=2)

    def send(self) :
        with open('dl.json', 'r+') as f:
            f1=open('dldata.txt',"a")
            pos=f1.tell()
            dicdl = json.load(f)
            sbuf = self.dlno.get() + "/" + self.fname.get() + "/" + self.lname.get() + "/" + self.dob.get() + "/" + self.addr.get() + "/" + self.vdate.get() + "/" + self.ltype.get()+"/"
            dicdl[self.dlno.get()] = pos
            while len(sbuf)<=100 :
                sbuf+="_"
            f1.write(sbuf)
            f1.close()
            f.seek(0)
            json.dump(dicdl, f)
        self.top.destroy()

#vehicle registration,called by the vehicle class for registration
class vlreg :
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("VEHICLE REGISTRATION ")
        top.geometry("630x450")
        f=open("rg.json","r")
        dic=json.load(f)
        listkey = list(dic.keys())
        listkey.sort(reverse=True)
        f.close()
        self.label1 = Label(top, text="ENTER THE DETAILS", font='Helvetica 18 bold')
        self.label1.grid(row=0, column=0, pady=8, padx=5)
        self.rgnol = Label(top,text="Registration number",font='Helvetica 12 bold')
        self.rgnol.grid(row=1,column=0,padx=5,pady=8)
        self.rgn = Label(top, text=" Last number : "+listkey[0], font='Helvetica 12 bold')
        self.rgn.grid(row=1, column=2, padx=5, pady=8)
        self.rgno=Entry(top)
        self.rgno.grid(row=1,column=1,pady=8)
        self.fnamel = Label(top,text= "First name", font='Helvetica 12 bold')
        self.fnamel.grid(row=3, column=0, padx=5, pady=8)
        self.fname = Entry(top)
        self.fname.grid(row=3, column=1, pady=8)
        self.lnamel = Label(top,text= "last name", font='Helvetica 12 bold')
        self.lnamel.grid(row=5, column=0, padx=5, pady=8)
        self.lname = Entry(top)
        self.lname.grid(row=5, column=1, pady=8)
        self.dobl = Label(top,text ="D.O.B(dd-mm-yyyy) : ", font='Helvetica 12 bold')
        self.dobl.grid(row=7, column=0, padx=5, pady=8)
        self.dob = Entry(top)
        self.dob.grid(row=7, column=1, pady=8)
        self.addrl = Label(top, text="Address :  ", font='Helvetica 12 bold')
        self.addrl.grid(row=9, column=0, padx=5, pady=8)
        self.addr = Entry(top)
        self.addr.grid(row=9, column=1, pady=8)
        self.vdatel = Label(top, text="Validity date(dd-mm-yyyy) : ", font='Helvetica 12 bold')
        self.vdatel.grid(row=11, column=0, padx=5, pady=8)
        self.vdate = Entry(top)
        self.vdate.grid(row=11, column=1, pady=8)
        self.vtypel = Label(top,text= "Vehicle type ", font='Helvetica 12 bold')
        self.vtypel.grid(row=13, column=0, padx=5, pady=8)
        self.vtype = Entry(top)
        self.vtype.grid(row=13, column=1, pady=8)
        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.grid(row=14,columnspan=2)

    def send(self) :
        with open('rg.json', 'r+') as f:
            f1 = open('rgdata.txt', "a")
            pos = f1.tell()
            dicdl = json.load(f)
            sbuf = self.rgno.get() + "/" + self.fname.get() + "/" + self.lname.get() + "/" + self.dob.get() + "/" + self.addr.get() + "/" + self.vdate.get() + "/" + self.vtype.get()+"/"
            dicdl[self.rgno.get()] = pos
            while len(sbuf)<=100 :
                sbuf+="_"
            f1.write(sbuf)

            f1.close()
            f.seek(0)
            json.dump(dicdl, f)
        self.top.destroy()

#class to add fine called by the fine file

class freg :
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("ADD FINE ")
        top.geometry("530x350")
        self.label1 = Label(top, text="ENTER THE DETAILS", font='Helvetica 18 bold')
        self.label1.grid(row=0, column=0, pady=8, padx=5)
        self.rgnol = Label(top,text="Registration number",font='Helvetica 12 bold')
        self.rgnol.grid(row=1,column=0,padx=5,pady=8)
        self.rgno=Entry(top)
        self.rgno.grid(row=1,column=1,pady=8)
        self.fnamel = Label(top,text= "Offence", font='Helvetica 12 bold')
        self.fnamel.grid(row=3, column=0, padx=5, pady=8)
        self.offence = Entry(top)
        self.offence.grid(row=3, column=1, pady=8)
        self.lnamel = Label(top,text= "Amount", font='Helvetica 12 bold')
        self.lnamel.grid(row=5, column=0, padx=5, pady=8)
        self.amount = Entry(top)
        self.amount.grid(row=5, column=1, pady=8)
        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.grid(row=6,columnspan=2)

    def send(self) :
        with open('rg.json', 'r+') as f2:
            dic=json.load(f2)
            reg=self.rgno.get()
            if reg in dic :
                with open('fine.json', 'r+') as f:
                    dicdl = json.load(f)
                    regno = self.rgno.get()
                    if regno in dicdl:
                        name2 = self.offence.get()
                        fine2 = self.amount.get()
                        value2 = dicdl[regno]
                        list = value2.split("/")
                        fname = list[1] + "+" + name2
                        ffine = int(list[2]) + int(fine2)
                        sbuf2 = regno + "/" + fname + "/" + str(ffine)
                        dicdl[regno] = sbuf2
                        f.seek(0)
                        json.dump(dicdl, f)

                    else:
                        name = self.offence.get()
                        fine = self.amount.get()
                        sbuf = regno + "/" + name + "/" + fine
                        dicdl[regno] = sbuf
                        f.seek(0)
                        json.dump(dicdl, f)
                self.top.destroy()
            else :
                self.la = Label(self.top, text="Invalid Number", font='Helvetica 12 bold')
                self.la.grid(row=7, column=0, padx=5, pady=8)

#to search for the record
class deletedl :
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("DELETE DL ")
        top.geometry("530x450")
        self.label1 = Label(top, text="ENTER THE DL NUMBER", font='Helvetica 18 bold')
        self.label1.grid(row=0, column=0, pady=8, padx=5)
        self.dlno = Entry(top)
        self.dlno.grid(row=1, column=0, pady=8)
        self.mySubmitButton = Button(top, text='SEARCH',bg='#33cc33', font='bold', command=self.send)
        self.mySubmitButton.grid(row=3, columnspan=2)

    def send(self):
        with open('dl.json', 'r+') as f :

            dicdl = json.load(f)
            dl=self.dlno.get()
            if dl not in dicdl :
                self.label2 = Label(self.top, text="  RECORD NOT FOUND      ", font='Helvetica 12 bold')
                self.label2.grid(row=5, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                 ", font='Helvetica 12 bold')
                self.label2.grid(row=6, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                ", font='Helvetica 12 bold')
                self.label2.grid(row=7, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                ", font='Helvetica 12 bold')
                self.label2.grid(row=8, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                ", font='Helvetica 12 bold')
                self.label2.grid(row=9, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                  ", font='Helvetica 12 bold')
                self.label2.grid(row=10, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                    ", font='Helvetica 12 bold')
                self.label2.grid(row=11, column=0, pady=8, padx=5)
                self.mySubmitButton = Button(self.top, text='                                           ', font='bold', command=self.deleteit)
                self.mySubmitButton.grid(row=12, columnspan=2)
            else :
                f1 = open("dldata.txt", "r+")
                f1.seek(dicdl[dl])
                var=f1.readline()
                infolist = var.split("/")
                f1.close()
                self.label2 = Label(self.top, text="DL NUMBER : "+infolist[0], font='Helvetica 12 bold')
                self.label2.grid(row=5, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="FIRST NAME : " + infolist[1], font='Helvetica 12 bold')
                self.label2.grid(row=6, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="LAST NAME : " + infolist[2], font='Helvetica 12 bold')
                self.label2.grid(row=7, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="DOB : " + infolist[3], font='Helvetica 12 bold')
                self.label2.grid(row=8, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="ADDRESS : " + infolist[4], font='Helvetica 12 bold')
                self.label2.grid(row=9, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="VALIDITY DATE : " + infolist[5], font='Helvetica 12 bold')
                self.label2.grid(row=10, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="LICENCE TYPE : " + infolist[6], font='Helvetica 12 bold')
                self.label2.grid(row=11, column=0, pady=8, padx=5)
                self.mySubmitButton = Button(self.top, text='DELETE',bg='#ff0000', font='bold', command=self.deleteit)
                self.mySubmitButton.grid(row=12, columnspan=2)

    def deleteit(self):
        with open('dl.json', 'r+') as f :
            f1=open("dldata.txt",'r+')
            dicdl = json.load(f)
            dl=self.dlno.get()
            pos=dicdl[dl]
            f1.seek(pos)
            f1.write("*")
            f1.close()
            del dicdl[dl]
            f.seek(0)
            f.truncate()
            json.dump(dicdl,f)
            self.top.destroy()


#to search and delete for vehicle

class deletevehicle :
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("DELETE VEHICLE ")
        top.geometry("530x450")
        self.label1 = Label(top, text="ENTER THE REGISTRATION NUMBER", font='Helvetica 18 bold')
        self.label1.grid(row=0, column=0, pady=8, padx=5)
        self.dlno = Entry(top)
        self.dlno.grid(row=1, column=0, pady=8)
        self.mySubmitButton = Button(top, text='SEARCH',bg='#33cc33', font='bold', command=self.send)
        self.mySubmitButton.grid(row=3, columnspan=2)

    def send(self):
        with open('rg.json', 'r+') as f :
            f1 = open("dldata.txt", "r+")
            dicdl = json.load(f)
            dl=self.dlno.get()
            if dl not in dicdl :
                self.label2 = Label(self.top, text="          RECORD NOT FOUND                               ", font='Helvetica 12 bold')
                self.label2.grid(row=5, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                       ", font='Helvetica 12 bold')
                self.label2.grid(row=6, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                       ", font='Helvetica 12 bold')
                self.label2.grid(row=7, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                       ", font='Helvetica 12 bold')
                self.label2.grid(row=8, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                       ", font='Helvetica 12 bold')
                self.label2.grid(row=9, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                       ", font='Helvetica 12 bold')
                self.label2.grid(row=10, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                       ", font='Helvetica 12 bold')
                self.label2.grid(row=11, column=0, pady=8, padx=5)
                self.mySubmitButton = Button(self.top, text='                    ', font='bold', command=self.deleteit)
                self.mySubmitButton.grid(row=12, columnspan=2)

            else :
                f1 = open("rgdata.txt", "r+")
                f1.seek(dicdl[dl])
                var = f1.readline()
                infolist = var.split("/")
                f1.close()
                self.label2 = Label(self.top, text="REGISTRAION NUMBER : "+infolist[0], font='Helvetica 12 bold')
                self.label2.grid(row=5, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="FIRST NAME : " + infolist[1], font='Helvetica 12 bold')
                self.label2.grid(row=6, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="LAST NAME : " + infolist[2], font='Helvetica 12 bold')
                self.label2.grid(row=7, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="DOB : " + infolist[3], font='Helvetica 12 bold')
                self.label2.grid(row=8, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="ADDRESS : " + infolist[4], font='Helvetica 12 bold')
                self.label2.grid(row=9, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="VALIDITY DATE : " + infolist[5], font='Helvetica 12 bold')
                self.label2.grid(row=10, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="VEHICLE TYPE : " + infolist[6], font='Helvetica 12 bold')
                self.label2.grid(row=11, column=0, pady=8, padx=5)
                self.mySubmitButton = Button(self.top, text='DELETE',bg='#ff0000', font='bold', command=self.deleteit)
                self.mySubmitButton.grid(row=12, columnspan=2)

    def deleteit(self):
        with open('rg.json', 'r+') as f :
            f1= open("rgdata.txt", 'r+')
            dicdl = json.load(f)
            dl=self.dlno.get()
            pos = dicdl[dl]
            f1.seek(pos)
            f1.write("*")
            f1.close()
            del dicdl[dl]
            f.seek(0)
            f.truncate()
            json.dump(dicdl,f)
            self.top.destroy()
#delete fine
class deletefine :
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("PAY FINE  ")
        top.geometry("530x350")
        self.label1 = Label(top, text="ENTER THE REGISTRATION NUMBER", font='Helvetica 18 bold')
        self.label1.grid(row=0, column=0, pady=8, padx=5)
        self.rgno = Entry(top)
        self.rgno.grid(row=1, column=0, pady=8)
        self.mySubmitButton = Button(top, text='SEARCH',bg='#33cc33', font='bold', command=self.send)
        self.mySubmitButton.grid(row=3, columnspan=2)
        self.mySubmitButton = Button(top, text='GO BACK', bg='#33cc33', font='bold', command=self.dele)
        self.mySubmitButton.grid(row=4, columnspan=2)

    def send(self):
        with open('fine.json', 'r+') as f:
            with open('rg.json', 'r+') as f2:
                dicdl = json.load(f)
                dir2 = json.load(f2)
                dl = self.rgno.get()
                if dl in dir2:
                    if dl in dicdl:
                        value = dicdl[dl]
                        list = value.split("/")
                        self.label2 = Label(self.top, text="REGISTRAION NUMBER : " + list[0],font='Helvetica 12 bold')
                        self.label2.grid(row=5, column=0, pady=8, padx=5)
                        self.label2 = Label(self.top, text="OFFENCE : " + list[1], font='Helvetica 12 bold')
                        self.label2.grid(row=6, column=0, pady=8, padx=5)
                        self.label2 = Label(self.top, text="AMOUNT : " + list[2], font='Helvetica 12 bold')
                        self.label2.grid(row=7, column=0, pady=8, padx=5)
                        self.mySubmitButton = Button(self.top, text='PAY', bg='#ff0000', font='bold',command=self.pay)
                        self.mySubmitButton.grid(row=8, columnspan=2)


                    else:
                        self.label2 = Label(self.top, text="                             NO FINE                         ", font='Helvetica 12 bold')
                        self.label2.grid(row=5, column=0, pady=8, padx=5)
                        self.label2 = Label(self.top, text="                                                                                             ", font='Helvetica 12 bold')
                        self.label2.grid(row=6, column=0, pady=8, padx=5)
                        self.label2 = Label(self.top, text="                                                                                              ", font='Helvetica 12 bold')
                        self.label2.grid(row=7, column=0, pady=8, padx=5)
                        self.label2 = Label(self.top,text="                                                                                              ",font='Helvetica 12 bold')
                        self.label2.grid(row=8, column=0, pady=8, padx=5)



                else:
                    self.label2 = Label(self.top, text="              NUMBER INVALID                    ", font='Helvetica 12 bold')
                    self.label2.grid(row=5, column=0, pady=8, padx=5)
                    self.label2 = Label(self.top,text="                                                                                                    ",font='Helvetica 12 bold')
                    self.label2.grid(row=6, column=0, pady=8, padx=5)
                    self.label2 = Label(self.top,text="                                                                                                    ",font='Helvetica 12 bold')
                    self.label2.grid(row=7, column=0, pady=8, padx=5)
                    self.label2 = Label(self.top,text="                                                                                                    ",font='Helvetica 12 bold')
                    self.label2.grid(row=7, column=0, pady=8, padx=5)
    def pay (self):
        with open('fine.json', 'r+') as f:
            dic = json.load(f)
            d= self.rgno.get()
            del dic[d]
            f.seek(0)
            f.truncate()
            json.dump(dic, f)
            self.top.destroy()
    def dele (self):
        self.top.destroy()

#to search and modify the content of driving licence

class modifydl :
    sendl=""
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("DELETE DL ")
        top.geometry("530x450")
        self.label1 = Label(top, text="ENTER THE DL NUMBER", font='Helvetica 18 bold')
        self.label1.grid(row=0, column=0, pady=8, padx=5)
        self.dlno = Entry(top)
        senddl=self.dlno.get()
        self.dlno.grid(row=1, column=0, pady=8)
        self.mySubmitButton = Button(top, text='SEARCH',bg='#33cc33', font='bold', command=self.send)
        self.mySubmitButton.grid(row=3, columnspan=2)
    def send(self):
        with open('dl.json', 'r+') as f :
            dicdl = json.load(f)
            dl=self.dlno.get()
            if dl not in dicdl :
                self.label2 = Label(self.top, text="                        RECORD NOT FOUND                            ", font='Helvetica 12 bold')
                self.label2.grid(row=5, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                       ", font='Helvetica 12 bold')
                self.label2.grid(row=6, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                       ", font='Helvetica 12 bold')
                self.label2.grid(row=7, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                                                     ", font='Helvetica 12 bold')
                self.label2.grid(row=8, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                   ", font='Helvetica 12 bold')
                self.label2.grid(row=9, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                   ", font='Helvetica 12 bold')
                self.label2.grid(row=10, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                      ", font='Helvetica 12 bold')
                self.label2.grid(row=11, column=0, pady=8, padx=5)
                self.mySubmitButton =Label(self.top, text='                     ', font='bold')
                self.mySubmitButton.grid(row=12, columnspan=2,pady=8, padx=5)
            else :
                f1 = open("dldata.txt", "r+")
                f1.seek(dicdl[dl])
                var = f1.readline()
                infolist = var.split("/")
                f1.close()
                self.label2 = Label(self.top, text="DL NUMBER : " + infolist[0], font='Helvetica 12 bold')
                self.label2.grid(row=5, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="FIRST NAME : " + infolist[1], font='Helvetica 12 bold')
                self.label2.grid(row=6, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="LAST NAME : " + infolist[2], font='Helvetica 12 bold')
                self.label2.grid(row=7, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="DOB : " + infolist[3], font='Helvetica 12 bold')
                self.label2.grid(row=8, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="ADDRESS : " + infolist[4], font='Helvetica 12 bold')
                self.label2.grid(row=9, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="VALIDITY DATE : " + infolist[5], font='Helvetica 12 bold')
                self.label2.grid(row=10, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="LICENCE TYPE : " + infolist[6], font='Helvetica 12 bold')
                self.label2.grid(row=11, column=0, pady=8, padx=5)
                self.mySubmitButton = Button(self.top, text='MODIFY', bg='#ff0000', font='bold', command=self.modifyit)
                self.mySubmitButton.grid(row=12, columnspan=2)
    def modifyit(self):
        with open('dl.json', 'r+') as f:
            dicdl = json.load(f)
            dl = self.dlno.get()
            pos=dicdl[dl]
            f1=open("dldata.txt","r+")
            f1.seek(pos)
            var=f1.readline()
            f1.close()
            infolist = var.split("/")
            top = Toplevel(self.top)
            top.title("MODIFY DL ")
            top.geometry("530x450")
            self.label1 = Label(top, text="   ENTER THE DETAILS   ", font='Helvetica 18 bold')
            self.label1.grid(row=5, column=0, pady=8, padx=5)
            self.dlnol = Label(top, text="      DL number", font='Helvetica 12 bold')
            #self.dlnol.grid(row=6, column=0, padx=5, pady=8)
            self.dlno = Entry(top)
            self.dlno.insert(0,infolist[0])
            #self.dlno.grid(row=6, column=1, pady=8)
            self.fnamel = Label(top, text="      First name", font='Helvetica 12 bold')
            self.fnamel.grid(row=7, column=0, padx=5, pady=8)
            self.fname = Entry(top)
            self.fname.insert(0, infolist[1])
            self.fname.grid(row=7, column=1, pady=8)
            self.lnamel = Label(top, text="      last name", font='Helvetica 12 bold')
            self.lnamel.grid(row=8, column=0, padx=5, pady=8)
            self.lname = Entry(top)
            self.lname.insert(0, infolist[2])
            self.lname.grid(row=8, column=1, pady=8)
            self.dobl = Label(top, text="      D.O.B(dd-mm-yyyy) : ", font='Helvetica 12 bold')
            self.dobl.grid(row=9, column=0, padx=5, pady=8)
            self.dob = Entry(top)
            self.dob.insert(0, infolist[3])
            self.dob.grid(row=9,column=1,pady=8)
            self.addrl = Label(top, text="      Address :  ", font='Helvetica 12 bold')
            self.addrl.grid(row=10, column=0, padx=5, pady=8)
            self.addr = Entry(top)
            self.addr.insert(0, infolist[4])
            self.addr.grid(row=10, column=1, pady=8)
            self.vdatel = Label(top, text="      Validity date(dd-mm-yyyy) : ", font='Helvetica 12 bold')
            self.vdatel.grid(row=11, column=0, padx=5, pady=8)
            self.vdate = Entry(top)
            self.vdate.insert(0, infolist[5])
            self.vdate.grid(row=11, column=1, pady=8)
            self.ltypel = Label(top, text="      Licence type ", font='Helvetica 12 bold')
            #self.ltypel.grid(row=12, column=0, padx=5, pady=8)
            self.ltype = Entry(top)
            self.ltype.insert(0, infolist[6])
            #self.ltype.grid(row=12, column=1, pady=8)
            self.mySubmitButton = Button(top, text='Submit', command=self.sendit)
            self.mySubmitButton.grid(row=13, columnspan=2)

    def sendit(self):
        with open('dl.json', 'r+') as f:
            dicdl = json.load(f)
            sbuf = self.dlno.get() + "/" + self.fname.get() + "/" + self.lname.get() + "/" + self.dob.get() + "/" + self.addr.get() + "/" + self.vdate.get() + "/" + self.ltype.get()+"/"
            pos = dicdl[self.dlno.get()]
            f1 = open("dldata.txt", "r+")
            f1.seek(pos)
            while len(sbuf) <= 100:
                sbuf += "_"
            f1.write(sbuf)
            f1.close()
        self.top.destroy()
#to modify the record of the registration
class modi:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("MODIFY RG ")
        top.geometry("530x450")
        self.label1 = Label(top, text="REGISTRATION NUMBER", font='Helvetica 18 bold')
        self.label1.grid(row=0, column=0, pady=8, padx=5)
        self.dlno = Entry(top)
        self.dlno.grid(row=1, column=0, pady=8)
        self.mySubmitButton = Button(top, text='SEARCH',bg='#33cc33', font='bold', command=self.send)
        self.mySubmitButton.grid(row=3, columnspan=2)
    def send(self):
        with open('rg.json', 'r+') as f :
            dicdl = json.load(f)
            dl=self.dlno.get()
            if dl not in dicdl :
                self.label2 = Label(self.top, text="         RECORD NOT FOUND                            ", font='Helvetica 12 bold')
                self.label2.grid(row=5, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                                  ", font='Helvetica 12 bold')
                self.label2.grid(row=6, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                                 ", font='Helvetica 12 bold')
                self.label2.grid(row=7, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                                 ", font='Helvetica 12 bold')
                self.label2.grid(row=8, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                                  ", font='Helvetica 12 bold')
                self.label2.grid(row=9, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                                   ", font='Helvetica 12 bold')
                self.label2.grid(row=10, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="                                                                                    ", font='Helvetica 12 bold')
                self.label2.grid(row=11, column=0, pady=8, padx=5)
                self.mySubmitButton = Label(self.top, text='                 ', bg='#ff0000', font='bold')
                self.mySubmitButton.grid(row=12, columnspan=2, pady=8, padx=5)
            else :
                pos = dicdl[dl]
                f1 = open("rgdata.txt", "r+")
                f1.seek(pos)
                var = f1.readline()
                f1.close()
                infolist = var.split("/")
                self.label2 = Label(self.top, text="REGISTRATION NUMBER : " + infolist[0], font='Helvetica 12 bold')
                self.label2.grid(row=5, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="FIRST NAME : " + infolist[1], font='Helvetica 12 bold')
                self.label2.grid(row=6, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="LAST NAME : " + infolist[2], font='Helvetica 12 bold')
                self.label2.grid(row=7, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="DOB : " + infolist[3], font='Helvetica 12 bold')
                self.label2.grid(row=8, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="ADDRESS : " + infolist[4], font='Helvetica 12 bold')
                self.label2.grid(row=9, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="VALIDITY DATE : " + infolist[5], font='Helvetica 12 bold')
                self.label2.grid(row=10, column=0, pady=8, padx=5)
                self.label2 = Label(self.top, text="VEHICLE TYPE : " + infolist[6], font='Helvetica 12 bold')
                self.label2.grid(row=11, column=0, pady=8, padx=5)
                self.mySubmitButton = Button(self.top, text='MODIFY', bg='#ff0000', font='bold', command=self.modifyit)
                self.mySubmitButton.grid(row=12, columnspan=2)
    def modifyit(self):
        with open('rg.json', 'r+') as f:
            top = Toplevel(self.top)
            top.title("MODIFY RG ")
            top.geometry("530x450")
            dicdl = json.load(f)
            dl = self.dlno.get()
            pos = dicdl[dl]
            f1 = open("rgdata.txt", "r+")
            f1.seek(pos)
            var = f1.readline()
            f1.close()
            infolist = var.split("/")
            self.label1 = Label(top, text="ENTER THE DETAILS", font='Helvetica 18 bold')
            self.label1.grid(row=5, column=0, pady=8, padx=5)
            self.dlnol = Label(top, text="RG number        "+infolist[0], font='Helvetica 12 bold')
            #self.dlnol.grid(row=6, column=0, padx=5, pady=8)
            self.dlno = Entry(top)
            self.dlno.insert(0,infolist[0])
            #self.dlno.grid(row=6, column=1, pady=8)
            self.fnamel = Label(top, text="First name", font='Helvetica 12 bold')
            self.fnamel.grid(row=7, column=0, padx=5, pady=8)
            self.fname = Entry(top)
            self.fname.insert(0, infolist[1])
            self.fname.grid(row=7, column=1, pady=8)
            self.lnamel = Label(top, text="last name", font='Helvetica 12 bold')
            self.lnamel.grid(row=8, column=0, padx=5, pady=8)
            self.lname = Entry(top)
            self.lname.insert(0, infolist[2])
            self.lname.grid(row=8, column=1, pady=8)
            self.dobl = Label(top, text="D.O.B(dd-mm-yyyy) : ", font='Helvetica 12 bold')
            self.dobl.grid(row=9, column=0, padx=5, pady=8)
            self.dob = Entry(top)
            self.dob.insert(0, infolist[3])
            self.dob.grid(row=9,column=1,pady=8)
            self.addrl = Label(top, text="Address :  ", font='Helvetica 12 bold')
            self.addrl.grid(row=10, column=0, padx=5, pady=8)
            self.addr = Entry(top)
            self.addr.insert(0, infolist[4])
            self.addr.grid(row=10, column=1, pady=8)
            self.vdatel = Label(top, text="Validity date(dd-mm-yyyy) : ", font='Helvetica 12 bold')
            self.vdatel.grid(row=11, column=0, padx=5, pady=8)
            self.vdate = Entry(top)
            self.vdate.insert(0, infolist[5])
            self.vdate.grid(row=11, column=1, pady=8)
            self.ltypel = Label(top, text="Vehilce type            "+infolist[6], font='Helvetica 12 bold')
            #self.ltypel.grid(row=12, column=0, padx=5, pady=8)
            self.ltype = Entry(top)
            self.ltype.insert(0, infolist[6])
            #self.ltype.grid(row=12, column=1, pady=8)
            self.mySubmitButton = Button(top, text='Submit', command=self.sendit)
            self.mySubmitButton.grid(row=13, columnspan=2)

    def sendit(self):
        with open('rg.json', 'r+') as f:
            dicdl = json.load(f)
            sbuf = self.dlno.get() + "/" + self.fname.get() + "/" + self.lname.get() + "/" + self.dob.get() + "/" + self.addr.get() + "/" + self.vdate.get() + "/" + self.ltype.get()+"/"
            pos = dicdl[self.dlno.get()]
            f1 = open("rgdata.txt", "r+")
            f1.seek(pos)
            while len(sbuf)<=100 :
                sbuf+="_"
            f1.write(sbuf)
            f1.close()

        self.top.destroy()

def vr():
        inputDialog = vehicle(root)
        root.wait_window(inputDialog.top)

def dr():
        inputDialog = driving(root)
        root.wait_window(inputDialog.top)

def fine():
        inputDialog = finec(root)
        root.wait_window(inputDialog.top)

root=Tk()
root.title("RTO")
root.geometry("530x350")
label1 = Label(text="REGIONAL TRANSPORT OFFICE", font='Helvetica 18 bold')
b1 = Button(text="DRIVING LICENCE", width=25, bg='#2ECC71', font='bold',command=dr)
b2 = Button(text="VEHICLE REGISTRATION", width=25, bg='#2ECC71', font='bold',command=vr)
b3 = Button(text="FINE", width=25, bg='#2ECC71', font='bold',command=fine)
b4 = Button(text="QUIT", width=25, bg='#E74C3C', font='bold', command=quit)
label1.grid(row=0, column=0, pady=10, padx=50)
b1.grid(row=6, column=0, pady=10, padx=50)
b2.grid(row=12, column=0, pady=10, padx=50)
b3.grid(row=18, column=0, pady=10, padx=50)
b4.grid(row=24, column=0, pady=30, padx=50)
root.mainloop()

def vr ():
    inputDialog = vehicle(root)
    root.wait_window(inputDialog.top)
def dr():
    inputDialog = driving(root)
    root.wait_window(inputDialog.top)

def fine():
    inputDialog = finec(root)
    root.wait_window(inputDialog.top)