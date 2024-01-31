import re
text=''
for line in iter(input,''):
    text += line + '\n'
matchobj = re.findall(r'^.*singer="(.*)">(.*)</a>',text,re.M)
if matchobj:
	print(matchobj)
#re.M是多行匹配，就是一行一行的看
#re.S是忽略换行符的匹配，把整个文本当作一行处理
#findall是适用于多行搜索查找，且返回为元组的列表
#match函数只用于字符串查找，局限性大