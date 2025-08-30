age = int(input('ENTER YOUR AGE - '))

if age>=18:
    voterid = input('DO YOU HAVE VOTER ID? (y:YES | n:NO) - ')
    if voterid=='y' or voterid=='Y':
        print('CONGRATULATIONS! YOU CAN VOTE.')
    else:
        print('SORRY! YOU CAN NOT VOTE.')
else:
    print('YOU ARE NOT ELIGIBLE')