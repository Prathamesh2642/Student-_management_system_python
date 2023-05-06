import csv
#can we create an alias or shortcut name of exception classes
#ans= yes

#can we have multiple except blocks for a single try block
#ans=yes

#can we take default except as a first except block
#ans=no  

#else possiblw with try except
#yes


# try:
#     a=int(input("Enter number "))
#     b=int(input("Enter number "))
#     print(a/b)
# except ZeroDivisionError as message:
#     print(message," not possible")
# except ValueError as msg:
#     print(msg)

# except:
#     print("Not possible")
# else:
#     print("Hello World")
# finally:
#     print("Bye bye")

#if except is executed then else is skipped, finally is always executed

#csv file is lighter and consumes less memory than xsls file 


#working with csv files

# file=open("Student.csv","a",newline="")
# a=csv.writer(file)
# a.writerow(["Sid","name","yrs"])
# while True:
#     sid=input("Enter sid ")
#     name=input("Enter name ")
#     yrs=input("Enter YRS")
#     a.writerow([sid,name,yrs])
#     print("Record Inserted")
#     break


#student database
def getlastid():
    with open("Studentdb.csv",newline='') as f:
        read=csv.reader(f)
        lst=list(read)
    # print(len(lst))
    # print(lst[len(lst)-1][0])
        return int(lst[len(lst)-1][0])

def insert():
    file=open("Studentdb.csv","a",newline="")
    ins=csv.writer(file)
    # ins.writerow(["id","name","roll no","emailid","address","mobileno","p1","p2","p3","p4","p5","total","percentage","result"])
    name=input("Enter name ")
    rollno=input("Enter rollno ")
    emailid=input("Enter email id ")
    address=input("Enter address ")
    mobileno=int(input("Enter mobile "))
    m1=int(input("Enter marks in paper 1 "))
    m2=int(input("Enter marks in paper 2 "))
    m3=int(input("Enter marks in paper 3 "))
    m4=int(input("Enter marks in paper 4 "))
    m5=int(input("Enter marks in paper 5 "))

    total=m1+m2+m3+m4+m5
    perc=total/5
    if(m1>40 and m2>40 and m3>40 and m4>40 and m5>40):
        result="Pass"
    else:
        result="Fail"
    id1=getlastid()+1

    ins.writerow([id1,name,rollno,emailid,address,mobileno,m1,m2,m3,m4,m5,total,perc,result])
# id1=0
def update1(sid2,lis):
        file=open("Studentdb.csv","r+")
        with open("Studentdb.csv",newline='') as f:
            read=csv.reader(f)
            lst=list(read)
            for i in range(1,len(lst)):
                if(int(sid2)==i):
                    print(read[i])
                    

while True:
    ch=int(input("Enter Choice: 1.Insert 2.Read 3.Update 4.Delete 5.Exit : "))
    if (ch==1):
        insert()
    elif (ch==2):
        read()
    elif(ch==3):
        id3=input("Enter the id ")
        with open("Studentdb.csv","r") as f:
            read=list(csv.reader(f))
            print(read)
            for i in range(1,len(read)):
                if id3==read[i][0]:
                    updatelist=read[i]

        # update1(id3,updatelist)
    elif(ch==4):
        delete()
    elif(ch==5):
        break
    else:
        print("Enter valid values")
        continue
    

import csv
with open("Studentdb.csv",newline='') as f:
    read=csv.reader(f)
    lst=list(read)
    print(len(lst))
    print(lst[len(lst)-1][0])

    inp=int(input("Enter sid: "))
    # print(lst[2][0])
    for i in range(1,len(lst)):
        print(lst[i][0])
        if(inp==lst[i][0]):
            print("hi")
            print(lst[i])


# import csv
# with open("Studentdb.csv","r+") as f:
#                read=list(csv.reader(f))
#                for i in range(1,len(read)):
#                     # print(read[i])
#                     if(read[i][0]=='2'):
#                         print(read[i])
#                 # temp=read[i][0]
#                 # if 2==temp:
#                 #     print(read[i])
#                 # else:
#                 #     print("Hello")
    
#                 print(len(list(csv.reader(f))))
