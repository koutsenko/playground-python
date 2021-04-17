import os
import re

from bs4 import BeautifulSoup


def parse(path_to_file):
    with open(path_to_file, encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")
        body = soup.find(id="bodyContent")

    imgs = len(body.find_all('img', width=lambda x: int(x or 0) > 199))

    headers = sum(1 for tag in body.find_all(
        ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) if tag.get_text()[0] in "ETC")

    lists = sum(
        1 for tag in body.find_all(['ol', 'ul']) if not tag.find_parent(['ol', 'ul']))

    linkslen = 0

    for a in body.find_all('a'):
        current_streak = 1

        for tag in a.find_next_siblings():
            if tag.name == 'a':
                current_streak += 1
            else:
                break

        linkslen = current_streak if current_streak > linkslen else linkslen

    return [imgs, headers, linkslen, lists]


def get_statistics(path, start_page, end_page):
    """ÑÐ¾Ð±Ð¸ÑÐ°ÐµÑ ÑÑÐ°ÑÐ¸ÑÑÐ¸ÐºÑ ÑÐ¾ ÑÑÑÐ°Ð½Ð¸Ñ, Ð²Ð¾Ð·Ð²ÑÐ°ÑÐ°ÐµÑ ÑÐ»Ð¾Ð²Ð°ÑÑ, Ð³Ð´Ðµ ÐºÐ»ÑÑ - Ð½Ð°Ð·Ð²Ð°Ð½Ð¸Ðµ ÑÑÑÐ°Ð½Ð¸ÑÑ,
    Ð·Ð½Ð°ÑÐµÐ½Ð¸Ðµ - ÑÐ¿Ð¸ÑÐ¾Ðº ÑÐ¾ ÑÑÐ°ÑÐ¸ÑÑÐ¸ÐºÐ¾Ð¹ ÑÑÑÐ°Ð½Ð¸ÑÑ"""
    pages = build_bridge(path, start_page, end_page)
    statistic = {}

    for page in pages:
        statistic[page] = parse(os.path.join(path, page))

    return statistic


def get_links(path, page):
    """Ð²Ð¾Ð·Ð²ÑÐ°ÑÐ°ÐµÑ Ð¼Ð½Ð¾Ð¶ÐµÑÑÐ²Ð¾ Ð½Ð°Ð·Ð²Ð°Ð½Ð¸Ð¹ ÑÑÑÐ°Ð½Ð¸Ñ, ÑÑÑÐ»ÐºÐ¸ Ð½Ð° ÐºÐ¾ÑÐ¾ÑÑÐµ ÑÐ¾Ð´ÐµÑÐ¶Ð°ÑÑÑ Ð² ÑÐ°Ð¹Ð»Ðµ page"""

    with open(os.path.join(path, page), encoding="utf-8") as file:
        links = set(re.findall(r"(?<=/wiki/)[\w()]+", file.read()))
        if page in links:
            links.remove(page)
    return links


def get_backlinks(path, end_page, unchecked_pages, checked_pages, backlinks):
    """Ð²Ð¾Ð·Ð²ÑÐ°ÑÐ°ÐµÑ ÑÐ»Ð¾Ð²Ð°ÑÑ Ð¾Ð±ÑÐ°ÑÐ½ÑÑ ÑÑÑÐ»Ð¾Ðº (ÐºÐ»ÑÑ - ÑÑÑÐ°Ð½Ð¸ÑÐ°, Ð·Ð½Ð°ÑÐµÐ½Ð¸Ðµ - ÑÑÑÐ°Ð½Ð¸ÑÐ°
    Ñ ÐºÐ¾ÑÐ¾ÑÐ¾Ð¹ Ð²Ð¾Ð·Ð¼Ð¾Ð¶ÐµÐ½ Ð¿ÐµÑÐµÑÐ¾Ð´ Ð¿Ð¾ ÑÑÑÐ»ÐºÐµ Ð½Ð° ÑÑÑÐ°Ð½Ð¸ÑÑ, ÑÐºÐ°Ð·Ð°Ð½Ð½ÑÑ Ð² ÐºÐ»ÑÑÐµ)"""

    if end_page in checked_pages or not checked_pages:
        return backlinks

    new_checked_pages = set()

    for checked_page in checked_pages:
        unchecked_pages.remove(checked_page)
        linked_pages = get_links(path, checked_page) & unchecked_pages

        for linked_page in linked_pages:
            backlinks[linked_page] = backlinks.get(linked_page, checked_page)
            new_checked_pages.add(linked_page)

    checked_pages = new_checked_pages & unchecked_pages

    return get_backlinks(path, end_page, unchecked_pages, checked_pages, backlinks)


def build_bridge(path, start_page, end_page):
    """Ð²Ð¾Ð·Ð²ÑÐ°ÑÐ°ÐµÑ ÑÐ¿Ð¸ÑÐ¾Ðº ÑÑÑÐ°Ð½Ð¸Ñ, Ð¿Ð¾ ÐºÐ¾ÑÐ¾ÑÑÐ¼ Ð¼Ð¾Ð¶Ð½Ð¾ Ð¿ÐµÑÐµÐ¹ÑÐ¸ Ð¿Ð¾ ÑÑÑÐ»ÐºÐ°Ð¼ ÑÐ¾ start_page Ð½Ð°
    end_page, Ð½Ð°ÑÐ°Ð»ÑÐ½Ð°Ñ Ð¸ ÐºÐ¾Ð½ÐµÑÐ½Ð°Ñ ÑÑÑÐ°Ð½Ð¸ÑÑ Ð²ÐºÐ»ÑÑÐ°ÑÑÑÑ Ð² ÑÐµÐ·ÑÐ»ÑÑÐ¸ÑÑÑÑÐ¸Ð¹ ÑÐ¿Ð¸ÑÐ¾Ðº"""

    backlinks = \
        get_backlinks(path, end_page, set(os.listdir(path)), {start_page, }, dict())

    current_page, bridge = end_page, [end_page]

    while current_page != start_page:
        current_page = backlinks.get(current_page)
        bridge.append(current_page)

    return bridge[::-1]
