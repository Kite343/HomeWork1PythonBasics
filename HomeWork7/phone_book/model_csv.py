import csv

def write_files(name, text):
    text = [i.split("\n") for i in text.split("\n\n")]
    with open(name, 'w',encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in text:
            writer.writerow(row)
