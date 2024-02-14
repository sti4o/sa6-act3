strings = ["apple", "banana", "cherry", "date", "fig", "elderberry"]

sorted_strings = sorted(strings, key=lambda s: (len(s), s))


print(sorted_strings)
