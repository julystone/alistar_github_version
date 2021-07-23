from json_beautify import json_beautify
import uiautomator2 as u2


def loc_info_diff(d1, d2):
    diff_keys = d1.keys() & d2
    diff_values = [{k: [d1[k], d2[k]]} for k in diff_keys if d1[k] != d2[k]]
    return json_beautify(diff_values)


if __name__ == '__main__':
    d = u2.connect()
    elem1 = d(resourceId="esunny.test:id/es_item_cloud_conditional_order_tv_contract_no", text="纯碱112")
    elem2 = d(resourceId="esunny.test:id/es_item_cloud_conditional_order_tv_contract_no", text="纯碱201")
    dict1 = elem1.info
    dict2 = elem2.info
    loc_info_diff(dict1, dict2)
