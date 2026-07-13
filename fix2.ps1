$c = [System.IO.File]::ReadAllText('admin/js/users.js')

# Fix 1: Function signature
$c = $c.Replace('function showEditUser(id, username, email) {', 'function showEditUser(id, username, email, role, status) {')

# Fix 2: Role label
$c = $c.Replace(' + u.role + "' + '</td>' + "'", " + ({'super_admin':'super admin','admin':'admin','customer':'customer'}[u.role] || u.role) + '</td>'")

[System.IO.File]::WriteAllText('admin/js/users.js', $c, [System.Text.UTF8Encoding]::new($false))
Write-Host 'Done'
