import requests
import random

def listCategories(arg):
    switcher = {
        1: """
            1. Video games
            2. Films
            3. Musics
            4. Books
        """ ,
        2: """
            1. Easy
            2. Medium
            3. Hard
        """
    }
    return print(switcher.get(arg,''))

def selectCategory(arg):
    switcher = {
        '1': '15',
        '2': '11',
        '3': '12',
        '4': '10'
    }
    return switcher.get(arg, "Invalid category number")

def selectDifficulty(arg):
    switcher ={
        '1': 'easy',
        '2': 'medium',
        '3': 'hard'
    }
    return switcher.get(arg, "Invalid difficutly number")

def fetchData():
    try:
        listCategories(1)
        inputCategory = input('Input your category number: ')
        while int(inputCategory) > 4:
            print('Invalid number')
            inputCategory = input('Input your category number: ')
        listCategories(2)
        inputDifficulty = input('Input your difficutly number: ')
        while int(inputDifficulty) > 3:
            print('Invalid number')
            inputDifficulty = input('Input your difficutly number: ')
    except:
        return
    url = (f'https://opentdb.com/api.php?amount=1&category={selectCategory(inputCategory)}&difficutly={selectDifficulty(inputDifficulty)}')
    res =requests.get(url).json()
    print('Question: ', res['results'][0]['question'])
    print('-------------------------')

    correct_answer = res['results'][0]['correct_answer']
    incorrect_answers = res['results'][0]['incorrect_answers']
    incorrect_answers.append(str(correct_answer))

    count = 1
    for i in range(len(incorrect_answers)):
        print(f'{i + 1}: {str(incorrect_answers[i])} ')

    inputAnswer = input('Input your number answer: ')

    if inputAnswer == correct_answer:
        print('you right')
    
def __init__():
    while True:
        fetchData()
        next = input("Do you want to continue? y/n \n")
        if next == 'y':
            print('---------------')
            return False
        elif next == 'n' :
            print('Bye')
            return True
        else:
            next = input("Do you want to continue? y/n \n")

__init__()
