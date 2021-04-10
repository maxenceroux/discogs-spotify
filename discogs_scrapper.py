from selenium import webdriver
import time

query = "rone tohu bohu"
driver = webdriver.Chrome("./chromedriver")
query = [x for x in query.split(" ") if x != "&"]
url = f'https://www.discogs.com/search/?q={"+".join(query)}&type=all'
print(url)
driver.get(url)

privacy_button = driver.find_elements_by_id("onetrust-accept-btn-handler")
privacy_button[0].click()
all_results_div = driver.find_element_by_id("search_results")
results_query = all_results_div.find_elements_by_class_name("card_large")
results_query[0].click()
time.sleep(2)
try:
    driver.find_elements_by_class_name("blue_2acgV")[0].click()
except:
    pass
try:
    driver.find_elements_by_class_name("button-blue")[0].click()
except:
    pass

time.sleep(1)
try:
    if driver.find_elements_by_class_name("pagination_next")[0]:
        next_page = True
except:
    next_page = False
print(next_page)
sell_results = driver.find_element_by_id("pjax_container")
prices = sell_results.find_elements_by_class_name("converted_price")
for i in prices:
    print(i.text[i.text.find("€") + 1 :].split(" ")[0])
while next_page:
    driver.find_elements_by_class_name("pagination_next")[0].click()
    time.sleep(1.5)
    sell_results = driver.find_element_by_id("pjax_container")
    prices = sell_results.find_elements_by_class_name("converted_price")
    for i in prices:
        print(i.text[i.text.find("€") + 1 :].split(" ")[0])
    try:
        if driver.find_elements_by_class_name("pagination_next")[0]:
            next_page = True
    except:
        next_page = False
