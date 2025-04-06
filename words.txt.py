# Function to read words from the file and return them in a list
def read_words_from_file(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words


# Function to sort the list alphabetically without using the sort or sorted functions
def sort_words(words):
    # Using a simple bubble sort algorithm
    for i in range(len(words)):
        for j in range(0, len(words) - i - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]
    return words


# Function to write the sorted list of words to a new file
def write_sorted_words_to_file(words, filename):
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + '\n')


# Main code to execute the functions
if __name__ == "__main__":
    # Create and write the words into words.txt
    words = ['cat', 'dog', 'animal', 'goat', 'sheep', 'monkey', 'turtle']
    with open('words.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')

    # Read the words from the file
    words_from_file = read_words_from_file('words.txt')

    # Sort the words
    sorted_words = sort_words(words_from_file)

    # Write the sorted words to a new file
    write_sorted_words_to_file(sorted_words, 'sorted_words.txt')
    print("Sorted words have been written to sorted_words.txt.")
