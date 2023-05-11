import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


x = input('Enter your Email:')
y = input('Enter your Password:')
# initiate undetected-chromedriver
options = uc.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = uc.Chrome(options=options)

driver.maximize_window()
driver.get("https://login.live.com/oauth20_authorize.srf?client_id=1f907974-e22b-4810-a9de-d9647380c97e&scope=xboxlive.signin+openid+profile+offline_access&redirect_uri=https%3a%2f%2fwww.xbox.com%2fauth%2fmsa%3faction%3dloggedIn%26locale_hint%3den-US&response_type=code&state=eyJpZCI6ImMxMTNjNmNiLTVjODgtNGM0OS1hZTlhLWIzY2RlMzgyMTc1OSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3d%7chttps%253A%252F%252Fwww.xbox.com%252Fen-US%252Flive&response_mode=fragment&nonce=fcf3614d-9a81-4412-bb56-ded2c65ccc81&prompt=login&code_challenge=AH9car5TUFNPI9zzYswvO3inlJ_9yOq3TXHm7Egxomk&code_challenge_method=S256&x-client-SKU=msal.js.browser&x-client-Ver=2.32.2&uaid=cdd2e75f72b4422db1227cb39044cc8c&msproxy=1&issuer=mso&tenant=consumers&ui_locales=en-US&client_info=1&epct=PAQABAAEAAAD--DLA3VO7QrddgJg7WevrJcdE7qFr0uBY3MNQlkLvos74CxDYYegZxi6tZgXDR1tfU2pC_mUa7Wjj3AsifezK3TzSyXlxcpWYLm5KKr55FCfk11-61hQFRSk4AAW5shq7UmMBI5nLjExEnyWTh-e05O3LPwJZTnAtG2AJ65-yxf0W8zhQhOBIl-c3xes5j1Nnr9OdVpDmNx9-Qpn2yYDu7_BcbcTjqv3VaDMtR9gELCAA&jshs=0#")
sleep(2)
wait = WebDriverWait(driver, 30)


username = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#i0116')))
username.send_keys(x)
next = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="idSIButton9"]')))
next.click()
try:
    wait3 = WebDriverWait(driver, 5)
    otherways = wait3.until(EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]')))
    otherways.click()
    passwordway = wait3.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#credentialList > div:nth-child(2) > div > div > div.table-cell.text-left.content')))
    passwordway.click()
except:
    pass
wait2 = WebDriverWait(driver, 30)

password = wait2.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#i0118')))
password.send_keys(y)
signin = wait2.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="idSIButton9"]')))
signin.click()
try:
    staysignin = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input')))
    staysignin.click()
except:
    pass


# logged in

workbook = openpyxl.load_workbook('Book.xlsx')
worksheet = workbook['Sheet1']
count1 = 1
for row in worksheet.iter_rows(min_row=1, values_only=True):
    # Get the value of the first cell (assuming it's a link)
    link = row[0]
    
# driver.execute_script("window.location.href = '{}';".format(link))
    driver.get(link)
    
    waitfriend = WebDriverWait(driver, 40)

    friend_count = waitfriend.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app/core-page/div/section[1]/core-area/core-region/div/div/rendermodule/div/xbox-xboxsummary/div/div[2]/item-value-collection/div/item-value[2]/div/div[2]")))

    friend_count_text = friend_count.text
    friend_count_text = friend_count_text.replace(',', '') # remove comma
    f = int(friend_count_text)
    print(f)
    if(f>1000):
        f=1000
    driver.execute_script("window.scrollBy(0, 400);")
    sleep(1)
    try:
        waitbutton = WebDriverWait(driver, 40)
        friendsButton = waitbutton.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app/core-page/div/section[1]/core-area/core-region-pivot/section/section/header/a[3]")))
    #if "Friends" in friendsButton.text:

        friendsButton.click()
        sleep(4)

        # Initialize an empty list to store friend names
        friend_names = []

        # Loop through each friend on the page
        for i in range(1,f+1):  
            #print(f"Loop iteration {i}")
            # Construct the XPath for the friend's name using the index i
            xpath = f"/html/body/app/core-page/div/section[1]/core-area/core-region-pivot/section/section/section[3]/div/div/rendermodule/div/xbox-friends/div/div/xbox-friend-entity/div/ul/li[{i}]/div/xbox-people/div/a/xbox-profiletext/div/div[1]/span[1]"
            
            # Find the friend's name element using the XPath and extract its text
            try:
                wait5 = WebDriverWait(driver, 50)

                friend_name_element =wait5.until(EC.element_to_be_clickable((By.XPATH,xpath)))
                friend_name = friend_name_element.text
                
                # Add the friend's name to the list
                friend_names.append(friend_name)
            except:
                break
        # Print the list of friend names
        print(friend_names)

        with open("output.txt", "a") as f:
            
            f.write(f"-------Link of profile#{count1}: {link}-------\n")
            count1 += 1
            f.write(f"-------Friend Names:-------\n")
            count = 1
            for friend_name in friend_names:
                f.write(f"{count}. {friend_name}\n")
                count += 1
            f.write("\n\n\n")

        sleep(4)
    except:
        pass
sleep(50)
    



    