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

class Node(object):
    sums = []

    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def insert_tree_node(self, x):
        if self.value:
            if x < self.value:
                if self.left is None:
                    self.left = Node(x)
                else:
                    self.left.insert_tree_node(x)
            elif x > self.value:
                if self.right is None:
                    self.right = Node(x)
                else:
                    self.right.insert_tree_node(x)
        else:
            self.value = x

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value),
        if self.right:
            self.right.print_tree()

    def all_paths_sums(self, progressive_sum):
        progressive_sum = progressive_sum + self.value
        if self.left is None and self.right is None:
            self.sums.append(progressive_sum)
            print(self.sums)
        if self.left:
            self.left.all_paths_sums(progressive_sum)
        if self.right:
            self.right.all_paths_sums(progressive_sum)

    def has_path_with_sum(self, sum):
        self.sums = []
        print(self.sums)
        self.all_paths_sums(0)
        print(self.sums)
        answer = False
        if sum in self.sums:
            answer = True
        return answer

    # from exercises import Node
    # root = Node(20)
    # root.insert_tree_node(5)
    # root.insert_tree_node(60)
    # root.insert_tree_node(39)
    # root.insert_tree_node(7)
    # root.insert_tree_node(40)
    # root.insert_tree_node(21)
    # root.insert_tree_node(110)
    # root.insert_tree_node(11)
    # root.insert_tree_node(1)
    # root.has_path_with_sum(26)


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
