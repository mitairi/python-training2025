from model.contact import Contact
    
def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Counted"))
    app.contact.modify_first_contact(Contact(lastname = "Newlast", firstname = "Newfirst"))
