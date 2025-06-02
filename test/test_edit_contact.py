from model.contact import Contact
    
def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(lastname = "Newlast", firstname = "Newfirst"))
    app.session.logout()