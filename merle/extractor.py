from collections import OrderedDict
from importlib import import_module

def extract_element(element_name, resource):
    selectors = get_selectors_by_name(element_name)
    el_html = resource.doc
    candidates = OrderedDict()
    for key, sel in selectors.items():
        selstring = "//%s" % sel
        selval = el_html.xpath(selstring)
        if selval and selval[0]:
            candidates[key] = str(selval[0])
    return candidates


def get_selectors_by_name(element_name):
    return import_module('document_extracts.{0}'.format(element_name)).SELECTORS
