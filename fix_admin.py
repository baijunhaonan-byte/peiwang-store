# -*- coding: utf-8 -*-
with open('D:/git/peiwang-store/admin/js/admin.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the part after set-music-url and before save button, add login_bg
old = "body += '<input type=\"hidden\" id=\"set-music-url\" value=\"' + escapeHtml(s.site_music_url || '') + '\">';"
new = "body += '<input type=\"hidden\" id=\"set-music-url\" value=\"' + escapeHtml(s.site_music_url || '') + '\">';\n" + \
      "body += '<div style=\"margin-bottom:14px;\"><label style=\"display:block;font-size:13px;color:#666;margin-bottom:4px;\">登录背景图片</label>'" + \
      "+ '<div style=\"display:flex;align-items:center;gap:10px;\">'" + \
      "+ '<div id=\"login-bg-preview\" style=\"width:80px;height:50px;border-radius:6px;overflow:hidden;border:1px solid #ddd;background:#f9f9f9;display:flex;align-items:center;justify-content:center;font-size:11px;color:#999;\">' + (s.site_login_bg_url ? '√' : '未设置') + '</div>'" + \
      "+ '<div><input type=\"file\" id=\"login-bg-file-input\" accept=\"image/*\" style=\"display:none;\" onchange=\"uploadLoginBg()\">'" + \
      "+ '<button class=\"btn btn-sm btn-primary\" onclick=\"document.getElementById(\\'login-bg-file-input\\').click()\">上传图片</button>'" + \
      "+ '<button class=\"btn btn-sm btn-default\" onclick=\"clearLoginBg()\" style=\"margin-left:4px;\">清除</button>'" + \
      "+ '</div></div></div>' + '\\n' +" + \
      "'<input type=\"hidden\" id=\"set-login-bg-url\" value=\"' + escapeHtml(s.site_login_bg_url || '') + '\">';"

content = content.replace(old, new)

# Add login_bg_url to saveSettings
old_save = "site_music_url: document.getElementById('set-music-url').value"
new_save = "site_music_url: document.getElementById('set-music-url').value,\n      site_login_bg_url: document.getElementById('set-login-bg-url').value"
content = content.replace(old_save, new_save)

# Add uploadLoginBg and clearLoginBg functions before the closeForm function
old_close = "function closeForm"
new_functions = """function uploadLoginBg() {
    var fileInput = document.getElementById('login-bg-file-input');
    var file = fileInput.files[0];
    if (!file) return;
    var formData = new FormData();
    formData.append('image', file);
    try {
      var r = await fetch('/api/upload', { method: 'POST', headers: { 'Authorization': 'Bearer ' + adminToken }, body: formData });
      if (r.ok) {
        var data = await r.json();
        document.getElementById('set-login-bg-url').value = data.url;
        document.getElementById('login-bg-preview').innerHTML = '<img src=\"' + data.url + '\" style=\"width:100%;height:100%;object-fit:cover;\">';
        notify('图片已上传');
      } else { notify('上传失败'); }
    } catch(e) { notify('网络错误'); }
    fileInput.value = '';
  }
  function clearLoginBg() {
    document.getElementById('set-login-bg-url').value = '';
    document.getElementById('login-bg-preview').innerHTML = '未设置';
  }
  """ + "function closeForm"

content = content.replace(old_close, new_functions)

with open('D:/git/peiwang-store/admin/js/admin.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK admin.js updated')
