import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

comments = []
def get_links(topic):
    execute_path = r"{}".format(os.path.dirname(os.path.abspath(__file__)) + '\chromedriver.exe')
    service = Service(executable_path=execute_path)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--mute-audio')
    driver = webdriver.Chrome(service=service, options=options)
    topic_words = topic.split()
    search_url = "https://www.youtube.com/results?search_query="

    if(len(topic_words) == 1):
        search_url = search_url + topic
    else:
        for words in topic_words:
            search_url = search_url + "+" + words
    
    driver.get(search_url)
    time.sleep(3)
    links = driver.find_elements(By.XPATH, "//a[@id='video-title']")

    cleaned_links = []

    for link in links:
        cleaned_links.append(link.get_attribute('href'))
    
    cleaned_links = [element for element in cleaned_links if element != "https://www.youtube.com/"]
    cleaned_links = [element for element in cleaned_links if element != None] 
    cleaned_links = [element for element in cleaned_links if "@" not in element]
    cleaned_links = [element for element in cleaned_links if "shorts" not in element]
    cleaned_links = list(set(cleaned_links))
    
    return(cleaned_links)

def get_comments(links):
    execute_path = r"{}".format(os.path.dirname(os.path.abspath(__file__)) + '\chromedriver.exe')
    service = Service(executable_path=execute_path)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--mute-audio')
    
    driver = webdriver.Chrome(service=service, options=options)

    wait = WebDriverWait(driver, 1)

    data = []
    for link in links:
        driver.get(link)
        if(links.index(link) == 6):
            break
        for item in range(10): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(0.5)

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
            comments.append(comment.text)

    driver.close()
    driver.quit()

def return_comments():
    return comments
