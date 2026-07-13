# -*- coding: utf-8 -*-
with open('D:/git/peiwang-store/public/css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Change modal-box background from white to transparent with image support
old = '''.modal-box {
  background: #fff; border-radius: 12px;
  width: 90%; max-width: 400px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}'''

new = '''.modal-box {
  background: transparent;
  background-size: cover;
  background-position: center;
  border-radius: 12px;
  width: 90%; max-width: 400px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3);
  overflow: hidden;
}
.modal-box.has-bg .modal-box-header {
  background: rgba(0,0,0,0.3);
  border-bottom: 1px solid rgba(255,255,255,0.15);
}
.modal-box.has-bg .modal-box-header h3 { color: #fff; }
.modal-box.has-bg .modal-box-body { background: rgba(0,0,0,0.3); }
.modal-box.has-bg .modal-box-body label span { color: rgba(255,255,255,0.85); }
.modal-box.has-bg .modal-box-body input {
  background: rgba(255,255,255,0.2);
  border: 1px solid rgba(255,255,255,0.3);
  color: #fff;
}
.modal-box.has-bg .modal-box-body input::placeholder { color: rgba(255,255,255,0.6); }
.modal-box.has-bg .modal-box-body input:focus {
  border-color: #fff;
  box-shadow: 0 0 0 2px rgba(255,255,255,0.2);
}
.modal-box.has-bg .modal-link { color: #87ceeb; }
.modal-box.has-bg .modal-close-btn { color: rgba(255,255,255,0.8); }
.modal-box.has-bg .modal-close-btn:hover { color: #fff; }'''

content = content.replace(old, new)

with open('D:/git/peiwang-store/public/css/style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK style.css updated')
