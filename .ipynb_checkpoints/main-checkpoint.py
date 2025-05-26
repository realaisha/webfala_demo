class Expense:
    def __init__(self, name, amount, category):
        """
        Initialize an expense object
        :param name (str): the name of the expense
        :param amount (float): the amount of the expense
        :param category (str): the category of the expense
        """
        self.name = name
        self.amount =  amount
        self.category = category

    def __str__(self):
        """
        String representation on an expense object
        :return (str): formatted string with expense details
        """
        return f'{self.name}: ₦{self.amount} {self.category}'

class ExpenseTracker:
    def __init__(self, filename='expenses.txt'):
        """
        INitializes an ExpenseTracker object
        :param filename (str): the file to store expenses
        """
        self.filename = filename
        self.expenses = self.load_expenses()

    def add_expenses(self, expense):
        """  
        Add an expense to the tracker
        :param expense (Expense): the expense to add
        """
        self.expenses.append(expense)
        self.save_expenses()

    def load_expenses(self):
        """
        Load expenses from the file
        :return list: list of Expense objects
        """
        expenses = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, amount, category = line.strip().split(',')
                    expense = Expense(name, float(amount), category)
                    expenses.append(expense)
        except FileNotFoundError:
            pass
        return expenses

    def save_expenses(self):
        """
        save expenses to the file
        """
        with open(self.filename, 'w')as file:
            for expense in self.expenses:
                file.write(f'{expense.name}, {expense.amount}, {expense.category}\n')

    def display_expenses(self):
        """
        Display all expenses
        """
        for expense in self.expenses:
            print(expense)

    def get_total_expense(self):
        """
        Calculate the total expense amount
        :return (float): total expense amount
        """
        return sum(expense.amount for expense in self.expenses)

tracker = ExpenseTracker()
while True:
    print ('\nExpense Tracker')
    print('1. Add Expense')
    print('2. view Expenses')
    print('3. Get Total Expense')
    print('4. Exit')

    choice = input('Choose an option: ')
    if choice =='1':
        name = input('Enter expense name: ')
        amount = float(input('Enter expense amount: '))
        category = input('Enter expense category: ')
        expense = Expense(name, amount, category)
        tracker.add_expenses(expense)
        print('Expense added.')
    elif choice == '2':
        print('\n Expenses:')
        tracker.display_expenses()
    elif choice == '3':
        total = tracker.get_total_expense()
        print(f'\n Total Expense: ₦{total}')
    elif choice == '4':
        break
    else:
        print('Invalid choice. Please try again.')