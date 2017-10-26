#_*_coding:utf-8_*_
# Author:Topaz
expression_str =''
count = 0
for i in range(5):
    count += 1
    if i/2 and count != 5:
        expression_str += str(True) +  ' ' + 'and' + ' '
    else:
        expression_str += str(False) + ' '

print(expression_str)

if expression_str:
    # print(expression_str,type(expression_str))
    trigger_res = eval(expression_str)
else:
    print("没得")