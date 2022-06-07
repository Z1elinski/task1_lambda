import re
import csv
import os
import json


def read_file_to_string(path):
    # function reads text file and returns string
    try:
        with open(path, 'r') as file:
            text = file.read()
    except FileNotFoundError as e:
        print(e)
    return text


def extract_num_from_string(text):
    # function extract number from string and returns list in ascending folder
    numbers = []
    for elem in re.findall("\\d+", text):
        numbers.append(int(elem))
    numbers = list(set(numbers))
    numbers = sorted(numbers)
    return numbers


def fibonacci(last_num):
    x = [0, 1]
    for i in range(2, last_num + 1):
        x.append(x[i - 1] + x[i - 2])
    return x


def create_csv_file(numbers):
    # function finds Fibonacci numbers from observed numbers and returns csv file
    fib_numbers = fibonacci(max(numbers))
    path = os.getcwd() + r"\example_io\output.csv"
    with open(path, mode='w', newline='') as file:
        print('Creating file: {}'.format(os.path.basename(path)))
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['previous Fibonacci number', 'observed number', 'next Fibonacci number'])
        for elem in numbers:
            if elem not in fib_numbers:
                writer.writerow(['', elem, ''])
            else:
                i = fib_numbers.index(elem)
                if i != 0:
                    writer.writerow([fib_numbers[i-1], fib_numbers[i], fib_numbers[i+1]])
                else:
                    writer.writerow([0, 0, 0])


def find_words(text):
    # function finds words containing only alphabetical characters, counts the number of word occurrences
    words = {}
    for elem in re.findall(r"(?i)\b[a-z]+\b", text):
        elem = elem.lower()
        if elem.isalpha and elem not in words.keys():
            words[elem] = 1
        elif elem.isalpha and elem in words.keys():
            words[elem] += 1
    return words


def create_json_file(dictionary):
    path = os.getcwd() + r"\example_io\output.json"
    print('Creating file: {}'.format(os.path.basename(path)))
    with open(path, 'w') as file:
        json.dump(dictionary, file)


if __name__ == '__main__':
    fileLocation = os.getcwd() + r'\example_io\example_input.txt'
    fileContent = read_file_to_string(fileLocation)
    # print(fileContent)
    listOfNumbers = extract_num_from_string(fileContent)
    # print(listOfNumbers)
    create_csv_file(listOfNumbers)
    wordsCounted = find_words(fileContent)
    # print(wordsCounted)
    create_json_file(wordsCounted)
