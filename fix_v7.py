SQ = chr(39)
DQ = chr(34)
with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()
parts = []
parts.append('onclick=' + DQ + 'showEditUser(' + SQ + ' + u.id + ' + SQ + ',' + DQ + SQ + ' + escapeHtml(u.username) + ' + SQ + DQ + ',' + DQ + SQ + ' + escapeHtml(u.email || ' + SQ + SQ + ') + ' + SQ + DQ + ',' + DQ + SQ + ' + u.role + ' + SQ + DQ + ',' + DQ + SQ + ' + (u.status || ' + SQ + 'active' + SQ + ') + ' + SQ + DQ + ')' + DQ)
new_val = ''.join(parts)
parts2 = []
parts2.append('onclick=' + DQ + 'showEditUser(' + SQ + ' + u.id + ' + SQ + ',' + DQ + SQ + ' + name + ' + SQ + DQ + ',' + DQ + SQ + ' + email + ' + SQ + DQ + ')' + DQ)
old_val = ''.join(parts2)
c = c.replace(old_val, new_val)

# Delete onclick
parts3 = []
parts3.append('onclick=' + DQ + 'confirmDeleteUser(' + SQ + ' + u.id + ' + SQ + ',' + DQ + SQ + ' + escapeHtml(u.username) + ' + SQ + DQ + ')' + DQ)
new_del = ''.join(parts3)
parts4 = []
parts4.append('onclick=' + DQ + 'confirmDeleteUser(' + SQ + ' + u.id + ' + SQ + ',' + DQ + SQ + ' + name + ' + SQ + DQ + ')' + DQ)
old_del = ''.join(parts4)
c = c.replace(old_del, new_del)
open('admin/js/users.js','w',encoding='utf-8').write(c)
print('5 done')
