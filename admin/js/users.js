

// ======================== 用户管理 ========================
async function loadUsers() {
  var container = document.getElementById('user-table-container');
  try {
    var r = await fetch('/api/users', {
      headers: { 'Authorization': 'Bearer ' + adminToken }
    });
    if (!r.ok) { container.innerHTML = '<div class="empty-state">加载失败</div>'; return; }
    var users = await r.json();
    var html = '<div class="table-container"><table><thead><tr><th>ID</th><th>用户名</th><th>邮箱</th><th>角色</th><th>状态</th><th>创建时间</th><th>操作</th></tr></thead><tbody>';
    for (var i = 0; i < users.length; i++) {
      var u = users[i];
      var time = u.created_at ? new Date(u.created_at).toLocaleString('zh-CN') : '-';
      var email = escapeHtml(u.email || '-');
      html += '<tr><td>' + u.id + '</td><td>' + escapeHtml(u.username) + '</td><td>' + email + '</td><td>' + {'super_admin':'超级管理员','admin':'运营管理员','customer':'客户'}[u.role] || u.role) + '</td><td>' + (u.status === 'disabled' ? '<span style="color:red">已禁用</span>' : '<span style="color:green">正常</span>') + '</td><td>' + time + '</td>';
      html += '<td>';
        html += '<button class="btn btn-primary btn-sm" onclick="showEditUser(' + u.id + ',\'' + escapeHtml(u.username) + '\',\'' + escapeHtml(u.email || '') + '\',\'' + u.role + '\',\'' + (u.status || 'active') + '\')">编辑</button>';
        if (u.role !== 'super_admin') {
          html += ' <button class="btn btn-danger btn-sm" onclick="confirmDeleteUser(' + u.id + ',\'' + escapeHtml(u.username) + '\')">删除</button>';
        } else {
          html += ' <span style="color:#999;font-size:12px;">管理员</span>';
        }
        html += '</td>';
      
      html += '</tr>';
    }
    html += '</tbody></table></div>';
    container.innerHTML = html;
  } catch(e) {
    container.innerHTML = '<div class="empty-state">加载失败: ' + e.message + '</div>';
  }
}

function confirmDeleteUser(id, name) {
  if (!confirm('确定删除用户 \u201C' + name + '\u201D？此操作不可恢复！')) return;
  doDeleteUser(id);
}

async function doDeleteUser(id) {
  try {
    var r = await fetch('/api/users/' + id, {
      method: 'DELETE',
      headers: { 'Authorization': 'Bearer ' + adminToken }
    });
    if (r.ok) {
      notify('用户已删除');
      loadUsers();
    } else {
      var d = await r.json();
      notify(d.error || '删除失败');
    }
  } catch(e) {
    notify('网络错误');
  }
}


// ======================== 编辑用户 ========================
var editingUserId = null;

function showEditUser(id, username, email, role, status) {
  editingUserId = id;
  document.getElementById('modal-title').textContent = '编辑用户 - ' + escapeHtml(username);
  var body = '';
  body += '<label><span>用户名</span><input id="edit-username" value="' + escapeHtml(username) + '"></label>';
  body += '<label><span>邮箱</span><input id="edit-email" value="' + escapeHtml(email || '') + '"></label>';
  body += '<label><span>新密码</span><input id="edit-password" type="password" placeholder="留空不修改密码"></label>';
  function opt(val, label, selected) {
    return '<option value="' + val + '"' + (selected ? ' selected' : '') + '>' + label + '</option>';
  }
  body += '<label><span>角色</span><select id="edit-role">';
  body += opt('customer', '客户', role === 'customer');
  body += opt('admin', '运营管理员', role === 'admin');
  body += opt('super_admin', '超级管理员', role === 'super_admin');
  body += '</select></label>';
  body += '<label><span>状态</span><select id="edit-status">';
  body += opt('active', '正常', status !== 'disabled');
  body += opt('disabled', '已禁用', status === 'disabled');
  body += '</select></label>';
  body += '<div class="modal-box-actions">';
  body += '<button class="btn btn-primary" onclick="saveEditUser()">保存</button>';
  body += '<button class="btn btn-default" onclick="closeModal()">取消</button>';
  body += '</div>';
  body += '<div id="edit-error" class="form-error hidden"></div>';
  document.getElementById('modal-body').innerHTML = body;
  document.getElementById('modal-overlay').classList.remove('hidden');
}

async function saveEditUser() {
  var username = document.getElementById('edit-username').value.trim();
  var email = document.getElementById('edit-email').value.trim();
  var password = document.getElementById('edit-password').value;
  var role = document.getElementById('edit-role').value;
  var status = document.getElementById('edit-status').value;
  var errEl = document.getElementById('edit-error');
  if (!username) { errEl.textContent = '用户名不能为空'; errEl.classList.remove('hidden'); return; }
  errEl.classList.add('hidden');
  var data = { username: username, email: email, role: role, status: status };
  if (password) data.password = password;
  try {
    var r = await fetch('/api/users/' + editingUserId, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + adminToken },
      body: JSON.stringify(data)
    });
    if (r.ok) {
      closeModal();
      notify('用户信息已更新');
      loadUsers();
    } else {
      var d = await r.json();
      errEl.textContent = d.error || '更新失败';
      errEl.classList.remove('hidden');
    }
  } catch(e) {
    errEl.textContent = '网络错误';
    errEl.classList.remove('hidden');
  }
}

