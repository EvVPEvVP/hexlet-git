3.1.

from functools import partial

def tag(tag_name, content):
    return f"<{tag_name}>{content}</{tag_name}>"

bold = partial(tag, 'b')
italic = partial(tag, 'i')

# Пример:
print(tag('b', 'string'))  
print(bold('bold text'))   
print(italic('italic text'))  

3.2.

def tag(tag_name, content, attr=None):
    if attr is None:
        return f"<{tag_name}>{content}</{tag_name}>"
    else:
        attributes = ' '.join([f'{k}="{v}"' for k, v in attr.items()])
        return f"<{tag_name} {attributes}>{content}</{tag_name}>"

# Пример:
print(tag('li', 'item 23', {'class': 'list-group'}))

# или:
list_item = partial(tag, 'li', attr={'class': 'list-group'})
print(list_item('item 24'))
