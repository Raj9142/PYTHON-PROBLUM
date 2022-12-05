
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="sand123")
cursor=con.cursor()
cursor.execute("create database if not exists items")
cursor.execute("use items")
cursor.execute("create table if not exists cs(sno int,product varchar(20),cost int)")

sql="select*from cs"
cursor.execute(sql)
res=cursor.fetchall()
if res==[]:
    cursor.execute("insert into cs values(1,'cake',40)")
    cursor.execute("insert into cs values(2,'pastry',20)")
    cursor.execute("insert into cs values(3,'sweet',60)")
    cursor.execute("insert into cs values(4,'butters',30)")
    cursor.execute("insert into cs values(5,'cheese',30)")
    cursor.execute("insert into cs values(6,'dosa',50)")
    cursor.execute("insert into cs values(7,'chaumin',70)")
    
    con.commit()

    
cursor.execute ("create table if not exists vip(sno int,varieties varchar(20))")
sql="select*from vip"
cursor.execute(sql)
res=cursor.fetchall()
if res==[]:
    cursor.execute("insert into vip values(1,'vaniella')")
    cursor.execute("insert into vip values(2,'chocklate')")
    cursor.execute("insert into vip values(3,'strawberry')")
    cursor.execute("insert into vip values(4,'butter_scotch')")
    con.commit()


cursor.execute("create table if not exists worker(sno int,name varchar(20),salary int)")
sql="select*from worker"
cursor.execute(sql)
res=cursor.fetchall()
if res==[]:
    cursor.execute("insert into worker values (1,'mukesh',10000)")
    cursor.execute("insert into worker values (2,'ramesh',11000)")
    cursor.execute("insert into worker values (3,'suresh',12000)")
    cursor.execute("insert into worker values (4,'mahesh',15000)")
    con.commit()

from datetime import datetime

