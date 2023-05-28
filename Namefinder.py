import re
import docx

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

def file_name_finder(text):
    pattern = r'(?<=\/)[\w ]+(?:(?=\.doc)|(?=\.docx)|(?:\.txt))'
    result = re.findall(pattern, text)
    return result[0]

def get_text(filename):
    if filename.lower().endswith(('.docx')):
        fullText = []
        doc = docx.Document(filename)
        for para in doc.paragraphs:
            fullText.append(para.text)
            result = '\n'.join(fullText)
    elif filename.lower().endswith(('.txt')):
        file = open(filename, encoding="utf8")
        result = file.read()
    return result

