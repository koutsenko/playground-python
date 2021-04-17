import operator
from datetime import datetime
from typing import Dict, List, Union

from requests import exceptions, get

from settings import ACCESS_TOKEN, URL_API_FRIENDS, URL_API_USERID, VK_API_VER


def get_api_data(url: str) -> Union[Dict, List]:
    """ Метод получения данных с API """

    response = get(url).json().get("response")

    return response


def get_real_uid(uid: str) -> int:
    """ Получение id пользователя ВКонтакте по короткому адресу """

    api_userid_url = f'{URL_API_USERID}?v={VK_API_VER}&access_token={ACCESS_TOKEN}&user_ids={uid}'

    try:
        res_userid_data = get_api_data(url=api_userid_url)
        real_uid = res_userid_data[0].get('id')

        return real_uid

    except:
        raise SystemExit('get_real_id error')


def get_friends_birthdays(real_uid: int) -> List:
    """ Получение списка друзей пользователя ВКонтакте с указанным id """

    try:
        api_friendlist_url = f'{URL_API_FRIENDS}?v={VK_API_VER}&access_token={ACCESS_TOKEN}&user_id={real_uid}&fields=bdate'
        res_friendlist_data = get_api_data(url=api_friendlist_url)
        friend_list = res_friendlist_data.get('items')

        return friend_list

    except:
        raise SystemExit('get_friend_birthdays error')


def extract_year(date: str) -> Union[int, None]:
    """ Извлечение года из даты-строки

    :param date: date in string with format %d.%m.%Y or %d.%m
    :return: None if date format is %d.%m, int if %d.%m.%Y
    """

    year = None
    tokens = date.split(".")

    if len(tokens) == 3:
        year = int(tokens[2])

    return year


def get_friends_age_dist(username: str) -> List:
    """ Подсчет распределения возрастов друзей для указанного пользователя ВКонтакте """

    uid = get_real_uid(username)
    birthday_list = get_friends_birthdays(uid)

    # define processed data collector
    year_collector = {}

    # process data
    now = datetime.now()
    for friend in birthday_list:
        bdate = friend.get('bdate')
        if bdate:
            year = extract_year(bdate)
            if year:
                age = now.year - year
                if age in year_collector:
                    year_collector[age] += 1
                else:
                    year_collector[age] = 1

    # convert dict into list of tuple then sort it
    result = list(year_collector.items())
    result.sort(key=operator.itemgetter(0))
    result.sort(key=operator.itemgetter(1), reverse=True)

    return result


def main() -> None:
    result = get_friends_age_dist(username="reigning")

    print(result)


if __name__ == "__main__":
    main()
