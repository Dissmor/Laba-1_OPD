from bs4 import BeautifulSoup
import requests
import SaveToExcel


def parse():
    url = 'https://omsk.hh.ru/vacancies/programmist?hhtmFromLabel=rainbow_profession&hhtmFrom=main'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'}
    page = requests.get(url, headers=headers)
    print(page.status_code)

    filteredVacancies = []
    allVacancies = []

    soup = BeautifulSoup(page.text, "html.parser")

    allVacancies = soup.find_all('div', class_='')

    for data in allVacancies:
        if (data.find('a', class_='serp-item__title')) is not None:
            filteredVacancies.append(data.text)
    SaveToExcel.saveToExcel(data, filteredVacancies)