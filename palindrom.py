def is_palindrom(text):
    text_list = text.split(" ")
    first_text = ""

    for word in text_list:
        first_text += word

    inverted_text = first_text[::-1]

    return True if first_text == inverted_text else False
