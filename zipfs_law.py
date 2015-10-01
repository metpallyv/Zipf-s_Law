__author__ = 'Vardhaman'
import sys
import operator

index = {}
total_words = 0
index_len = 0

#code the build the index
def build_index(file):
    global total_words
    input = open(file, 'r')
    count = 0
    for line in input.readlines():
        #print (line)
        if index.has_key(line):
            index[line] += 1
            count = count +1
        else:
            index[line] = 1
            count = count + 1
    index_len = len(index)
    total_words=count
    print("Total number of unique words are",index_len)
    print("Total number of words are",total_words)

#code to print the index values
def print_values():
    for keyword in index.keys():
        print("Keyword and value is", keyword, index.get(keyword))

#code to get the top k frequent words, in this case its 25
Freq = {}
def frequent_words():
    #print("Total number of words are",total_words)
    #for keyword in sorted(index, key=index.get, reverse=True):
    #    print ("The word",keyword.strip(),"Frequency is",index[keyword])
    Freq = sorted(index, key=index.get, reverse=True)
    rank = 1
    for i in range(25):
        prob = float(index[Freq[i]])/total_words
        print(Freq[i].strip(),"has a frequency of",index[Freq[i]],"and is ranked",rank,"with Probability of",prob,"r*Pr value of",rank*prob)
        rank = rank +1
    print("Now printing the data for keywords starting with m..")
    #This prints the top 25 keywords starting with "m"
    M_list = []
    flag = 0
    for k in Freq:
        if k.startswith('m') and (flag <=25):
            M_list.append(k)
            flag = flag +1
    rank =1
    for keyword in M_list:
        prob = float(index[keyword])/total_words
        rank = Freq.index(keyword)
        print(keyword.strip(),"has a frequency of",index[keyword],"and is ranked",rank,"with Probability of",prob,"r*Pr value of",rank*prob)
        '''for keyword in Freq:
            print("Word is",keyword.strip(),"Frequency is",index[keyword],"Rank is ",rank, "Probability is",index[keyword]/total_words)#terms/Freq[1])
            rank = rank + 1'''
  
if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = sys.argv[1]
        build_index(file)
        frequent_words()
        #print_values()
    else:
        print("Enter the Alice in wonderland file")
