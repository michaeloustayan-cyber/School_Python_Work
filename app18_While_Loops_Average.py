'''
practice while loops and testing commit and push
customer buys items. this total amount is random.
The goal is to find the average cost of the items.
'''

count_item = int(input("How many items are you buying?: "))
count = 1
total = 0
while count <= count_item:
    price = float(input("Enter the prices of each item: "))
    count += 1
    total += price / count_item
print(f"Average Cost of products is: {total:.2f}")
