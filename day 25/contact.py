
"""
28th march 2020
Author: Abhishek singh
topics:- inheritance,super(),multiple inheritance, overridding,mixin class
"""

class ContactList(list):
    def search(self, name):
        ''' return thr contacts which contaian search values into their name '''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
    
class Contact:
    all_contacts = ContactList()

    def __init__(self, name , email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class Mailsender:
    def send_mail(self, message):
        self.message = message
        print("sending email to " + self.message)
class Emailablecontact(Contact,Mailsender):
    pass# mixin class
class AddressHolder:
    def  __init__(self, street, city, state, code ):
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        
        
class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(name, email)
        AddressHolder. __init__(self, street, city, state, code)
        self.phone = phone





c1 = Contact("Abhishek","imavicq@fmail.com")
c1 = Contact("ab","don.qon.quixottte@gmail.com")

c1 = ContactList()
print(c1.search("ab"))




