def word_frequency_counter(file_name,top_num):
    with open(file_name, 'r') as file:
        text=file.read()
        words=text.split()

        word_frequenc={}
        for word in words:
            if word in word_frequenc:
                word_frequenc[word]+=1
            else:
                word_frequenc[word]=1
        print(word_frequenc)
        
word_frequency_counter("notes.txt",3)

                