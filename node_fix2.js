const fs = require('fs');
let content = fs.readFileSync('admin/js/users.js', 'utf-8');
// Add role label display
content = content.replace(
  'html += .<td>. + u.role + .</td>.',
  'html += .<td>. + ({.super_admin.:.超级管理员.,.admin.:.运营管理员.,.customer.:.客户.}[u.role] || u.role) + .</td>.'
);
fs.writeFileSync('admin/js/users.js', content, 'utf-8');
console.log('Done 2');
