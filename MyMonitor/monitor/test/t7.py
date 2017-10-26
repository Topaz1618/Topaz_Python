#_*_coding:utf-8_*_
# Author:Topaz
list = [99,88,77]
count = 0
e_str = ''
list_len = len(list)
# print(list_len)

for i in list:
    count +=1
    if list_len > 1 and list_len > count :
        # print("ok")
        e_str += str(i) + ' and' + ' '
    else:
        e_str += str(i)

    # print(e_str)
# if expression_obj.logic_type:
#     print(function_str)
#     expression_str += function_str + ' ' + expression_obj.logic_type + ' '
# else:
#     expression_str += function_str + ' '


dic = {'trigger':''}
if 'trigger' in dic:
    print("jjjj")
print(len(dic['trigger']))