import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [25, 35, 30, 28],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}

df = pd.DataFrame(data)

selected_col = df [['Name','City']]

print("Selected Table:")
print(selected_col)