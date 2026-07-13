import re
with open("admin/js/users.js", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Function signature
c = c.replace("function showEditUser(id, username, email) {", "function showEditUser(id, username, email, role, status) {")

# 2. Delete condition
c = c.replace("if (u.role !== " + chr(39) + "admin" + chr(39) + ")", "if (u.role !== " + chr(39) + "super_admin" + chr(39) + ")")

# 3. Add status column header (between role and created time)
c = c.replace("<th>角色</th><th>创建时间</th>", "<th>角色</th><th>状态</th><th>创建时间</th>")

# 4. Fix role display + add status cell
c = c.replace(
    "(" + chr(39) + "</td>" + chr(39) + ")",
    "(" + chr(39) + "</td>" + chr(39) + " + (u.status === " + chr(39) + "disabled" + chr(39) + " ? " + chr(39) + "<span style=\\\\\"color:red\\\\\">已禁用</span>" + chr(39) + " : " + chr(39) + "<span style=\\\\\"color:green\\\\\">正常</span>" + chr(39) + ") + " + chr(39) + "</td>" + chr(39) + " + time"
)

# 5. Replace role display with label
SQ = chr(39)
role_dict = "{super_admin:" + SQ + "超级管理员" + SQ + ",admin:" + SQ + "运营管理员" + SQ + ",customer:" + SQ + "客户" + SQ + "}"
c = c.replace(
    " + u.role + " + SQ + "</td>" + SQ,
    " + (" + role_dict + "[u.role] || u.role) + " + SQ + "</td><td>" + SQ
)

# 6. Fix onclick for edit - add role and status params
old_onclick_edit = "onclick=\\\"showEditUser(" + SQ + " + u.id + " + SQ + ",\\" + SQ + " + name + " + SQ + "\\",\\" + SQ + " + email + " + SQ + "\\")\\""
new_onclick_edit = "onclick=\\\"showEditUser(" + SQ + " + u.id + " + SQ + ",\\" + SQ + " + escapeHtml(u.username) + " + SQ + "\\",\\" + SQ + " + escapeHtml(u.email || " + SQ + SQ + ") + " + SQ + "\\",\\" + SQ + " + u.role + " + SQ + "\\",\\" + SQ + " + (u.status || " + SQ + "active" + SQ + ") + " + SQ + "\\")\\""
c = c.replace(old_onclick_edit, new_onclick_edit)

# 7. Fix onclick for delete
old_onclick_del = "onclick=\\\"confirmDeleteUser(" + SQ + " + u.id + " + SQ + ",\\" + SQ + " + name + " + SQ + "\\")\\""
new_onclick_del = "onclick=\\\"confirmDeleteUser(" + SQ + " + u.id + " + SQ + ",\\" + SQ + " + escapeHtml(u.username) + " + SQ + "\\")\\""
c = c.replace(old_onclick_del, new_onclick_del)

# 8. Remove old name variable line
old_name_line = "      var name = escapeHtml(u.username);\n      var email = escapeHtml(u.email || " + SQ + "-" + SQ + ");\n"
new_name_line = "      var email = escapeHtml(u.email || " + SQ + "-" + SQ + ");\n"
c = c.replace(old_name_line, new_name_line)

# 9. Add role and status selects in edit modal body
old_body_end = "body += " + SQ + "<label><span>新密码</span><input id=\\"edit-password\\" type=\\"password\\" placeholder=\\"留空不修改密码\\"></label>" + SQ + ";"
new_body_extra = (
    "body += " + SQ + "<label><span>新密码</span><input id=\\"edit-password\\" type=\\"password\\" placeholder=\\"留空不修改密码\\"></label>" + SQ + ";\n"
    + "  function opt(val, label, selected) {\n"
    + "    return " + SQ + "<option value=\\" + SQ + " + val + " + SQ + "\\"" + SQ + " + (selected ? " + SQ + " selected" + SQ + " : " + SQ + SQ + ") + " + SQ + ">" + SQ + " + label + " + SQ + "</option>" + SQ + ";\n"
    + "  }\n"
    + "  body += " + SQ + "<label><span>角色</span><select id=\\"edit-role\\">" + SQ + ";\n"
    + "  body += opt(" + SQ + "customer" + SQ + ", " + SQ + "客户" + SQ + ", role === " + SQ + "customer" + SQ + ");\n"
    + "  body += opt(" + SQ + "admin" + SQ + ", " + SQ + "运营管理员" + SQ + ", role === " + SQ + "admin" + SQ + ");\n"
    + "  body += opt(" + SQ + "super_admin" + SQ + ", " + SQ + "超级管理员" + SQ + ", role === " + SQ + "super_admin" + SQ + ");\n"
    + "  body += " + SQ + "</select></label>" + SQ + ";\n"
    + "  body += " + SQ + "<label><span>状态</span><select id=\\"edit-status\\">" + SQ + ";\n"
    + "  body += opt(" + SQ + "active" + SQ + ", " + SQ + "正常" + SQ + ", status !== " + SQ + "disabled" + SQ + ");\n"
    + "  body += opt(" + SQ + "disabled" + SQ + ", " + SQ + "禁用" + SQ + ", status === " + SQ + "disabled" + SQ + ");\n"
    + "  body += " + SQ + "</select></label>" + SQ + ";"
)
c = c.replace(old_body_end, new_body_extra)

# 10. Add role/status variables in saveEditUser
old_vars = "var password = document.getElementById(" + SQ + "edit-password" + SQ + ").value;\n  var errEl"
new_vars = "var password = document.getElementById(" + SQ + "edit-password" + SQ + ").value;\n  var role = document.getElementById(" + SQ + "edit-role" + SQ + ").value;\n  var status = document.getElementById(" + SQ + "edit-status" + SQ + ").value;\n  var errEl"
c = c.replace(old_vars, new_vars)

# 11. Fix save data to include role and status
old_save_data = "var data = { username: username, email: email };\n  if (password) data.password = password;"
new_save_data = "var data = { username: username, email: email, role: role, status: status };\n  if (password) data.password = password;"
c = c.replace(old_save_data, new_save_data)

with open("admin/js/users.js", "w", encoding="utf-8") as f:
    f.write(c)

print("ALL DONE")

