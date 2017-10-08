a='123'
b='122aaa'
print(float(a))

def judge(ch):
    try:
        return bool(float(ch))
    except ValueError:
        return False

print(judge(a))
# import re
#
# my_re = re.compile(r'[A-Za-z]')
#
# my_str_1 = 'fasdfsaf1231231'
# my_str_2 = '123123123'
# print(bool(re.match(my_re, my_str_1)))
# print(bool(re.match(my_re, my_str_2)))
#
#
# def isNumber(line, label_column):  # 判断是否存在非数值数据
#     ch_re = re.compile(r'[A-Za-z]')
#     for i in range(len(line)):
#         if (i != label_column):
#             if (re.match(ch_re,line[i])):
#                 return False
#     return True