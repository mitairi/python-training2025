# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name = "ddd54676", header = "fgnghc", footer = "fgjgyj"))

def test_add_empty_group(app):
    app.group.create(Group(name = "", header = "", footer = ""))
