import data_tree as tree

def get_unicode(root, word):
    un = ""
    word += '*'
    uniPrint(0, root, word, root, 1, un)


def uniPrint(count, root, word, ROOT, s, un): 
    node = root
    temp = root
    state = 0
    puni = '\u0000'
    if count >= (len(word)+1):

        print("exit")
        return

    for child in node.children:
        if count >= (len(word)):
            #print("  ")
           
            log_file='new.txt'
            fob=open(log_file,'a')
            fob.write('\n')
            un = un.replace('*','')
            un = un.replace(' ','')
            print un.decode('unicode-escape')

            return 

        if(child.letter == word[count]):
            # print(222)
            temp = child
            state = 1

            uniPrint(count+1, child, word, ROOT, s, un)
            break
        else:
            pass
    val = ''
    if(state == 0):
        if(s == 1 ):
            val = root.unic[0]
            s = 0
            if(val == ''):
                val = root.unic[2]
                s = 2
        elif(s == 2):

            val = root.unic[0]
            s = 0
        else:
            val = root.unic[1]
            s = 1
            if(val == ''):
                val = '\u0DCA'
                val += root.unic[0]
                s = 0

        un += val


        uniPrint(count, ROOT, word, ROOT, s, un)
    return

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
    
    new_node = tree.Tree(word[count])
    node.children.append(new_node)
    node = new_node
    node.letter = word[count]
    count = count + 1
    add(node, count, word, unic, s)
    return

def add_unicode(root):
    add(root, 0, "*", ' ', 0)
    add(root, 0, "sri", '\u0DC1\u0DD3\u0DD6', 0)
    add(root, 0, "k", '\u0D9A', 0)
    add(root, 0, "Kh", '\u0D9B', 0)
    add(root, 0, "g", '\u0D9C', 0)
    add(root, 0, "Gh", '\u0D9D', 0)
    add(root, 0, "NG", '\u0D9E', 0)
    add(root, 0, "G", '\u0D9F', 0)
    add(root, 0, "ch", '\u0DA0', 0)
    add(root, 0, "cj", '\u0DA1', 0)
    add(root, 0, "j", '\u0DA2', 0)
    add(root, 0, "JH", '\u0DA3', 0)
    add(root, 0, "NY", '\u0DA4', 0)
    add(root, 0, "JNY", '\u0DA5', 0)
    add(root, 0, "NYJ", '\u0DA6', 0)
    add(root, 0, "t", '\u0DA7', 0)
    add(root, 0, "T", '\u0DA8', 0)
    add(root, 0, "d", '\u0DA9', 0)
    add(root, 0, "Dh", '\u0DAA', 0)
    add(root, 0, "N", '\u0DAB', 0)
    add(root, 0, "ND", '\u0DAC', 0)
    add(root, 0, "th", '\u0DAD', 0)
    add(root, 0, "Th", '\u0DAE', 0)
    add(root, 0, "dh", '\u0DAF', 0)
    add(root, 0, "Dh", '\u0DB0', 0)
    add(root, 0, "n", '\u0DB1', 0)

    add(root, 0, "Dh", '\u0DB3', 0)
    add(root, 0, "p", '\u0DB4', 0)
    add(root, 0, "Ph", '\u0DB5', 0)
    add(root, 0, "b", '\u0DB6', 0)
    add(root, 0, "Bh", '\u0DB7', 0)
    add(root, 0, "m", '\u0DB8', 0)
    add(root, 0, "Mb", '\u0DB9', 0)
    add(root, 0, "y", '\u0DBA', 0)
    add(root, 0, "r", '\u0DBB', 0)
    add(root, 0, "l", '\u0DBD', 0)
    add(root, 0, "v", '\u0DC0', 0)
    add(root, 0, "w", '\u0DC0', 0)
    add(root, 0, "sh", '\u0DC1', 0)
    add(root, 0, "Sh", '\u0DC2', 0)
    add(root, 0, "s", '\u0DC3', 0)
    add(root, 0, "h", '\u0DC4', 0)
    add(root, 0, "L", '\u0DC5', 0)
    add(root, 0, "f", '\u0DC6', 0)
    add(root, 0, "NN", '\u0D82', 2)

    add(root, 0, "a", '*', 1)
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
    add(root, 0, "RR", '\u0DCA\u200D\u0DBB', 1)
    add(root, 0, "RRi", '\u0DCA\u200D\u0DBB\u0DD2', 1)
    add(root, 0, "RRii", '\u0DCA\u200D\u0DBB\u0DD3', 1)


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
    return root
