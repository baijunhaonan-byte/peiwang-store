const fs = require('fs');
let content = fs.readFileSync('admin/js/users.js', 'utf-8');
content = content.split('function showEditUser(id, username, email) {').join('function showEditUser(id, username, email, role, status) {');
fs.writeFileSync('admin/js/users.js', content, 'utf-8');
console.log('Done 1');
