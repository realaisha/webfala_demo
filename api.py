def exchange(dollar, rate=1550):
    '''A function that converts Dollar to naira'''
    naira = dollar*rate
    print('NGN',naira)
    
exchange(float(input('Enter in dollar💲:')))