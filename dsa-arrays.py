expenses = [2200, 2350, 2600, 2130, 2190]
months = ["January", "February", "March", "April", "May"]
# 1. 
extra_feb = expenses[1] - expenses[0]
print(f"1. Extra spent in February compared to January: ${extra_feb}")
# 2. 
total_q1 = sum(expenses[:3])
print(f"2. Total expense in the first quarter: ${total_q1}")
# 3.
spent_2000 = 2000 in expenses
print(f"3. Did you spend exactly $2000 in any month? {spent_2000}")
# 4.
expenses.append(1980)
months.append("June")
print(f"4. Expenses after adding June: {expenses}")
# 5.
expenses[3] -= 200
print(f"5. Expenses after a $200 refund in April: {expenses}")



# Qno2
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
# 1.
print("1. Length of the list:", len(heros))
# Add 'black panther' at the end
heros.append('black panther')
print("2. After adding 'black panther' at the end:", heros)
#  Move 'black panther' after 'hulk'
heros.remove('black panther')
hulk_index = heros.index('hulk')
heros.insert(hulk_index + 1, 'black panther')
print("3. After moving 'black panther' after 'hulk':", heros)
 
#  Replace 'thor' and 'hulk' with 'doctor strange' in one line
heros[1:3] = ['doctor strange']
print("4. After replacing 'thor' and 'hulk' with 'doctor strange':", heros)

#  Sort the list alphabetically
heros.sort()
print("5. Sorted hero list alphabetically:", heros)
