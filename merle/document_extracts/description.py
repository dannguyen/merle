from collections import OrderedDict

SELECTORS = OrderedDict()
SELECTORS['og'] = """head/meta[@property="og:description"]/@content"""
SELECTORS['twitter'] = """head/meta[@property="twitter:description"]/@content"""
SELECTORS['meta'] = """head/meta[@name="description"]/@content"""
SELECTORS['itemprop'] = """head/meta[@itemprop="description"]/@content"""
SELECTORS['first'] = """body/*[contains(@class, "description")][0]/text()"""
