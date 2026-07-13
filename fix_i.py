with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()
import re
# Fix missing opening parenthesis before {
c = c.replace(' + ' + chr(123) + chr(39) + 'super_admin', ' + ' + chr(40) + chr(123) + chr(39) + 'super_admin')
open('admin/js/users.js','w',encoding='utf-8').write(c)
print('fixed')
