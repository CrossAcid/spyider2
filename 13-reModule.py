import re

html = """
<div><p>www.bianchengbang.com</p></div>
<div><p>编程帮</p></div>
"""

# 贪婪匹配
pattern = re.compile('<div><p>.*</p></div>', re.S)
re_list = pattern.findall(html)
print(re_list)

# 非贪婪
pattern = re.compile('<div><p>.*?</p></div>', re.S)
re_list2 = pattern.findall(html)
print(re_list2)

# 正则表达式分组
website = "编程帮 www.biancheng.net"
pattern_1 = re.compile('\w+\s+\w+\.\w+\.\w+')
print(pattern_1.findall(website))

pattern_2 = re.compile('(\w+)\s+\w+\.\w+\.\w+')
print(pattern_2.findall(website))

# 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

# 有两个及以上的()则以元组形式显示
pattern_3 = re.compile('(\w+)\s+(\w+\.\w+\.\w+)')
print(pattern_3.findall(website))
