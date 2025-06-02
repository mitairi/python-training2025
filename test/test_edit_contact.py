from model.contact import Contact
    
def test_add_contact(app):
    app.contact.modify_first_contact(Contact(lastname = "Newlast", firstname = "Newfirst"))
