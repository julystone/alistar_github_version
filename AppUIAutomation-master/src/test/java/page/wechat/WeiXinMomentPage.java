package page.wechat;

import framework.BasePage;
import framework.Driver;
import framework.Util;
import io.appium.java_client.MobileElement;

//朋友圈的Page类
public class WeiXinMomentPage extends BasePage {

    //能过静态方法返回页面实例
    public static WeiXinMomentPage verify(){
        if( !Util.isAndroid() ) {
            //默认情况下写的Page类是Android的UI
            //若Android与iOS UI上有差异，需继承Android的Page类再写个iOS Page
            return new WeiXinMomentPageiOS();
        }

        return new WeiXinMomentPage();
    }

    //不允许调用构造函数,构造函数会对页面的关键元素做检查，确保当前页面是期望的页面
    protected WeiXinMomentPage(){
        Driver.findElementByText(getRes("MOMENT_PAGE_ME_TEXT"));
    }

    //所有成员函数只返回this或void,确保每个Page类的独立性，不依赖于任何其它Page类
    public WeiXinMomentPage scroll(){
        Driver.scrollUp();

        return this;
    }

    public WeiXinMomentPage clickMyMoment(){
        //查找带图片的朋友圈
        MobileElement elem = Driver.findElemByIdWithoutException (getRes("MY_POST_PAGE_MOMENT_PIC_ID"));

        if(elem == null){
            //如果没有带图片的朋友全，则查找"转发"类的朋友圈
            elem = Driver.findElementById(getRes("MY_POST_PAGE_MOMENT_ARTICLE_ID"));
        }

        elem.click();

        return this;
    }
}
