import csv

def write_files(name, text):
    # if isinstance(text, str):
    #     text = [i.split("\n") for i in text.split("\n\n")]
    with open(name, 'w',encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in text:
            writer.writerow(row)

def read_file(name='phonebook.csv'):
    with open(name, encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res

def add_data(text, name='phonebook.csv'):
    with open(name, "a", encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';', lineterminator="\r")
        writer.writerow(text)

def update_phonebook(text, name="phonebook.csv"):
    # text = [i.split("\n") for i in text]
    with open(name, 'w',encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in text:
            writer.writerow(row)

