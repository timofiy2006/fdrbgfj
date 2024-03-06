def process_text(text, reverse=False, *args, **kwargs):
    if reverse:
        text = text[::-1]
    for arg in args:
        text += arg
    if 'separator' in kwargs:
        text += kwargs['separator']
    return text
print(process_text("Hello"))  
print(process_text("Hello", reverse=True))  
print(process_text("Hello", " ", "world"))  
print(process_text("Hello", " ", "world", separator=", "))  