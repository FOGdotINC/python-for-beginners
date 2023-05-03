import requests
import bs4
import concurrent.futures

def scrape_page(url):
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('p')
    return [d.text for d in data]

def main():
    urls = ['https://www.example1.com', 'https://www.example2.com', 'https://www.example3.com']
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = [executor.submit(scrape_page, url) for url in urls]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

if __name__ == '__main__':
    main()
