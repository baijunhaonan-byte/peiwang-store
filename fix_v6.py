SQ = chr(39)
DQ = chr(34)
with open('admin/js/users.js','r',encoding='utf-8') as f: c = f.read()
la = chr(27491)+chr(24120)
ld = chr(24050)+chr(31105)+chr(29992)
parts = []
parts.append(SQ + '</td>' + SQ + ' + (u.status === ' + SQ + 'disabled' + SQ + ' ? ' + SQ + '<span style=' + DQ + 'color:red' + DQ + '>' + ld + '</span>' + SQ + ' : ' + SQ + '<span style=' + DQ + 'color:green' + DQ + '>' + la + '</span>' + SQ + ') + ' + SQ + '</td>' + SQ + ' + time')
nt = ''.join(parts)
ot = SQ + '</td>' + SQ + ' + time'
c = c.replace(ot, nt)
open('admin/js/users.js','w',encoding='utf-8').write(c)
print('4 done')
