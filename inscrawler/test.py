import re

str = '" title="trevorzt" href="/trevorzt/">trevorzt</a></h3><span><a class="notranslate" href="/ufcchamp0/">@ufcchamp0</a> 相爱相杀嗷</span></div></div></div></li><li class="gElp9 " role="menuitem"><div class="P9YgZ"><div class="C7I1f X7jCj"><div class="C4VMK"><h3 class="_6lAjh"><a class="'
name = str.split(">")[1].split("<")[0]
# message = str.split(">")[4].split("<")[0]
str1 = str.split(">")[5].split("<")[0]


# if str1[0] == '@':


aa = re.findall(r"<span>(.*)</span>", str)[0]
new = re.sub(u"<.*?>", "", aa)

print(new)
# print(message)
