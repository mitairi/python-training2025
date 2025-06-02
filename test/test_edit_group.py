# -*- coding: utf-8 -*- 
from model.group import Group

def test_modify_first_group(app):
    app.group.modify_first_group(Group(name = "NewName", header = "NewHeader", footer = "NewFooter"))

def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name = "New Name"))

def test_modify_first_group_footer(app):
    app.group.modify_first_group(Group(footer = "New Footer"))

def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header = "New Header"))
