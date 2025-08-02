import sys 
import re
def word_frequency_counter(file_name,top_num):
    with open(file_name, 'r',encoding='utf-8') as file:
        text=file.read()
        words=text.split()
#words = re.findall(r'\b\w+\b', text.lower())

        word_frequency={}
        for word in words:
            if word in word_frequency:
                word_frequency[word]+=1
            else:
                word_frequency[word]=1
        print(word_frequency)
        sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

# הדפסת top_num מילים
#for word, freq in sorted_words[:top_num]:
#    print(f"{word}: {freq}")

        
word_frequency_counter("c:/inetpub/wwwroot/CSharp/OR_JS_16.12.2024/excersize_7/homework/notes.txt", 1)

                