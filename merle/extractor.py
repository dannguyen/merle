from collections import OrderedDict
from importlib import import_module

def extract_element_from_doc(element_name, doc):
    selectors = get_selectors_by_name(element_name)
    candidates = OrderedDict()
    for key, sel in selectors.items():
        selstring = "//%s" % sel
        selval = doc.xpath(selstring)
        if selval and selval[0]:
            candidates[key] = str(selval[0])
    return candidates


def extract_element(element_name, resource): # to be deprecated...?    
    return extract_element_from_doc(resource.doc)



def get_selectors_by_name(element_name):
    return import_module('document_extracts.{0}'.format(element_name)).SELECTORS
