from selenium import webdriver 
import clipboard 
import time , json

driver = webdriver.Chrome("D:\chromedriver.exe")
def wait(second):
    for i in range(second):
        time.sleep(1)
        print(f'Waiting {second-i}')

def convert(x):
    x = x.split(' ')[0]
    if x.endswith('.'):
        return float(x[:-1])
    else:
        return float(x)

def sort_dict(data):
    data = dict(sorted(data.items(), key=lambda x: x[1]['slno']))

    for key, value in data.items():
        value['videos'] = dict(sorted(value['videos'].items(), key=lambda x: x[1]['slno']))
    
    return data 

driver.get("https://www.mediafire.com/login/")
email_elem = driver.find_element_by_css_selector('#widget_login_email')
pass_elem = driver.find_element_by_css_selector('#widget_login_pass')
email = input('Enter email: ')
password = input('Enter password: ')
email_elem.send_keys(email)
pass_elem.send_keys(password)
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
    # wait(5)
    parent_div = cpyBtn.find_element_by_xpath('../..')
    childern = parent_div.find_elements_by_xpath('*')
    child = childern[2].find_element_by_css_selector('button')
    chapter= child.get_attribute('title')
    print(chapter, link)
    slno = convert(chapter[6:])
    chapters_list[chapter[6:]] = { 'link': link, 'slno': slno }    


for chapter, link in chapters_list.items():
    all_chapters = link['link']

    driver.get(all_chapters)

    input('Page loaded?')

    videos_list = {}

    cpyBtns = driver.find_elements_by_css_selector('button[title="Copy share link"]')
    for cpyBtn in cpyBtns:
        cpyBtn.click()
        link = clipboard.paste()
        wait(5)

        parent_div = cpyBtn.find_element_by_xpath('../..')
        childern = parent_div.find_elements_by_xpath('*')
        child = childern[2].find_element_by_css_selector('button')
        video= child.get_attribute('title')
        print(video, link)
        videos_list[video[9:]] = { 'link': link, 'slno': convert(video[9:]) }


    chapters_list[chapter]['videos'] = videos_list

    with open(f'json/data.json', 'w') as f:
        f.write(json.dumps(chapters_list))


with open('json/data.json', 'r') as f:
    data = json.loads(f.read()) 
    with open('sorted.json', 'w') as f:
        f.write(json.dumps(sort_dict(data)))









