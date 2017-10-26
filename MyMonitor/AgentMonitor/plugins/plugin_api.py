#_*_coding:utf-8_*_
# Author:Topaz
# from linux import cpu
import time
def LinuxCpu():
    a = {'iowait': '0.00', 'system': '27.55', 'idle': '70.92', 'user': '1.53', 'steal': '0.00', 'nice': '0.00'}
    time.sleep(4)
    return a
def LinuxMemory():
    a = {'status': 0, 'MemTotal': '236124', 'MemUsage': 130332, 'Cached': '77480', 'MemUsage_p': '55', 'SwapFree': '776460', 'SwapUsage': 9968, 'SwapTotal': '786428', 'MemFree': '5116', 'SwapUsage_p': '2', 'Buffers': '23196'}
    time.sleep(4)
    return a

def LinuxNetwork():
    a = {'status': 0, 'data': {'lo': {'t_in': '0.00', 't_out': '0.00'}, 'eth0': {'t_in': '0.12', 't_out': '0.05'}}}
    time.sleep(4)
    return a

def Mysql():
    time.sleep(4)
    a = {"this is mysql": 13}
    return a

def LinuxLoad():
    a = {"this is load": 926}
    time.sleep(4)
    return a