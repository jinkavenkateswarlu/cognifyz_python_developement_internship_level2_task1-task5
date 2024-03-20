def count_word_occurrences(file_path):
    word_counts = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip().lower().strip('.,!?;:"')
                if word:
                    word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def display_word_counts(word_counts):
   
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])

    for word, count in sorted_word_counts:
        print(f"{word}: {count}")
file_path = 'example.txt'  
word_counts = count_word_occurrences(file_path)
display_word_counts(word_counts)
