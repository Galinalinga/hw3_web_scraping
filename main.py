import json
from hand_hunter import get_vacancies_by_criteria


if __name__ == "__main__":
    with open('vacancies.json', 'w', encoding='utf-8') as f:
        json.dump(get_vacancies_by_criteria(), f, ensure_ascii=False, indent=5)