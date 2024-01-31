import re
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

prime_html  = urlopen("http://db.18183.com/wzry/")#打开主网页，上面有各种英雄的名字
prime_bsobj = BeautifulSoup(prime_html,"html.parser")#创建主网页的BeautifulSoup对象
hrefs       = prime_bsobj.findAll("a",{"href":re.compile('\/wzry\/hero\/[0-9]*\.html')})
#寻找主网页中"href"形为'\/wzry\/hero\/[0-9]*\.html'的<a>tag，创建关于其的对象列表
json_file   = open('data.json','w+')#创建并打开json文件
i=0
for href in hrefs[0:50] : #对爬取不同英雄的信息进行循环操作，共50个
    i+=1
    print(i)
    url=href["href"] #提取href对象中"href"的信息
    temp_html=urlopen("http://db.18183.com"+url) #打开单个英雄的网页
    temp_bsobj=BeautifulSoup(temp_html,"html.parser") #创建该网页的beautifulsoup对象
    text0=href.text[2:] 
    text0=text0[:-1] #由于在主网页上面的英雄姓名爬取后带有"\n"，所以要进行切片操作
    dict_={"英雄名字":text0} #将英雄名字纳入字典dict_之中
    text1=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('最大生命：.*')).text)
    #text1首先通过find方法找到含有最大生命的tag，再用findall方法找到其中含有数值的关键信息
    text2=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('最大法力：.*')).text)
    text3=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('物理攻击：.*')).text)
    text4=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('法术攻击：.*')).text)
    text5=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('物理防御：.*')).text)
    text6=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('法术防御：.*')).text)
    text7=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('物理减伤率：.*')).text)
    text8=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('法术减伤率：.*')).text)
    text9=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('移速：*')).text)
    text10=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('物理护甲穿透：.*')).text)
    text11=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('法术护甲穿透：.*')).text)
    text12=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('攻速加成：.*')).text)
    text13=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('暴击几率：.*')).text)
    text14=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('暴击效果：.*')).text)
    text15=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('物理吸血：.*')).text)
    text16=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('法术吸血：.*')).text)
    text17=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('冷却缩减：.*')).text)
    text18=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('攻击范围：.*')).text)
    text19=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('韧性：.*')).text)
    text20=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('生命回复：.*')).text)
    text21=re.findall(r"(：)(.*)",temp_bsobj.find(text=re.compile('法力回复：.*')).text)
    star_list=temp_bsobj.findAll("span",{"class":re.compile("star star-[0-9][0-9]*")})
    #由于英雄的属性有的是星级表示，故该星级属性需要通过<span>tag中”class“属性的特征进行寻找
    text22=re.findall(r"(star-)([0-9]*[0-9]*)",star_list[0]["class"][1])
    text23=re.findall(r"(star-)([0-9]*[0-9]*)",star_list[1]["class"][1])
    text24=re.findall(r"(star-)([0-9]*[0-9]*)",star_list[2]["class"][1])
    text25=re.findall(r"(star-)([0-9]*[0-9]*)",star_list[3]["class"][1])
    #text1-text21均为相似操作
    #text22-text25提取找出的<span>tag中星级的具体数值
    dict_["最大生命"]=text1[0][1]
    dict_["最大法力"]=text2[0][1]
    dict_["物理攻击"]=text3[0][1]
    dict_["法术攻击"]=text4[0][1]
    dict_["物理防御"]=text5[0][1]
    dict_["法术防御"]=text6[0][1]
    dict_["物理减伤率"]=text7[0][1]
    dict_["法术减伤率"]=text8[0][1]
    dict_["移速"]=text9[0][1]
    dict_["物理护甲穿透"]=text10[0][1]
    dict_["法术护甲穿透"]=text11[0][1]
    dict_["攻速加成"]=text12[0][1]
    dict_["暴击几率"]=text13[0][1]
    dict_["暴击效果"]=text14[0][1]
    dict_["物理吸血"]=text15[0][1]
    dict_["法术吸血"]=text16[0][1]
    dict_["冷却缩减"]=text17[0][1]
    dict_["攻击范围"]=text18[0][1]
    dict_["韧性"]=text19[0][1]
    dict_["生命回复"]=text20[0][1]
    dict_["法力回复"]=text21[0][1]
    dict_["生存能力"]=text22[0][1]
    dict_["攻击伤害"]=text23[0][1]
    dict_["技能效果"]=text24[0][1]
    dict_["上手难度"]=text25[0][1]
    #添加字典的键对值
    #json_str=str(dict_) #将字典转化为str对象
    json_str=json.dumps(dict_,ensure_ascii=False,indent=4)
    json_file.write(json_str) #写入文件
    json_file.write('\n') #换行
json_file.close() #关闭文件
    
    