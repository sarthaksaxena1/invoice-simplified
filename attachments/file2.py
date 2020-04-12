import sys
# print(sys.argv[1])
import os
import pdftables_api #IMPORTANT LIBRARY 
import time
print("Started Computer Vision To Analyaze PDF Files")
time.sleep(2)
dirs= os.listdir()
for file in dirs:
    if(file.endswith('.pdf')):
        print("Analyzing : ",file)
        c = pdftables_api.Client('hksh1ytt3b6o') # MY API SECRET KEY 
        print("Generating Excel For : ",file)
        time.sleep(2)
        c.xlsx(file, file+'.xlsx') # FOR EXCEL
        print("Generating XML For DataScience Enthusiasts : ",file)
        time.sleep(2)
        c.xml(file, file+'.xml') # FOR XML
        # c.csv('main.pdf','output.csv') //IF YOU WANT CSV FILE UNCOMMENT THIS 
        # c.html('main.pdf','output.html') //IF YOU WANT HTML GILE UNCOMMENT THIS

os.system('mkdir files')
os.system("mv *.xlsx ./files/ && mv *.xml ./files/")
print("Making Final Zip File ")
time.sleep(3)
os.system("cd ./files && powershell Compress-Archive * final.zip")
print("Zip FIle Created With Name : final.zip")
print("[1]- To Open Zip File \n ")
print("[2]- To Email Zip File \n ")
option=int(input("Please Choose An Option Given Above [Enter Integer Only] : \n"))
if(option==1):
    print("Opening Zip File ....")
    time.sleep(4)
    print("Calling System Process To Allocate Memory .....")
    time.sleep(2)
    print("Opening Zip !! ")
    os.system('cd files && final.zip')
elif(option==2):
    os.system("cd files && mv final.zip ../")
    print("Email Wizard Loading ....")
    time.sleep(2)
    print("Calling System Process To Allocate Memory For Processing Emails .....")
    time.sleep(2)
    print(" \n\n PLEASE NOTE I USED MY CUSTOM MAIL SERVER IF YOU WANT TO USE GMAIL USE GMAIL SMTP SERVER \n \n")
    time.sleep(1)
    recv_name=email=input(" \n TO NAME : ")
    recv_email=input("\n TO EMAIL : ")
    send_email=input("\n FROM EMAIL : " )
    email_pass=input("\n Your Password : ")
    
    
    print("Checking Internet Connection .....")
    time.sleep(4)
    print("Launching EmailSend Process ...")
    os.system('python3 ./mail.py '+recv_name+' '+recv_email+' '+send_email+' '+email_pass)
        


