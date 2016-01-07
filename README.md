# Zipf's_Law

Goal of this project is verify Zipf's Law on a text document based on the following: 

Link to Zipf's law: https://en.wikipedia.org/wiki/Zipf%27s_law

1.  Download Alice in Wonderland by Lewis Carol (Plain Text UTF-8 format) from Gutenberg website. http://www.gutenberg.org/ebooks/11. 
2.  From the html file, strip off the header, and thus consider only the text starting at "ALICE'S ADVENTURES IN WONDERLAND", just preceding "CHAPTER 1"; also, strip off the footer, eliminating the license agreement and other extraneous text, and thus consider only the text up through, and including, "THE END". 
3.  Use the perl script(parse.pl) to strip the text of punctuation obtaining the original text as a list of words. For example, on a unix based systems, you should run a command like : parse.pl alice30.txt > out.txt
4.  Write code that counts word frequencies. For the most frequent 25 words and for the most frequent 25 additional words that start with the letter m (a total of 50 words), print the word, the number of times it occurs, its rank in the overall list of words, the probability of occurrence, and the product of the rank and the probability. Also indicate the total number of words and the total number of unique words that you found. 
5.  Discuss whether this text satisfies Zipf's Law.






