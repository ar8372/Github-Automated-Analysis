

try: 
    import requests 
    from bs4 import BeautifulSoup 
    import pandas as pd  
except Exception as e: 
    print("Some Modules are Missing {}".format(e))

def get_repo_csv(url):

    r  = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    d = soup.findAll('div', class_="d-inline-block mb-1")
    
    base_url = "https://github.com/"


    titles = []
    isForked = []
    repo_links = []

    for _,i in enumerate(d):
        for a in i.findAll('a'):
            newUrl = base_url + a["href"]
        t = " ".join(i.text.strip().split())
        # Public word should be there in the text t
        assert "Public" in t 
        title, rest = t.split("Public")
        if "Forked" in rest:
            isForked += [1] 
        else:
            isForked += [0]
        titles.append(title.strip())
        repo_links.append(newUrl)

        # print(_, "==>"," ".join(i.text.strip().split()), newUrl)
        # print()

    df1 = pd.DataFrame(zip(titles, isForked, repo_links), columns=["title", "isForked", "repo_links"])
    print(df1.head(2))
    return df1 

if __name__ == "__main__":
    
    url = "https://github.com/ar8372?tab=repositories" 
    df = get_repo_csv(url)
    df.to_csv("repo_report.csv", index=False)



