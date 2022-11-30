from __future__ import print_function, unicode_literals

def options_cli():
    from PyInquirer import style_from_dict, Token, prompt, Separator
    list = ['Return','New Directory','Delete File','Delete Directory','Upload File','Download File','Quit']
    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '#ff0000',  # default
        Token.Answer: '#ff0000',
        Token.Question: '#ff0000 bold'
    })

    questions = [
        {
            'type': 'list',
            'message': '<<Select an Option>>',
            'name': 'ans',
            'choices': list
        }
    ]
    
    answers = prompt(questions, style=style)
    answer = answers['ans']
    return answer

