# -*- coding: utf-8 -*-
with open('D:/git/peiwang-store/public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add hidden input for login bg url before closing body
old = '  <audio id="bgm-audio" src="/music/bgm.m4a" loop preload="auto"></audio>'
new = '  <input type="hidden" id="login-bg-url" value="">\n  <audio id="bgm-audio" src="/music/bgm.m4a" loop preload="auto"></audio>'
content = content.replace(old, new)

# Remove the white modal-box background in the inline modals - ensure modals are clean
# The modal-box CSS already handles transparency now

with open('D:/git/peiwang-store/public/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK index.html updated')
