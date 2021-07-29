from src.test.scripts.page.rightToolBar._SettingBasePage import SettingBasePage


class CloudServicePage(SettingBasePage):
    # 详细信息
    pass_modify = ("resourceId", "esunny.test:id/es_activity_cloud_tv_modify_password")
    data_clear = ("resourceId", "esunny.test:id/es_activity_cloud_tv_clear_data")
    logout_btn = ("resourceId", "esunny.test:id/es_activity_cloud_tv_log_out")
    favorite_to_cloud = ("resourceId", "esunny.test:id/es_activity_cloud_rl_sync_favorite_to_cloud")
    favorite_from_cloud = ("resourceId", "esunny.test:id/es_activity_cloud_rl_sync_favorite_from_cloud")
    computer_fav = ("resourceId", "esunny.test:id/es_activity_cloud_rl_sync_pc_from_cloud")
    setting_to_cloud = ("resourceId", "esunny.test:id/es_activity_cloud_rl_sync_setting_to_cloud")
    setting_from_cloud = ("resourceId", "esunny.test:id/es_activity_cloud_rl_sync_setting_from_cloud")
    # 校验项
    title_text = '云端服务'

    def logOut(self):
        return self.click(self.logout_btn)


if __name__ == '__main__':
    debugPage = CloudServicePage()
    debugPage.logOut()
