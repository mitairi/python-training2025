from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Counted"))
    app.contact.delete_first_contact()
