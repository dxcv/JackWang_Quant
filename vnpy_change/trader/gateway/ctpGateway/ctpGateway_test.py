#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test的时候，引入的gateway也是模块，而不是类
"""


from vnpy_change.trader.gateway import ctpGateway
from vnpy_change.trader.vtEngine import MainEngine
from vnpy_change.event.eventEngine import EventEngine
from vnpy_change.trader.vtObject import VtSubscribeReq
import time


def main():
    modl = ctpGateway
    ee = EventEngine()
    me = MainEngine(ee)
    me.addGateway(ctpGateway)

    x = VtSubscribeReq()
    x.symbol = 'rb1901'


    me.connect('CTP')
    me.subscribe(x, 'CTP')
    while True:
        try:
            print("time:{0} ,price:{1:.2f}".format(me.dataEngine.tickDict['rb1901'].time,
                                                   me.dataEngine.tickDict['rb1901'].lastPrice))
            time.sleep(3)
        except Exception:
            time.sleep(3)
    print('Done')



if __name__ == '__main__':
    main()