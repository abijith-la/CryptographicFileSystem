from __future__ import print_function, unicode_literals
from functions import *

import os

def file_manager_cli(list):
    import os
    os.system('clear')
    from PyInquirer import style_from_dict, Token, prompt, Separator

    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })
    if nothomedir(os.getcwd()) == True:
        list.insert(0,'..')
    list.insert(0,'//More Options//')
    questions = [
        {
            'type': 'list',
            'message': os.getcwd(),
            'name': 'ans',
            'choices': list
        }
    ]
    
    answers = prompt(questions, style=style)
    answer = answers['ans']
    return answer