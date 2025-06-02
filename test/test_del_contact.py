from model.contact import Contact

def test_delete_contact(app):
    app.contact.delete_first_contact()
