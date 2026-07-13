import re
with open("admin/js/users.js", "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("function showEditUser(id, username, email) {", "function showEditUser(id, username, email, role, status) {")
c = c.replace("if (u.role !== " + chr(39) + "admin" + chr(39) + ")", "if (u.role !== " + chr(39) + "super_admin" + chr(39) + ")")
open("admin/js/users.js", "w", encoding="utf-8").write(c)
print("DONE")

