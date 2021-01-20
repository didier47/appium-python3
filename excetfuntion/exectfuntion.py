""" 
@author: lileilei
@file: exectfuntion.py 
@time: 2018/4/17 13:46 
"""
import time

from untils.log import logger, LOG
from untils.operyaml import open_da
from untils.py_app import driver_fengzhuang as feng

'''Analizar los pasos de prueba y realizar casos de prueba de acuerdo con los requisitos.
   El último conjunto de posicionamiento predeterminado es la aserción.
'''


@logger('Analizar los pasos de la prueba')
class Makeappcase():
    def __init__(self, driver, path):
        self.driver = driver
        self.path = path

    def open_file(self):
        return open_da(path=self.path)

    def exce_case(self, **kwargs):
        data = self.open_file()['data']
        case_der = feng(driver=self.driver)
        for i in range(len(data) - 1):
            f = case_der.find_elemens(lujing=data[i]['element_info'], fangfa=data[i]['find_type'])
            if data[i]['operate_type'] == 'click':
                self.driver.find_element_by_xpath(data[i]['element_info']).click()
            elif data[i]['operate_type'] == 'set_value':
                self.driver.find_element_by_xpath(data[i]['element_info']).send_keys(data[i]['msg'])
            elif data[i]['operate_type'] == 'send_key':
                f[int(data[i]['index'])].clear()
                f[int(data[i]['index'])].set_value(kwargs.get(data[i]['key']))
            else:
                LOG.info('Comprueba los pasos de tu prueba')
            time.sleep(1)
        f = case_der.find_elemens(lujing=data[-1]['element_info'], fangfa=data[-1]['find_type'])
        if data[-1]['operate_type'] == 'text':
            duanyan = {'code': 0, 'data': f[int(data[-1]['index'])].text}
        else:
            duanyan = {'code': 1, 'data': "Verifique que el último paso de su paso de prueba sea para la afirmación"}
            LOG.info('Verifique que el último paso de su paso de prueba sea para la afirmación')
        return duanyan
