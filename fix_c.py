SQ = chr(39); DQ = chr(34); NL = chr(10)
rl = chr(36229)+chr(32423)+chr(31649)+chr(29702)+chr(21592)
al = chr(36816)+chr(33829)+chr(31649)+chr(29702)+chr(21592)
cl = chr(23458)+chr(25143)
la = chr(27491)+chr(24120)
ld = chr(24050)+chr(31105)+chr(29992)
ry = chr(35282)+chr(33394)
st = chr(29366)+chr(24577)
pw = chr(26032)+chr(23494)+chr(30721)
pl = chr(30041)+chr(31354)+chr(19981)+chr(20462)+chr(25913)+chr(30721)

with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()

old = 'body += ' + SQ + '<label><span>' + pw + '</span><input id=' + DQ + 'edit-password' + DQ + ' type=' + DQ + 'password' + DQ + ' placeholder=' + DQ + pl + '</label>' + SQ + ';'

extra = ''
extra += NL + '  function opt(val, label, selected) {'
extra += NL + '    return ' + SQ + '<option value=' + DQ + SQ + ' + val + ' + SQ + DQ + SQ + ' + (selected ? ' + SQ + ' selected' + SQ + ' : ' + SQ + SQ + ') + ' + SQ + '>' + SQ + ' + label + ' + SQ + '</option>' + SQ + ';'
extra += NL + '  }'
extra += NL + '  body += ' + SQ + '<label><span>' + ry + '</span><select id=' + DQ + 'edit-role' + DQ + '>' + SQ + ';'
extra += NL + '  body += opt(' + SQ + 'customer' + SQ + ', ' + SQ + cl + SQ + ', role === ' + SQ + 'customer' + SQ + ');'
extra += NL + '  body += opt(' + SQ + 'admin' + SQ + ', ' + SQ + al + SQ + ', role === ' + SQ + 'admin' + SQ + ');'
extra += NL + '  body += opt(' + SQ + 'super_admin' + SQ + ', ' + SQ + rl + SQ + ', role === ' + SQ + 'super_admin' + SQ + ');'
extra += NL + '  body += ' + SQ + '</select></label>' + SQ + ';'
extra += NL + '  body += ' + SQ + '<label><span>' + st + '</span><select id=' + DQ + 'edit-status' + DQ + '>' + SQ + ';'
extra += NL + '  body += opt(' + SQ + 'active' + SQ + ', ' + SQ + la + SQ + ', status !== ' + SQ + 'disabled' + SQ + ');'
extra += NL + '  body += opt(' + SQ + 'disabled' + SQ + ', ' + SQ + ld + SQ + ', status === ' + SQ + 'disabled' + SQ + ');'
extra += NL + '  body += ' + SQ + '</select></label>' + SQ + ';'

c = c.replace(old, old + extra)

open('admin/js/users.js','w',encoding='utf-8').write(c)
print('modal fixed')
