try: 
    import requests 
    from bs4 import BeautifulSoup 
    import pandas as pd  
    import glob 
except Exception as e: 
    print("Some Modules are Missing {}".format(e))

wanted_file_extensions = [
    # C and C++
    '.c', '.cpp', '.cc', '.h', '.hpp',
    # Java
    '.java', '.jar',
    # Python
    '.py',
    # JavaScript
    '.js',
    # HTML
    '.html', '.htm',
    # CSS
    '.css',
    # Ruby
    '.rb',
    # PHP
    '.php',
    # Swift
    '.swift',
    # Kotlin
    '.kt',
    # C# (C-Sharp)
    '.cs',
    # Go
    '.go',
    # Rust
    '.rs',
    # TypeScript
    '.ts',
    # Shell Scripts
    '.sh',
    # Markup and Configuration Files
    '.xml', '.json', '.yaml', '.yml',
    # SQL
    '.sql',
    # MATLAB
    '.m',
    # R
    '.r', '.R',
    # Batch Scripts
    '.bat',
    # Added extensions
    # pdf and text files 
    '.pdf', '.txt',
    # Readme also imp 
    '.md',
    # ipynb files 
    #'.ipynb',
]


unwanted_file_extentions = [ 
    ".gitignore",
    ".png", 
    ".jpeg",
    ".h5", 
    "hdf5",
    ".gif", 
    ".meta",
]
def string_ends_with(st, elements):
    for el in elements:
        if st.endswith(el):
            return True 
    return False 



def get_code(repo_url, raw_title, raw_text, all_titles):
    # print("="*40)
    # print("Entered:", repo_url)
    storage_file = string_ends_with(raw_title, unwanted_file_extentions)
    if storage_file: 
        return raw_text, all_titles
    
    # input: repo_url 
    # output: all code in we structured format

    r  = requests.get(repo_url)

    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup)
    # class="flex-auto min-width-0 col-md-2 mr-3"
    d = soup.findAll('div', class_="flex-auto min-width-0 col-md-2 mr-3")
    # c = soup.findAll('div', class_="notebook-container")
    # paragraph = soup.select("div ~ div ~ div ~ div ")
    # print(paragraph)

    # print("DDDDDDDDDDD")
    # Find code cells
    # code_cells = soup.find_all('code')
    # print(code_cells)
    # Find markdown cells
    #markdown_cells = soup.find_all('div', {'class': 'text_cell_render'})
    # print(markdown_cells)
    #print(soup)
    if d == []:
        storage_file = string_ends_with(raw_title, wanted_file_extensions)
        # no need to check if raw_title = "" because we can't be inside a file without a file name.
        if not storage_file: 
            return raw_text, all_titles
    
        # # Remove script and style tags
        for script in soup(["script", "style", "footer", "nav"]):
            script.extract()

        #print(soup)

        j= " ".join(soup.get_text().strip().split())
        # print("HERE",j)
        # print()
        # print(soup)
        if "Open in GitHub Desktop Open with Desktop View raw View blame" in j:
            j = (j.split("Open in GitHub Desktop Open with Desktop View raw View blame")[-1]).strip()
        if "Copy lines Copy permalink View git":
            j= (j.split("Copy lines Copy permalink View git")[0]).strip()
        #print(j)
        #input()
        n = len(all_titles)
        raw_text = raw_text + "\n" +f"File no {n+1}: "+ raw_title +"\n"+ str(j)
        
        print(f"{n+1}.File")
        return raw_text  + "\n", all_titles + [raw_title]
    base_url = "https://github.com/"



    for _,i in enumerate(d):
        for a in i.findAll('a'):
            newUrl = base_url + a["href"]
        t = " ".join(i.text.strip().split())
        # Public word should be there in the text t
        print(t)
        print(newUrl)
        # if t == "main2.py":
        #     print(newUrl)
        #     print(a)
        #     print()
        raw_text, all_titles = get_code(newUrl, raw_title + "/"+ t, raw_text, all_titles) 
        
    return raw_text, all_titles

if __name__ == "__main__":
    v= get_code("https://github.com/ar8372/ML_algos_from_scratch/blob/master/HAC_Single_Link.ipynb", "simple.ipynb", "", [])

    print(v)
        
