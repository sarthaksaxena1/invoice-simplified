import email
import getpass, imaplib
import os
import sys
import time
import subprocess
# import easyai
import numpy
import pandas
filenames=[]
detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
    os.mkdir('attachments')

userName = "na"
passwd = "NA"

try:
    imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
    typ, accountDetails = imapSession.login(userName, passwd)
    if typ != 'OK':
        print 'Not able to sign in!'
        raise
    
    imapSession.select('Paypal')
    typ, data = imapSession.search(None, "ALL")
    if typ != 'OK':
        print 'Error searching Inbox.'
        raise
    
    # Iterating over all emails
    for msgId in data[0].split():
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
        if typ != 'OK':
            print 'Error fetching mail.'
            raise

        emailBody = messageParts[0][1]
        mail = email.message_from_string(emailBody)
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                # print part.as_string()
                continue
            if part.get('Content-Disposition') is None:
                # print part.as_string()
                continue
            fileName = part.get_filename()

            if bool(fileName):
                filePath = os.path.join(detach_dir, 'attachments', fileName)
                if not os.path.isfile(filePath) :
                    print "Downloading File : "+fileName
                    filenames.append(fileName)
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
    imapSession.close()
    imapSession.logout()
except :
    print 'Not able to download all attachments.'

# OTHER CODE 
print "Caluclating No Of Files Downloaded : "
time.sleep(2)
print "Total Files Downloaded : " + str(len(filenames))


cmd = "cd attachments && python3 ./file2.py"
os.system(cmd)



