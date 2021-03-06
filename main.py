# A mini project by Bao Nguyen

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

categoryOptions = {
    '1': '15',
    '2': '11',
    '3': '12',
    '4': '10'
}
difficutlyOptions ={
    '1': 'easy',
    '2': 'medium',
    '3': 'hard'
}


def selectCategory(arg):
    return categoryOptions.get(arg, "Invalid category number")

def selectDifficulty(arg):
    return difficutlyOptions.get(arg, "Invalid difficutly number")

def fetchData(category, difficutly):
    url = (f'https://opentdb.com/api.php?amount=1&type=multiple&category={category}&difficutly={difficutly}')
    res =requests.get(url).json()
    return res['results'][0]

def handleUser():
    try:
        listCategories(1)
        inputCategory = input('Input your category number: ')
        while int(inputCategory) > len(categoryOptions):
            print('Invalid number')
            inputCategory = input('Input your category number: ')
        listCategories(2)
        inputDifficulty = input('Input your difficutly number: ')
        while int(inputDifficulty) > len(difficutlyOptions):
            print('Invalid number')
            inputDifficulty = input('Input your difficutly number: ')
    except:
        return
    response = fetchData(selectCategory(inputCategory), selectDifficulty(inputDifficulty))
    print('-------------------------')
    print('Question: ', response['question'])

    correct_answer = response['correct_answer']
    incorrect_answers = response['incorrect_answers']
    incorrect_answers.append(str(correct_answer))

    for i in range(len(incorrect_answers)):
        print(f'{i + 1}: {str(incorrect_answers[i])} ')

    inputAnswer = input('Input your answer: ')

    if inputAnswer.strip() == correct_answer:
        print('Correct answer')
    else:
        print('Incorrect answer')
    
def __init__():
    loop = True
    while loop:
        handleUser()
        print('---------------')
        next = input("Do you want to continue? (yes/no) \n")
        if next.strip() == 'yes':
            print('---------------')
            loop = True
        elif next.strip() == 'no' :
            print('Bye')
            loop = False
        else:
            print("Invalid answer")
            loop = False

__init__()
