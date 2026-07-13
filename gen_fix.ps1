$pyPath = Join-Path (Get-Location) "fix_v3.py"
$sw = New-Object System.IO.StreamWriter($pyPath, $false, [System.Text.Encoding]::UTF8)
$sw.WriteLine("# -*- coding: utf-8 -*-")
$sw.WriteLine("import re")
$sw.WriteLine("SQ = chr(39)")
$sw.WriteLine("with open(\"admin/js/users.js\", \"r\", encoding=\"utf-8\") as f:")
$sw.WriteLine("    c = f.read()")
$sw.WriteLine("c = c.replace(\"function showEditUser(id, username, email) {\", \"function showEditUser(id, username, email, role, status) {\")")
