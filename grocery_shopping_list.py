# here we write function print_shopping_list()
# that select unique product names and add values

def print_shopping_list(dish1, dish2):
    data = set(dish1.keys()).union(dish2.keys())
    
    for i in data:              # check for two conditions in a loop
        amount = 0
        if i in dish1.keys():
            amount += dish1[i]
        if i in dish2.keys():
            amount += dish2[i]
            
        print(i + ':', amount)
        
# here we can change the names of the ingredients and their quantity
pizza = {'flour, kg': 1,
         'tomatoes, kg': 1.5,
         'champignons, kg': 1.5,
         'cheese, kg': 0.8,
         'olive oil, liters': 0.1,
         'yeast, gr.': 50}

salad = {'cucumbers, kg': 1,
         'peppers, kg': 1,
         'tomatoes, kg': 1.5,
         'olive oil, liters': 0.1,
         'lettuce, kg': 0.4}

print_shopping_list(pizza, salad)