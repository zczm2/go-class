from lib2to3.pgen2 import driver
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager  #因浏览器驱动不会跟随浏览器实时更新，此包保证浏览器驱动为最新
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

user=""
passwd=""

def go_clacee():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    driver.get("https://e.ecust.edu.cn/login/login")
    driver.implicitly_wait(0.5)
    driver.find_element(By.ID, "userName").send_keys(user)
    driver.find_element(By.ID, "passWord").send_keys(passwd)
    sleep(5)                                                    #5秒内手动输入验证码
    driver.find_element(By.CLASS_NAME,"loginBtn").click()
    driver.implicitly_wait(5)  
    driver.switch_to.frame("frame_content")                     #iframe嵌套，需要切换页面
    driver.find_element(By.PARTIAL_LINK_TEXT,"进入学习").click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])           #更换页面
    sleep(5)                                                    #手动点进一节没有学的课，进入播放页面
    while True:
        driver.switch_to.frame("iframe")                            #切换页面嵌套
        driver.implicitly_wait(0.5)
        driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='ext-gen1042']/iframe"))  #切换页面嵌套
        driver.find_element(By.XPATH,"//*[@id='video']/button").click()                        #点击播放 
        driver.implicitly_wait(0.5)

        for i in range(100):                                                                   #js前几次取不到值，循环检测视频总时长
            total_time = driver.find_element_by_xpath("//*[@id='video']/div[5]/div[4]/span[2]").text
            sleep(1)
            if total_time != "0:00":
                break
        total_time = (int(total_time.split(":")[0])*60)+int(total_time.split(":")[1])
        print(total_time)
        sleep(total_time)    
        driver.switch_to.default_content()                          #返回主页面嵌套
        driver.find_element(By.XPATH,'//*[@id="mainid"]/div[1]/div[2]').click()     #点击下一课
go_clacee()
