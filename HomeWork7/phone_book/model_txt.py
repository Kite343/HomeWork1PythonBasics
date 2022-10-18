def read_file(name='phonebook.txt'):
    with open(name, "r", encoding='utf-8') as file:
        text = file.read()
        return text

def write_files(name, text):
    with open(name, 'w', encoding='utf-8') as new_file:
        new_file.write(text)

def add_data(text, name='phonebook.txt'):
    with open(name, "a", encoding='utf-8') as file:
        file.write("\n\n" + '\n'.join(text))
        

# print([i.split("\n") for i in read_file('phonebook.txt').split("\n\n")])
# print(read_file())