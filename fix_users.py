# -*- coding: utf-8 -*-
import re

with open("admin/js/users.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix function signature
content = content.replace(
    "function showEditUser(id, username, email) {",
    "function showEditUser(id, username, email, role, status) {"
)

# 2. Fix onclick to pass role and status
old_onclick = "onclick=\\\"showEditUser(' + u.id + ',\\\"' + name + '\\\"',\\\"' + email + '\\\"')\""
new_onclick = "onclick=\\\"showEditUser(' + u.id + ',\\\"' + escapeHtml(u.username) + '\\\"',\\\"' + escapeHtml(u.email || '') + '\\\"',\\\"' + u.role + '\\\"',\\\"' + (u.status || 'active') + '\\\"')\""
content = content.replace(old_onclick, new_onclick)

# 3. Fix showEditUser body - add role and status selects
old_body = "  editingUserId = id;\n  document.getElementById('modal-title').textContent = '缂栬緫鐢ㄦ埛 - ' + escapeHtml(username);\n  var body = '';\n  body += '<label><span>鐢ㄦ埛鍚?/span><input id=\"edit-username\" value=\"' + escapeHtml(username) + '\"></label>';\n  body += '<label><span>閭</span><input id=\"edit-email\" value=\"' + escapeHtml(email || '') + '\"></label>';\n  body += '<label><span>鏂板瘑鐮?/span><input id=\"edit-password\" type=\"password\" placeholder=\"鐣欑┖涓嶄慨鏀瑰瘑鐮?></label>';\n  body += '<div class=\"modal-box-actions\">';\n  body += '<button class=\"btn btn-primary\" onclick=\"saveEditUser()\">淇濆瓨</button>';\n  body += '<button class=\"btn btn-default\" onclick=\"closeModal()\">鍙栨秷</button>';\n  body += '</div>';\n  body += '<div id=\"edit-error\" class=\"form-error hidden\"></div>';\n  document.getElementById('modal-body').innerHTML = body;\n  document.getElementById('modal-overlay').classList.remove('hidden');"

new_body = "  editingUserId = id;\n  document.getElementById('modal-title').textContent = '缂栬緫鐢ㄦ埛 - ' + escapeHtml(username);\n  function opt(val, label, selected) {\n    return '<option value=\"' + val + '\"' + (selected ? ' selected' : '') + '>' + label + '</option>';\n  }\n  var body = '';\n  body += '<label><span>鐢ㄦ埛鍚?/span><input id=\"edit-username\" value=\"' + escapeHtml(username) + '\"></label>';\n  body += '<label><span>閭</span><input id=\"edit-email\" value=\"' + escapeHtml(email || '') + '\"></label>';\n  body += '<label><span>鏂板瘑鐮?/span><input id=\"edit-password\" type=\"password\" placeholder=\"鐣欑┖涓嶄慨鏀瑰瘑鐮?></label>';\n  body += '<label><span>瑙掕壊</span><select id=\"edit-role\">';\n  body += opt('customer', '瀹㈡埛', role === 'customer');\n  body += opt('admin', '杩愯惀绠＄悊鍛?', role === 'admin');\n  body += opt('super_admin', '瓒呯骇绠＄悊鍛?', role === 'super_admin');\n  body += '</select></label>';\n  body += '<label><span>鐘舵€?/span><select id=\"edit-status\">';\n  body += opt('active', '姝ｅ父', status !== 'disabled');\n  body += opt('disabled', '绂佺敤', status === 'disabled');\n  body += '</select></label>';\n  body += '<div class=\"modal-box-actions\">';\n  body += '<button class=\"btn btn-primary\" onclick=\"saveEditUser()\">淇濆瓨</button>';\n  body += '<button class=\"btn btn-default\" onclick=\"closeModal()\">鍙栨秷</button>';\n  body += '</div>';\n  body += '<div id=\"edit-error\" class=\"form-error hidden\"></div>';\n  document.getElementById('modal-body').innerHTML = body;\n  document.getElementById('modal-overlay').classList.remove('hidden');"

content = content.replace(old_body, new_body)

# 4. Fix saveEditUser to include role and status
old_save = "async function saveEditUser() {\n  var username = document.getElementById('edit-username').value.trim();\n  var email = document.getElementById('edit-email').value.trim();\n  var password = document.getElementById('edit-password').value;\n  var errEl = document.getElementById('edit-error');\n  if (!username) { errEl.textContent = '鐢ㄦ埛鍚嶄笉鑳戒负绌?; errEl.classList.remove('hidden'); return; }\n  errEl.classList.add('hidden');\n  var data = { username: username, email: email };\n  if (password) data.password = password;\n  try {\n    var r = await fetch('/api/users/' + editingUserId, {\n      method: 'PUT',\n      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + adminToken },\n      body: JSON.stringify(data)\n    });\n    if (r.ok) {\n      closeModal();\n      notify('鐢ㄦ埛淇℃伅宸叉洿鏂?);\n      loadUsers();\n    } else {\n      var d = await r.json();\n      errEl.textContent = d.error || '鏇存柊澶辫触';\n      errEl.classList.remove('hidden');\n    }\n  } catch(e) {\n    errEl.textContent = '缃戠粶閿欒';\n    errEl.classList.remove('hidden');\n  }\n}"

new_save = "async function saveEditUser() {\n  var username = document.getElementById('edit-username').value.trim();\n  var email = document.getElementById('edit-email').value.trim();\n  var password = document.getElementById('edit-password').value;\n  var role = document.getElementById('edit-role').value;\n  var status = document.getElementById('edit-status').value;\n  var errEl = document.getElementById('edit-error');\n  if (!username) { errEl.textContent = '鐢ㄦ埛鍚嶄笉鑳戒负绌?; errEl.classList.remove('hidden'); return; }\n  errEl.classList.add('hidden');\n  var data = { username: username, email: email, role: role, status: status };\n  if (password) data.password = password;\n  try {\n    var r = await fetch('/api/users/' + editingUserId, {\n      method: 'PUT',\n      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + adminToken },\n      body: JSON.stringify(data)\n    });\n    if (r.ok) {\n      closeModal();\n      notify('鐢ㄦ埛淇℃伅宸叉洿鏂?);\n      loadUsers();\n    } else {\n      var d = await r.json();\n      errEl.textContent = d.error || '鏇存柊澶辫触';\n      errEl.classList.remove('hidden');\n    }\n  } catch(e) {\n    errEl.textContent = '缃戠粶閿欒';\n    errEl.classList.remove('hidden');\n  }\n}"

content = content.replace(old_save, new_save)

# 5. Add role label in table display
content = content.replace(
    "html += '<td>' + u.role + '</td>'",
    "html += '<td>' + ({'super_admin':'瓒呯骇绠＄悊鍛?','admin':'杩愯惀绠＄悊鍛?','customer':'瀹㈡埛'}[u.role] || u.role) + '</td>'"
)

# 6. Add status column
content = content.replace(
    "<th>瑙掕壊</th><th>鍒涘缓鏃堕棿</th>",
    "<th>瑙掕壊</th><th>鐘舵€?/th><th>鍒涘缓鏃堕棿</th>"
)

# 7. Add status data cell
content = content.replace(
    " + '</td><td>' + time + '</td>'",
    " + '</td><td>' + (u.status === 'disabled' ? '<span style=\"color:red\">宸茬鐢?/span>' : '<span style=\"color:green\">姝ｅ父</span>') + '</td><td>' + time + '</td>'"
)

# 8. Update delete check from 'admin' to 'super_admin'
content = content.replace(
    "if (u.role !== 'admin')",
    "if (u.role !== 'super_admin')"
)

# 9. Fix the name variable reference to use escapeHtml directly
# The old code uses 'name' variable which was removed
content = content.replace(
    "var name = escapeHtml(u.username);\n      var email = escapeHtml(u.email || '-');",
    "var email = escapeHtml(u.email || '-');"
)

# 10. Update the onclick reference
content = content.replace(
    "html += '<button class=\"btn btn-danger btn-sm\" onclick=\"confirmDeleteUser(' + u.id + ',\\\"' + name + '\\\"')\">',
    "html += '<button class=\"btn btn-danger btn-sm\" onclick=\"confirmDeleteUser(' + u.id + ',\\\"' + escapeHtml(u.username) + '\\\"')\">"
)

with open("admin/js/users.js", "w", encoding="utf-8") as f:
    f.write(content)

print("DONE")
