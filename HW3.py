##EX1
def remove_stop_words(word, stop_list):
    if word in stop_list:
        return False
    return True


def remove_numbers(word):
    if word.isnumeric():
        return False
    return True


def remove_max_suffix(word, suffix_l):
    if len(suffix_l):
        return word[:-len(max(suffix_l, key=len))]
    return word


def relevant_suffix(word, stem_l):
    return tuple(filter(lambda suffix: word.endswith(suffix), stem_l))


def get_bigrams(text, stop_list, stem_rules):
    x = list(filter(lambda n: remove_stop_words(n, stop_list=stop_list), filter(remove_numbers, text.lower().split())))
    y = list(map(lambda word: relevant_suffix(word, stem_rules), x))
    z = list(map(remove_max_suffix, x, y))
    print(tuple((z[i], z[i + 1]) for i in range(len(z) - 1)))

print('#######EX1')
stop_list = ('is', 'it', 'are', 'our', 'my', 'the', 'they', 'and')
stem_rules = ('less', 'ship', 'ing', 'es', 'ly', 's')
text = 'My 100 friends are very friendly They are keeping our friendship'
get_bigrams(text,stop_list,stem_rules)


##EX2
def add_two_shapes(shape_a,shape_b):
    return shape_a.perimeter() + shape_b.perimeter()
class Square:
    def __init__(self,a):
        self.a=a
    def __str__(self):
        return 'Square with side  {}'.format(self.a)
    def __add__(self,other):
        return add_two_shapes(self,other)
    def __repr__(self):
        return f'Square({self.a})'
    def perimeter(self):
        return self.a*4


class Triagle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __str__(self):
        return 'Triangle with sides equal {}, {}, and {}'.format(self.a,self.b,self.c)
    def __add__(self,other):
        return add_two_shapes(self,other)
    def __repr__(self):
        return f'Triagle({self.a},{self.b},{self.c})'
    def perimeter(self):
        return self.a+self.b+self.c

types_tag = {Triagle: 'shape',Square: 'shape'}
def add(z1,z2):
    types = frozenset((types_tag[type(z1)],types_tag[type(z2)]))
    return add.implementation[types](z1,z2)

add.implementation={}
add.implementation[frozenset(("shape","shape"))] = add_two_shapes

print('#######EX2')
t = Triagle(1,2,3)
print(t.perimeter())
6
s = Square(2)
print(s.perimeter())
8
print(s+s)
16
print(t+s)
14
print(add(s,t))
14
z = eval(repr(t))
print(t)


##EX3
class Node(object):

    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d

class LinkedList (object):
    def __init__(self):
        self.root = None
        self.size = 0

    def get_size (self):
        return self.size

    def listprint(self):
        printval = self.root
        while printval is not None:
            print (printval.data)
            printval = printval.next_node

    def insert(self, d):
        new_node = Node (d)
        if self.root == None:
            self.root = new_node
            self.size += 1
            return
        prev = self.root
        while prev.next_node:
            prev = prev.next_node
        prev.next_node =new_node
        self.size +=1
        return

    def insert1(self, x, position):
        temp = Node(x);
        if position == 0 and self.root == None:
            temp.next = self.root;
            self.root = temp;
            return
        cur = self.root;
        for i in range(0, position - 1):
            cur = cur.next_node;
            if cur.next_node == None:
                break;
        temp.next_node = cur.next_node;
        cur.next_node = temp;



    def remove (self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True		# data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found


    def remove (self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True		# data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def DeleteBookAtPosition(self, n):

        # If linked list is empty
        if self.root == None:
            return

        # Store head node
        temp = self.root

        # If head needs to be removed
        if n == 0:
            self.root = temp.next_node
            temp = None
            return

        # Find previous node of the node to be deleted
        for i in range(n -1 ):
            temp = temp.next_node
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next_node is None:
            return

        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next_node.next_node

        # Unlink the node from linked list
        temp.next_node = None
        temp.next_node = next

    def search (self, d):

        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    def reverse(self):
        prev = None
        current = self.root
        while (current is not None):
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.root = prev

print('#######EX3')
myList = LinkedList()
myList.insert(1)
myList.insert(5)
myList.insert(3)
myList.insert(8)
myList.insert1(11,3)
print('print linked list ' )
myList.listprint()
print('search by value 1 ->index is {}'.format(  myList.search(1)) )
print('delete by index 1 ')
myList.DeleteBookAtPosition(2)
myList.listprint()

myList.reverse()
print('print linked list reverse 1' )
myList.listprint()




