from modules.extractors.wwr import __extract_wwr_jobs
from modules.extractors.indeed import __extract_indeed_jobs

keyword = input(f"What do you want to search for??")

indeed = __extract_indeed_jobs(keyword)
wwr = __extract_wwr_jobs(keyword)

jobs = indeed + wwr

file = open(f"{keyword}.csv","w")

file.write("Postion,Company,Location,URL\n")

for job in jobs :
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()


