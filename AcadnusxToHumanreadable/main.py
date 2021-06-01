from docx import Document

path = 'Teoriuli masala1.docx'

document = Document(path)

DICTIONARY = {
    'a': 'ა',
    'b': 'ბ',
    'c': 'ც',
    'd': 'დ',
    'e': 'ე',
    'f': 'ფ',
    'g': 'გ',
    'h': 'ჰ',
    'i': 'ი',
    'j': 'ჯ',
    'k': 'კ',
    'l': 'ლ',
    'm': 'მ',
    'n': 'ნ',
    'o': 'ო',
    'p': 'პ',
    'q': 'ქ',
    'r': 'რ',
    's': 'ს',
    't': 'ტ',
    'u': 'უ',
    'v': 'ვ',
    'w': 'წ',
    'x': 'ხ',
    'y': 'ყ',
    'z': 'ზ',
    'C': 'ჩ',
    'S': 'შ',
    'R': 'ღ',
    'J': 'ჟ',
    'W': 'ჭ',
    'T': 'თ',
    'Z': 'ძ'
}


def change_in_text(to_pass):
    """
    რადგანაც პითონის სტრინგი არის უცვლელი საჭიროა მთლიანი ტექსტ
    ობიექტის ასო ასო გარდაქმნა და შემდეგ მთლიანად ჩანაცვლება
    """
    new_object = ''

    for character in to_pass.text:
        if character in DICTIONARY.keys():
            new_object += DICTIONARY[character]
        else:
            new_object += character

    return new_object

for paragraphs in document.paragraphs:
    text = paragraphs.runs
    for object in text:
        to_pass = object
        if object.font.name == "AcadNusx" or object.font.name == "AcadMtavr":
            object.font.name = "Calibri"
            object.text = change_in_text(to_pass)


new_path = "1111.docx"
document.save(new_path)
