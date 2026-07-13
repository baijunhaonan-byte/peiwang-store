import sys
with open('admin/js/users.js', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add status column header
# Find the header with role and add status column
old_header = (
    '<th>'
    + 'ID'
    + '</th><th>'
    + '用户名'
    + '</th><th>'
    + '邮箱'
    + '</th><th>'
    + '角色'
    + '</th><th>'
    + '创建时间'
    + '</th><th>'
    + '操作'
    + '</th>'
)
new_header = (
    '<th>'
    + 'ID'
    + '</th><th>'
    + '用户名'
    + '</th><th>'
    + '邮箱'
    + '</th><th>'
    + '角色'
    + '</th><th>'
    + '状态'
    + '</th><th>'
    + '创建时间'
    + '</th><th>'
    + '操作'
    + '</th>'
)
c = c.replace(old_header, new_header)

# 2. Replace role display with label and add status cell
old_role = (
    " + u.role + "
    + "'"
    + "</td>"
    + "'"
)
# After role, add status cell, then time cell
new_role_status = (
    " + ({"
    + "'"
    + "super_admin"
    + "'"
    + ":"
    + "'"
    + "超级管理员"
    + "'"
    + ","
    + "'"
    + "admin"
    + "'"
    + ":"
    + "'"
    + "运营管理员"
    + "'"
    + ","
    + "'"
    + "customer"
    + "'"
    + ":"
    + "'"
    + "客户"
    + "'"
    + "}[u.role] || u.role) + "
    + "'"
    + "</td><td>"
    + "'"
    + " + (u.status === "
    + "'"
    + "disabled"
    + "'"
    + " ? "
    + "'"
    + '<span style="color:red">已禁用</span>'
    + "'"
    + " : "
    + "'"
    + '<span style="color:green">正常</span>'
    + "'"
    + ") + "
    + "'"
    + "</td><td>"
    + "'"
    + " + time"
)
c = c.replace(old_role, new_role_status)

# 3. Fix onclick for edit - pass role and status
# The current onclick: onclick=\"showEditUser(' + u.id + ',\"' + name + '\",\"' + email + '\")\"
# Target: onclick=\"showEditUser(' + u.id + ',\"' + escapeHtml(u.username) + '\",\"' + escapeHtml(u.email || '') + '\",\"' + u.role + '\",\"' + (u.status || 'active') + '\")\"
old_onclick = (
    'onclick='
    + '"'
    + 'showEditUser('
    + "'"
    + ' + u.id + '
    + "'"
    + ','
    + '"'
    + "'"
    + ' + name + '
    + "'"
    + '"'
    + ','
    + '"'
    + "'"
    + ' + email + '
    + "'"
    + '"'
    + ')'
    + '"'
)
new_onclick = (
    'onclick='
    + '"'
    + 'showEditUser('
    + "'"
    + ' + u.id + '
    + "'"
    + ','
    + '"'
    + "'"
    + ' + escapeHtml(u.username) + '
    + "'"
    + '"'
    + ','
    + '"'
    + "'"
    + ' + escapeHtml(u.email || '
    + "'"
    + ''
    + "'"
    + ') + '
    + "'"
    + '"'
    + ','
    + '"'
    + "'"
    + ' + u.role + '
    + "'"
    + '"'
    + ','
    + '"'
    + "'"
    + ' + (u.status || '
    + "'"
    + 'active'
    + "'"
    + ') + '
    + "'"
    + '"'
    + ')'
    + '"'
)
c = c.replace(old_onclick, new_onclick)

# 4. Fix delete onclick
old_del = (
    'onclick='
    + '"'
    + 'confirmDeleteUser('
    + "'"
    + ' + u.id + '
    + "'"
    + ','
    + '"'
    + "'"
    + ' + name + '
    + "'"
    + '"'
    + ')'
    + '"'
)
new_del = (
    'onclick='
    + '"'
    + 'confirmDeleteUser('
    + "'"
    + ' + u.id + '
    + "'"
    + ','
    + '"'
    + "'"
    + ' + escapeHtml(u.username) + '
    + "'"
    + '"'
    + ')'
    + '"'
)
c = c.replace(old_del, new_del)

# 5. Remove old name variable
old_name_var = (
    'var name = escapeHtml(u.username);'
    + ' '
    + ' '
    + ' '
    + ' '
    + ' '
    + ' '
    + 'var email = escapeHtml(u.email || '
    + "'"
    + '-'
    + "'"
    + ');'
)
new_name_var = (
    'var email = escapeHtml(u.email || '
    + "'"
    + '-'
    + "'"
    + ');'
)
c = c.replace(old_name_var, new_name_var)

with open('admin/js/users.js', 'w', encoding='utf-8') as f:
    f.write(c)
print('Step 2 OK')
