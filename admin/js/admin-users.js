
// ======================== 管理员账号管理 ========================
var currentAdminUsers = [];

async function loadAdminUsers() {
  try {
    var users = await apiGet("/api/admin/users");
    currentAdminUsers = users;
    renderAdminUsers(users);
  } catch(e) {
    var el = document.getElementById("admin-user-table-container");
    if(el) el.innerHTML = '<div class="empty-state">加载失败: ' + e.message + '</div>';
  }
}

function renderAdminUsers(users) {
  var container = document.getElementById("admin-user-table-container");
  if (!container) return;
  if (!users || users.length === 0) {
    container.innerHTML = '<div class="empty-state">暂无管理员账号</div>';
    return;
  }
  var html = '<div class="table-container"><table><thead><tr><th>ID</th><th>用户名</th><th>邮箱</th><th>角色</th><th>状态</th><th>操作</th></tr></thead><tbody>';
  for (var i = 0; i < users.length; i++) {
    var u = users[i];
    var roleLabel = { super_admin: "超级管理员", admin: "运营管理员", customer: "客户" }[u.role] || u.role;
    var statusLabel = u.status === "disabled" ? '<span style="color:red">已禁用</span>' : '<span style="color:green">正常</span>';
    html += '<tr><td>' + u.id + '</td><td>' + escapeHtml(u.username) + '</td><td>' + escapeHtml(u.email) + '</td><td>' + roleLabel + '</td><td>' + statusLabel + '</td>';
    html += '<td><button class="btn btn-sm" onclick="editAdminUser(' + u.id + ')">编辑</button> ';
    if (u.role !== "super_admin") {
      html += '<button class="btn btn-sm btn-danger" onclick="deleteAdminUser(' + u.id + ')">删除</button>';
    }
    html += '</td></tr>';
  }
  html += '</tbody></table></div>';
  container.innerHTML = html;
}

function showCreateAdmin() {
  closeForm("admin-user-form");
  var d = document.createElement("div");
  d.id = "admin-user-form";
  d.className = "modal-overlay";
  var html = '<div class="modal-box" style="max-width:450px;">';
  html += '<div class="modal-box-header"><h3>新增账号</h3><span class="modal-close-btn" onclick="closeForm(\'admin-user-form\')">&times;</span></div>';
  html += '<div class="modal-box-body">';
  html += '<label><span>用户名</span><input id="au-username" placeholder="输入用户名" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px;"></label>';
  html += '<label><span>密码</span><input id="au-password" type="password" placeholder="设置密码" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px;"></label>';
  html += '<label><span>邮箱</span><input id="au-email" placeholder="选填" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px;"></label>';
  html += '<label><span>角色</span><select id="au-role" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px;"><option value="admin">运营管理员</option><option value="customer">客户</option></select></label>';
  html += '<div class="modal-box-actions"><button class="btn btn-primary" onclick="createAdminUser()">确认创建</button><button class="btn btn-default" onclick="closeForm(\'admin-user-form\')">取消</button></div>';
  html += '</div></div>';
  d.innerHTML = html;
  document.body.appendChild(d);
}

async function createAdminUser() {
  var username = document.getElementById("au-username").value.trim();
  var password = document.getElementById("au-password").value;
  var email = document.getElementById("au-email").value.trim();
  var role = document.getElementById("au-role").value;
  if (!username || !password) { notify("请填写用户名和密码"); return; }
  try {
    var r = await fetch("/api/admin/users", {
      method: "POST",
      headers: { "Content-Type": "application/json", "Authorization": "Bearer " + adminToken },
      body: JSON.stringify({ username: username, password: password, email: email, role: role })
    });
    var data = await r.json();
    if (!r.ok) { notify(data.error || "失败"); return; }
    notify("创建成功");
    closeForm("admin-user-form");
    loadAdminUsers();
  } catch(e) { notify("网络错误"); }
}

function editAdminUser(id) {
  var u = null;
  for (var i = 0; i < currentAdminUsers.length; i++) {
    if (currentAdminUsers[i].id === id) { u = currentAdminUsers[i]; break; }
  }
  if (!u) return;
  function opt(val, label, selected) {
    return '<option value="' + val + '"' + (selected ? ' selected' : '') + '>' + label + '</option>';
  }
  closeForm("admin-user-form");
  var d = document.createElement("div");
  d.id = "admin-user-form";
  d.className = "modal-overlay";
  d.innerHTML = '<div class="modal-box" style="max-width:450px;">' +
    '<div class="modal-box-header"><h3>编辑 - ' + escapeHtml(u.username) + '</h3><span class="modal-close-btn" onclick="closeForm(\'admin-user-form\')">&times;</span></div>' +
    '<div class="modal-box-body">' +
    '<label><span>用户名</span><input id="au-username" value="' + escapeHtml(u.username) + '" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px;"></label>' +
    '<label><span>密码</span><input id="au-password" type="password" placeholder="留空不修改" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px;"></label>' +
    '<label><span>邮箱</span><input id="au-email" value="' + escapeHtml(u.email || "") + '" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px;"></label>' +
    '<label><span>角色</span><select id="au-role" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px;">' +
    opt("super_admin", "超级管理员", u.role === "super_admin") +
    opt("admin", "运营管理员", u.role === "admin") +
    opt("customer", "客户", u.role === "customer") +
    '</select></label>' +
    '<label><span>状态</span><select id="au-status" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px;">' +
    opt("active", "正常", u.status !== "disabled") +
    opt("disabled", "禁用", u.status === "disabled") +
    '</select></label>' +
    '<div class="modal-box-actions"><button class="btn btn-primary" onclick="saveAdminUser(' + id + ')">保存</button>' +
    '<button class="btn btn-default" onclick="closeForm(\'admin-user-form\')">取消</button></div></div></div>';
  document.body.appendChild(d);
}

async function saveAdminUser(id) {
  var fields = {};
  var username = document.getElementById("au-username").value.trim();
  if (username) fields.username = username;
  var password = document.getElementById("au-password").value;
  if (password) fields.password = password;
  fields.email = document.getElementById("au-email").value.trim();
  fields.role = document.getElementById("au-role").value;
  fields.status = document.getElementById("au-status").value;
  try {
    await apiPut("/api/admin/users/" + id, fields);
    notify("保存成功");
    closeForm("admin-user-form");
    loadAdminUsers();
  } catch(e) { notify("网络错误"); }
}

async function deleteAdminUser(id) {
  if (!confirm("确定删除此账号？")) return;
  try {
    await apiDelete("/api/admin/users/" + id);
    notify("已删除");
    loadAdminUsers();
  } catch(e) { notify("网络错误"); }
}

function closeForm(id) {
  var el = document.getElementById(id);
  if (el) el.remove();
}
