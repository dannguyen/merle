from collections import OrderedDict

def extract_element(element_name, doc):
    selectors = get_selectors_by_name(element_name)
    el_html = doc['html']
    candidates = OrderedDict()
    for key, sel in selectors.items():
        selstring = "//%s" % sel
        selval = el_html.xpath(selstring)
        if selval and selval[0]:
            candidates[key] = str(selval[0])
    return candidates


def get_selectors_by_name():
    pass
