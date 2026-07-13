import sys
c = open('admin/js/users.js', 'r', encoding='utf-8').read()
c = c.replace('function showEditUser(id, username, email) {', 'function showEditUser(id, username, email, role, status) {')
c = c.replace('if (u.role !== ' + "'admin'" + ')', 'if (u.role !== ' + "'super_admin'" + ')')
open('admin/js/users.js', 'w', encoding='utf-8').write(c)
print('OK')
