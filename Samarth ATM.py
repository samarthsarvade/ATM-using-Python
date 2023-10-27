print('Samarth Bank Co-operation Limited')
print("Select Language \ भाषा निवडा -\n[1] मराठी\n[2] English")
language=int(input())
if language==1:
    print("...तुमचे स्वागत आहे...")
    account=input("खात्याचे नाव: ")
    password=int(input("तुमचा पासवर्ड एंटर करा: "))
    m=500000
    if account=="Samarth Ramakant Sarvade" and password==454545:
        print('तुमचे पर्याय निवडा -\n[1] पैसे काढणे\n[2] क्रेडिट\n[3] शिल्लक\n[4] बाहेर पडा')
        option=int(input())
        if option==1:
            a=int(input("पैसे काढण्याची रक्कम प्रविष्ट करा: "))
            if a<m and m%100==0:
                print("व्यवहार पूर्ण..\nकृपया तुमची रक्कम काढा: $",a)
                import time
                time.sleep(5)
                print("कृपया पुन्हा भेट द्या")
            else:
                print("व्यवहार अयशस्वी..")
        if option==2:
            b=int(input("क्रेडिट रक्कम प्रविष्ट करा: "))
            if b<=20000:
                print("व्यवहार पूर्ण..\nआता, तुमची एकूण शिल्लक: $",b+m)
                import time
                time.sleep(5)
                print("कृपया पुन्हा भेट द्या")
            else:
                print("व्यवहार अयशस्वी..$20000 पर्यंत क्रेडिटची परवानगी आहे")
        if option==3:
            print("खात्यातील शिल्लक: $",m)
            import time
            time.sleep(5)
            print("कृपया पुन्हा भेट द्या")
        if option==4:
            print("कृपया पुन्हा भेट द्या")
   

if language == 2:
    print("...Welcome...")
    account = input("Account Name: ")
    password = int(input("Enter Your Password: "))
    m = 500000
    if account == "Samarth Ramakant Sarvade" and password == 454545:
        print('Choose your options -\n[1] Withdrawal\n[2] Credit\n[3] Balance\n[4] Exit')
        option = int(input())
        if option == 1:
            a = int(input("Enter Withdraw Amount: "))
            if a < m and m % 100 == 0:
                print("Transaction Complete..\nPlease withdraw your amount: $", a)
                import time
                time.sleep(5)
                print("Please Visit Again")
            else:
                print("Transaction Failed..")
        elif option == 2:
            b = int(input("Enter Credit Amount: "))
            if b <= 20000:
                print("Transaction Complete..\nNow, your total balance: $", b+m)
                import time
                time.sleep(5)
                print("Please Visit Again")
            else:
                print("Transaction Failed..Upto $20000 Credit allowed")
        elif option == 3:
            print("Account Balance: $", m)
            import time
            time.sleep(5)
            print("Please Visit Again")
        elif option == 4:
            print("Please Visit Again")
    else:
        print("Invalid Password")
exit()


 
