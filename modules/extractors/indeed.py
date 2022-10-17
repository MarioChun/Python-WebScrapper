from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def __get_page_count(keyword):
    base_URL = "https://kr.indeed.com/jobs?q="
    search_term = keyword

    browser = webdriver.Chrome()
    browser.get(f"{base_URL}{search_term}&limit=50")
 
    soup = BeautifulSoup(browser.page_source, "html.parser")

    navigation = soup.find("nav", role="navigation")

    if navigation == None :
        return 1
    
    pages = navigation.find_all("div",recursive=False)
    count = len(pages)

    if count >= 5 :
        #print(5)
        return 5
    else :
        #print(count)
        return count

def __extract_indeed_jobs(keyword) :

    pages = __get_page_count(keyword)

    results = []

    print(f"pages 카운트 : {pages}")

    for page in range(pages) :

        base_URL = "https://kr.indeed.com/jobs"
        search_term = keyword

        browser = webdriver.Chrome()
        browser.get(f"{base_URL}?q={search_term}&start={page*10}")

        print(f"url : {base_URL}?q={search_term}&start={page*10}")

        # if문으로 status 이상 유무 확인해야함

        soup = BeautifulSoup(browser.page_source, "html.parser")

        job_list = soup.find("ul", class_ = "jobsearch-ResultsList")

        jobs = job_list.find_all("li",recursive=False)

        for job in jobs :
            zone = job.find("div", class_= "mosaic-zone")

            if zone == None :
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span",class_="companyName")
                location = job.find("div",class_="companyLocation")

                job_data = {
                    'link' : f"https://kr.indeed.com{link}",
                    'company' : company.string.replace(",","") if company.string != None else "",
                    'location' : location.string.replace(",","") if location.string != None else "" ,
                    'position' : title.replace(",","")
                }

                results.append(job_data)

    return results

