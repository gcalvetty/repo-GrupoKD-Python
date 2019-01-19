var1 = 'Hola mundo'
var2 = ''
print(var1)

def minombre():
        name = input('Cual es tu nombre?\n')
        print('Hola, %s.' % name)        
        st = name
        print(st[:4])
        if name == 's':
                var2 = 's'
        else:                       
                return False


while (var2==''):
        minombre()
