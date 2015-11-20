#!/home/cdieken/applied_python/bin/python

import email_helper

recipient = 'cdieken@verisign.com'
subject = 'Test message'
message = '''
This is a fictional message.

Regards
Chris
'''

sender = 'cdieken@verisign.com'

email_helper.send_mail(recipient, subject, message, sender)


