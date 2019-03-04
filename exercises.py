import operator


# Rotate Image

def rotate_image(matrix):
    new_matrix = []
    for element in matrix:
        new_matrix.append([])
    matrix.reverse()
    for index, element in enumerate(matrix[0]):
        new_matrix[index].append(element)
        for row in matrix[1:]:
            new_matrix[index].append(row[index])
    print(new_matrix)


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

######################################################################################

# class Node(object):
#     def __init__(self, x):
#         self.value = x
#         self.left = None
#         self.right = None
#
#
# def create_binary_tree(x):
#     if (x >= 2):
#         print(x)
#         node = Node(x)
#         less = int(x / 2)
#         more = x * 2
#         node.left = less
#         node.right = more
#         create_binary_tree(node.left)
#         create_binary_tree(node.right)


# def has_path_with_given_sum(tree, sum):

######################################################################################


# Word Ladder

start_word = 'cat'
goal_word = 'dog'
usable_words = ['lol', 'hey', 'bat', 'bot', 'dot', 'bow', 'dok', 'hok', 'hog']


def longest_word_ladder(start_word, goal_word, usable_words):
    result_array = []
    result_array.append(start_word)
    while start_word != goal_word:
        matching_words = number_of_matching_words(start_word, usable_words)
        if len(matching_words) == 1:
            result_array.append(matching_words[0])
            start_word = matching_words[0]
            usable_words.remove(start_word)
        elif len(matching_words) > 1:
            result_array.append(best_option_to_choose(matching_words, usable_words))
            start_word = best_option_to_choose(matching_words, usable_words)
            usable_words.remove(start_word)
        elif len(matching_words) == 0:
            return []
        if words_match(start_word, goal_word) and len(number_of_matching_words(goal_word, usable_words)) == 0:
            result_array.append(goal_word)
            start_word = goal_word
    return result_array


def words_match(word1, word2):
    count = 0
    for index, character in enumerate(list(word1)):
        if character != word2[index]:
            count = count + 1
    if count == 1:
        return True
    return False


def number_of_matching_words(word, array_of_words):
    count = 0
    matching_words = []
    for element in array_of_words:
        for index, character in enumerate(list(element)):
            if character != word[index]:
                count = count + 1
        if count == 1:
            matching_words.append(element)
        count = 0
    return matching_words


def best_option_to_choose(array_of_possible_words, array_of_all_words):
    matching_words = {}
    for element in array_of_possible_words:
        if len(number_of_matching_words(element, array_of_all_words)) is not 0:
            matching_words[element] = len(number_of_matching_words(element, array_of_all_words))
    return min(matching_words.items(), key=operator.itemgetter(1))[0]
