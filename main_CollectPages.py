from selenium import webdriver
import time

driver = webdriver.Firefox()

##Every week check how many pages the site has and update i
#week number
#j=1, (May 27)
#j=2, (May 30)
#j=3  (June 6)
#j=4  (June 24)
#j=5 (July 3)
#j=6(July 11)
#j=7 (july 28)
#j=8(august 10)
j=9

##############fashionphile############

for i in range(0, 47): #number of total pages=i
    url = "https://www.fashionphile.com/shop/categories/handbag-styles?pageSize=180&sort=date-desc&page=" + str(i + 1)

    driver.get(url)
    html = driver.page_source
    time.sleep(10)

    file = open("week" + str(j)+ "_fashionphile_page" + str(i+1) + ".txt", "w", encoding='utf-8')
    file.write(html)
    file.close()
    print(i)


############Rebag####################

for i in range(0, 165): #number of total pages=i

    url = "https://shop.rebag.com/collections/all-bags?page="+ str(i + 1)

    driver.get(url)
    html = driver.page_source
    time.sleep(10)

    file = open("week" + str(j)+ "_rebag_page" + str(i+1) + ".txt", "w", encoding='utf-8')
    file.write(html)
    file.close()
    print(i)


##########Luxury GarageSale###########

for i in range(0, 9): #number of total pages=i

    url = "https://luxurygaragesale.com/women/bags?page="+ str(i + 1)

    driver.get(url)
    html = driver.page_source
    time.sleep(10)

    file = open("week" + str(j)+ "_luxurygaragesale_page" + str(i+1) + ".txt", "w", encoding='utf-8')
    file.write(html)
    file.close()
    print(i)



##########StockX###########

for i in range(0, 24): #number of total pages=i

    url = "https://stockx.com/handbags?page="+ str(i + 1)

    driver.get(url)
    html = driver.page_source
    time.sleep(10)

    file = open("week" + str(j)+ "_StockX_page" + str(i+1) + ".txt", "w", encoding='utf-8')
    file.write(html)
    file.close()
    print(i)



##########The Outnet###########

for i in range(0, 7): #number of total pages=i

    url = "https://www.theoutnet.com/en-us/shop/bags?pageNumber="+ str(i + 1)

    driver.get(url)
    html = driver.page_source
    time.sleep(10)

    file = open("week" + str(j)+ "_Theoutnet_page" + str(i+1) + ".txt", "w", encoding='utf-8')
    file.write(html)
    file.close()
    print(i)



##########The Luxury Closet###########
###This time Just go up to a couple of pages of sold########

for i in range(0, 1541): #number of total pages=i

    url = "https://theluxurycloset.com/women/womens-handbags?category_level_one_ids=women&category_level_two_ids=womens-handbags&initial_params=category_level_one_ids%3Dwomen%23category_level_two_ids%3Dwomens-handbags&page="+ str(i + 1)

    driver.get(url)
    html = driver.page_source
    time.sleep(10)

    file = open("week" + str(j)+ "_Theluxurycloset_page" + str(i+1) + ".txt", "w", encoding='utf-8')
    file.write(html)
    file.close()
    print(i)



##########The RealReal###########

for i in range(0, 16): #number of total pages=i

    url = "https://www.therealreal.com/shop/women/handbags?after=YXJyYXljb25uZWN0aW9uOjExOQ%3D%3D&first=120&page="+ str(i + 1)

    driver.get(url)
    html = driver.page_source
    time.sleep(10)

    file = open("week" + str(j)+ "_Therealreal_page" + str(i+1) + ".txt", "w", encoding='utf-8')
    file.write(html)
    file.close()
    print(i)

####################################
    
driver.close()

