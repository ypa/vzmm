import sendgrid
from django.conf import settings

class SGClient(object):

    def __init__(self):
        self.sg = sendgrid.SendGridClient(settings.SG_USER, settings.SG_PWD)

    def compose_msg(self, subject=None, text=None):
        self.message = sendgrid.Mail()    
        self.message.set_subject(subject)
        self.message.set_html('Body')
        self.message.set_text(text)    

    def send(self, from_email=None, domain=None):
        to_email = lookup_to_contact(domain)
        self.message.set_from(from_email)
        self.message.add_to(to_email)
        status, msg = self.sg.send(self.message)
        return (status, msg)



def lookup_to_contact(domain):
    contacts = settings.DOMAIN_CONTACTS
    return contacts[domain]


