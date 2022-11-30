from __future__ import print_function, unicode_literals


def password_cli():
    from PyInquirer import prompt, print_json
    from examples import custom_style_2
    from pyfiglet import Figlet
    f = Figlet(font='cybermedium')
    print (f.renderText('Cryptographic File System'))
    questions = [
        {
            'type': 'password',
            'message': 'Enter the access code: ',
            'name': 'password'
        }
    ]
    
    answers = prompt(questions, style=custom_style_2)
    answer = answers['password']
    return answer