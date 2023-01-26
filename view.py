def requestStudent():
    surname=input('Введите вашу фамилию: ')        
    return surname

def requestTeacher():
    subject=input('Выберете предмет mathematics(1),russian(2),literature(3),music(4): ')
    surname=input('Введите фамилию ученика: ')
    grade=input('Введите оценку ученика: ')
    return subject,surname,grade


