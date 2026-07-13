
import re
with open('admin/js/users.js','r',encoding='utf-8') as f:
    c = f.read()

# Add status column header
c = c.replace(
    chr(60)+chr(116)+chr(104)+chr(62)+chr(35282)+chr(33394)+chr(33394)+chr(33394)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(21019)+chr(24314)+chr(26102)+chr(38388)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(25805)+chr(20316)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(25805)+chr(33394)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(29366)+chr(24314)+chr(26102)+chr(38388)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(25805)+chr(20316)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(25805)+chr(33394)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(25805)+chr(33394)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(25805)+chr(33394)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(25805)+chr(33394)+chr(62),
    chr(60)+chr(116)+chr(104)+chr(62)+chr(73)+chr(68)+chr(60)+chr(47)+chr(116)+chr(104)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(29992)+chr(25143)+chr(21517)+chr(60)+chr(47)+chr(116)+chr(104)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(37038)+chr(31665)+chr(60)+chr(47)+chr(116)+chr(104)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(35282)+chr(33394)+chr(60)+chr(47)+chr(116)+chr(104)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(29366)+chr(24577)+chr(60)+chr(47)+chr(116)+chr(104)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(21019)+chr(24314)+chr(26102)+chr(38388)+chr(60)+chr(47)+chr(116)+chr(104)+chr(62)+chr(60)+chr(116)+chr(104)+chr(62)+chr(25805)+chr(20316)+chr(60)+chr(47)+chr(116)+chr(104)+chr(62)
)
print('Step 1 done')
with open('admin/js/users.js','w',encoding='utf-8') as f:
    f.write(c)
print('OK')
