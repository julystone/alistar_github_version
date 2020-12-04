 package framework;

import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.support.ui.FluentWait;

import java.time.Duration;

public class AppiumDriverWait extends FluentWait<AppiumDriver> {
    public static  AppiumDriverWait getInstance(AppiumDriver driver,int seconds){
        return new AppiumDriverWait(driver,seconds);
    }

    public AppiumDriverWait(AppiumDriver driver) {
        this(driver,ConfigUtil.getDefaultWaitSec(),ConfigUtil.getDefaultPollingIntervalSec());
    }

    public AppiumDriverWait(AppiumDriver driver, long timeOutInSeconds) {
        this(driver,timeOutInSeconds,ConfigUtil.getDefaultPollingIntervalSec());
    }

    public AppiumDriverWait(AppiumDriver driver, long timeOutInSeconds, long duration) {
        super(driver);
        withTimeout(Duration.ofSeconds(timeOutInSeconds));
        pollingEvery(Duration.ofSeconds(duration));
    }
}