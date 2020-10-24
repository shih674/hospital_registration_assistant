# 掛號程式

# 使用套件
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import json

# 從txt讀取參數
print(f'你好 感謝您使用輔助掛號程式')
print(f'chrome driver version 86')
print(f'現在正為您載入使用者資訊')
try:
    with open('patient_info.txt', 'r', encoding='utf8') as f:
        content = json.load(f)
except:
    print(':: Error msg :: 找不到使用者資訊檔，請先執行info_manager')

day_of_doctor = '20200203' #輸入看診日 YYYYMMDD
click_hour = '00'
click_minute = '00'

IDNO = content["id_number"]
BDYear = content["BDYear"]
BDMonth = int(content["BDMonth"]) - 1
BDDay = int(content["BDDay"]) - 1
print('='*30)
print("身份證字號為:", IDNO)
print("出生日期為:", BDYear, '年', BDMonth, '月', BDDay, '日')
print("我將用以上資料替您掛號")
print('='*30, '\n')

# 使用者輸入掛號日期
control_key = True
while control_key == True:
    day_of_doctor = str(input('輸入預約西元年月日 YYYYMMDD (8位數,eg 20200111)'))
    if len(day_of_doctor) != 8:
        print('只接受八位數字')
    else:
        isNumber_key = True
        for i in day_of_doctor:
            number_lib = ['1','2','3','4','5','6','7','8','9','0']
            k = i in number_lib
            if k == False:
                print(i,'為非法輸入')
                isNumber_key = False
        if isNumber_key == True:
            print('檢查合格')
            control_key = False
control_key = True
while control_key == True:
    click_time = str(input('輸入確認鍵按下24小時制時間 HHMM (4位數,eg 0606)\n\t>>'))
    if len(click_time) != 4:
        print('只接受四位數字')
    else:
        isNumber_key = True
        for i in click_time:
            number_lib = ['1','2','3','4','5','6','7','8','9','0']
            k = i in number_lib
            if k == False:
                print(i,'為非法輸入')
                isNumber_key = False
        if isNumber_key == True:
            print('檢查合格')
            control_key = False
click_hour = click_time[0] + click_time[1]
click_minute = click_time[2] + click_time[3] 
print('click_hour ',click_hour)
print('click_minute ',click_minute)

#是否帶入預設資料 1是 0否
control_key = True
while control_key == True:
    oldData = str(input('是否帶入預設病患資料: 1是 0否\n\t>>'))
    if len(oldData) != 1:
        print('輸入 1 或 0')
    else:
        isNumber_key = True
        for i in oldData:
            number_lib = ['1', '0']
            k = i in number_lib
            if k == False:
                print(i,'為非法輸入')
                isNumber_key = False
        if isNumber_key == True:
            print('檢查合格')
            control_key = False
if oldData == '0':
    print('目前未開放自行輸入資料')

src = 'http://register.vghtc.gov.tw/register/listDoctor.jsp?init=sub&section=CV#何鴻鋆醫師'
WebDriver = webdriver.Chrome('.\chromedriver')  # chrome套件
WebDriver.get(src)  # 透過chrome開啟網頁

# 開啟掛號頁面
for i in range(11):
    print(f'剩下 {10-i} 秒')
    time.sleep(1)
css_selector_target = 'a[href="javascript:document.T'+day_of_doctor+'A2322.submit();"]'
WebDriver.find_element_by_css_selector(css_selector_target).click()

#自動帶入資料
name_input = WebDriver.find_element_by_name('patientID')
name_input.send_keys(IDNO)
#ID_input = WebDriver.find_element_by_name('passportNo')
#ID_input.send_keys(IDNO)
BDYear_input = WebDriver.find_element_by_name('patientBirthYear')
BDYear_input.send_keys(BDYear)
BDMonth_input = Select(WebDriver.find_element_by_name('patientBirthMonth'))
BDMonth_input.select_by_index(BDMonth)
BDMonth_input = Select(WebDriver.find_element_by_name('patientBirthDate'))
BDMonth_input.select_by_index(BDDay)

# 開始計時器環節
hour = time.strftime('%H', time.localtime())
minutes = time.strftime('%M', time.localtime())
sec = time.strftime('%S', time.localtime())
print(hour, '-', minutes, '-', sec)
while True:
    hour = time.strftime('%H', time.localtime())
    minutes = time.strftime('%M', time.localtime())
    sec = time.strftime('%S', time.localtime())
    # 當現在時間超過啟動時間，則啟動
    if hour == click_hour and minutes >= click_minute:
        print(hour, '-', minutes, '-', sec)
        break
    else:
        print('現在時間:', hour, '點  ', minutes, '分  ',sec, '秒')
        time.sleep(60)
        
WebDriver.find_element_by_id("Submit").click()

print('完成')
