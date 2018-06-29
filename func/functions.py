#!/usr/bin/env python

''' Create our class to log emails '''
class ParseEmail(object):
    
    def __init__(self, email_from, subject, msg):
        self.email_from = email_from
        self.subject = subject
        self.msg = msg 

    def print_email(self):
        print ('>> Returned an email matching search criteria \n')
        print ('Email from: ' + self.email_from + '\n')
        print ('Subject: ' + self.subject + '\n')
        print str(self.msg)
    


    