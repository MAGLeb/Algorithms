class Node:
    def __init__(self, value=None, dictionary=None):
        if dictionary is None:
            dictionary = {}
        if value is None:
            value = []
        self.value = value
        self.dictionary = dictionary


def only_upper_case(string):
    result_string = ''

    for letter in string:
        if letter.isupper():
            result_string += letter

    return result_string


class Bor:
    def __init__(self):
        self.root_node = Node()

    def add_string(self, string):
        current_node = self.root_node
        only_upper_letters = only_upper_case(string)

        for index, upper_letter in enumerate(only_upper_letters):
            if index == len(only_upper_letters) - 1:
                if upper_letter in current_node.dictionary:
                    #TODO sort when add string
                    current_node.dictionary[upper_letter].value += [string]
                else:
                    current_node.dictionary[upper_letter] = Node([string])
            elif upper_letter in current_node.dictionary:
                current_node = current_node.dictionary[upper_letter]
            else:
                current_node.dictionary[upper_letter] = Node()
                current_node = current_node.dictionary[upper_letter]

    def find_strings_by_template(self, template):
        def recursive(node):
            result = []
            if node.value:
                result += node.value

            for key in node.dictionary:
                result += recursive(node.dictionary[key])

            return result

        current_node = self.root_node

        for letter in template:
            if letter in current_node.dictionary:
                current_node = current_node.dictionary[letter]
            else:
                return []

        results_string = recursive(current_node)

        return sorted(results_string)


f = open('K.txt', 'r')
number_strings = int(f.readline())
array_of_strings = []

for _ in range(number_strings):
    array_of_strings.append(f.readline().strip())

number_templates = int(f.readline())
array_of_templates = []

for _ in range(number_templates):
    array_of_templates.append(f.readline().strip())


def solution(array_strings, array_templates):
    bor = Bor()

    for string in array_strings:
        bor.add_string(string)

    for template in array_templates:
        result_array = bor.find_strings_by_template(template)
        for result_item in result_array:
            print(result_item)


solution(array_of_strings, array_of_templates)
