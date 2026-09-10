'''
ATM project
-------------
'''
vamsi_details_sbi ={
    'name':'vamsi',
    'adr':'0987654321',
    'pan':'india1234l',
    'atmpin':'2005',
    'balance':10000,
    'MINI state': []
}
all_attempts=3
while all_attempts >0:
    user_pin=input('Enter your atm pin:')
    if len(user_pin) != 4:
        print('atmpin must contain 4 digits')
        continue
    if user_pin in vamsi_details_sbi['atmpin']:
        print('welcome sbi atm')
        choice_=int(input('Enter \n1.withdraw \n2.deposited \n3.Balance \n4.Select one: '))
        if choice_==1:
            with_m=int(input('Enter amount to withdraw:'))
            if with_m<=vamsi_details_sbi['balance'] and with_m%100==0:
                vamsi_details_sbi['balance'] -=with_m
                print(f'take your cash and the balance is {vamsi_details_sbi['balance']}')
                vamsi_details_sbi['MINI state'].append(f'withdrawl: {with_m}')
                
                user_opt = int(input('Enter \n1.Home page \n2.Exit:'))
                if user_opt ==1:
                    print('Taking to Home page')
                    continue
                elif user_opt ==2:
                    print('Thanks for visiting')
                    break
                
            else:
                print('insufficient balance or this can not provide change')
                break
        elif choice_ ==2:
            dept_m=int(input('Enter deposit amount:'))
            if dept_m%100==0:
                vamsi_details_sbi['balance']+=dept_m
                print(f'amount to deposit and total amount in the bank {vamsi_details_sbi['balance']}')
                vamsi_details_sbi['MINI state'].append(f'deposite: {dept_m}')
                print(f'{vamsi_details_sbi['MINI state']}')

                user_opt = int(input('Enter \n1.Home page \n2.Exit:'))
                if user_opt ==1:
                    print('Taking to Home page')
                    continue
                elif user_opt ==2:
                    print('Thanks for visiting')
                    break
                
            else:
                print('this atm is not accept change')
        elif choice_==3:
                print(f'your balance is {vamsi_details_sbi['balance']}')
        break
    else:
        all_attempts -=1
        if all_attempts >0:
            print(f'incorrect pin entered and you have {all_attempts}')
        else:
            print('your card is blocked..')





































    









