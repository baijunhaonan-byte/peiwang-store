# -*- coding: utf-8 -*-
with open('D:/git/peiwang-store/public/js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the loadSiteSettings function end and add login bg loading
old = """    } catch(e) { console.warn('设置加载失败:', e); }
  }"""
new = """    // 登录背景图片
    var loginBgInput = document.getElementById('login-bg-url');
    if (s.site_login_bg_url && loginBgInput) {
      loginBgInput.value = s.site_login_bg_url;
    }
    // 应用登录背景到模态框
    var loginModal = document.getElementById('login-modal');
    var regModal = document.getElementById('register-modal');
    var loginBox = loginModal ? loginModal.querySelector('.modal-box') : null;
    var regBox = regModal ? regModal.querySelector('.modal-box') : null;
    if (s.site_login_bg_url) {
      var bgStyle = 'url(' + s.site_login_bg_url + ')';
      if (loginBox) { loginBox.style.backgroundImage = bgStyle; loginBox.classList.add('has-bg'); }
      if (regBox) { regBox.style.backgroundImage = bgStyle; regBox.classList.add('has-bg'); }
    } else {
      if (loginBox) { loginBox.style.backgroundImage = ''; loginBox.style.background = 'transparent'; loginBox.classList.remove('has-bg'); }
      if (regBox) { regBox.style.backgroundImage = ''; regBox.style.background = 'transparent'; regBox.classList.remove('has-bg'); }
    }
    } catch(e) { console.warn('设置加载失败:', e); }
  }"""

content = content.replace(old, new)

with open('D:/git/peiwang-store/public/js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK app.js updated')
