from requests import get
from bs4 import BeautifulSoup

def __extract_wwr_jobs(keyword) :

    base_url = "https://weworkremotely.com/remote-jobs/search?term="

    search_term = keyword

    response = get(f"{base_url}{search_term}")

    if response.status_code != 200:
        print("Can't response website")
    else :
        results = []
        # print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('section', class_='jobs')
        for job_section in jobs :
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)
            for post in job_posts :
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                '''
                list_of_numbers = [1,2,3]
                first,second,third = list_of_numbers
                '''
                # company, kind, region = anchor.find_all('span', class_ = 'company')

                if len(anchor.find_all('span', class_ = 'company')) == 3 :
                    company, kind, region = anchor.find_all('span', class_ = 'company')
                else :
                    company, kind = anchor.find_all('span', class_ = 'company')
                    region = anchor.find_all('span', class_ = 'region')
                
                if company == None :
                    company = ""
                if kind == None :
                    kind = ""
                if region == None :
                    region = ""

                title = anchor.find('span', class_='title')

                # print(company.string, kind.string, region.string, title.string, link)
                # print('-----------------------------------------------------------')

                job_data = {
                    'link' : f"https://weworkremotely.com{link}",
                    'company' : company.string.replace(",","") if len(company) != 0 else "",
                    'location' : region.string.replace(",","") if len(region) != 0 else "",
                    'position' : title.string.replace(",","") if len(title) != 0 else ""
                }

                results.append(job_data)
        
        return results