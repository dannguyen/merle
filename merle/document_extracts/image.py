from collectinos import OrderedDict
SELECTORS = OrderedDict()
SELECTORS['og'] = """head/meta[@property="og:image"]/@content"""
SELECTORS['twitter'] = """head/meta[@property="twitter:image"]/@content"""
SELECTORS['itemprop'] = """head/meta[@itemprop="image"]/@content"""
