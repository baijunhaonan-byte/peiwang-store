# -*- coding: utf-8 -*-
import re
with open('admin/js/users.js', 'r', encoding='utf-8') as f:
    c = f.read()
SQ = chr(39)
c = c.replace('function showEditUser(id, username, email) {', 'function showEditUser(id, username, email, role, status) {')
