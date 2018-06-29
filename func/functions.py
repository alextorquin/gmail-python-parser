#!/usr/bin/env python
import creds.login as cred

#|------------------------------------
#| ParseEmail Class
#|------------------------------------
#| A collection of functions to parse and interact with our returned emails

class ParseEmail(object):
    
    ''' We expect our email to have a sender, a subject and a msg payload '''
    def __init__(self, email_from, subject, msg):
        self.email_from = email_from
        self.subject = subject
        self.msg = msg 

    ''' Our function to print the email to the screen for debugging '''
    def print_email(self):
        print ('>> Returned an email matching search criteria')
        print ('Email from: ' + self.email_from)
        print ('Subject: ' + self.subject + '\n')
        print str(self.msg)

    ''' Our function to filter through emails to look for a specific sender '''
    def find_specific(self):
        if( self.email_from == cred.PARSE_BY):
            found_email = ParseEmail(self.email_from, self.subject, self.msg)
            print found_email.print_email()
        else:
            pass