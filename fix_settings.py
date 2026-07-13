# -*- coding: utf-8 -*-
import re

with open('D:/git/peiwang-store/server.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add site_login_bg_url to settings GET default
old_get = '''var s = d.settings || { site_name: "白君的俱乐部", site_logo: "", site_logo_url: "", site_description: "专业游戏服务", site_video_url: "", site_music_url: "" };'''
new_get = '''var s = d.settings || { site_name: "白君的俱乐部", site_logo: "", site_logo_url: "", site_description: "专业游戏服务", site_video_url: "", site_music_url: "", site_login_bg_url: "" };'''
content = content.replace(old_get, new_get)

# Add site_login_bg_url to settings PUT handler
old_put = '''if (body.site_music_url !== undefined) d.settings.site_music_url = body.site_music_url;'''
new_put = '''if (body.site_music_url !== undefined) d.settings.site_music_url = body.site_music_url;
      if (body.site_login_bg_url !== undefined) d.settings.site_login_bg_url = body.site_login_bg_url;'''
content = content.replace(old_put, new_put)

with open('D:/git/peiwang-store/server.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK settings updated')
