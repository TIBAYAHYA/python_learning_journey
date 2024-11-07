import sys
import pyperclip
import requests
import bs4
import webbrowser

def get_search_input():
    if len(sys.argv) > 1:
        return ' '.join(sys.argv[1:])
    else:
        return pyperclip.paste()

def construct_search_url(search_input):
    return "https://www.google.com/search?q=" + search_input

def fetch_search_results(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve search results")
        sys.exit(1)

def parse_html(html_content):
    soup = bs4.BeautifulSoup(html_content, "html.parser")
    return soup.select('a')

def extract_urls(links):
    urls = []
    for link in links:
        href = link.get('href')
        if href and href.startswith('/url?q='):
            url = href.split('&')[0].replace('/url?q=', '')
            if not url.startswith('http'):
                continue
            urls.append(url)
    return urls

def open_urls(urls, max_open=5):
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    for url in urls[:max_open]:
        print("Opening:", url)
        webbrowser.get(edge_path).open(url)

def main():
    search_input = get_search_input()
    print("Searching for:", search_input)
    
    search_url = construct_search_url(search_input)
    print("Search URL:", search_url)
    
    html_content = fetch_search_results(search_url)
    print("Fetched HTML content")
    
    links = parse_html(html_content)
    print("Parsed HTML content")
    
    urls = extract_urls(links)
    print("Extracted URLs:", urls)
    
    open_urls(urls)

if __name__ == "__main__":
    main()