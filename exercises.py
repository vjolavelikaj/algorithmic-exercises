def rotate_array(array):
    new_array = []
    for element in array:
        new_array.append([])
    array.reverse()
    for index, element in enumerate(array[0]):
        new_array[index].append(element)
        for row in array[1:]:
            new_array[index].append(row[index])
    print(new_array)


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


##########################################################

class Node(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def create_binary_tree(x):
    if (x >= 2):
        print(x)
        node = Node(x)
        less = int(x / 2)
        more = x * 2
        node.left = less
        node.right = more
        create_binary_tree(node.left)
        create_binary_tree(node.right)

# def has_path_with_given_sum(tree, sum):
