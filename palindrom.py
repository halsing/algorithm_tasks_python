"""
Function to check if text is palindrom 
"""
def is_palindrom(text):
    first_text = "".join(text.split(" "))
    inverted_text = first_text[::-1]

    return True if first_text == inverted_text else False
