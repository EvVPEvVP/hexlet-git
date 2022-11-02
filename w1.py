from docx import Document


def replaceword(a,b,c):
    document = Document(a)
    for paragraph in document.paragraphs:
        if b not in paragraph.text:
            continue
        x = paragraph.runs
        for j in x:
            j.text = j.text.replace(b, c)

    document.save(a)
    return True
