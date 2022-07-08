user_input = 'random'
data = []
def show_menu
print ('Menu:'):
print('1. Add Item')
print ('2. Mark as done')
print('3. View Item')
print('4. Exit')
while user_input != '4'
show_menu

user_input = input('Enter your choice')

if user_input == '1':
    item = input ('what is to ne done?')
    data.append(item)
    print('Added Item', item)
    elif user_input == '2':     
        item = input ('what is to be marked as done?')
        if item in data:
            data.remove(item)
            print ('removed item' , item)
        else
        print('item does not exist in the list')    
     elif user_input == '3':
        print('list of items in the tod-list')
            for item in data:
            print (item)
     elif user_input == '4':
                print ('Goodbye')
else 
print ('Please select either 1,2,3 or 4')


