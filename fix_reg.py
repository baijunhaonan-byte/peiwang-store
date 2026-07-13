# -*- coding: utf-8 -*-
import re

with open('D:/git/peiwang-store/server.js', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''    var cd = captchaStore[body.captcha_id];
    if (!cd || cd.code !== body.captcha || cd.expires < Date.now()) {
      delete captchaStore[body.captcha_id];
      return json({ error: "验证码错误或已过期" }, 400);
    }'''

new = '''    // 后端注册校验
    if (body.username.length < 2) return json({ error: "用户名至少2个字符" }, 400);
    if (body.password.length < 4) return json({ error: "密码至少4个字符" }, 400);
    if (body.password.length > 50) return json({ error: "密码不能超过50个字符" }, 400);
    if (body.username.length > 20) return json({ error: "用户名不能超过20个字符" }, 400);
    if (!/^[a-zA-Z0-9_\\u4e00-\\u9fa5]+$/.test(body.username)) return json({ error: "用户名只能包含字母、数字、下划线和中文" }, 400);
    if (body.email) {
      if (body.email.length > 100) return json({ error: "邮箱不能超过100个字符" }, 400);
      if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(body.email)) return json({ error: "邮箱格式不正确" }, 400);
    }
    if (body.email) {
      var allUsers = db.getAllUsers();
      for (var i = 0; i < allUsers.length; i++) {
        if (allUsers[i].email === body.email) return json({ error: "该邮箱已被绑定" }, 409);
      }
    }
    var cd = captchaStore[body.captcha_id];
    if (!cd || cd.code !== body.captcha || cd.expires < Date.now()) {
      delete captchaStore[body.captcha_id];
      return json({ error: "验证码错误或已过期" }, 400);
    }'''

content = content.replace(old, new)

with open('D:/git/peiwang-store/server.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK server.js updated')
