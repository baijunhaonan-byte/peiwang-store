$c = [System.IO.File]::ReadAllText('admin/js/users.js', [System.Text.Encoding]::UTF8)

# Fix function signature
$c = $c.Replace('function showEditUser(id, username, email) {', 'function showEditUser(id, username, email, role, status) {')

# Fix role display  
$c = $c.Replace(" + u.role + '</td>'", " + " + "({char(39)}super_admin{char(39)}:{char(39)}超级管理员{char(39)}, {char(39)}admin{char(39)}:{char(39)}运营管理员{char(39)}, {char(39)}customer{char(39)}:{char(39)}客户{char(39)})[u.role] || u.role" + " + '</td>'")

[System.IO.File]::WriteAllText('admin/js/users.js', $c, [System.Text.Encoding]::UTF8)
Write-Host 'Done'
