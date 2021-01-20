# encoding: utf-8
"""
@author: lileilei
@software: PyCharm
@file: regpub.py
@time: 2017/4/27 9:03
"""
'''
注册测试
'''
import os

from excetfuntion.exectfuntion import Makeappcase
from untils.log import LOG, logger


@logger('Prueba de registro')
class RegFuntion:
    def __init__(self, driver):
        path = os.getcwd()
        path_ = os.path.join(os.path.join(path, 'data'), 'location')
        self.path = os.path.join(path_, 'eribank.yaml')
        self.driver = driver
        self.open = Makeappcase(self.driver, path=self.path)

    def reg(self, **kwargs):
        f = self.open.exce_case(**kwargs)
        if f['code'] == 1:
            LOG.info('Incapaz de obtener una afirmación')
            return
        else:
            beijing = f['data']
            return beijing
