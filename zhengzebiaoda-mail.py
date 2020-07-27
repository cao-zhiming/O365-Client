import re
'''正则表达式的库文件'''

line = input('请输入邮件地址：')
parts = re.split(r'[;]', line)
'''将其分割并加入列表parts'''
print(parts)
