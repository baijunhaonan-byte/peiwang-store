with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()
c = c.replace(' + name + ', ' + escapeHtml(u' + chr(46) + 'username) + ')
open('admin/js/users.js','w',encoding='utf-8').write(c)
print('name fixed')
