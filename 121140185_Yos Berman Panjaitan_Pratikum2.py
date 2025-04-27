import random

# Daftar kata-kata
words = [
    'server', 'client', 'cookie', 'database', 'hosting', 'python', 'hardware',
    'software', 'firewall', 'router', 'backend', 'frontend', 'network', 'socket',
    'thread', 'kernel', 'linux', 'windows', 'android', 'ios', 'cloud', 'backup',
    'encryption', 'firmware', 'protocol', 'domain', 'malware', 'phishing',
    'password', 'vpn', 'browser', 'email', 'api', 'cache', 'storage'
]

# Gambar Hangman sederhana
hangman_stages = [
    '''
     .----.
    /      \\
   |        |
    \\      /
     '----'
        |
        |
        |
    =========
    ''',
    '''
     .----.
    /      \\
   |        |
    \\      /
     '----'
       (o_o)
        |
        |
        |
    =========
    ''',
    '''
     .----.
    /      \\
   |        |
    \\      /
     '----'
       (o_o)
        |
       /|
        |
    =========
    ''',
    '''
     .----.
    /      \\
   |        |
    \\      /
     '----'
       (o_o)
       \\|/
        |
    =========
    ''',
    '''
     .----.
    /      \\
   |        |
    \\      /
     '----'
       (o_o)
       \\|/
        |
       / 
    =========
    ''',
    '''
     .----.
    /      \\
   |        |
    \\      /
     '----'
       (x_x)
       \\|/
        |
       / \\
    =========
    '''
]


# Pilih kata secara acak
word = random.choice(words)
word_display = ['_' for _ in word]
guessed_letters = set()
wrong_guesses = 0
max_wrong = len(hangman_stages) - 1

# Game loop
while True:
    print(hangman_stages[wrong_guesses])
    print("The word is:", ' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Correct!")
        for idx, letter in enumerate(word):
            if letter == guess:
                word_display[idx] = guess
    else:
        print("Wrong!")
        wrong_guesses += 1

    if '_' not in word_display:
        print("Congratulations! You've guessed the word:", word)
        break

    if wrong_guesses == max_wrong:
        print(hangman_stages[wrong_guesses])
        print("Game Over! The word was:", word)
        break
