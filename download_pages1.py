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

all_chapters = "https://app.mediafire.com/d8i7hnvbmxbwl"

driver.get(all_chapters)

input('Page loaded?')

chapters_list = {}

cpyBtns = driver.find_elements_by_css_selector('button[title="Copy share link"]')
for cpyBtn in cpyBtns:
    cpyBtn.click()
    link = clipboard.paste()

    parent_div = cpyBtn.find_element_by_xpath('../..')
    childern = parent_div.find_elements_by_xpath('*')
    child = childern[2].find_element_by_css_selector('button')
    chapter= child.get_attribute('title')
    print(chapter, link)
    chapters_list[chapter[6:]] = link    


with open('json/chapters.json', 'w') as f:
    f.write(json.dumps(chapters_list))


# for chapter, link, videos in chapters_list:
#     print(f"{chapter}\n{link}")
#     driver.get(link) 
#     input("Scroll the page...")
    
#     cpyBtns = driver.find_elements_by_css_selector('button[title="Copy share link"]')
#     for cpyBtn in cpyBtns:
#         cpyBtn.click()
#         video_link = clipboard.paste()

#         parent_div = cpyBtn.find_element_by_xpath('../..')
#         childern = parent_div.find_elements_by_xpath('*')
#         child = childern[2].find_element_by_css_selector('button')
#         video= child.get_attribute('title')
#         print(f"\t{video}\n\t{video_link}")
#         videos.append([video, video_link])






