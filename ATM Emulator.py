import sqlite3
import sys
db=sqlite3.connect("ATM")
cur = db.cursor()
#cur.execute('''create table u_accn (account_no integer(5) PRIMARY KEY,u_name varchar(50),u_pin integer(4),u_bal integer(10))''')
#db.commit()
#print 'Table formed successfully !!!!'

#cur.execute('''insert into u_accn(account_no,u_name,u_pin,u_bal) values(?,?,?,?)''',(10010,'Lavanya',5682,56000))
#print 'Data Inserted!!!!'
#db.commit()
if cur.execute('''select account_no,u_name,u_pin,u_bal from u_accn'''):
    print 'Records got successfully!!!!'

print '-------------------------------------'
recordsAll=cur.fetchall()
for record in recordsAll:
    print('{0},{1},{2},{3}'.format(record[0],record[1],record[2],record[3]))


print 'Welcome to HPES Bank.'
s=input('Please enter account_no:\n')
p=input('Please enter PIN :\n')
if cur.execute('''SELECT u_name from u_accn where account_no=? and u_pin=?''',(s,p,)):
        record1=cur.fetchone()
        if(record1==None):
            print 'Invalid Account_no or PIN.!!!Please try again later!'
        else:

            print 'Welcome %s'%(record1)
            n=input('Please enter\n1.Cash Withdrawal\n2.View Account Balance\n3.Exit\n')
            if(n==3):
                sys.exit()
            if(n==2):
                if cur.execute('''SELECT u_bal from u_accn where account_no=? and u_pin=?''',(s,p,)):
                    record1 = cur.fetchone()
                    print 'Your balance is: Rs.%d'%(record1)
            elif(n==1):
                if cur.execute('''SELECT u_bal from u_accn where account_no=? and u_pin=?''',(s,p,)):
                    record1 = cur.fetchone()

                    a = input("Enter Amount to be Withdrawn \n")
                    j=record1[0];
                    if(a>int(record1[0])):
                        print 'You have entered more amount than available in your account!!!Please try again later !'
                    else:
                        t1 = a % 2000
                        t2 = t1 % 500
                        t3 = t2 % 100
                        t4 = t3 % 50
                        r1 = a / 2000
                        r2 = t1 / 500
                        r3 = t2 / 100
                        r4 = t3 / 50

                        if a % 50 == 0 and a % 100 == 0 and a % 500 == 0 and a % 2000 == 0:
                            e = a / 2000
                            print "2000 X", e, "=", 2000 * e
                            f = j - a

                            if cur.execute('''update u_accn set u_bal=? where account_no=?''', (f, s,)):
                                print 'Transaction completed successfully!!!!Amount Withdrawn : ', a
                                print "Reamaining Balance in your account : ", f
                                db.commit()

                        elif a % 50 == 0:

                            if t1 != 0:

                                print "2000 X ", r1, "=", 2000 * r1
                                print "500 X ", r2, "=", 500 * r2
                                print "100 X ", r3, "=", 100 * r3
                                print "50 X ", r4, "=", 50 * r4
                            elif t2 != 0:
                                print "500 X ", r2, "=", 500 * r2
                                print "100 X ", r3, "=", 100 * r3
                                print "50 X ", r4, "=", 50 * r4
                            elif t3 != 0:
                                print "100 X ", r3, "=", 100 * r3
                                print "50 X ", r4, "=", 50 * r4
                            elif t4 != 0:
                                print "50 X ", r4, "=", 50 * r4
                            f = j - a

                            if cur.execute('''update u_accn set u_bal=? where account_no=?''', (f, s,)):
                                print 'Transaction completed successfully!!!!Amount Withdrawn : ',a
                                print "Remaining Balance in your account : ", f
                                db.commit()
                        else:
                            print "Invalid Amount!!!! Please Try Again Later! "
                            print "Please enter amount in multiples of 50"




            else:
                print 'You have entered more amount than available in your account'

raw_input("Thanks for using HPES Bank !!!!")
