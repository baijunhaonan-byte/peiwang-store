# -*- coding: utf-8 -*-
import re

with open("admin/js/users.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add status column header
content = content.replace(
    "<th>ID</th><th>鐢ㄦ埛鍚?/th><th>閭</th><th>瑙掕壊</th><th>鍒涘缓鏃堕棿</th><th>鎿嶄綔</th>",
    "<th>ID</th><th>鐢ㄦ埛鍚?/th><th>閭</th><th>瑙掕壊</th><th>鐘舵€?/th><th>鍒涚珛鏃堕棿</th><th>鎿嶄綔</th>"
)

# 2. Fix role display
old_role = "html += '<td>' + u.role + '</td>'"
new_role = "html += '<td>' + ({'super_admin':'瓒呯骇绠＄悊鍛?','admin':'杩愯惀绠＄悊鍛?','customer':'瀹㈡埛'}[u.role] || u.role) + '</td>'"
content = content.replace(old_role, new_role)

# 3. Fix onclick to pass role/status
old_onclick = "onclick=\\"showEditUser(' + u.id + ',\\"' + name + '\\",\\"' + email + '\\")\\""
new_onclick = "onclick=\\"showEditUser(' + u.id + ',\\"' + escapeHtml(u.username) + '\\",\\"' + escapeHtml(u.email || '') + '\\",\\"' + u.role + '\\",\\"' + (u.status || 'active') + '\\")\\""
content = content.replace(old_onclick, new_onclick)

# 4. Fix delete onclick
old_del = "onclick=\\"confirmDeleteUser(' + u.id + ',\\"' + name + '\\")\\""
new_del = "onclick=\\"confirmDeleteUser(' + u.id + ',\\"' + escapeHtml(u.username) + '\\")\\""
content = content.replace(old_del, new_del)

# 5. Remove old name variable
content = content.replace(
    "var name = escapeHtml(u.username);\n      var email = escapeHtml(u.email || '-');",
    "var email = escapeHtml(u.email || '-');"
)

# 6. Change delete condition
content = content.replace(
    "if (u.role !== 'admin')",
    "if (u.role !== 'super_admin')"
)

# 7. Fix function signature
content = content.replace(
    "function showEditUser(id, username, email) {",
    "function showEditUser(id, username, email, role, status) {"
)

# 8. Add status cell after role
old_time = " + '</td><td>' + time + '</td>'"
new_time = " + '</td><td>' + (u.status === 'disabled' ? '<span style=\"color:red\">宸茬鐢?/span>' : '<span style=\"color:green\">姝ｅ父</span>') + '</td><td>' + time + '</td>'"
content = content.replace(old_time, new_time)

# 9. Add role/status selects in modal
old_body = "body += '<label><span>鏂板瘑鐮?/span><input id=\"edit-password\" type=\"password\" placeholder=\"鐣欑┖涓嶄慨鏀瑰瘑鐮?></label>';"
new_body = """body += '<label><span>鏂板瘑鐮?/span><input id=\"edit-password\" type=\"password\" placeholder=\"鐣欑┖涓嶄慨鏀瑰瘑鐮?></label>';
  function opt(val, label, selected) {
    return '<option value=\"' + val + '\"' + (selected ? ' selected' : '') + '>' + label + '</option>';
  }
  body += '<label><span>瑙掕壊</span><select id=\"edit-role\">';
  body += opt('customer', '瀹㈡埛', role === 'customer');
  body += opt('admin', '杩愯惀绠＄悊鍛?', role === 'admin');
  body += opt('super_admin', '瓒呯骇绠＄悊鍛?', role === 'super_admin');
  body += '</select></label>';
  body += '<label><span>鐘舵€?/span><select id=\"edit-status\">';
  body += opt('active', '姝ｅ父', status !== 'disabled');
  body += opt('disabled', '绂佺敤', status === 'disabled');
  body += '</select></label>';"""
content = content.replace(old_body, new_body)

# 10. Fix saveEditUser
old_save = "var data = { username: username, email: email };\n  if (password) data.password = password;"
new_save = "var data = { username: username, email: email, role: role, status: status };\n  if (password) data.password = password;"
content = content.replace(old_save, new_save)

# 11. Add role/status variables in saveEditUser
old_vars = "var password = document.getElementById('edit-password').value;"
new_vars = "var password = document.getElementById('edit-password').value;\n  var role = document.getElementById('edit-role').value;\n  var status = document.getElementById('edit-status').value;"
content = content.replace(old_vars, new_vars)

with open("admin/js/users.js", "w", encoding="utf-8") as f:
    f.write(content)

print("DONE")
