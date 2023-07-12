import requests
import bs4
from fake_headers import headers, Headers


def create_headers():
    headers = Headers(browser="firefox", os="win")
    return headers.generate()

def get_list_vacancies():
    head_hunter_url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

    params = {
        'area': (1, 2),
        'text': 'Django, Flask',
        'page': 0,
        'items_on_page': 20
    }

    hand_hunter_html = requests.get(url=head_hunter_url, params=params, headers=create_headers()).text
    hand_hunter_soup = bs4.BeautifulSoup(hand_hunter_html, "lxml")
    hh_main_content_tag = hand_hunter_soup.find('div', id='a11y-main-content')
    return hh_main_content_tag.find_all('div', class_='serp-item')

def get_vacancies_by_criteria():

    collect_all_data = []
    for div_serp_item in get_list_vacancies():
        h3_tag = div_serp_item.find('h3')
        # получаем название вакансии
        vacancy = h3_tag.text
        # получаем ссылку на вакансию
        link = h3_tag.find('a').get('href')
        # получаем сведения о заработной плате
        try:
            salary = div_serp_item.find('span', class_='bloko-header-section-3').text
        except:
            salary = 'Нет сведений о заработной плате'
        # получаем название компании
        company_name = div_serp_item.find('a', class_='bloko-link bloko-link_kind-tertiary').text
        # получаем название города
        city = div_serp_item.find('div', class_='vacancy-serp-item__info').contents[1].contents[0]

        collect_all_data.append(
                    {
                    'vacancies': vacancy,
                    'link': link,
                    'salary': salary,
                    'company_name': company_name,
                    'city': city
                    }
                )

    return collect_all_data