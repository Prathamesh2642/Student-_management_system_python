# @classmethod decorator

# class method only contains static variables 
#garbage collector is supported by thread, threading and multithreading always runs in background removes the object that is unused by the program

# destructor in python is called by __del__  python garbage collector and destructor has good communication whenever garbage collector removes an element from 
#the memory using destructor

#compile time polymorphism static  - function overloading same name different number of arguements

#runtime polymorphism                funtion overriding 

# python doesn't support method overloading and constructor overloading
# python does support method overriding and constructor overriding
# in the case of method overloading python always considers last method

#Student info
class basicinfo:
    collegename="Dr.D.Y. Patil Institute of Technology"
    def __init__(self):
        self.name=None
        self.perc=0
        self.grade=None
        self.sem=0
        self.login()
    
    def login(self):
        while(True):
            try:
                self.Username=input("Enter name: ")
                password=input("Enter password: ")
                if(self.Username=="Prathamesh" and password=="12345"):
                    print("Login Successfull\nWelcome ",self.Username)
                    break
                else:
                    print("Wrong username or password! please try again")
            except ValueError as msg:
                print(msg)

class branch(basicinfo):
    def __init__(self):
        self.branchinfo()
    def branchinfo(self):
        while(True):
            self.branch=int(input("Enter Branch number: \n1.AI&DS\n2.Computer Science\n3.IT\n4.E&TC\n5.Mechanical\n6.Electrical\n7.A&R"))
            if(self.branch==1):
                self.Aids()
                break
            elif(self.branch==2):
                self.comp()
                break
            elif(self.branch==3):
                self.it()
                break
            elif(self.branch==4):
                self.it()
                break
            elif(self.branch==5):
                self.it()
                break
            elif(self.branch==6):
                self.it()
                break
            elif(self.branch==7):
                self.it()
                break
            else:
                print("Enter Valid number")
                continue

    def semesterinfo(self):
            while(True):
                self.sem=int(input("Enter your semester: "))
                if(self.sem>=0 and self.sem<=2):
                    return self.sem
                else:
                    print("Enter valid semester number, semester can be 1 and 2 only")
    def firstyearfirstsem(self):
                self.m1=int(input("Enter Marks in M1: "))
                self.m2=int(input("Enter Marks in SME: "))
                self.m3=int(input("Enter Marks in PPS: "))
                self.m4=int(input("Enter Marks in BEE: "))
                self.m5=int(input("Enter Marks in CHEMISTRY: "))
                self.lstmarks=[self.m1,self.m2,self.m3,self.m4,self.m5]
    def firstyearsecondsem(self):
                self.m1=int(input("Enter Marks in M2: "))
                self.m2=int(input("Enter Marks in EG: "))
                self.m3=int(input("Enter Marks in EM: "))
                self.m4=int(input("Enter Marks in BXE: "))
                self.m5=int(input("Enter Marks in PHYSICS: "))
                self.lstmarks=[self.m1,self.m2,self.m3,self.m4,self.m5]
    def aids2ndyear1stsem(self):
                self.m1=int(input("Enter Marks in DM: "))
                self.m2=int(input("Enter Marks in FDS: "))
                self.m3=int(input("Enter Marks in OOP: "))
                self.m4=int(input("Enter Marks in CG: "))
                self.m5=int(input("Enter Marks in OS: "))
                self.lstmarks=[self.m1,self.m2,self.m3,self.m4,self.m5]
    def aids2ndyear2ndsem(self):
                self.m1=int(input("Enter Marks in Statistics: "))
                self.m2=int(input("Enter Marks in DSA: "))
                self.m3=int(input("Enter Marks in SE: "))
                self.m4=int(input("Enter Marks in IOT: "))
                self.m5=int(input("Enter Marks in MIS: "))
                self.lstmarks=[self.m1,self.m2,self.m3,self.m4,self.m5]

    def Aids(self):
            print("Welcome to AI&DS ")
            while(True):
                self.yr=int(input("Enter your year: 1.First year 2.Second year 3.Third Year 4.Fourth Year:\n"))
                if(self.yr==1):
                    sem=self.semesterinfo()
                    if(sem==1):
                        self.firstyearfirstsem()
                    elif(sem==2):
                        self.firstyearsecondsem()
                    break
                elif(self.yr==2):
                    sem=self.semesterinfo()
                    self.aids2ndyear1stsem()
                    break
                elif(self.yr==3):
                    sem=self.semesterinfo()
                    break
                elif(self.yr==4):
                    sem=self.semesterinfo()
                    break
                else:
                    print("Enter valid year 1-4 only!!")
                    continue
    def listsofsubjects(self,year,sem,branch):
        if(branch==1):
            if(year==1 and sem==1):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==1 and sem==2):
                return ["M2 ","EG","EM","BXE","PHY"]
            elif(year==2 and sem==1):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==2 and sem==2):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==3 and sem==1):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==3 and sem==2):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==4 and sem==1):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==4 and sem==2):
                return ["M1 ","SME","PPS","BEE","CHE"]
        elif(branch==2):
            if(year==1 and sem==1):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==1 and sem==2):
                return ["M2 ","EG","EM","BXE","PHY"]
            elif(year==2 and sem==1):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==2 and sem==2):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==3 and sem==1):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==3 and sem==2):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==4 and sem==1):
                return ["M1 ","SME","PPS","BEE","CHE"]
            elif(year==4 and sem==2):
                return ["M1 ","SME","PPS","BEE","CHE"] # computer subject list
        elif(branch==3):
            pass # IT subject list
        elif(branch==4):
            pass # E&TC subject list
        elif(branch==5):
            pass # Mechanical subject list
        elif(branch==6):
            pass # Electrical subject list            
        elif(branch==7):
            pass # A&R subject list
        else:
            print("Enter valid branch number")
class result(branch):
    def __init__(self):
        basicinfo.__init__(self)
        branch.__init__(self)
        print(self.yr,self.sem,self.branch)
        self.listofsub=self.listsofsubjects(self.yr,self.sem,self.branch)
        print(self.listofsub)
    def calculate(self):
            total=self.m1+self.m2+self.m3+self.m4+self.m5
            self.perc=total/5
            print(self.perc)
    def gradecalculation(self):
        self.grade=""
        if(self.perc>75):
            self.grade="Distinction"
        elif(self.perc>75):
            self.grade="Distinction"
    def printresult(self):
        print("=====================================================================================================")
        print("|                                                                                                   |")
        print("|                                                                                                   |")
        print(f"|                              {self.collegename}                                |")
        print(f"|                               {self.Username}                                                          |")
        print("|                                                                                                   |")
        print("=====================================================================================================")
        # print(f"Percentage is {self.perc}")
        print("|Subject name                Total marks                            obtained marks                  |")
        print("-----------------------------------------------------------------------------------------------------")
        for i,j in list(zip(self.listofsub,self.lstmarks)):
            print("|",i,f"        |                  100           :                        {j}                          |")
        print("=====================================================================================================")
        print(f"|                                                             percentage:{self.perc}                       |")
        print("=====================================================================================================")
            

obj=result()
obj.calculate()
obj.printresult()
