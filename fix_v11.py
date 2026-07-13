SQ = chr(39)
DQ = chr(34)
BS = chr(92)
with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()

# Edit onclick - fix arguments
old = 'onclick=' + DQ + 'showEditUser(' + SQ + ' + u.id + ' + SQ + ',' + BS + SQ + SQ + ' + name + ' + SQ + BS + SQ + ',' + BS + SQ + SQ + ' + email + ' + SQ + BS + SQ + ')' + DQ
new = 'onclick=' + DQ + 'showEditUser(' + SQ + ' + u.id + ' + SQ + ',' + BS + SQ + SQ + ' + escapeHtml(u.username) + ' + SQ + BS + SQ + ',' + BS + SQ + SQ + ' + escapeHtml(u.email || ' + SQ + SQ + ') + ' + SQ + BS + SQ + ',' + BS + SQ + SQ + ' + u.role + ' + SQ + BS + SQ + ',' + BS + SQ + SQ + ' + (u.status || ' + SQ + 'active' + SQ + ') + ' + SQ + BS + SQ + ')' + DQ
c = c.replace(old, new)

# Delete onclick
old2 = 'onclick=' + DQ + 'confirmDeleteUser(' + SQ + ' + u.id + ' + SQ + ',' + BS + SQ + SQ + ' + name + ' + SQ + BS + SQ + ')' + DQ
new2 = 'onclick=' + DQ + 'confirmDeleteUser(' + SQ + ' + u.id + ' + SQ + ',' + BS + SQ + SQ + ' + escapeHtml(u.username) + ' + SQ + BS + SQ + ')' + DQ
c = c.replace(old2, new2)

open('admin/js/users.js','w',encoding='utf-8').write(c)
print('9 done')
