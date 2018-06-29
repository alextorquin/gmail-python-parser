#!/usr/bin/env python

# |-------------------------------------------------------------
# | Gmail Python Parser v1.0
# |-------------------------------------------------------------
#
# A python script designed to consume and parse emails from Gmail
# and push the data to a MySQL database.

import smtplib
import imaplib
import email
import creds.login as cred
import func.functions as func

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(cred.SMTP_SERVER, cred.SMTP_PORT)
        mail.login(cred.FROM_EMAIL, cred.FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id, first_email_id, -1):
            type, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']

                    if( email_from == cred.PARSE_BY ):
                        func.display_email(email_from, email_subject, msg)
                    else:
                        print email_from

    except Exception, e:
        print str(e)

read_email_from_gmail()