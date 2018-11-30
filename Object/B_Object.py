#!/usr/bin/env python
# -*- coding: utf-8 -*-


from logging import INFO
import time
from datetime import datetime
from config.constant import *


########################################################################
class BackBaseData(object):
    """回测框架推送数据的基础类，其他数据类继承于此"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass


########################################################################


class BackBarData(BackBaseData):
    """回测框架的K线数据"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(BackBarData, self).__init__()

        self.symbol = EMPTY_STRING  # 代码
        self.exchange = EMPTY_STRING  # 交易所

        self.open = EMPTY_FLOAT  # OHLC
        self.high = EMPTY_FLOAT
        self.low = EMPTY_FLOAT
        self.close = EMPTY_FLOAT

        self.date = EMPTY_STRING  # bar开始的时间，日期
        self.time = EMPTY_STRING  # 时间
        self.datetime = None  # python的datetime时间对象

        self.volume = EMPTY_INT  # 成交量
        self.openInterest = EMPTY_INT  # 持仓量
        self.interval = EMPTY_UNICODE  # K线周期


########################################################################
class BackTradeData(BackBaseData):
    """
    回测框架内的交易数据
    """

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(BackTradeData, self).__init__()

        # 代码编号相关
        self.symbol = EMPTY_STRING  # 合约代码
        self.exchange = EMPTY_STRING  # 交易所代码

        # 成交相关
        self.openTime = EMPTY_STRING  # 开仓时间
        self.openDirection = EMPTY_STRING  # 开仓方向
        self.openprice = EMPTY_FLOAT  # 开仓价格
        self.openvolume = EMPTY_FLOAT  # 开仓数量
        self.openCommission = EMPTY_FLOAT  # 开仓手续费

        self.closeTime = EMPTY_STRING  # 平仓时间
        self.closeDirection = EMPTY_UNICODE  # 平仓方向
        self.closeprice = EMPTY_FLOAT  # 平仓价格
        self.closevolume = EMPTY_FLOAT  # 平仓数量
        self.closeCommission = EMPTY_FLOAT  # 平仓手续费

        self.profitloss = EMPTY_FLOAT  # 平仓盈亏
        self.netprofitloss = EMPTY_FLOAT  # 净盈亏


########################################################################
class BackPositionData(BackBaseData):
    """详细持仓数据类"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(BackPositionData, self).__init__()

        # 代码编号相关
        self.symbol = EMPTY_STRING  # 合约代码
        self.exchange = EMPTY_STRING  # 交易所代码

        # 持仓相关
        self.openTime = EMPTY_STRING  # 开仓时间
        self.direction = EMPTY_STRING  # 持仓方向
        self.position = EMPTY_INT  # 持仓量
        self.price = EMPTY_FLOAT  # 持仓价格

        self.ydPosition = EMPTY_INT  # 是否是昨持仓
        self.stingOpen = EMPTY_STRING  # 结算时是否盯开盘
        self.positionProfit = EMPTY_FLOAT  # 持仓盯市盈亏
        self.bytradeProfit = EMPTY_FLOAT  # 持仓逐笔盈亏


class BackPositionsData(BackBaseData):
    """持仓数据类"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(BackPositionsData, self).__init__()

        # 代码编号相关
        self.symbol = EMPTY_STRING  # 合约代码
        self.exchange = EMPTY_STRING  # 交易所代码

        # 持仓相关
        self.direction = EMPTY_STRING  # 持仓方向
        self.position = EMPTY_INT  # 持仓量
        self.frozen = EMPTY_INT  # 冻结数量
        self.price = EMPTY_FLOAT  # 持仓均价

        self.positionProfit = EMPTY_FLOAT  # 持仓盯市盈亏
        self.bytradeProfit = EMPTY_FLOAT  # 持仓逐笔盈亏



########################################################################
class BackAccountData(BackBaseData):
    """账户数据类"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(BackAccountData, self).__init__()

        # 账号代码相关
        self.accountID = EMPTY_STRING  # 账户代码
        self.BackAccountID = EMPTY_STRING  # 账户在Back中的唯一代码，通常是 Gateway名.账户代码

        # 数值相关
        self.preBalance = EMPTY_FLOAT  # 昨日账户结算净值
        self.balance = EMPTY_FLOAT  # 账户净值
        self.available = EMPTY_FLOAT  # 可用资金
        self.commission = EMPTY_FLOAT  # 今日手续费
        self.margin = EMPTY_FLOAT  # 保证金占用
        self.closeProfit = EMPTY_FLOAT  # 平仓盈亏
        self.positionProfit = EMPTY_FLOAT  # 持仓盈亏


########################################################################
class BackErrorData(BackBaseData):
    """错误数据类"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(BackErrorData, self).__init__()

        self.errorID = EMPTY_STRING  # 错误代码
        self.errorMsg = EMPTY_UNICODE  # 错误信息
        self.additionalInfo = EMPTY_UNICODE  # 补充信息

        self.errorTime = time.strftime('%X', time.localtime())  # 错误生成时间


########################################################################
class BackLogData(BackBaseData):
    """日志数据类"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(BackLogData, self).__init__()

        self.logTime = time.strftime('%X', time.localtime())  # 日志生成时间
        self.logContent = EMPTY_UNICODE  # 日志信息
        self.logLevel = INFO  # 日志级别


########################################################################
class BackHistoryData(object):
    """K线时间序列数据"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.BackSymbol = EMPTY_STRING  # Back系统代码
        self.symbol = EMPTY_STRING  # 代码
        self.exchange = EMPTY_STRING  # 交易所

        self.interval = EMPTY_UNICODE  # K线时间周期
        self.queryID = EMPTY_STRING  # 查询号
        self.barList = []  # BackBarData列表
