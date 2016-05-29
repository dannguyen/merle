from collections import OrderedDict
SELECTORS = OrderedDict()
SELECTORS['head'] = """link[@rel="canonical"]/@href"""
SELECTORS['og'] = """meta[@property="og:url"]/@content"""
SELECTORS['twitter'] = """meta[@property="twitter:url"]/@content"""
