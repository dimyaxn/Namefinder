import re

file = open('file.txt', encoding="utf8")
text = file.read()

def name_finder(text):
    result = set()
    pattern_1 = r'[А-ЯЁ][а-яё]+ [А-ЯЁ]\.[А-ЯЁ]\.'
    pattern_2 = r'[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+\b'
    pattern_3 = r'[А-ЯЁ]\.[А-ЯЁ]\. [А-ЯЁ][а-яё]+\b'
    pattern_4 = r'[А-ЯЁ]{2,} [А-ЯЁ]{2,} [А-ЯЁ]{2,} \b'

    result.update(re.findall(pattern_1, text))
    result.update(re.findall(pattern_2, text))
    result.update(re.findall(pattern_3, text))
    result.update(re.findall(pattern_4, text))
    return sorted(result)

num_set = name_finder(text)

print(*num_set, sep='\n')