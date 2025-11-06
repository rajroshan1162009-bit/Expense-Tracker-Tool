#  Expense Tracker (Personal Finance Manager)
print('   --- Welcome to Expense Tracker Application ---   ')
# 1. Ask for some data and save into the file
def add_expenses():
    date = (input('Enter date (YYYY-MM-DD): ')).strip()
    category = input('Enter category: ').strip().title()
    try:
        amount = float(input('Enter amount: '))
    except ValueError:
        print('Invalid Amount! | Please enter a valid amount.')
        return
    description = input('provide details: ').strip()
    with open('expense.txt','a') as file:
        file.write(f'{date} | {category} | {amount} | {description}\n')
    print(f'Your expenses successfully save in our application✅')

# 2. Read file and display them to the user as output
def view_all_expenses():
    with open('expense.txt','r') as file:
        content = file.readlines()
    if not content:
        print('No expenses recorded yet!')
    else:
        print("Displaying all the expenses:\n")
        for i,line in enumerate(content,start=1):
            print(f'{i}. {line.strip()}')

# 3. Search expense by date and display them to the user
def search_expenses_by_date():
    search_date = input('Enter date (YYYY-MM-DD): ').strip()
    found = False
    with open('expense.txt','r') as file:
        content = file.readlines()
        for line in content:
            line = line.strip()
            if line:
                parts = [p.strip() for p in line.split("|")]
                date = parts[0]
                category = parts[1]
                amount = parts[2]
                description = parts[3]

                if date == search_date:
                    print(f'\nDate: {date}\nCategory: {category}\nAmount: {amount}\nDescription: {description}\n')
                    found = True
    if not found:
        print(f'No expenses recorded on {search_date}')
        
# 4. Calculate the total expense
def total_expense():
    with open('expense.txt','r') as file:
        content = file.readlines()
        total = 0
        for line in content:
            line = line.strip()
            if line:
                parts = line.split("|")
                amount = parts[2]
                amount = float(amount)
                total+=amount
        print(f'Your total spending is Rs {total}')

while True:
    try:
        print(f'Menu:\n1. Add Expenses\n2. View All Expenses\n3. Search Expenses by date\n4. Show Total Expenses\n5. Exit')
        user_choice = int(input('Enter your Choice(1-5): '))

        if user_choice == 1:
            add_expenses()

        elif user_choice == 2:
            view_all_expenses()

        elif user_choice == 3:
            search_expenses_by_date()

        elif user_choice == 4:
            total_expense()

        # 5. Exit from the program 
        elif user_choice == 5:
            print('Exiting from the program. | Thanks for using.')
            break

    except Exception:
        print('Error occur! | please Retry...')