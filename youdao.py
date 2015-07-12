# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import requests
import sys

err_dict = {
    20: 'word is too long.',
    30: 'unable to translate.',
    40: 'language is not supported.',
    50: 'key is invalid.',
    60: 'no result found'
}

url_config_dict = {
    "keyfrom": "Susheng",
    "key": "187591385",
    "type": "data",
    "doctype": "json",
    "version": "1.1"
}


def youdao(query):
    url = "http://fanyi.youdao.com/openapi.do"
    url_config_dict["q"] = query
    res = requests.get(url, params=url_config_dict).json()
    if res["errorCode"] == 0:
        if res["basic"]:
            return res["basic"]["explains"]
        elif res["translation"]:
            return res["translation"]
    else:
        return [err_dict.get(res["errorCode"])]


def output(titlelist, icon):
    items = ET.Element("items")
    for title in titlelist:
        item = ET.SubElement(items, "item", valid="no")
        ET.SubElement(item, "title").text = title
    ET.SubElement(item, "icon").text = icon
    return ET.tostring(items, encoding='UTF-8', method='xml')

if __name__ == '__main__':
    print output(youdao(sys.argv[1]), "icon.png")
