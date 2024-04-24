import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [25, 35, 30, 28],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}

df = pd.DataFrame(data)

mean_age = df['Age'].mean()

print("Mean Age")
print(mean_age)