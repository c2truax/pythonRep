students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(dicty):
    for count in range(len(dicty)):
        string = ''
        for key, val in dicty[count].items():
            if string == '':
                string = key+' - '+val
            else:
                string += ' , '
                string += key+' - '+val
        print(string)

iterateDictionary(students)