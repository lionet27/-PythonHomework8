mathPath="math.txt"
russianPath="russian.txt"
literaturePath="literature.txt"
musicPath="music.txt"

def txtInDict(path):
    
    dictionary={}
    with open(path, "r") as f:
        text=f.read()
    lines=text.split('\n')
    
    for i in range(0,len(lines)-1):
        if lines[i].isalpha():
            dictionary[lines[i]]=lines[i+1]
    return dictionary

def findPath(number):
    if number=='1':
        path=mathPath
    elif number=='2':
        path=russianPath
    elif number=='3':
        path=literaturePath
    elif number=='4':
        path=musicPath
    else:
        print('неправильный номер')
    return path    
   
def addGrade(dictForAdd,data):
    if data[1] in dictForAdd:
        dictForAdd[data[1]]+=','+data[2]
    else: dictForAdd[data[1]]=data[2]
    return dictForAdd

import inspect
def getVariableName(var):
    return [name for name, value in inspect.currentframe().f_back.f_locals.items() if value is var]

def findGrades(surname,mathPath,russianPath,literaturePath,musicPath):

    math=txtInDict(mathPath)
    russian=txtInDict(russianPath)
    literature=txtInDict(literaturePath)
    music=txtInDict(musicPath)
    spisokItems=[math,russian,literature,music]
    scoreSheet={}
    
    for el in spisokItems:        
        if surname in el:
            name=getVariableName(el) 
            scoreSheet[name[0]]=el[surname]
    
    return scoreSheet

def rewriteTxt(path,dictionary):
        with open(path, "w") as f:
            for item in dictionary:
                f.write('{}\n{}\n'.format(item,dictionary[item]))

def gradesPrint(scoreSheet):
    print('Ваши оценки по предметам:')
    for item in scoreSheet:
        print('{}:{}'.format(item,scoreSheet[item]))




          
    
