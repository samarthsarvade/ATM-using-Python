print('Samarth Bank Co-operation Limited')
print("Select Language -\n[1] Marathi\n[2] English")
language=int(input())
if language==1:
    print("...Aple Swagat Ahe...")
      
if language==2:
    print("...Welcome...")
    account=input("Account Name: ")
    password=int(input("Enter Your Password: "))
    m=500000
    if account=="Samarth Ramakant Sarvade" and password==454545:
        print('Choose your options -\n[1] Withdrawal\n[2] Credit\n[3] Balance\n[4] Exit')
        option=int(input())
        if option==1:
            a=int(input("Enter Withdraw Amount: "))
            if a<m and m%100==0:
                print("Transaction Complete..\nPlease withdraw your amount: $",a)
                import time
                time.sleep(5)
                print("Please Visit Again")
            else:
                print("Transaction Failed..")
        if option==2:
            b=int(input("Enter Credit Amount: "))
            if b<=20000:
                print("Transaction Complete..\nNow, your total balance: $",b+m)
                import time
                time.sleep(5)
                print("Please Visit Again")
            else:
                print("Transaction Failed..Upto $20000 Credit allowed")
        if option==3:
            print("Account Balance: $",m)
            import time
            time.sleep(5)
            print("Please Visit Again")
        if option==4:
            print("Please Visit Again")
   
            
    else:
        print("Invalid Password")
    exit()
        
       
exit()


 
