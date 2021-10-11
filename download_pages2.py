from selenium import webdriver 
import clipboard 
import time , json

driver = webdriver.Chrome("D:\chromedriver.exe")
def wait(second):
    for i in range(second):
        time.sleep(1)
        print(f'Waiting {second-i}')

driver.get("https://www.mediafire.com/login/")
email_elem = driver.find_element_by_css_selector('#widget_login_email')
pass_elem = driver.find_element_by_css_selector('#widget_login_pass')
email_elem.send_keys("vpq33855@zwoho.com")
pass_elem.send_keys("storage")
pass_elem.submit()
input("Page Loaded?")

with open("json/chapters.json", 'r') as f:
    chapters = json.loads(f.read())

for chapter, link in chapters.items():
    all_chapters = link 

    driver.get(all_chapters)

    input('Page loaded?')

    chapters_list = {}

    cpyBtns = driver.find_elements_by_css_selector('button[title="Copy share link"]')
    for cpyBtn in cpyBtns:
        cpyBtn.click()
        link = clipboard.paste()
        wait(5)

        parent_div = cpyBtn.find_element_by_xpath('../..')
        childern = parent_div.find_elements_by_xpath('*')
        child = childern[2].find_element_by_css_selector('button')
        chapter= child.get_attribute('title')
        print(chapter, link)
        chapters_list[chapter[9:]] = link    


    with open(f'json/{chapter}.json', 'w') as f:
        f.write(json.dumps(chapters_list))







