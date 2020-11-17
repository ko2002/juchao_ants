'''
CREATE TABLE `stk_quot_idx` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `Date` datetime NOT NULL COMMENT '日期',
  `InnerCode` int(11) DEFAULT NULL COMMENT '内部编码',
  `PreClose` decimal(20,2) DEFAULT NULL COMMENT '前一个交易日的收盘价',
  `Open` decimal(20,2) DEFAULT NULL COMMENT '开盘价',
  `High` decimal(20,2) DEFAULT NULL COMMENT '最高价',
  `Low` decimal(20,2) DEFAULT NULL COMMENT '最低价',
  `Close` decimal(20,2) DEFAULT NULL COMMENT '收盘价',
  `Volume` decimal(20,5) DEFAULT NULL COMMENT '成交量(手)',
  `Amount` decimal(20,5) DEFAULT NULL COMMENT '成交额',
  `TotalShares` decimal(20,4) DEFAULT NULL COMMENT '总股本',
  `FloatShares` decimal(20,4) DEFAULT NULL COMMENT '流通股本',
  `Turnover` decimal(20,6) DEFAULT NULL COMMENT '换手率(%)',
  `Change` decimal(20,2) DEFAULT NULL COMMENT '涨跌',
  `ChangeActual` decimal(20,2) DEFAULT NULL COMMENT '实际涨跌',
  `PreCloseBasetoday` decimal(20,2) DEFAULT NULL COMMENT '昨收基今价',
  `ChangePerc` decimal(20,6) DEFAULT NULL COMMENT '涨跌幅(%)',
  `ChangePercActual` decimal(20,6) DEFAULT NULL COMMENT '实际涨跌幅(%)',
  `CREATETIMEJZ` datetime DEFAULT CURRENT_TIMESTAMP,
  `UPDATETIMEJZ` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `un1` (`Date`,`InnerCode`),
  KEY `InnerCode` (`InnerCode`),
  KEY `Date` (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='日行情指标' ;

字段:
Date: 日期
InnerCode: 证券内部编码
PreClose: 前一个交易日的收盘价
Open: (今日)开盘价
High: (今日)最高价
Low: (今日) 最低价
Close: (今日) 收盘价
Volume: (今日) 成交量 (单位: 手)
Amount: (今日) 成交额
TotalShares: 总股本
FloatShares: 流通股本
Turnover: 换手率

Change: 涨跌
ChangeActual: 实际涨跌
PreCloseBasetoday: 昨收基今价
ChangePerc: 涨跌幅(%)
ChangePercActual: 实际涨跌幅(%)


CREATE TABLE `sf_const_announcement` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `EventMainTypeCode` varchar(20) NOT NULL COMMENT '事件所属的大类代码',
  `EventMainTypeName` varchar(50) NOT NULL COMMENT '事件所属的大类名称',
  `EventCode` varchar(50) NOT NULL COMMENT '事件代码',
  `EventName` varchar(100) NOT NULL COMMENT '事件名称',
  `EventOneWordLabel` varchar(50) DEFAULT NULL COMMENT '事件类型一字标签',
  `Sentiment` tinyint(4) NOT NULL COMMENT '情感倾向(1-正面，-1-负面，0-中性)',
  `Level` int(4) NOT NULL COMMENT '舆情级别：0为中性，负数越小，影响越利空；正数越大，影响越利多',
  `EventDayChgPerc` decimal(10,4) NOT NULL COMMENT '公告发布当日的涨跌幅',
  `EventDayWinRatio` decimal(10,4) NOT NULL COMMENT '公告发布当日的胜率',
  `NextDayWinRatio` decimal(10,4) NOT NULL COMMENT '次日胜率',
  `NextDayChgPerc` decimal(10,2) NOT NULL COMMENT '次日涨幅',
  `ThreeDayChgPerc` decimal(10,2) NOT NULL COMMENT '3日涨幅',
  `FiveDayChgPerc` decimal(10,2) NOT NULL COMMENT '5日涨幅',
  `Desc` varchar(1000) DEFAULT NULL COMMENT '事件描述',
  `IfShow` tinyint(4) NOT NULL DEFAULT 1 COMMENT '软件是否展示：0-不展示，1-展示',
  `FirstLevelShowRank` int(10) DEFAULT NULL COMMENT '公告智选前端展示排序-一级事件（对应EventMainTypeCode）（一个一级事件下面对应的多个二级事件每条数据需要保证这个字段一致）',
  `SecondLevelShowRank` int(10) DEFAULT NULL COMMENT '公告智选前端展示排序-二级事件（对应EventCode）',
  `CreateTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `UpdateTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `u1` (`EventName`),
  UNIQUE KEY `u2` (`EventCode`),
  UNIQUE KEY `u3` (`EventMainTypeCode`,`EventCode`,`SecondLevelShowRank`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='常量表-公告事件' ;

需要的字段:
EventMainTypeCode: 事件所属大类代码 : 后台人工录入 待后台接口完善后调用接口
EventMainTypeName: 事件所属大类名称:  后台人工录入 待后台接口完善后调用接口
EventCode 事件代码: 后台人工录入 待后台接口完善后调用接口
EventName 事件名称: 后台人工录入 待后台接口完善后调用接口
EventOneWordLabel: 事件类型--字标签: 后台管理
Sentiment: 情感倾向(1-正面，-1-负面，0-中性): 后台管理
Level: 舆情级别: 后台管理，0 为中性，负数越小，影响越利空； 整数越大，影响越利多

EventDayChgPerc :公告发布当日的涨跌幅: 近一年同类型的公告统计, 交易日收盘更新
EventDayWinRatio: 公告发布当日的胜率: 近一年同类型的公告统计, 交易日收盘更新
NextDayWinRatio: 次日胜率: 近一年同类型的公告统计, 交易日收盘更新
NextDayChgPerc: 次日平均涨幅: 近一年同类型的公告统计, 交易日收盘更新
ThreeDayChgPerc: 3日平均涨幅: 近一年同类型的公告统计, 交易日收盘更新
FiveDayChgPerc: 5日平均涨幅: 近一年同类型的公告统计, 交易日收盘更新

Desc: 事件描述: 后台管理
IfShow: 软件是否展示：0-不展示，1-展示: 后台管理
FirstLevelShowRank: 公告智选前端展示排序-一级事件（对应EventMainTypeCode）（一个一级事件下面对应的多个二级事件每条数据需要保证这个字段一致）: 后台管理
SecondLevelShowRank: 公告智选前端展示排序-二级事件（对应EventCode）: 后台管理
CreateTime: 创建时间
UpdateTime: 更新时间

生成逻辑:
综合上表需要生成的字段有:
EventDayChgPerc
EventDayWinRatio
NextDayWinRatio
NextDayChgPerc
ThreeDayChgPerc
FiveDayChgPerc

此表的涨幅和胜率，每个交易日由程序刷新，其他字段交给后台管理。每日更新一次，每次更新的流程如下:
(1) 获取事件代码列表: select EventCode from sf_const_announcement; // select distinct(EventCode) from sf_const_announcement;

(2) 逐个事件代码遍历, 获取这个事件近一年的公告明细数据:
select PubTime, SecuCode from dc_ann_event_source_ann_detail where EventCode = 'A0001001' and PubTime > '2019-11-16';

(3) 根据取出的 SecuCode list 结合行情数据计算需生成的几个字段：
select ChangePercActual from stk_quot_idx where InnerCode = '{}' and Date > '{}' order by Date limit {};
遍历 SecuCode:
    # 次日平均涨幅
    [x, y] = [0.1, 0.2]
    ret1 = (1+x)*(1+y) - 1
    print(ret)

    # 3 日平均涨幅
    [x, y, z] = [0.1, 0.2, -0.1]
    ret2 = (1+x)*(1+y)*(1+z) - 1
    print(ret)

    # 5 日平均涨幅
    [x, y, z, m, n] = [0.1, 0.2, -0.1, -0.2, -0.3]
    ret3 = (1+x)*(1+y)*(1+z)*(1+m)*(1+n) - 1
    print(ret)
    return [ret1, ret2, ret3]

{
"SecuCodde1": [ret1, ret2, ret3],
"SecuCodde2": [ret1, ret2, ret3],
"SecuCodde3": [ret1, ret2, ret3],
"SecuCodde4": [ret1, ret2, ret3],
...
}
纵向求平均

# 什么是胜率: 涨跌幅大于 0 就是记作胜，小于等于 0 就记作败, 比如 100 个股票，20 个涨跌幅大于 0，他的胜率就是 20%

# 当日的胜率
[SecuCode1, SecuCode2, SecuCode3, SecuCode4 ] = [0.1, 0.2, -0.1, -0.2]     50%

# 次日的胜率
用次日的实际涨幅算
'''
import datetime
import multiprocessing
import os
import pprint
import sys
import time
import traceback
from functools import wraps

