import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')  # 列与列之间的分隔符
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1001', 'Mike', 20])
    writer.writerow(['1002', 'Bob', 21])
    writer.writerow(['1003', 'Jordan', 88])
    writer.writerows([['1004', 'Amy', 32], [1007, 'Ella', 21]])

with open('data.csv', 'a', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '1001', 'name': 'Mike', 'age': 20})



with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        print(row)

import pandas as pd

df = pd.read_csv('data.csv')
print(df)




