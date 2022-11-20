#Node class to create a new node for optimal binary serach tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


#Level order traversal of the optimal binary search tree
def height(node): 
    if node is None: 
        return 0 
    else : 
     
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1
        
def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        print('........................................................................')
        x=[]
        print("Level:",i)
        printGivenLevel(root, i,x) 
        print(x)
    print('........................................................................')
  
  

def printGivenLevel(root , level,x): 
    if root is None: 
        return
    if level == 1: 
        x.append(root.data) 
    elif level > 1 : 
        printGivenLevel(root.left , level-1,x) 
        printGivenLevel(root.right , level-1,x)
        
        
#Function to return level for a word that has been serched by the user       
def getLevelUtil(node, data, level): 
    if (node == None): 
        return 0
  
    if (node.data == data) : 
        return level  
  
    downlevel = getLevelUtil(node.left, data, level + 1)  
    if (downlevel != 0) : 
        return downlevel  
  
    downlevel = getLevelUtil(node.right, data, level + 1)  
    return downlevel  
  
def getLevel(node, data) : 
    return getLevelUtil(node, data, 1)  


#Input text file for the data of optimal binary search tree
words = []
with open('input.txt','r') as file:      
    for line in file:     
        for word in line.split():   
            words.append(word)
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''
dict_list=[]
for word in words:
    no_punct = ""
    for char in word:
        if char not in punctuations:
            no_punct = no_punct + char
    if no_punct != "":
        dict_list.append(no_punct.lower())
key = []
for word in dict_list:
    if word not in key:
        key.append(word)
freq = []
for i in range(len(key)):
    freq.append(dict_list.count(key[i]))
    

#Cost of the optimal binary serach tree
def summ(P, I, J):
    sum_p = 0
    for m in range(I, J + 1):
        sum_p += P[m][1]
    return sum_p

n = len(key)
keys = []

for i in range(n):
    keys.append((key[i],freq[i]))


keys.sort(key = lambda x: x[0])
R = [[0 for x in range(n + 1)] for y in range(n + 1)]
A = [[0 for x in range(n + 1)] for y in range(n + 1)]
for i in range(n):
   
    A[i][i - 1] = 0
    R[i][i - 1] = 0
   
    A[i][i] = keys[i][1]
    R[i][i] = i
    
for diagonal in range(n):
    for i in range(n - diagonal):
        j = i + diagonal
        if i < j:
            min_list = []
            for k in range(i, j + 1):
              
                min_list.append(((A[i][k - 1] + A[k + 1][j]), k))
            min_list.sort()
            A[i][j] = min_list[0][0] + summ(keys, i, j)
            R[i][j] = min_list[0][1]
            

def tree(keys, k, i, j):
    r = k[i][j]

    if i == j:
        root = Node(keys[r][0])

    else:
        root = Node(keys[r][0])
        if i <= r - 1:
            root.left = tree(keys, k, i, r - 1)
        if r + 1 <= j:
            root.right = tree(keys, k, r + 1, j)

    return root

root = tree(keys, R, 0, n - 1)
print('Cost of Optimal binary search is ' + str(A[0][n - 1]))


#printing of the OBST and finding the word
printLevelOrder(root)
search_word = input("Enter the keyword to find:")
depth = getLevel(root,search_word)
if depth != 0:
    print(search_word,"found at depth :",depth)
else:
    print(search_word,"not found!!")