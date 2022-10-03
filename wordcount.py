"""Count words in file."""


# put your code here.
# test_file = open('test.txt')

# def each_word_count(test_file):
#     '''Return a dictionary of word:word count'''

#     word_counts = {}

    

#     for line in test_file:
#         words = line.strip().split(' ')

#         for word in words:
#             word_counts[word] = word_counts.get(word, 0) + 1

#     return word_counts


# word_counts = each_word_count(test_file)

# for word, word_count in word_counts.items():
#     print(f'{word} {word_count}')

# test_file.close()

test_file = open('twain.txt')

def each_word_count(test_file):
    '''Return a dictionary of word:word count'''

    word_counts = {}

    

    for line in test_file:
        words = line.strip().split(' ')

        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


word_counts = each_word_count(test_file)

for word, word_count in word_counts.items():
    print(f'{word} {word_count}')

test_file.close()


