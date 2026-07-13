with open("D:/git/peiwang-store/public/js/app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "catch(e) { console.warn" in line:
        new_lines = [
            "    // 登录背景图片\n",
            "    var loginBgInput = document.getElementById('login-bg-url');\n",
            "    if (s.site_login_bg_url && loginBgInput) {\n",
            "      loginBgInput.value = s.site_login_bg_url;\n",
            "    }\n",
            "    // 应用登录背景到模态框\n",
            "    var loginModal = document.getElementById('login-modal');\n",
            "    var regModal = document.getElementById('register-modal');\n",
            "    var loginBox = loginModal ? loginModal.querySelector('.modal-box') : null;\n",
            "    var regBox = regModal ? regModal.querySelector('.modal-box') : null;\n",
            "    if (s.site_login_bg_url) {\n",
            "      var bgStyle = 'url(' + s.site_login_bg_url + ')';\n",
            "      if (loginBox) { loginBox.style.backgroundImage = bgStyle; loginBox.classList.add('has-bg'); }\n",
            "      if (regBox) { regBox.style.backgroundImage = bgStyle; regBox.classList.add('has-bg'); }\n",
            "    } else {\n",
            "      if (loginBox) { loginBox.style.backgroundImage = ''; loginBox.style.background = 'transparent'; loginBox.classList.remove('has-bg'); }\n",
            "      if (regBox) { regBox.style.backgroundImage = ''; regBox.style.background = 'transparent'; regBox.classList.remove('has-bg'); }\n",
            "    }\n",
        ]
        lines[i:i] = new_lines
        break

with open("D:/git/peiwang-store/public/js/app.js", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("OK app.js updated")
