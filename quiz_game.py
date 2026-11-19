print('Welcome to the Quiz Game!')

playing = input('Do you want to play? (yes/no): ').lower()

if playing != 'yes':

    print('Maybe next time. Goodbye!')
    quit()

print('Great! Let\'s start the quiz.')
score = 1

answers = input('What is CPU in full? ').lower()

if answers == 'central processing unit':

    print('Correct!')
    score += 1
else:
    print('Incorrect! The correct answer is Central Processing Unit.')

answers = input('What is the capital city of Rwanda? ') .lower()

if answers == 'kigali':

    print('Correct!')
    score += 1
else:
    print('Incorrect! The correct answer is Kigali.')

answers = input('What is the best programming language? ').lower()

if answers == 'python':

    print('Correct!')
    score += 1
else:
    print('Incorrect! The correct answer is Python.')

answers = input('What is the most watched TV show? ').lower()

if answers == 'game of thrones':

    print('Correct!')
    score += 1
else:
    print('Incorrect! The correct answer is Game of Thrones.')

answers = input('What is the best chatbot for relaxing? ') .lower()
    
if answers == 'Pi':
    
        print('Correct!')
        score += 1
        
else:
        print('Incorrect! The correct answer is Pi.')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 5) * 100) + '%.')