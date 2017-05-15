import os
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
def word_count(text):
    text=text.lower()
    skips=[".",",",";",":","'",'"',"(",")"]
    for ch in skips:
        text=text.replace(ch,"")
    
    wordcount=Counter(text.split(" "))
    return wordcount

def read_book(title_path):
    with open(title_path,"r",encoding="utf8") as current_book:
        text=current_book.read()
        text=text.replace("\n","").replace("\r","")
    return text
    
    
def word_stat(wordcount):
    num_uniq=len(wordcount)
    counts=wordcount.values()
    return (num_uniq,counts)
    
def main(): 
    
    stats=pd.DataFrame(columns=("language","author","title","length","unique"))
    num=1
    book_dir="Books"
    for language in os.listdir(book_dir):
        for author in os.listdir(book_dir + "/" + language):
            for title in os.listdir(book_dir + "/" + language + "/"+ author):
                inputfile=book_dir + "/" + language + "/"+ author + "/" + title
                print(inputfile)
                text=read_book(inputfile)
                (num_unique,counts)=word_stat(word_count(text))
                stats.loc[num]= language, author.upper(), title.replace(".txt",""), sum(counts), num_unique
                num+=1
    print("\n\n The table of data is ",stats)
    plt.figure(figsize =(10,10))
    subset=stats[stats.language=="English"]
    plt.loglog(subset.length,subset.unique,"bo",label="English")
    subset=stats[stats.language=="French"]
    plt.loglog(subset.length,subset.unique,"go",label="French")
    subset=stats[stats.language=="German"]
    plt.loglog(subset.length,subset.unique,"yo",label="Gremen")
    subset=stats[stats.language=="Portuguese"]
    plt.loglog(subset.length,subset.unique,"ro",label="Portuguese")
    plt.legend()
    plt.xlabel("book length")
    plt.ylabel("number of unique words")
    plt.savefig("graph.pdf")
if "__name__"==main():
    main() 
    
            

    