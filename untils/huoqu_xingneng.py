# -*- coding: utf-8 -*-
# @Date    : 2017-06-12
# @Author  : lileilei
'''
获取配置相关手机性能的数据
'''
import os
import platform

from untils.log import logger


def getsystemsta():
    '''根据所运行的系统获取adb不一样的筛选条件'''
    system = platform.system()
    if system == 'Windows':
        find_manage = 'findstr'
    else:
        find_manage = 'grep'
    return find_manage


find = getsystemsta()


@logger('采集cpu信息')
def caijicpu(packagename, devices):
    '''La CPU recopilada aquí se puede utilizar para realizar la recopilación de operaciones, que es -n -d intervalo de actualización'''
    try:
        cpu = 'adb -s %s shell top -n 1| %s %s' % (devices, find, packagename)
        re_cpu = os.popen(cpu).read().split()[2]
        return re_cpu
    except:
        pass


@logger('获取使用的物理内存信息')
def getnencun(devices, packagename):
    '''Memoria física total utilizada real'''
    try:
        cpu = 'adb -s %s shell top -n 1| %s %s' % (devices, find, packagename)
        re_cpu = os.popen(cpu).read().split()[6]
        re_cpu_m = str(round(int(re_cpu[:-1]) / 1024)) + 'M'
        return re_cpu_m
    except:
        pass
