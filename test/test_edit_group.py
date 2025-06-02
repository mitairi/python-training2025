# -*- coding: utf-8 -*- 
from model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name = "NewName", header = "NewHeader", footer = "NewFooter"))
    app.session.logout()

def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name = "New Name"))
    app.session.logout()

def test_modify_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(footer = "New Footer"))
    app.session.logout()

def test_modify_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header = "New Header"))
    app.session.logout()