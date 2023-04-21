print('-------------------------------')
print()
print('Welcome to the ETS Quiz')
print('--------------------------------')

start = input('Are you ready to start?: ')

if start == 'Yes':
    print("Ready...")
else:
    quit('Come back when you are ready')

score = 0

answer1 = int(input('What is 2 / 0 ? '))
if answer1 == 0:
    print('Correct')
    score += 1
else:
    print('Incorrect')



answer2 = int(input('What is 10 / 10 ? '))
if answer2 == 1:
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer3 = input('What does API mean ? ')
if answer3 == 'Application programming interface':
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer4 = input('What year is it ? ')
if answer4 == '2023':
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer5 = int(input('How many continents are there ? '))
if answer5 == 7:
    print('Correct')
    score += 1
else:
    print('Incorrect')

print(f'Your final score is {(score/5)*100}%')

registration = (score/5)*100 

if registration <= 70:
    print('Sorry. Please retake this exams ')
elif registration >= 80 or registration <= 89:
    print('You may take the GMAT')
else:
    print('Welcome Genius to our array of examinations. Please study')



