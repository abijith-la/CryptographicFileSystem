from __future__ import print_function, unicode_literals

def password_change_cli():
    from PyInquirer import prompt, print_json
    from examples import custom_style_2
    questions = [
        {
            'type': 'password',
            'message': 'Enter the current password: ',
            'name': 'password'
        }
    ]
    
    answers = prompt(questions, style=custom_style_2)
    answer = answers['password']
    return answer