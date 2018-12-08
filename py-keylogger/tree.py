class Tree(object):
    """docstring for Tree"""

    def __init__(self, letter):
        # super(Tree, self).__init__()
        self.letter = letter
        self.children = []
        self.unic = 0


def add(node, count, word, unic):
	if count == (len(word)):
		# node.letter = word[count-1]
		node.unic = unic
		return
	for chaild in node.children:

		if chaild.letter == word[count]:
			node = chaild
			count = count + 1
			add(node, count, word, unic)
			return
	# print (word[count])
	new_node = Tree(word[count])
	node.children.append(new_node)
	node = new_node
	node.letter = word[count]
	count = count + 1
	add(node, count, word, unic)
	return


def find(root, word):
    uniPrint(0, root, word,root)


def uniPrint(count, root, word,ROOT):
    node = root
    temp = root
    state = 0
    if count >= (len(word)+1):
        return

    for child in node.children:
        #print(child.unic)
        if count >= (len(word)):
            return

        if(child.letter == word[count]):
            temp = child
            state = 1
            uniPrint(count+1,child,word,ROOT)
            break
        else:
            pass
    if(state == 0):
        print(root.unic)
        uniPrint(count,ROOT,word,ROOT)

   

    return
root = Tree('*')
add(root,0, "a", 'A')
add(root,0, "m", 'M')
add(root,0, "t", 'T')
add(root,0, "k", 'K')
add(root,0, "p", 'P')
add(root,0, "r", 'R')
add(root,0, "ra", 'RA')
add(root,0, "ch", 'CH')
add(root,0, "cha", 'CHA')
add(root,0, "th", 'TH')
add(root,0, "thu", 'THU')
add(root,0, "u", 'U')
add(root,0, "n", 'N')
add(root,0, "g", 'G')
add(root,0, "ga", 'GA')
add(root,0, "i", 'I')
add(root,0, "l", 'L')
find(root, "chathurangachathurangachathurangachathurangachathurangachathurangachathurangachathurangachathurangachathuranga")
