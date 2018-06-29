#!/usr/bin/env python 

# Define our user login information for their specific gmail account
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "your-email" + ORG_EMAIL
FROM_PWD    = "your-password"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# Set a specific email you want to parse by 
PARSE_BY = 'John Doe <foo@bar.ca>'