print("---------##DIPLOMA COMPUTER SCIENCE PROJECT##--------------")
print("@@@@@@@@@@@@@@@@@@@   WELCOME   @@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("---------RESTAURTANTS E-MENU MANAGENMENT PROJECT-----------")
print("MADE BY - SANDEEP KUMAR VERMA.\n          SHAILAJA KUMARI. \n          RAJNANDANI KUMARI. \n")
print("SUBMITTED BY- GOVERNMENT POLYTECHNIC BHAGALPUR")
print("---------- SESSION= 2020-2023-----------------")
print("______________________________________________")

ch=' '
while ch!='N' or ch!='n':
 print("\n\n\nPlease choose \n1. FOR ADMIN\n2. FOR COSTUMER\n3. FOR EXIT:\n")
 choice=int(input("Enter your choice:"))
 if choice==3:
     break
 if choice==1:
    admin=input("Username:")
    password=int(input("Enter password:"))
    if password==1234:
        
        print("------------------------------------------------------")
        print("    HELLO SIR,YOU LOGGED IN AS ADMIN SUCCESSFULLY     ")
        print("------------------------------------------------------\n")
        print("press 1 To add item in the shop.......................")
        print("press 2 To see item in the shop.......................")
        print("press 3 To update cost of any item....................")
        print("press 4 To add varieties of cake in the shop..........")
        print("press 5 To add worker in the shop.....................")
        print("press 6 TO see workers................................")
        print("press 7 To update salary of any worker:...............\n")

        c=int(input("enter your choice:"))
        if c==1:
           def add():
            sno=int(input("enter sno:"))
            product1=input("enter product name:")
            cost=int(input("enter the cost:"))
            d1=(sno,product1,cost)
            s1='insert into cs values(%s,%s,%s)'
            cursor.execute(s1,d1)
            con.commit()
            print("---------ITEMS ADD SUCESSFULLY--------")
           add()
        elif c==2:
          def items():
           print("item in the shop:")
           sql="select*from cs"
           cursor.execute(sql)
           res=cursor.fetchall()
           t=(['sno','products','cost'])
           for sno,products,cost in res:
            print(sno,":","\t",products,":","\t",'cost',cost)
          items()
        elif c==3:
          def money():
           sno=input("enter the sno of product:")
           n_cost=input("enter the Rupees to be added:")
           cursor.execute("update cs set cost = cost+ "+n_cost+ "where sno=" +sno+ ";")
           con.commit()
           print("Table After Updation:")
           sq="select*from cs"
           cursor.execute(sq)
           res=cursor.fetchall()
           t=(['sno','products','cost'])
           for sno,products,cost in res:
            print(sno,":","\t",products,":","\t","cost",cost)
          money()
        elif c==4:
          def variety():
           sno=input("Enter sno:")
           varieties=input("Enter variety:")
           d2=(sno,varieties)
           s2="insert into vip values(%s,%s)"
           cursor.execute(s2,d2)
          variety()
        elif c==5:
          def ad():
           sno=int(input("Enter sno:"))
           emp=input("Enter name:")
           salary=int(input("Enter the salary:"))
           dx=(sno,emp,salary)
           sy='insert into worker values(%s,%s,%s)'
           cursor.execute(sy,dx)
           con.commit()
           print('-------worker add successfully-----')
          ad()
        elif c==6:
          def worker():
            print("workers in the shop:")
            sql="select*from worker"
            cursor.execute(sql)
            res=cursor.fetchall()
            t=(['sno','name','salary'])
            for sno,name,salary in res:
             print(sno,":","\t",name,":","\t",salary)
          worker()
        elif c==7:
          def up():
             print("chooce 1 to increase the salary:")
             print("choose 2 to decrease the salery:")
             
             name=input("enter the name of employee:")
             
             n_salary=input("enter the rupees to be added:")
             sig=input("enter choice(1/2):")
             if sig==1:
                cursor.execute("update worker set salary=salary+"+n_salary+"where name="+name+';')
                con.commit()
                print("table after updation:")
                sq="select*from worker"
                cursor.execute(sq)
                res=cursor.fetchall()
                t=(['sno','name','salary'])
                for sno,name,salary in res:
                 print(sno,":","\t",name,":","\t",salary)
             if sig==2:
                cursor.execute("update workre set salary=salary-"+n_salary+"where name="+name+';')
                con.commit()
                print("table after updation:")
                sq="select*from worker"
                cursor.execute(sq)
                res=cursor.fetchall()
                t=(['sno','name','salary'])
                for sno,name,salary in res:
                 print(sno,":","\t",name,":","\t",salary)
          up()
  #   else:
  #       print("sorry.....you have entered the wrong input,input from 1to 7")
  # else:
  #     print("\t\t\t\t\t\t\t********wrong password")
 elif choice==2:
          name=input("enter your name:")
          phone=int(input("enter your phone number:"))
          print('press 1 to see the menu:',sep="  ")
          print('press 2 to order an item:')
          c=int(input('enter your choice:'))
          if c==1:
              def items():
                print("item in the shop:")
                sql="select*from cs"
                cursor.execute(sql)
                res=cursor.fetchall()
                t=(['sno','product','cost'])
                for sno,products,cost in res:
                  print(sno,":","\t",products,":","\t",'cost',cost)
              items()
          elif c==2:
           print("what do you want to drder?")
           sql="select*from cs"
           cursor.execute(sql)
           res=cursor.fetchall()
           t=(['sno','products','cost'])
           for sno,products,cost in res:
            print(sno,":","\t",products,":","\t",'cost',cost)
          sql="select * from cs"
          cursor.execute(sql)
          res=cursor.fetchall()
          print(res)
          l=[]
          for i in range(len(res)):
              l.append(res[i][0])
          # print(i)     
          d=input("enter your serial number of item to Buy:")
          if d==1:
             def items():
               print("which cake do you want?")
               kl="select*from vip"
               cursor.execute(kl)
               srh=cursor.fetchall()
               f=(['sno','varieties'])
               for sno,varieties in srh:
                print(sno,":","\t\t",varieties)
               print("choose which cake do you want want ?")
               ck=int(input("enter choice:"))
               if ck==1:
                 print("how much quantity of vaniella cake do you want?")
                 qty=int(input("enter qty"))
                 print("you have successfully ordered your cake!!!\t:")
                 cursor.execute("select*from cs where products='cake'"';')
                 for i in cursor:
                  c=i[2]
                  con.commit()
                 print("Total ammount:",qty*c)
                 print("\n")
                 print(".........................................")
                 print("your Bill")
                 print("costumer's name:",name)
                 print("contact number:",phone)
                 print("cake type: vaniella")
                 print("Number of cakes:",qty)
                 print("total amount:",qty*c)
                 print("THANK YOU FOR ORDERING THE ITEM")
                 print("\t\t\t\t\t\t Date:",datetime.now())
               if ck==2:
                 print("HOW MUCH QUANTITY OF CHOCOLATE CAKE DO YOU WANT?")
                 qty=int(input("enter qty."))
                 print("You have successfully ordered your cake!!t:")
                 cursor.execute("select*from cs where products='cake'" ':')
                 for i in cursor:
                  L=i[2]
                  print("Total amount",qty*L)
                  print("\n")
                  print("........................................")
                  print("YOUR BILL")
                  print("_________________________________________")
                  print("costumer's name:",name)
                  print("costumer's number",phone)
                  print("cake type:CHOCOLATE")
                  print("NO. of cakes:",qty)
                  print("Total amount:",qty*L)
                  print("THANK YOU FOR ORDERING THE ITEM")
                  print("\t\t\t\t\t\t\t\t\t\tDate:",datetime.now())
               if ck==3:
                    print("HOW MUCH QUANTITY OF STRAWBERRY CAKE DO YOU WANT?")
                    qty=int(input("Enter qty."))
                    print("You have successfully ordered your cake!!!\t:")
                    cursor.excute("select*from cs where products='cake'"':')
                    for i in cursor:
                      N=i[2]
                    print("Total amount",qty*N)
                    print("\n")
                    print("..........................................")
                    print("YOUR BILL")
                    print("__________________________________________")
                    print("COSTUMER'S NAME:",name)
                    print("CONTACT NUMBDER:",phone)
                    print("cake type: strawberry")
                    print("Number of cakes:",qty)
                    print("Total amount:",qty*N)
                    print("THANK YOU  FOR ORDERING THE ITEM")
                    print("\t\t\t\t\t\tDate:",datetime.now())

               if ck==4:
                    print("How much quantity of butter scotch cake do you want?")
                    qty=int(input("Enter qty."))
                    print("YOU HAVE SUCCESSFULLY ORDERDE YOUR CAKE!!!\t:")
                    cursor.execute("select*from cs where products='cake'"';')
                    for i in cursor:
                        M=i[2]
                    print("Total ammount",qty*M)
                    print("\n")
                    print("............................................")
                    print("YOUR BILL")
                    print("Costumer's name:",name)
                    print("Contact number:",phone)
                    print("cake type:butter_scotch")
                    print("total amount:",qty*M)
                    print("@@@@@@THANK_YOU FOR ORDERING THE ITEM@@@@@@")
                    print("\t\t\t\t\t\t\t\t\tDate:",datetime.now())
             items()
          elif d==2:
              print("How much pastry do you want:")
              past=int(input("Enter your choice:"))
              cursor.execute("select*from cs where products='pastry'"';')
              for i in cursor:
                  c=i[2]
                  print("Total amount=",past*c)
                  print("\n")
                  print("____________________________________________")
                  print("YOUR BILL")
                  print("____________________________________________")
                  print("Costumer's name",name)
                  print("contact number",phone)
                  print("number of pastry:",past)
                  print("Total amount:",past*c)
                  print("THANK YOU FOR ORDERING THE ITEM")
                  print("\t\t\t\t\t\t\t\t\t\tDate:",datetime.now())
          elif d==3:
                  print("How much liters of milk do you want?")
                  mlk=int(input("Enter your choice:"))
                  print("you have successfully ordered",mlk,"L of milk.")
                  cursor.execute("select*from cs where product='milk'"';')
                  for i in cursor:
                    c=i[2]
                  print("Total amount=",mlk*c)
                  print("\n")
                  print("____________________________________________")
                  print("YOUR BILL")
                  print("____________________________________________")
                  print("Costumer's name",name)
                  print("contact number",phone)
                  print("number of pastry:",mlk)
                  print("Total amount:",mlk*c)
                  print("THANK YOU FOR ORDERING THE ITEM")
                  print("\t\t\t\t\t\t\t\t\t\tDate:",datetime.now())
          elif d==4:
                  print("How many packets(20gm) of butter do you want?")
                  but=int(input("Enter your choice:"))
                  print("you have successfully ordered",but,"packet of butter.")
                  cursor.execute("select*from cs where product='butter'"';')
                  for i in cursor:
                    c=i[2]
                  print("Total amount=",but*c)
                  print("\n")
                  print("____________________________________________")
                  print("YOUR BILL")
                  print("____________________________________________")
                  print("Costumer's name",name)
                  print("contact number",phone)
                  print("quantity of butter:",but)
                  print("Total amount:",but*c)
                  print("THANK YOU FOR ORDERING THE ITEM")
                  print("\t\t\t\t\t\t\t\t\t\tDate:",datetime.now())
          elif d==5:
                  print("How much cheese(in kg)do you want?")
                  chs=int(input("Enter your choice:"))
                  print("you have successfully ordered",chs,"kg of cheese.")
                  cursor.execute("select*from cs where product='cheese'"';')
                  for i in cursor:
                    c=i[2]
                  print("Total amount=",chs*c)
                  print("\n")
                  print("____________________________________________")
                  print("YOUR BILL")
                  print("____________________________________________")
                  print("Costumer's name",name)
                  print("contact number",phone)
                  print("quantity of butter:",chs)
                  print("Total amount:",chs*c)
                  print("THANK YOU FOR ORDERING THE ITEM")
                  print("\t\t\t\t\t\t\t\t\t\tDate:",datetime.now())
          elif d in l:
                  qty=int(input("Enter qty."))
                  print("you have successfully ordered your selected item!!!\t:")
                  cursor.execute("Select*from cs where sno="+str(d))
                  for i in cursor:
                      L=i[2]

                  print("Total amount=",qty*L)
                  print("\n")
                  print("____________________________________________")
                  print("YOUR BILL")
                  print("____________________________________________")
                  print("Costumer's name",name)
                  print("contact number",phone)
                  print("number of pastry:",qty)
                  print("Total amount:",qty*L)
                  print("THANK YOU FOR ORDERING THE ITEM")
                  print("\t\t\t\t\t\t\t\t\t\tDate:",datetime.now())
          else:
              print("Wrong Input")

 else: 
          print("\t\t\t\t\t\t**************Wrong password")

    
      
