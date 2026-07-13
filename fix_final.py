SQ = chr(39)
with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()

c = c.replace(' + name + ', ' + escapeHtml(u.username) + ')

pw = chr(26032)+chr(23494)+chr(30721)
pl = chr(30041)+chr(31354)+chr(19981)+chr(20462)+chr(25913)+chr(30721)
old = 'body += ' + SQ + '<label><span>' + pw + '</span><input id=' + chr(34) + 'edit-password' + chr(34) + ' type=' + chr(34) + 'password' + chr(34) + ' placeholder=' + chr(34) + pl + '</label>' + SQ + ';'
ry = chr(35282)+chr(33394)
st = chr(29366)+chr(24577)
rl = chr(36229)+chr(32423)+chr(31649)+chr(29702)+chr(21592)
al = chr(36816)+chr(33829)+chr(31649)+chr(29702)+chr(21592)
cl = chr(23458)+chr(25143)
la = chr(27491)+chr(24120)
ld = chr(24050)+chr(31105)+chr(29992)
ex = chr(10) + '  body += ' + SQ + '<label><span>' + ry + '</span><select id=' + chr(34) + 'edit-role' + chr(34) + '>' + SQ + ';' + chr(10) + '  body += opt(' + SQ + 'customer' + SQ + ', ' + SQ + cl + SQ + ', role === ' + SQ + 'customer' + SQ + ');' + chr(10) + '  body += opt(' + SQ + 'admin' + SQ + ', ' + SQ + al + SQ + ', role === ' + SQ + 'admin' + SQ + ');' + chr(10) + '  body += opt(' + SQ + 'super_admin' + SQ + ', ' + SQ + rl + SQ + ', role === ' + SQ + 'super_admin' + SQ + ');' + chr(10) + '  body += ' + SQ + '</select></label>' + SQ + ';' + chr(10) + '  body += ' + SQ + '<label><span>' + st + '</span><select id=' + chr(34) + 'edit-status' + chr(34) + '>' + SQ + ';' + chr(10) + '  body += opt(' + SQ + 'active' + SQ + ', ' + SQ + la + SQ + ', status !== ' + SQ + 'disabled' + SQ + ');' + chr(10) + '  body += opt(' + SQ + 'disabled' + SQ + ', ' + SQ + ld + SQ + ', status === ' + SQ + 'disabled' + SQ + ');' + chr(10) + '  body += ' + SQ + '</select></label>' + SQ + ';'
c = c.replace(old, old + ex)
open('admin/js/users.js','w',encoding='utf-8').write(c)
print('FINAL DONE')
