#_*_coding:utf-8_*_
# Author:Topaz
data = {'status': 0, 'data': {'lo': {'t_in': '0.00', 't_out': '0.00'}, 'eth0': {'t_in': '0.12', 't_out': '0.05'}}}
tmp_dic ={}

for k1,v1 in data['data'].items():
    # print(k1,v1)
    tmp_dic[k1] ={}
    for k2,v2 in v1.items():
        # print(k2,v2)
        tmp_dic[k1][k2] = []

    print(tmp_dic)

