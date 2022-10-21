def read_file(name='phonebook.txt'):
    with open(name, "r", encoding='utf-8') as file:
        text = file.read()
        return text

def write_files(name, text):
    if isinstance(text, list):
        text = "\n\n".join(["\n".join(i) for i in text])
    with open(name, 'w', encoding='utf-8') as new_file:
        new_file.write(text)

def add_data(text, name='phonebook.txt'):
    with open(name, "a", encoding='utf-8') as file:
        file.write("\n\n" + '\n'.join(text))
        
def update_phonebook(text, name="phonebook.txt"):
    text = "\n\n".join(text)
    with open(name, 'w', encoding='utf-8') as new_file:
        new_file.write(text)

