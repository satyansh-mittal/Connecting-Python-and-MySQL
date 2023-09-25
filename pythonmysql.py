import mysql.connector as mys
mycon = mys.connect(host='localhost',user='root',passwd='password',
                    database='project')
if mycon.is_connected():
    print('MySQL is successfully connected')
cursor = mycon.cursor()

def start():
 print("******************************************"*2,"\n")
 print("\t\t\t**********ST MARY'S CONVENT S.S..SCHOOL,UJJAIN **********\n")
 print("\t\t\t\t**********BLOOD BANK INFORMATION SYSTEM**********\n")
 print("Designed and Maintained By:\n")
 print("SATYANSH MITTAL - CLASS XII SCIENCE - ROLL NO - 19   [２０20-21]")
 print("ATIRATH KAPOOR - CLASS XII SCIENCE - ROLL NO - 7    [２０20-21]\n")
 print("******************************************"*2,"\n")
 input("press any key to continue")
 print()

#INTRODUCTION OF PROJECT
def pintro():
 print("-This is a python program which can help you to BLOOD BANK DATABASE")
 print("-This can help you to view,analyze and modify blood bank database")
 print("-You can do analysis of each and every blood tansaction")
 print("-Hope this project work can make your work easier :)")
 input("press any key to continue")

#START OF THE PROGRAM
ch = 0 
start()
pintro()
while ch !=7:
    #MENU OF PROGRAM
    print("\tMAIN MENU")
    print("\t1.SHOW ALL PATIENT DETAILS")
    print("\t2.SEARCH A PATIENT BY NAME")
    print("\t3.SEARCH A PATIENT BY BLOOD GROUP")
    print("\t4.ADD NEW PATIENT")
    print("\t5.UPDATE PATIENT DATA")
    print("\t6.REMOVE PATIENT DATA")
    print("\t7.EXIT")
    print()
    print("\tSelect Your Option (1-7) ")
    ch = int(input("enter = "))
    print()
    if ch==1:
        cursor.execute("select*from bloodbank")
        data = cursor.fetchall()
        for row in data:
            print(row,'\n')
    elif ch==2:
        name = input("Enter name to search = ")
        print()
        cursor.execute("select* from bloodbank where Patient_Name='{}'".format(name))
        data=cursor.fetchall()
        if data:
            print('DATA FOUND\n')
            print(data,"\n")
        else:
            print('INVALID NAME! PLEASE SEARCH BY A RECORDED NAME')
    elif ch==3:
        bg = input("Enter blood group of patients you want to search = ")
        print()
        cursor.execute("select * from bloodbank where Blood_Group='{}'".format(bg))
        data = cursor.fetchall()
        if data:
            print('DATA FOUND\n')
            for row in data:
                print(row,"\n")
        else:
            print('BLOOD GROUP NOT FOUND!')
    elif ch==4:
        a = input('Enter patient code = ')
        b = input("Enter patient's name = ")
        c = input("Enter patient's date of entry = ")
        d = input("Enter patient type(donor/receiver) = ")
        e = int(input('Enter age = '))
        f = input('Enter blood group = ')
        print()
        qry="insert into bloodbank values ('{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f)
        cursor.execute(qry)
        final = input('Save records(y/n) = ')
        if final=='y':
            mycon.commit()    
            print('\n RECORDS SAVED\n')
        else:
            print("OK!")
    elif ch==5:
        a = input("Which patient number's data do you want to update ? = " )
        b = input("Enter the new patient number = ")
        c = input("Enter the new patient's name =")
        d = input('Enter date of entry(yyyy-mm-dd) = ')
        e = input('Enter the new patient type(donor/receiver) = ')
        f = int(input("Enter new age = "))
        g = input("Enter the patient's new blood group = ")
        qry = "update bloodbank set PatientNo='{}',Patient_Name='{}',DOE='{}',Patient_Type='{}',Age='{}',Blood_Group='{}' where PatientNo='{}'".format(b,c,d,e,f,g,a)
        cursor.execute(qry)
        mycon.commit()
        print('SUCCESSFULLY UPDATED!')
    elif ch==6:
        ask = input('By which patient number you want to delete data? = ')
        cursor.execute("delete from bloodbank where PatientNo='{}' ".format(ask))
        mycon.commit()
        print('\nSUCCESSFULLY DELETED\n')
    elif ch==7:
        print('\nTHANKS FOR USING\n')
        print("********************END**********************","\n")
    else:
        print('\nINVALID CHOICE! PLEASE TRY AGAIN.\n')
        continue
        
        
        
 

