from collections import OrderedDict


SELECTORS = OrderedDict()
SELECTORS['og'] = """head/meta[@property="article:published_time"]/@content"""
SELECTORS['meta'] = """head/meta[@property="article:published"]/@content"""
SELECTORS['item_prop'] = """head/meta[@itemprop="datePublished"]/@content"""
SELECTORS['class:date'] = """body/*[contains(@class, "publish") and (contains(@class, "date") or contains(@class, "time"))]/text()"""
SELECTORS['tag:time'] = """body/time[0]/@content"""
SELECTORS['class:time'] = """body/*[contains(@class, "time") or contains(@class, "date")][0]/text()"""
