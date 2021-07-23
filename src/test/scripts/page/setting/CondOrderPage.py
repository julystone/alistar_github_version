from src.test.scripts.page.setting.SettingBasePage import SettingBasePage


class CondOrderPage(SettingBasePage):
    # 详细信息
    contract_no = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_contract_no")
    status = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_status")
    type = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_type")
    condition_1 = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_condition")
    condition_2 = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_bonus")
    direction = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_direct")
    lots = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_qty")
    order_price = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_orderPrice")
    valid_type = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_validType")
    create_time = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_insertTime")
    delegate_type = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_delegate_type")
    feedback_info = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_feedback")
    hedge = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_hedge")
    # 点击工具栏
    kline = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_kline")
    order_modify = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_modify")
    order_suspend = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_suspend")
    order_cancel = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_tv_revoke")
    # 校验项
    title_text = "云条件单"

    def getOrderInfo(self, contractNo):
        order_list = ("resourceId", "esunny.test:id/es_item_cloud_conditional_order_ll_main")
        elem = self.findElement(order_list).child_by_text(contractNo)
        elem2 = self.findElement(order_list)
        return elem


if __name__ == '__main__':
    debugPage = CondOrderPage()
    print(debugPage.getOrderInfo('纯碱201'))
