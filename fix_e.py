with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()
lines = c.split(chr(10))
import re
for i in range(len(lines)):
  if i == 36:
    lines[i] = '  if (!confirm(' + chr(39) + chr(30830)+chr(23450)+chr(21024)+chr(38500)+chr(29992)+chr(25143) + chr(92) + chr(117) + chr(50) + chr(48) + chr(49) + chr(67) + chr(39) + ' + name + ' + chr(39) + chr(92) + chr(117) + chr(50) + chr(48) + chr(49) + chr(68) + chr(12290)+chr(27492)+chr(25805)+chr(20316)+chr(19981)+chr(33021)+chr(22797)+chr(65281) + chr(39) + ')) return;'
  if 'escapeHtml(u' + chr(46) + 'username)' in lines[i] and 'onclick' not in lines[i] and 'showEditUser' not in lines[i]:
    lines[i] = lines[i].replace('escapeHtml(u' + chr(46) + 'username)', 'name')
c = chr(10).join(lines)
open('admin/js/users.js','w',encoding='utf-8').write(c)
print('fixed')
