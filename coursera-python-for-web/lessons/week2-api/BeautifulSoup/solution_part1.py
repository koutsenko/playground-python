from bs4 import BeautifulSoup
import unittest

def parse(path_to_file):
    with open(path_to_file, encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'lxml')
    root = soup.find('div', id='bodyContent')
        
    imgs = len(root.find_all(
        lambda tag:tag.name == "img" and
        "width" in tag.attrs and 
        int(tag["width"]) >= 200
    ))
    
    headers_first = root.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    headers_first = [header.text for header in headers_first]
    headers = []
    for i in range(len(headers_first)):
        if headers_first[i][0] in ['E','T','C']:
            headers.append(headers_first[i])
    headers = len(headers)

    lengths = []   
    for link in root.find_all('a'):
        counter = 1
        for l in link.find_next_siblings():
            if l.name  != 'a':
                break
            counter += 1
        lengths.append(counter)
    linkslen = max(lengths)
        
    lists = 0
    for listitem in root.find_all(['ul', 'ol']):
        if not listitem.find_parent('li'):
            lists += 1                                 
    
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
    # unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # Run unit-tests in Jupyter

    