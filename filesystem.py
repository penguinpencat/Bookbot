def get_book_text(path_to_file):
    contents = ""
    with open(path_to_file) as file:
        contents = file.read()
    return contents