# -*- coding: utf-8 -*-
from model.contact import Contact
    
def test_add_contact(app):
    app.contact.create(Contact(lastname = "last", firstname = "first"))











