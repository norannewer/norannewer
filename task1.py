documents = [
    "new home sales top forecasts",
    "home sales rise in July",
    "increase in home sales in July",
    "July new home sales rise",
]

inverted_index = {}

for i, document in enumerate(documents):
    for word in document.split():
        if word not in inverted_index:
            inverted_index[word] = [i + 1]
        else:
            inverted_index[word].append(i + 1)

term = input("Enter a term: ")

postings_list = inverted_index.get(term, [])

print(postings_list)
