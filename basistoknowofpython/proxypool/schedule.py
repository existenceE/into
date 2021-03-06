

TESTER_CYCLE = 20
GETTER_CYCLE = 20
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

from multiprocessing import Process
from .api import _app
from getter import Getter
from .tester import Tester
import time


class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        '''
        定时测试代理
        :param cycle:
        :return:
        '''
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        '''
        定时h获取代理
        :param cycle:
        :return:
        '''
        getter = Getter()
        while True:
            print('k开始z抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        '''
        开启API
        :return:
        '''
        app.run(API_HOST, API_PORT)

    def run(self):
        print('d代理池开始运行')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()














