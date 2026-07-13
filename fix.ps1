$c = [System.IO.File]::ReadAllText('admin/js/users.js')

$c = $c.Replace('function showEditUser(id, username, email) {', 'function showEditUser(id, username, email, role, status) {')

[System.IO.File]::WriteAllText('admin/js/users.js', $c, [System.Text.UTF8Encoding]::new($false))
Write-Host 'OK'
