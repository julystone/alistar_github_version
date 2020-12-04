package page.wechat;

import framework.BasePage;
import framework.Driver;
import io.appium.java_client.MobileElement;


import java.util.Random;

public class WeiXinArticlePage extends BasePage {

    private MobileElement adText;

    public static WeiXinArticlePage verify(){
        return new WeiXinArticlePage();
    }

    protected WeiXinArticlePage(){
        Driver.findElementByTextWithoutScroll(getRes("ARTICLE_PAGE_AD_TEXT"));
    }

    public void clickAD(){
        int x = Driver.getDeviceWidth() / 2;
        int y = Driver.getDeviceHeight() / 2;

        Driver.sleep(5);

        //在文章界面 下划两次， 休眠时间随机
        for(int i = 0 ;i < 3; i++) {
            Driver.scrollUp(x,y,y-10);
        }

        Driver.sleep(new Random().nextInt(5) + 5);

        adText = Driver.findElementByText(getRes("ARTICLE_PAGE_AD_TEXT"));

        //广告位置约为 "广告"字底部 + 100
        y = adText.getLocation().y + adText.getRect().getHeight() + 100;

        log.info("Trying to click AD");
        Driver.clickByCoordinate(x,y);
    }
}
