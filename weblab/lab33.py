'''

filename = input("Enter file name: ")
with open(filename, 'r') as file:
    content = file.read()

words = content.lower().split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("\nTop 10 Words:")
for i in range(min(10, len(sorted_items))):
    print(sorted_items[i][0], "->", sorted_items[i][1])

'''

def get_word_counts(file):
    word_freq = {}
    for line in file:
        words = line.strip().lower().split()
        for word in words:
            word = word.strip('.,"(){}[]!')
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq

file = open('input.txt', 'r')
word_counts = get_word_counts(file)

sorted_counted = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
print(sorted_counted)