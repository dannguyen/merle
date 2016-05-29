from collections import OrderedDict

SELECTORS = OrderedDict()
SELECTORS['og'] = """head/meta[@property="og:title"]/@content"""
SELECTORS['twitter'] = """head/meta[@property="twitter:title"]/@content"""
SELECTORS['itemprop'] = """head/meta[@itemprop="name"]/@content"""
SELECTORS['head'] = """head/title/text()"""
SELECTORS['h1#'] = """body/h1[contains(@id, "title")]/text()"""
SELECTORS['h1.'] = """body/h1[contains(@class, "title")]/text()"""
SELECTORS['first_h1'] = """body/h1[1]/text()"""
