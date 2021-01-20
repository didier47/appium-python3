
import datetime
import os
import random
import unittest
from multiprocessing import Pool

from testcase.regcasetest import regtest
from untils.AppiumServer import AppiumServer
from untils.BaseApk import getPhoneInfo, AndroidDebugBridge
from untils.Parmeris import Parmer
from untils.log import LOG, logger
from untils.makecase import makecasefile
from untils.pyreport_excel import create

l_devices = []
from config.config import *


@logger('Grupo de procesos para generar enlaces de configuración de dispositivos')
def runnerPool(getDevices):
    devices_Pool = []
    for i in range(0, len(getDevices)):
        _pool = []
        _initApp = {}
        if Test_mobile_type == "Android":
            _initApp["deviceName"] = getDevices[i]["devices"]
            _initApp["udid"] = getDevices[i]["devices"]
            _initApp["platformVersion"] = '10'
            _initApp["platformName"] = "android"
            _initApp["port"] = getDevices[i]["port"]
            _initApp["appPackage"] = TestappPackage
            _initApp["appActivity"] = TestAppActivity
            _initApp["automationName"] = "automation2"
        else:
            print("Tipo de dispositivo no admitido")
            return
        _pool.append(_initApp)
        devices_Pool.append(_initApp)
    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()


@logger('Organizar casos de prueba')
def runnerCaseApp(devices):
    '''
    Utilice el conjunto de pruebas de unittest para organizar casos de prueba
    '''
    test_suit = unittest.TestSuite()
    test_suit.addTest(Parmer.parametrize(testcase_klass=regtest, param=devices))  # Los otros casos de prueba de la extensión se agregan así
    unittest.TextTestRunner(verbosity=2).run(test_suit)


if __name__ == "__main__":
    LOG.info("Ejecución de pruebas")
    start_time = datetime.datetime.now()
    devicess = AndroidDebugBridge().attached_devices()

    makecasefile('reg', 'reg', 'reg')  # Solo se generará cuando no lo haya, generalmente habrá este archivo
    path = os.getcwd()
    report_path = os.path.join(path, "testreport")
    filenm = os.path.join(report_path , 'result.xls')
    if len(devicess) > 0:
        for dev in devicess:
            app = {}
            app["devices"] = dev
            app["port"] = str(random.randint(4593, 4598))
            l_devices.append(app)
        appium_server = AppiumServer(l_devices)
        appium_server.start_server()  # Empieza el servicio
        runnerPool(l_devices)
        try:
            appium_server.stop_server(devicess)
        except Exception as e:
            LOG.info("No se pudo cerrar el servicio, motivo：%s" % e)
        end_time = datetime.datetime.now()
        hour = end_time - start_time
        create(filename=filenm, devices_list=devicess, Test_version=testversion,
               testtime=str(hour))
        LOG.info("La prueba se ejecutó en：%s" % hour)
    else:
        LOG.info("No hay dispositivo Android disponible")

