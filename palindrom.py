def is_palindrom(text):
    text_list = text.split(" ")
    first_text = ""
    inverted_text = ""

    for word in text_list:
        first_text += word

    inverted_text = first_text[::-1]

    if first_text == inverted_text:
        print("This text is palindrom")
    else:
        print("This text is not a palindrom")