from view import requestStudent, requestTeacher
from model import txtInDict, findPath, addGrade, getVariableName,findGrades,rewriteTxt, gradesPrint

mathPath="math.txt"
russianPath="russian.txt"
literaturePath="literature.txt"
musicPath="music.txt"

def actionChoice():
    while (True):
        n=input('Вы ученик(1) или учитель(2),выйти из программы (3): ')
        if n=='1':
            surname=requestStudent()
            grades=findGrades(surname,mathPath,russianPath,literaturePath,musicPath)
            gradesPrint(grades)

        elif n=='2':
            dataTeacher=requestTeacher()
            path=findPath(dataTeacher[0])
            gradesForAdd=txtInDict(path)
            newgrades=addGrade(gradesForAdd,dataTeacher)
            rewriteTxt(path,newgrades)
        elif n=='3':
            break
        else:
            print('Неправильно ввели номер. Попробуйте еще раз.') 

