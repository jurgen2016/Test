import random

koloda = [2,3,4,6,7,8,9,10,11]
random.shuffle(koloda)
print ('zdravstvujte!')
count=0

while True:
    choise = input('berite kartu?  y/n\n')
    if choise == 'y':
        current = koloda.pop()
        print('Вам попалась карта достоинством %d' %current)
        count += current
        if count > 21:
            print('sorry vy proigrali')
            break
        elif count ==21:
            print('vy vygtrali')
            break
        else:
            print ('u vas %d ochkov' %count)
            
    elif choise == 'n':
        print ('u vas 0 ochkov, game over'%count)
        break
    break
        
    

