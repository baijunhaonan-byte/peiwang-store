with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()
lines = c.split(chr(10))
SQ = chr(39)
for i in range(len(lines)):
  if 'opt(' + SQ + 'super_admin' in lines[i]:
    lines[i] = ''
c = chr(10).join(lines)
open('admin/js/users.js','w',encoding='utf-8').write(c)
print('removed super_admin option')
