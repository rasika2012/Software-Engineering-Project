
class Tree(object):
    """docstring for Tree"""

    def __init__(self, letter):
        # super(Tree, self).__init__()
        self.letter = letter
        self.children = []
        self.unic = ['', '', '']
        self.s = 0


def add(node, count, word, unic, s):
    if count == (len(word)):
        node.unic[s] = unic
        # print(node.unic)
        return

    for chaild in node.children:

        if chaild.letter == word[count]:
            node = chaild
            count = count + 1
            add(node, count, word, unic, s)
            return

    new_node = Tree(word[count])
    node.children.append(new_node)
    node = new_node
    node.letter = word[count]
    count = count + 1
    add(node, count, word, unic, s)
    return


def find(root, word):
    print(word)
    un = ""

    print(un)
    uniPrint(0, root, word, root, 0, un)


def uniPrint(count, root, word, ROOT, s, un):
    # print(root.unic)
    node = root
    temp = root
    state = 0
    puni = '\u0000'
    if count >= (len(word)+1):
        print("exit")
        return

    for child in node.children:
        if count >= (len(word)):
            print("  ")
            print(un)
            return

        if(child.letter == word[count]):
            # print(222)
            temp = child
            state = 1

            uniPrint(count+1, child, word, ROOT, s, un)
            break
        else:
            pass

    if(state == 0):
        if(s == 1 | s == 2):
            val = root.unic[0]
            s = 0
            if(val == ''):
                val = root.unic[2]
                s = 2

        else:
            # print(root.unic)
            # print(root.unic[0])
            val = root.unic[1]
            s = 1
            if(val == ''):
                val = root.unic[0]
                s = 0
                if(val == ''):
                    val = root.unic[2]
                    s = 2

        #print(val, end=' ')
        un += val

        uniPrint(count, ROOT, word, ROOT, s, un)
    return


root = Tree('*')

add(root, 0, "ka", '\u0D9A', 0)
add(root, 0, "k", '\u0D9A', 0)
add(root, 0, "kha", '\u0D9B', 0)
add(root, 0, "ga", '\u0D9C', 0)
add(root, 0, "gha", '\u0D9D', 0)
add(root, 0, "nga", '\u0D9E', 0)
add(root, 0, "nnga", '\u0D9F', 0)
add(root, 0, "cha", '\u0DA0', 0)
add(root, 0, "chaa", '\u0DA1', 0)
add(root, 0, "ja", '\u0DA2', 0)
add(root, 0, "jha", '\u0DA3', 0)
add(root, 0, "nya", '\u0DA4', 0)
add(root, 0, "jnya", '\u0DA5', 0)
add(root, 0, "nyja", '\u0DA6', 0)
add(root, 0, "tta", '\u0DA7', 0)
add(root, 0, "ttha", '\u0DA8', 0)
add(root, 0, "dda", '\u0DA9', 0)
add(root, 0, "ddha", '\u0DAA', 0)
add(root, 0, "nna", '\u0DAB', 0)
add(root, 0, "nndda", '\u0DAC', 0)
add(root, 0, "th", '\u0DAD', 0)
add(root, 0, "tha", '\u0DAE', 0)
add(root, 0, "da", '\u0DAF', 0)
add(root, 0, "dha", '\u0DB0', 0)
add(root, 0, "na", '\u0DB1', 0)

add(root, 0, "nda", '\u0DB3', 0)
add(root, 0, "pa", '\u0DB4', 0)
add(root, 0, "pha", '\u0DB5', 0)
add(root, 0, "ba", '\u0DB6', 0)
add(root, 0, "bha", '\u0DB7', 0)
add(root, 0, "ma", '\u0DB8', 0)
add(root, 0, "mba", '\u0DB9', 0)
add(root, 0, "ya", '\u0DBA', 0)
add(root, 0, "ra", '\u0DBB', 0)
add(root, 0, "la", '\u0DBD', 0)
add(root, 0, "va", '\u0DC0', 0)
add(root, 0, "sha", '\u0DC1', 0)
add(root, 0, "ssa", '\u0DC2', 0)
add(root, 0, "sa", '\u0DC3', 0)
add(root, 0, "ha", '\u0DC4', 0)
add(root, 0, "lla", '\u0DC5', 0)
add(root, 0, "fa", '\u0DC6', 0)

add(root, 0, "aa", '\u0DCF', 1)
add(root, 0, "ae", '\u0DD0', 1)
add(root, 0, "aae", '\u0DD1', 1)
add(root, 0, "i", '\u0DD2', 1)
add(root, 0, "ii", '\u0DD3', 1)
add(root, 0, "u", '\u0DD4', 1)
add(root, 0, "uu", '\u0DD6', 1)
add(root, 0, "r", '\u0DD8', 1)
add(root, 0, "e", '\u0DD9', 1)
add(root, 0, "ee", '\u0DDA', 1)
add(root, 0, "ai", '\u0DDB', 1)
add(root, 0, "o", '\u0DDC', 1)
add(root, 0, "oo", '\u0DDD', 1)
add(root, 0, "au", '\u0DDE', 1)
add(root, 0, "I", '\u0DDF', 1)
add(root, 0, "rr", '\u0DF2', 1)
add(root, 0, "II", '\u0DF3', 1)

add(root, 0, "a", '\u0D85', 2)
add(root, 0, "aa", '\u0D86', 2)
add(root, 0, "ae", '\u0D87', 2)
add(root, 0, "aae", '\u0D88', 2)
add(root, 0, "i", '\u0D89', 2)
add(root, 0, "ii", '\u0D8A', 2)
add(root, 0, "u", '\u0D8B', 2)
add(root, 0, "uu", '\u0D8C', 2)
add(root, 0, "r", '\u0D8D', 2)
add(root, 0, "rr", '\u0D8E', 2)
add(root, 0, "I", '\u0D8F', 2)
add(root, 0, "II", '\u0D90', 2)
add(root, 0, "e", '\u0D91', 2)
add(root, 0, "ee", '\u0D92', 2)
add(root, 0, "ai", '\u0D93', 2)
add(root, 0, "o", '\u0D94', 2)
add(root, 0, "oo", '\u0D95', 2)
add(root, 0, "au", '\u0D96', 2)
# print('\u0D9A\u0DCA')
while(1):
    a = "                "
    a = input()
    find(root, a)
