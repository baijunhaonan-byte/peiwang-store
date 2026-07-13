SQ = chr(39)
with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()
old = 'var password = document.getElementById(' + SQ + 'edit-password' + SQ + ').value;'
new = old + chr(10) + '  var role = document.getElementById(' + SQ + 'edit-role' + SQ + ').value;' + chr(10) + '  var status = document.getElementById(' + SQ + 'edit-status' + SQ + ').value;'
c = c.replace(old, new)
old2 = 'var data = { username: username, email: email };' + chr(10) + '  if (password) data.password = password;'
new2 = 'var data = { username: username, email: email, role: role, status: status };' + chr(10) + '  if (password) data.password = password;'
c = c.replace(old2, new2)
open('admin/js/users.js','w',encoding='utf-8').write(c)
print('7 done')
