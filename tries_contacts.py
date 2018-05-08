class Tries:
    def __init__(self):
        self.root = Node('*')

    def add_contact(self, parent, contact):
        if len(contact) > 0:
            letter = contact[0]
            child = parent.children.get(letter)

            if child is None:
                parent.children[letter] = Node(letter)
                child = parent.children[letter]

            child.add_word()
            self.add_contact(child, contact[1:])

    def find_contact(self, parent, contact):
        if len(contact) > 0:
            letter = contact[0]
            child = parent.children.get(letter)

            if child is None:
                print(0)
            else:
                self.find_contact(child, contact[1:])
        else:
            print(parent.words_count)

class Node:
    def __init__(self, letter):
        self.children = {}
        self.letter = letter
        self.words_count = 0

    def add_word(self):
        self.words_count += 1

n = int(input().strip())
tries = Tries()

for a0 in range(n):
    op, contact = input().strip().split(' ')

    if op == 'add':
        tries.add_contact(tries.root, contact)
    elif op == 'find':
        tries.find_contact(tries.root, contact)
