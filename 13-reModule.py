import re

# html = """
# <div><p>www.bianchengbang.com</p></div>
# <div><p>编程帮</p></div>
# """
#
# # 贪婪匹配
# pattern = re.compile('<div><p>.*</p></div>', re.S)
# re_list = pattern.findall(html)
# print(re_list)
#
# # 非贪婪
# pattern = re.compile('<div><p>.*?</p></div>', re.S)
# re_list2 = pattern.findall(html)
# print(re_list2)
#
# # 正则表达式分组
# website = "编程帮 www.biancheng.net"
# pattern_1 = re.compile('\w+\s+\w+\.\w+\.\w+')
# print(pattern_1.findall(website))
#
# pattern_2 = re.compile('(\w+)\s+\w+\.\w+\.\w+')
# print(pattern_2.findall(website))
#
# # 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
#
# # 有两个及以上的()则以元组形式显示
# pattern_3 = re.compile('(\w+)\s+(\w+\.\w+\.\w+)')
# print(pattern_3.findall(website))

# 从html中获取两部电影的名称和主演信息
html = """
<div class="movie-item-info">
<p class="name">
<a title="你好，李焕英">你好，李焕英</a>
</p>
<p class="star">
主演：贾玲,张小斐,沈腾
</p>    
</div>
<div class="movie-item-info">
<p class="name">
<a title="刺杀，小说家">刺杀，小说家</a>
</p>
<p class="star">
主演：雷佳音,杨幂,董子健,于和伟
</p>    
</div> 
"""
pattern = re.compile('<div.*?<a title="(.*?)".*?star">(.*?)</p.*?div>', re.S)
r_list = pattern.findall(html)
print(r_list)
if r_list:
    for r_info in r_list:
        print("影片名称：", r_info[0])
        print("影片主演：", r_info[1].strip())
        print(20*"*")
