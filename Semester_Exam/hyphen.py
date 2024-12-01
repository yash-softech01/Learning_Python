# Python Program to Accept a Hyphen Separated Sequence of Words as Input and Print the Words in a Hyphen-Separated Sequence after Sorting them Alphabetically

# Input: Hyphen-separated sequence of words
sequence = input("Enter a hyphen-separated sequence of words: ")

# Split the sequence into a list of words
words = sequence.split('-')

# Sort the words alphabetically
sorted_words = sorted(words)

# Join the sorted words back into a hyphen-separated sequence
result = '-'.join(sorted_words)

# Output the result
print("Sorted sequence:", result)
