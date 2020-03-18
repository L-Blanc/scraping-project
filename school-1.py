import time
import csv
import requests
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\Users\flowe\Documents\python\env\scraping\chromedriver')

driver.get("https://www.niche.com/k12/search/best-public-schools/s/florida/")

    #open the csvfile
csvfile = open('schools.csv', "w", newline="", encoding='utf-8')
#     #make python writer object
c = csv.writer(csvfile)
#     #write each row to csvfile
c.writerow(["school_name", "district_or_city", "total_count_of_students", "student_teacher_ratio", "niche_grade"])

page = driver.page_source
soup = BeautifulSoup(page, "html.parser")
list_of_schools = soup.find_all("div", class_="search-result")

def scrape_one_school(soup):
    list_of_schools = soup.find_all("div", class_="search-result")
    for item in list_of_schools:
        total_scope=0
        public_school = item.find("div", class_="search-result")
        school_names = item.find('h2', class_="search-result__title").get_text()
        try:
            niche_grade = item.find("figure").find("div").get_text()
        except:
            pass
        district_or_city = item.find("li", class_="search-result-tagline__item").get_text()
        student_count = item.find_all('span', class_="search-result-fact__value")

        student_teacher_ratio = student_count[0].get_text()
        total_count = student_count[1].get_text()

        school_details = [school_names, district_or_city, student_teacher_ratio, total_count, niche_grade]

        c.writerow(school_details)

        for i in school_details:
            try:
             print(i)
             print()
            except:
                pass
            s = randint(1, 11)
                # sleep that number of seconds
            time.sleep(s)

def scrape(soup):
    for n in range(1):
        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        scrape_one_school(soup)
        try:
            driver.find_element_by_css_selector('.icon-arrowright-thin--pagination').click()
            driver.find_element_by_css_selector('.cookie-banner').click()
        except:
            pass
        s = randint(1, 11)
        time.sleep(s)

scrape(soup)
driver.quit()
#for name in school_names:
#    print(name.get_text())

#for ratio in student_teacher_ratio:
    #    print(ratio.get_text())

#for grade in niche_grade:
    #print(grade.get_text())

#for district in district_or_city:
    #print(district.get_text())

#def get_single_url(school_url):
#    page = requests.get(my_url)
    #soup = BeautifulSoup(page.text, "html.parser")
    #school_urls = []
#my_url = "https://www.niche.com/k12/search/best-public-schools/s/florida/"

    #list_of_schools = soup.find('div', class_="search-results")
    #school_links = list_of_schools.find_all("div", class_="card")
    #rows = school_links.find_all('li')


#get_single_url(my_url)
    #for row in rows:
    #    cells = row.find_all('a')
    #    try:
        #    links = cells[0].a.attrs['href']
        #    teacher_urls.append(links)
        #except:
        #    pass

    #    return teacher_urls

#url_list = get_single_url(my_url)
#

#driver.quit()
# niche_grade = item.find("div",class_="niche__grade--small--a").get_text()
# niche_grade = item.find("div",class_="niche__grade--small--a-minus").get_text()
# niche_grade = item.find("div",class_="niche__grade--small--b").get_text()
# niche_grade = item.find("div",class_="niche__grade--small--b-plus").get_text()
# niche_grade = item.find("div",class_="niche__grade--small--b-minus").get_text()
# niche_grade = item.find("div",class_="niche__grade--small--c").get_text()
# niche_grade = item.find("div",class_="niche__grade--small--c-plus").get_text()
# niche_grade = item.find("div",class_="niche__grade--small--c-minus").get_text()
# niche_grade = item.find("div",class_="niche__grade--small--d").get_text()
# niche_grade = item.find("div",class_="niche__grade--small--d-plus").get_text()
# niche_grade = item.find("div",class_="niche__grade--small--d-minus").get_text()
# niche_grade = item.find("div",class_="niche__grade--small--ng").get_text()
