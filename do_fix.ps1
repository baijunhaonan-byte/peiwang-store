# encoding: utf-8
$c = [System.IO.File]::ReadAllText("admin/js/users.js", [System.Text.Encoding]::UTF8)
$SQ = [string][char]39
$DQ = [string][char]34

# 1. Function signature
$c = $c.Replace("function showEditUser(id, username, email) {", "function showEditUser(id, username, email, role, status) {")

# 2. Delete condition: admin -> super_admin
$c = $c.Replace("if (u.role !== " + $SQ + "admin" + $SQ + ")", "if (u.role !== " + $SQ + "super_admin" + $SQ + ")")

# 3. Add status column in header (between role and created time)
$header = "<th>" + [string][char]35282 + [string][char]33394 + "</th><th>" + [string][char]21019 + [string][char]24314 + [string][char]26102 + [string][char]38388 + "</th>"
$newHeader = "<th>" + [string][char]35282 + [string][char]33394 + "</th><th>" + [string][char]29366 + [string][char]24577 + "</th><th>" + [string][char]21019 + [string][char]24314 + [string][char]26102 + [string][char]38388 + "</th>"
$c = $c.Replace($header, $newHeader)

# 4. Replace role display with label
$oldRole = " + u.role + ")
$roleLabel = [string][char]36229 + [string][char]32423 + [string][char]31649 + [string][char]29702 + [string][char]21592 + [string][char]21527
$adminLabel = [string][char]36816 + [string][char]33829 + [string][char]31649 + [string][char]29702 + [string][char]21592 + [string][char]21527
$custLabel = [string][char]23458 + [string][char]25143
$newRole = " + ({$SQ"super_admin"$SQ:$SQ" + $roleLabel + "$SQ,$SQ"admin"$SQ:$SQ" + $adminLabel + "$SQ,$SQ"customer"$SQ:$SQ" + $custLabel + "$SQ}[u.role] || u.role) + "
$c = $c.Replace($oldRole, $newRole)

# 5. Add status cell after role
$activeLabel = [string][char]27491 + [string][char]24120
$disabledLabel = [string][char]24050 + [string][char]31105 + [string][char]29992
$oldTime = $SQ + "</td>" + $SQ + " + time"
$statusCell = $SQ + "</td>" + $SQ + " + (u.status === " + $SQ + "disabled" + $SQ + " ? " + $SQ + "<span style=" + $DQ + "color:red" + $DQ + ">" + $disabledLabel + "</span>" + $SQ + " : " + $SQ + "<span style=" + $DQ + "color:green" + $DQ + ">" + $activeLabel + "</span>" + $SQ + ") + " + $SQ + "</td>" + $SQ + " + time"
$c = $c.Replace($oldTime, $statusCell)

# 6. Remove name variable
$oldName = "      var name = escapeHtml(u.username);"
$c = $c.Replace($oldName, "")

# 7. Fix onclick for edit - replace name with escapeHtml and add role/status
$oldEdit = "onclick=" + $DQ + "showEditUser(" + $SQ + " + u.id + " + $SQ + "," + $DQ + $SQ + " + name + " + $SQ + $DQ + "," + $DQ + $SQ + " + email + " + $SQ + $DQ + ")" + $DQ
$newEdit = "onclick=" + $DQ + "showEditUser(" + $SQ + " + u.id + " + $SQ + "," + $DQ + $SQ + " + escapeHtml(u.username) + " + $SQ + $DQ + "," + $DQ + $SQ + " + escapeHtml(u.email || " + $SQ + $SQ + ") + " + $SQ + $DQ + "," + $DQ + $SQ + " + u.role + " + $SQ + $DQ + "," + $DQ + $SQ + " + (u.status || " + $SQ + "active" + $SQ + ") + " + $SQ + $DQ + ")" + $DQ
$c = $c.Replace($oldEdit, $newEdit)

# 8. Fix onclick for delete
$oldDel = "onclick=" + $DQ + "confirmDeleteUser(" + $SQ + " + u.id + " + $SQ + "," + $DQ + $SQ + " + name + " + $SQ + $DQ + ")" + $DQ
$newDel = "onclick=" + $DQ + "confirmDeleteUser(" + $SQ + " + u.id + " + $SQ + "," + $DQ + $SQ + " + escapeHtml(u.username) + " + $SQ + $DQ + ")" + $DQ
$c = $c.Replace($oldDel, $newDel)

# 9. Add role/status selects in edit modal body
$oldBody = "body += " + $SQ + "<label><span>" + [string][char]26032 + [string][char]23494 + [string][char]30721 + "</span><input id=" + $DQ + "edit-password" + $DQ + " type=" + $DQ + "password" + $DQ + " placeholder=" + $DQ + [string][char]30041 + [string][char]31354 + [string][char]19981 + [string][char]20462 + [string][char]25913 + [string][char]30721 + "</label>" + $SQ + ";"
$newBodyExtra = "  function opt(val, label, selected) {`n    return " + $SQ + "<option value=" + $DQ + $SQ + " + val + " + $SQ + $DQ + $SQ + " + (selected ? " + $SQ + " selected" + $SQ + " : " + $SQ + $SQ + ") + " + $SQ + ">" + $SQ + " + label + " + $SQ + "</option>" + $SQ + ";`n  }`n  body += " + $SQ + "<label><span>" + [string][char]35282 + [string][char]33394 + "</span><select id=" + $DQ + "edit-role" + $DQ + ">" + $SQ + ";`n  body += opt(" + $SQ + "customer" + $SQ + ", " + $SQ + $custLabel + $SQ + ", role === " + $SQ + "customer" + $SQ + ");`n  body += opt(" + $SQ + "admin" + $SQ + ", " + $SQ + $adminLabel + $SQ + ", role === " + $SQ + "admin" + $SQ + ");`n  body += opt(" + $SQ + "super_admin" + $SQ + ", " + $SQ + $roleLabel + $SQ + ", role === " + $SQ + "super_admin" + $SQ + ");`n  body += " + $SQ + "</select></label>" + $SQ + ";`n  body += " + $SQ + "<label><span>" + [string][char]29366 + [string][char]24577 + "</span><select id=" + $DQ + "edit-status" + $DQ + ">" + $SQ + ";`n  body += opt(" + $SQ + "active" + $SQ + ", " + $SQ + $activeLabel + $SQ + ", status !== " + $SQ + "disabled" + $SQ + ");`n  body += opt(" + $SQ + "disabled" + $SQ + ", " + $SQ + $disabledLabel + $SQ + ", status === " + $SQ + "disabled" + $SQ + ");`n  body += " + $SQ + "</select></label>" + $SQ + ";"
$c = $c.Replace($oldBody, $oldBody + "`n" + $newBodyExtra)

# 10. Add role/status variables in saveEditUser
$oldVars = "var password = document.getElementById(" + $SQ + "edit-password" + $SQ + ").value;"
$newVars = $oldVars + "`n  var role = document.getElementById(" + $SQ + "edit-role" + $SQ + ").value;`n  var status = document.getElementById(" + $SQ + "edit-status" + $SQ + ").value;"
$c = $c.Replace($oldVars, $newVars)

# 11. Add role/status to save data
$oldSave = "var data = { username: username, email: email };" + "`n  if (password) data.password = password;"
$newSave = "var data = { username: username, email: email, role: role, status: status };" + "`n  if (password) data.password = password;"
$c = $c.Replace($oldSave, $newSave)

[System.IO.File]::WriteAllText("admin/js/users.js", $c, [System.Text.Encoding]::UTF8)
Write-Host "ALL FIXES DONE"
