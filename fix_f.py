SQ = chr(39)
with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()
lines = c.split(chr(10))
# Fix line 16: + name + -> + escapeHtml(u.username) +
lines[16] = lines[16].replace(SQ + ' + name + ' + SQ, SQ + ' + escapeHtml(u' + chr(46) + 'username) + ' + SQ)
# Fix line 36: wrong confirm message chars
la = chr(30830)+chr(23450)+chr(21024)+chr(38500)+chr(29992)+chr(25143)
lb = chr(12290)+chr(27492)+chr(25805)+chr(20316)+chr(19981)+chr(33021)+chr(22797)+chr(65281)
lines[36] = '  if (!confirm(' + SQ + chr(30830)+chr(23450)+chr(21024)+chr(38500)+chr(29992)+chr(25143)+chr(32)+chr(92)+chr(117)+chr(50)+chr(48)+chr(49)+chr(67)+SQ + ' + name + ' + SQ + chr(92)+chr(117)+chr(50)+chr(48)+chr(49)+chr(68)+chr(65311)+chr(27492)+chr(25805)+chr(20316)+chr(19981)+chr(33021)+chr(22797)+chr(65281) + SQ + ')) return;'
c = chr(10).join(lines)
open('admin/js/users.js','w',encoding='utf-8').write(c)
print('fixed')
