from random import randint


def choice():
    print('Please enter your question')
    input()
    print(answers[randint(0, len(answers) - 1)])
    print('Is there anything else you want to ask? Enter "yes" or "no"')
    one_more_question = input()
    while True:
        if one_more_question == 'yes':
            choice()
        elif one_more_question == 'no':
            print('Come back if you have any questions!')
            exit()
        else:
            print('Please enter "yes" or "no"')
            one_more_question = input()


answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it',
           'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'Try again',
           'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
           'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
print('Hello World, I am magic ball and I know answer for every your question. What is your name?')
username = input()
print('Hello,', username.capitalize() + '!')
choice()
