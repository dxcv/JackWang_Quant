#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
所有的回测事件类型

"""


# 系统相关
EVENT_TIMER = 'eTimer'                  # 计时器事件，每隔1秒发送一次
EVENT_LOG = 'eLog'                      # 日志事件，全局通用

# 回测相关
EVENT_TICK = 'eTick.'                   # TICK行情事件，可后接具体的vtSymbol
EVENT_TRADE = 'eTrade.'                 # 成交回报事件
EVENT_ORDER = 'eOrder.'                 # 报单回报事件
EVENT_POSITION = 'ePosition.'           # 持仓回报事件
EVENT_ACCOUNT = 'eAccount.'             # 账户回报事件
EVENT_CONTRACT = 'eContract.'           # 合约基础信息回报事件
EVENT_ERROR = 'eError.'                 # 错误回报事件
EVENT_HISTORY = 'eHistory.'             # K线数据查询回报事件

