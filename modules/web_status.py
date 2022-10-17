from requests import get

def __web_status(websites) :

    websites = websites

    results = {}

    for website in websites :
        if not website.startswith("https://") :
            website = f"https://{website}"
        respose = get(website)
        
        if respose.status_code == 200:
            results[website] = "OK"
            #print(f"{website} is ok")
        else :
            results[website] = "FAILED"
            #print(f"{website} not ok")
    return results

'''
return_web_status = web_status(["naver.com"])
print(return_web_status)
'''