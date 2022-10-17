from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def __extract_wanted_jobs(keyword) :

    base_url = "https://www.wanted.co.kr/search?query="

    search_term = keyword

    browser = webdriver.Chrome()
    browser.get(f"{base_url}{search_term}")
    # response = get(f"{base_url}{search_term}")

    results = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    browser.close()
    
    jobs = soup.find_all('div', class_='List_List_container__JnQMS')
    
    for job_section in jobs :
        job_posts = job_section.find_all('li')
        for post in job_posts :
            anchors = post.find_all('a')
            anchor = anchors[0]
            link = anchor['href']
            company = anchor['data-company-name']
            position = anchor['data-position-name']
            location = anchor.find("div",class_="job-card-company-location")
               
                
            # print(company.string, kind.string, region.string, title.string, link)
            # print('-----------------------------------------------------------')

            job_data = {
                'link' : f"https://www.wanted.co.kr/{link}",
                'company' : company.string.replace(",","") if len(company) != 0 else "",
                'location' : location.string.replace(",","") if location.string != None else "" ,
                'position' : position.string.replace(",","") if len(position) != 0 else ""
            }

            results.append(job_data)
        
    print(results)

__extract_wanted_jobs('CF')
