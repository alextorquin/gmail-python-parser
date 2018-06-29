#!/usr/bin/env python

# |-------------------------------------------------------------
# | Gmail Python Parser v1.0
# |-------------------------------------------------------------
#
# A python script designed to consume and parse emails from Gmail
# and push the data to a MySQL database.

''' import our required modules '''
import smtplib
import imaplib
import email
import creds.login as cred
import func.functions as func

def read_email_from_gmail():
    try:
        ''' Create our connection to our Gmail account '''
        mail = imaplib.IMAP4_SSL(cred.SMTP_SERVER, cred.SMTP_PORT)
        mail.login(cred.FROM_EMAIL, cred.FROM_PWD)
        mail.select('inbox')

        ''' Search through our selected folder '''
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        ''' Count our emails '''
        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        ''' iterate through each of our counted emails '''
        for i in range(latest_email_id, first_email_id, -1):
            type, data = mail.fetch(i, '(RFC822)' )
            for response_part in data:

                try:
                    ''' Load our captured email data into variables '''
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']

                    ''' Pass our captured email to our Parsing class '''
                    captured_email = func.ParseEmail(email_from, email_subject, msg)
                    return captured_email.find_specific()

                except Exception, e:
                    pass

    except Exception, e:
        print str(e)

    # Close our selected folder and logout 
    finally:
        mail.close()
        mail.logout()

read_email_from_gmail()