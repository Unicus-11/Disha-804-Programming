#Word Frequency Counter
#Take a paragraph of text as input and print the top 3 most frequent words_HashMap, Sorting, Strings
text = "Hello, I am Disha from BCA EB section.And want to join ACE society programming .I am currently solving the question of text Word Frequency Counter: Take a paragraph of text as input and print the top 3 most frequent words using HashMap, Sorting, and String operations. Trutfully I don't know what hasmap is "

words = text.split() # Using split to collect word from text 

#class_type = type(words) This split method create a list. Uncomment it to find
#print(class_type) 


word_count = {} # empty dictionary 

for word in words:
    word_count[word] = word_count.get(word, 0) + 1 
    
    # get method_Return the value for key if key is in the dictionary, else default.Here we add 0 in place of default for calculation 

#Sort words by frequency (descending) and get top 3

most_words = sorted(word_count.items(), key=lambda x: -x[1])[:3]

print("Top 3 most frequent words:")

for word, freq in most_words:
    print(f"{word} -> {freq}")
    


 

