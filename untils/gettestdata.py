""" 
@author: lileilei
@file: ddd.py 
@time: 2018/1/19 11:43 
"""
'''从Excel获取测试用例相关数据'''
import xlrd

from untils.log import logger, LOG


@logger('Obtenga los parámetros requeridos por el caso de prueba')
def huoqu_test(filepath, index):
    try:
        file = xlrd.open_workbook(filepath)
        me = file.sheets()[index]
        nrows = me.nrows
        listdata = []
        for i in range(1, nrows):
            dict_canshu = {}
            dict_canshu['id'] = me.cell(i, 0).value
            dict_canshu['model'] = me.cell(i, 0).value
            dict_canshu['logout'] = (me.cell(i, 2).value)
            dict_canshu.update(eval(me.cell(i, 3).value))
            dict_canshu.update(eval(me.cell(i, 4).value))
            listdata.append(dict_canshu)
        return listdata
    except Exception as e:
        LOG.info('¡No se pudieron obtener los parámetros del caso de prueba! Razón del fracaso：%s' % e)
        return e
