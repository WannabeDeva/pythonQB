import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [25, 35, 30, 28],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}

index_labels = ['A','B','C','D']

df = pd.DataFrame(data, index_labels)

print("Table with index labels:")

print(df)