import pymysql
import schedule

cur_path = os.path.split(os.path.realpath(__file__))[0]
file_path = os.path.abspath(os.path.join(cur_path, ".."))
sys.path.insert(0, file_path)

from configs import (DC_HOST, DC_PORT, DC_USER, DC_PASSWD, DC_DB, YQ_HOST, YQ_PORT, YQ_USER,
                     YQ_PASSWD, YQ_DB, )


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('[' + func.__name__ + ']used:' + str(end - start))
        with open('final3.log', "a") as f:
            f.write('[' + func.__name__ + str(args[1]) + ']used:' + str(end - start) + '\n')
        return r
    return wrapper


class FinalConstAnn(object):
    def __init__(self):
        self.dc_table_name = 'stk_quot_idx'  # 日行情指标表 从 datacenter 数据库中获取
        self.target_table_name = 'sf_const_announcement'  # 目标数据库: 公告事件常量表
        self.source_table_name = 'dc_ann_event_source_ann_detail'  # 源数据库: 公告明细表
        self.tool_table_name = 'secumain'
        self.dc_cfg = {  # datacenter 数据库的配置
            "host": DC_HOST,
            "port": int(DC_PORT),
            "user": DC_USER,
            "password": DC_PASSWD,
            "db": DC_DB,
            'charset': 'utf8'
        }
        self.yq_cfg = {  # 舆情数据库的配置
            "host": YQ_HOST,
            "port": int(YQ_PORT),
            "user": YQ_USER,
            "password": YQ_PASSWD,
            "db": YQ_DB,
            'charset': 'utf8'
        }
        # self.today = datetime.datetime.now() - datetime.timedelta(days=10)
        self.today = datetime.datetime.now()
        self.today_of_lastyear = self.today - datetime.timedelta(days=365)
        self.innercode_map = None

    def innercode_map_init(self):
        if not self.innercode_map:
            self.innercode_map = self.get_inner_code_map()

    def make_sql_conn(self, cfg: dict):
        try:
            conn = pymysql.connect(**cfg)
            return conn
        except:
            traceback.print_exc()
            return None

    def get_inner_code_map(self):
        sql = '''select SecuCode, InnerCode from {} where SecuCode in (select distinct(SecuCode) from {}); '''.format(self.tool_table_name, self.source_table_name)
        __map = {}
        try:
            yq_conn = self.make_sql_conn(self.yq_cfg)
            yq_cursor = yq_conn.cursor()
            yq_cursor.execute(sql)
            res = yq_cursor.fetchall()
            for r in res:
                __map[r[0]] = r[1]
            yq_cursor.close()
            yq_conn.close()
            return __map
        except:
            traceback.print_exc()
            return {}

    def const_event_codes(self):
        sql = '''select distinct(EventCode) from {};'''.format(self.target_table_name)
        try:
            yq_conn = self.make_sql_conn(self.yq_cfg)
            yq_cursor = yq_conn.cursor()
            yq_cursor.execute(sql)
            res = yq_cursor.fetchall()
            yq_cursor.close()
            yq_conn.close()
            event_codes = [one[0] for one in res]
            return event_codes
        except:
            traceback.print_exc()
            return []

    def get_event_detail(self, event_code: str):
        sql = '''select PubTime, SecuCode from {} where EventCode = '{}' and PubTime between '{}' and '{}' ;'''.format(self.source_table_name, event_code, self.today_of_lastyear, self.today)
        try:
            yq_conn = self.make_sql_conn(self.yq_cfg)
            yq_cursor = yq_conn.cursor()
            yq_cursor.execute(sql)
            res = yq_cursor.fetchall()
            yq_cursor.close()
            yq_conn.close()
            return res
        except:
            traceback.print_exc()
            return []

    # def generate_eventdaywinratio(self, detail_info: tuple):
    #     "计算证券列表的当日胜率与次日胜率"
    #     winlist_onday = []
    #     winlist_nextday = []
    #
    #     for event_happen_day, secucode in detail_info:
    #         fivedays_cpt = self.get_fivedays_changepercactual(secucode, event_happen_day)
    #         winlist_onday.append(float(fivedays_cpt[0]))
    #         winlist_nextday.append(float(fivedays_cpt[1]))
    #
    #     on_count = 0
    #     for rate in winlist_onday:
    #         if rate > 0:
    #             on_count += 1
    #     onday_winrate = on_count / len(winlist_onday)
    #
    #     next_count = 0
    #     for rate in winlist_nextday:
    #         if rate > 0:
    #             next_count += 1
    #     nextday_winrate = next_count / len(winlist_nextday)
    #     return onday_winrate, nextday_winrate

    def get_fivedays_changepercactual(self, secucode: str, dt: datetime.datetime):
        innercode = self.innercode_map.get(secucode)
        if not innercode:
            return []
        sql = '''select Date, ChangePercActual from {} where InnerCode = '{}' and Date >= '{}' order by Date limit 5;'''.format(self.dc_table_name, innercode, dt)
        try:
            dc_conn = self.make_sql_conn(self.dc_cfg)
            dc_cursor = dc_conn.cursor()
            dc_cursor.execute(sql)
            res = dc_cursor.fetchall()
            dc_cursor.close()
            dc_conn.close()
            return res
        except:
            traceback.print_exc()
            return []

    def generate_changepercactual_index(self, index_datas):
        """计算单只证券的 次\3\5日 累计涨幅"""
        cpt_scores = [float(data[1]) for data in index_datas]
        # print("&&&&&", cpt_scores)

        days_len = len(cpt_scores)
        x = y = z = m = n = None

        if days_len == 0 or days_len == 1:
            return []

        elif days_len == 2:
            x, y = cpt_scores
        elif days_len == 3:
            x, y, z = cpt_scores
        elif days_len == 4:
            x, y, z, m = cpt_scores
        else:
            x, y, z, m, n = cpt_scores
        # print("*****", x, y, z, m, n)
        ret1 = ret2 = ret3 = None
        # 次日累计涨幅
        ret1 = (1 + x) * (1 + y) - 1
        # 3 日累计涨幅
        if z is not None:
            ret2 = (1 + x) * (1 + y) * (1 + z) - 1
            if m is not None and n is not None:
                # 5 日累计涨幅
                ret3 = (1 + x) * (1 + y) * (1 + z) * (1 + m) * (1 + n) - 1
        # print(">>>>>", ret1, ret2, ret3)
        return [ret1, ret2, ret3]

    @timing
    def process_single_eventcode(self, eventcode: str):
        print("NOW IS:", eventcode)
        record = {}
        record["EventCode"] = eventcode
        # (3) 对于某一个事件来说， 近一年发生该事件的证券以及发生时间列表
        event_detail_info = self.get_event_detail(eventcode)
        print(f"EVENT DETAIL COUNT: {len(event_detail_info)}")
        event_count = len(event_detail_info)
        if event_count == 0:
            print(f"NO RVENT OF CODE {eventcode}")
            return None
        winlist_onday = []  # 针对事件全部股票列表在时间发生时间的当日胜率与次日胜率
        winlist_nextday = []

        total_rate = 0
        total_rate2 = 0  # 针对事件全部股票列表在时间发生时间的次\3\5日平均涨幅
        total_rate3 = 0
        total_rate5 = 0

        # secuCode_rate_info = {}
        for happen_dt, secuCode in event_detail_info:
            # (4) 获取单只证券在发生时间后(包括当日)的5日涨幅
            fiveday_rateinfo = self.get_fivedays_changepercactual(secuCode, happen_dt)
            # print(happen_dt, '\n', secuCode, '\n', fiveday_rateinfo)
            if fiveday_rateinfo == list() or len(fiveday_rateinfo) != 5:
                print(f"{secuCode} - {happen_dt} 5 日数据不足")
                continue
            winlist_onday.append(float(fiveday_rateinfo[0][1]))
            winlist_nextday.append(float(fiveday_rateinfo[1][1]))
            # secuCode_rate_info[secuCode]['fiveday_rateinfo'] = fiveday_rateinfo
            # (5) 计算单只证券的 次\3\5日 累计涨幅
            accumulated_rate2, accumulated_rate3, accumulated_rate5 = self.generate_changepercactual_index(
                fiveday_rateinfo)
            total_rate2 += accumulated_rate2
            total_rate3 += accumulated_rate3
            total_rate5 += accumulated_rate5
            total_rate += float(fiveday_rateinfo[0][1])
            # secuCode_rate_info[secuCode]['accumulated_rates'] = [accumulated_rate2, accumulated_rate3, accumulated_rate5]

        # (6) 计算当日胜率
        on_count = 0
        for rate in winlist_onday:
            if rate > 0:
                on_count += 1
        onday_winrate = on_count / len(winlist_onday)
        # (7) 计算次日胜率
        next_count = 0
        for rate in winlist_nextday:
            if rate > 0:
                next_count += 1
        nextday_winrate = next_count / len(winlist_nextday)
        # (8) 计算平均涨幅
        average_rate = total_rate / event_count
        average_rate2 = total_rate2 / event_count
        average_rate3 = total_rate3 / event_count
        average_rate5 = total_rate5 / event_count

        record['EventDayChgPerc'] = average_rate
        record['NextDayChgPerc'] = average_rate2
        record['ThreeDayChgPerc'] = average_rate3
        record['FiveDayChgPerc'] = average_rate5
        record['EventDayWinRatio'] = onday_winrate
        record['NextDayWinRatio'] = nextday_winrate
        print(pprint.pformat(record))
        if record is not None:
            self.save_record(record)
        return record

    def save_record(self, record):
        yq_conn = self.make_sql_conn(self.yq_cfg)
        yq_cursor = yq_conn.cursor()
        sql = '''update {} set EventDayChgPerc={}, NextDayChgPerc={}, ThreeDayChgPerc={}, FiveDayChgPerc={}, EventDayWinRatio={},  NextDayWinRatio={} where EventCode = '{}'; '''.format(
            self.target_table_name,
            record.get("EventDayChgPerc"), record.get('NextDayChgPerc'), record.get('ThreeDayChgPerc'),
            record.get("FiveDayChgPerc"), record.get("EventDayWinRatio"), record.get("NextDayWinRatio"),
            record.get("EventCode"),
        )
        print(sql)
        try:
            yq_cursor.execute(sql)
            yq_conn.commit()
        except:
            print("error: ", sql)
            traceback.print_exc()
            yq_conn.rollback()
        yq_cursor.close()
        yq_conn.close()

    def launch(self):
        self.innercode_map_init()
        # (1) 获取事件列表
        eventcode_lst = sorted(self.const_event_codes())    # 57
        print(len(eventcode_lst))

        # (2) 遍历 (多进程)
        pool = multiprocessing.Pool(processes=8)
        result = []
        for eventcode in eventcode_lst:
            result.append(pool.apply_async(self.process_single_eventcode, (eventcode, )))
        pool.close()
        pool.join()

        # for res in result:
        #     record = res.get()
        #     if record is not None:
        #         self.save_record(record)


if __name__ == '__main__':
    restart_run = int(os.environ.get("RUN", 0))

    def task():
        start_time = time.time()
        final3 = FinalConstAnn()
        final3.launch()
        print(f"用时: {time.time() - start_time}")

    if restart_run:
        task()

    schedule.every().day.at("15:02").do(task)

    while True:
        schedule.run_pending()
        time.sleep(20)
