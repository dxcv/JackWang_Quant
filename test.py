#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd
import os
import talib
from single import frame_single



def main():
    # 数据部分，需要重新接入
    file_path = os.path.join(os.getcwd(),  'adaeth.xls')
    bardata = pd.read_excel(file_path)
    # 数据的简单处理
    sma_short = talib.MA(bardata['收'], 5)
    sma_long = talib.MA(bardata['收'], 20)

    # 引入轻量级回测框架
    backtest = frame_single('adaeth')
    #==============================这里是策略
    for i1 in range(0, len(bardata)):
        if i1 > 0 and divmod(i1, 50)[1] == 0:
            print(i1)
        md = backtest.marketdata_new()
        order = backtest.order_new()
        # marketdata 处理
        md.loc[0, '时间'] = bardata.loc[i1, '时间']
        md.loc[0, '品种'] = 'adaeth'
        if i1 == 0:
            md.loc[0, '昨收'] = bardata.loc[i1, '开']
        else:
            md.loc[0, '昨收'] = bardata.loc[i1-1, '收']
        md.loc[0, '开盘'] = bardata.loc[i1, '开']
        md.loc[0, '最高'] = bardata.loc[i1, '高']
        md.loc[0, '最低'] = bardata.loc[i1, '低']
        md.loc[0, '今收'] = bardata.loc[i1, '收']
        md.loc[0, '成交量'] = 1
        # order逻辑
        if i1 >= 20: # 过滤掉前20根K线
            # 当前无持仓，则给持仓
            cross_up = sma_short[i1] > sma_long[i1] and sma_short[i1-1] < sma_long[i1-1]
            cross_down = sma_short[i1] < sma_long[i1] and sma_short[i1-1] > sma_long[i1-1]
            if i1 ==20: # 首次
                if sma_short[i1] > sma_long[i1]:
                    order.loc[0, '时间'] = md.loc[0, '时间']
                    order.loc[0, '品种'] = 'adaeth'
                    order.loc[0, '买卖'] = '买开'
                    order.loc[0, '成交价'] = md.loc[0, '今收']
                    order.loc[0, '数量'] = 1
                elif sma_short[i1] < sma_long[i1]:
                    order.loc[0, '时间'] = md.loc[0, '时间']
                    order.loc[0, '品种'] = 'adaeth'
                    order.loc[0, '买卖'] = '卖开'
                    order.loc[0, '成交价'] = md.loc[0, '今收']
                    order.loc[0, '数量'] = 1
            if cross_up:
                # 如果发生了上穿
                order.loc[0, '时间'] = md.loc[0, '时间']
                order.loc[0, '品种'] = 'adaeth'
                order.loc[0, '买卖'] = '买平'
                order.loc[0, '成交价'] = md.loc[0, '今收']
                order.loc[0, '数量'] = 1

                order.loc[1, '时间'] = md.loc[0, '时间']
                order.loc[1, '品种'] = 'adaeth'
                order.loc[1, '买卖'] = '买开'
                order.loc[1, '成交价'] = md.loc[0, '今收']
                order.loc[1, '数量'] = 1
            if cross_down:
                # 如果发生了下穿
                order.loc[0, '时间'] = md.loc[0, '时间']
                order.loc[0, '品种'] = 'adaeth'
                order.loc[0, '买卖'] = '卖平'
                order.loc[0, '成交价'] = md.loc[0, '今收']
                order.loc[0, '数量'] = 1

                order.loc[1, '时间'] = md.loc[0, '时间']
                order.loc[1, '品种'] = 'adaeth'
                order.loc[1, '买卖'] = '卖开'
                order.loc[1, '成交价'] = md.loc[0, '今收']
                order.loc[1, '数量'] = 1

            # 最后一个
            if i1 == len(bardata) - 1:
                if backtest.position.loc[0,'多空'] == '多':
                    order.loc[0, '时间'] = md.loc[0, '时间']
                    order.loc[0, '品种'] = 'adaeth'
                    order.loc[0, '买卖'] = '卖平'
                    order.loc[0, '成交价'] = md.loc[0, '今收']
                    order.loc[0, '数量'] = 1
                elif backtest.position.loc[0, '多空'] == '空':
                    order.loc[0, '时间'] = md.loc[0, '时间']
                    order.loc[0, '品种'] = 'adaeth'
                    order.loc[0, '买卖'] = '买平'
                    order.loc[0, '成交价'] = md.loc[0, '今收']
                    order.loc[0, '数量'] = 1
        backtest.backtest_loop(md,order)
        position = backtest.position
        if len(position) > 2:
            print(position)
    #==============================策略结束

    backtest.record_process()
    backtest.backtest_record_save('test', 'sma-20-5')




if __name__ == '__main__':
    main()