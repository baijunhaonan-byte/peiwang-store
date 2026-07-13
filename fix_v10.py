SQ = chr(39)
DQ = chr(34)
with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()
la = chr(27491)+chr(24120)
ld = chr(24050)+chr(31105)+chr(29992)
ot = SQ + '</td><td>' + SQ + ' + time'
parts = []
parts.append(SQ + '</td><td>' + SQ + ' + (u.status === ' + SQ + 'disabled' + SQ + ' ? ' + SQ + '<span style=' + DQ + 'color:red' + DQ + '>' + ld + '</span>' + SQ + ' : ' + SQ + '<span style=' + DQ + 'color:green' + DQ + '>' + la + '</span>' + SQ + ') + ' + SQ + '</td><td>' + SQ + ' + time')
nt = ''.join(parts)
c = c.replace(ot, nt)

# Edit onclick
parts2 = []
parts2.append('onclick=' + DQ + 'showEditUser(' + SQ + ' + u.id + ' + SQ + ',' + DQ + SQ + ' + escapeHtml(u.username) + ' + SQ + DQ + ',' + DQ + SQ + ' + escapeHtml(u.email || ' + SQ + SQ + ') + ' + SQ + DQ + ',' + DQ + SQ + ' + u.role + ' + SQ + DQ + ',' + DQ + SQ + ' + (u.status || ' + SQ + 'active' + SQ + ') + ' + SQ + DQ + ')' + DQ)
new_val = ''.join(parts2)
parts3 = []
parts3.append('onclick=' + DQ + 'showEditUser(' + SQ + ' + u.id + ' + SQ + ',' + DQ + SQ + ' + name + ' + SQ + DQ + ',' + DQ + SQ + ' + email + ' + SQ + DQ + ')' + DQ)
old_val = ''.join(parts3)
c = c.replace(old_val, new_val)

# Delete onclick
parts4 = []
parts4.append('onclick=' + DQ + 'confirmDeleteUser(' + SQ + ' + u.id + ' + SQ + ',' + DQ + SQ + ' + escapeHtml(u.username) + ' + SQ + DQ + ')' + DQ)
new_del = ''.join(parts4)
parts5 = []
parts5.append('onclick=' + DQ + 'confirmDeleteUser(' + SQ + ' + u.id + ' + SQ + ',' + DQ + SQ + ' + name + ' + SQ + DQ + ')' + DQ)
old_del = ''.join(parts5)
c = c.replace(old_del, new_del)

open('admin/js/users.js','w',encoding='utf-8').write(c)
print('8 done')
