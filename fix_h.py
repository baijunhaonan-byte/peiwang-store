SQ = chr(39)
with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()
lines = c.split(chr(10))
bu = chr(19981); ke = chr(21487); hui = chr(24674); fu = chr(22797)
ci = chr(27492); cao = chr(25805); zuo = chr(20316)
# Fix line 36 confirm message
lines[36] = '  if (!confirm(' + SQ + chr(30830)+chr(23450)+chr(21024)+chr(38500)+chr(29992)+chr(25143)+chr(32)+chr(92)+chr(117)+chr(50)+chr(48)+chr(49)+chr(67)+SQ + ' + name + ' + SQ + chr(92)+chr(117)+chr(50)+chr(48)+chr(49)+chr(68)+chr(65311)+ci+cao+zuo+bu+ke+hui+fu+chr(65281) + SQ + ')) return;'
c = chr(10).join(lines)
open('admin/js/users.js','w',encoding='utf-8').write(c)
print('fixed')
