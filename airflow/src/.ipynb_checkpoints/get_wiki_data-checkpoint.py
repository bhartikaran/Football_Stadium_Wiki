def get_wiki_page(url):
    import requests
    try:
        response = requests.get(url,timeout=10,verify=False)
        response.raise_for_status()
        
        return response.text
    except requests.RequestException as e:
        print(f"An error occured : {e}")

def get_wiki_data(**kwargs):
    from bs4 import BeautifulSoup
    html = get_wiki_page(kwargs['url'])
    soup = BeautifulSoup(html,features='html.parser')
    table = soup.find_all("table",attrs={"class":"wikitable sortable sticky-header"})[0]

    table_rows = table.find_all('tr')
    list_of_stadium=[] 
    for i in range(1,len(table_rows)):
      row = table_rows[i]
      rank = i
      stadium_name = row[1].text.strip().replace('♦','')
      seating_cap = row[1].text.strip()
      list_of_stadium.append()
    return stadium;




class Stadium:
    def __init__(self, stadium=None, seating_capacity=None, region=None, country=None, city=None, images_url=None, home_team=None, rank=None):
        self.stadium = stadium
        self.seating_capacity = seating_capacity
        self.region = region
        self.country = country
        self.city = city
        self.images_url = images_url
        self.home_team = home_team
        self.rank = rank

get_wiki_data(url=https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity)