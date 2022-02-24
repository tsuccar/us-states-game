
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
print(df)

records = df.to_records(index=False)
result = list(records)
print(result)