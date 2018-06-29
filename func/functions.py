#!/usr/bin/env python

class Count(object):
    def __init__(self):
        self.count = 0

    def msg_status(self, result):
        if( self.count != 0 ):
            self.count += 1

def display_email(email_from, email_subject, msg):
    print ('>> Found an email matching the search criteria..\n\n')
    print 'From : ' + email_from
    print 'Subject : ' + email_subject + '\n'
    print msg
    print '\n\n'


    