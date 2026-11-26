while True:
    print('========== CALCULATOR ==========')
    print('1. ADDITION (+)')
    print('2. SUBTRACTION (-)')
    print('3. MULTIPLICATION (*)')
    print('4. DIVISION (/)')
    print('5. EXPONENT (a^b)')
    print('6. EXIT')

    choice = int(input('enter your operation (select number !!!) : '))
    if choice == 6:
        print('========== EXIT ==========')
        break
    
    
    if choice not in [1,2,3,4,5,6]:
        continue
    
    num1 = float(input('a = '))
    num2 = float(input('b = '))



    if choice == 1:
        print(f'a+b = {num1 + num2}')


    if choice == 2:
        print(f'a-b = {num1 - num2}')

    if choice == 3:
        print(f'a*b = {num1 * num2}')

    if choice == 4:
        if num2 == 0:
            print('invalid operation')
            continue
        print(f'a/b = {num1 / num2}')
    if choice == 5:
        print(f'a^b = {num1**num2}')

    
    