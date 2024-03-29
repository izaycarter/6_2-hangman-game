import random

randomlst = [
    'people',
    'history',
    'way',
    'art',
    'world',
    'information',
    'map',
    'two',
    'family',
    'government',
    'health',
    'system',
    'computer',
    'meat',
    'year',
    'thanks',
    'music',
    'person',
    'reading',
    'method',
    'data',
    'food',
    'understanding',
    'theory',
    'law',
    'bird',
    'literature',
    'problem',
    'software',
    'control',
    'knowledge',
    'power',
    'ability',
    'economics',
    'love',
    'internet',
    'television',
    'science',
    'library',
    'nature',
    'fact',
    'product',
    'idea',
    'temperature',
    'investment',
    'area',
    'society',
    'activity',
    'story',
    'industry',
    'media',
    'thing',
    'oven',
    'community',
    'definition',
    'safety',
    'quality',
    'development',
    'language',
    'management',
    'player',
    'variety',
    'video',
    'week',
    'security',
    'country',
    'exam',
    'movie',
    'organization',
    'equipment',
    'physics',
    'analysis',
    'policy',
    'series',
    'thought',
    'basis',
    'boyfriend',
    'direction',
    'strategy',
    'technology',
    'army',
    'camera',
    'freedom',
    'paper',
    'environment',
    'child',
    'instance',
    'month',
    'truth',
    'marketing',
    'university',
    'writing',
    'article',
    'department',
    'difference',
    'goal',
    'news',
    'audience',
    'fishing',
    'growth',
    'income',
    'marriage',
    'user',
    'combination']

randomword = (" ".join([randomlst[random.randrange(0, len(randomlst))]]))

word = randomword

print("Welcome to Hangman!! \n")


#runs untill errors is 6 for the mistakes
guessed = []
wrong = []

tries = 7

while tries > 0:

    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        break

    print("Guess the word:", out)
    print(tries, "chances left")

    guess = input()

    if guess in guessed or guess in wrong:
        print("Already guessed", guess)
    elif guess in word:
        print("Yay you got a letter")
        guessed.append(guess)
    else:
        print("that is not in the word")
        tries = tries - 1
        wrong.append(guess)

    print()

if tries:
    print("YOU WIN!!!!")
else:
    print("You Lost..")
