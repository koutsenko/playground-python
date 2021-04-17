import unittest

from bs4 import BeautifulSoup


def parse(path_to_file):
    with open(path_to_file, encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")
        body = soup.find(id="bodyContent")

    # коли�е��во ка��инок (img) � �и�иной (width) не мен��е 200
    imgs = len(body.find_all('img', width=lambda x: int(x or 0) > 199))

    # коли�е��во заголовков (h1, h2, h3, h4, h5, h6), пе�ва� б�ква �ек��а вн���и ко�о���
    # �оо�ве���в�е� заглавной б�кве E, T или C
    headers = sum(1 for tag in body.find_all(
        ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) if tag.get_text()[0] in "ETC")

    # коли�е��во �пи�ков (ul, ol), не вложенн�� в д��гие �пи�ки
    lists = sum(
        1 for tag in body.find_all(['ol', 'ul']) if not tag.find_parent(['ol', 'ul']))

    # �лин� мак�имал�ной по�ледова�ел�но��и ���лок, межд� ко�о��ми не� д��ги� �егов
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


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()