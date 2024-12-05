string=''
with open('headers.txt','r',encoding='utf-8') as f:
    s=f.read()
    string += s

import re 
pattern='":(\s)(\S+)'
replace='":\\1\"\\2",'

result=re.sub(pattern,replace,string)
with open("headers.txt",'w') as f:
    f.write(result)