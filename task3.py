LoTM_dec = {
    "Name": "Lord of the Mysteries",
    "Author": "Cuttlefish That Loves Diving",
    "Year": 2018,
    "Genre": "Fantasy, Mystery, Adventure"
}
print(LoTM_dec["Name"])

print("Book Information:")
for key, value in LoTM_dec.items():
    print(f"{key}: {value}")

print(LoTM_dec.values())
print(LoTM_dec.keys())

Year = LoTM_dec.update({"Year": 2020})

print(f"Updated Year: {LoTM_dec['Year']}")