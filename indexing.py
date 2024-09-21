#-------------------------------------------------------------------------
# AUTHOR: Erika Ledesma
# FILENAME: indexing.py
# SPECIFICATION: Reads provided 'collection.csv' file, calculates and returns a document-term matrix
# FOR: CS 4250- Assignment #1
# TIME SPENT: 5 HRS
#-----------------------------------------------------------*/

#Importing some Python libraries
import csv
import math
from tabulate import tabulate

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'her', 'They', 'their'}

#add defined stopwords into a new list
stopward_removal = []

for row in documents:
    split_row = row.split()
    for word in split_row:
        #Remove stopwords from the row of each document
        if word in stopWords:
            split_row.remove(word)
    stopward_removal.append(split_row)
            
#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {
    "cats": "cat",
    "dogs": "dog",
    "loves": "love"
}

stemmed_rows = []

for row in stopward_removal:
    res = []
    for word in row:
        res.append(stemming.get(word, word))
    res = ' '.join(res)
    stemmed_rows.append(res)

#Identifying the index terms.
#--> add your Python code here
# all words that have not been identified as stopwords
terms = []

for row in stemmed_rows:
    stemmed_split = row.split()
    for term in stemmed_split:
        if term not in terms:
            terms.append(term)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []
# for formatting table headers
docTermMatrix.append(terms)

# calculate idf
term_idfs = {}
for term in terms:
    count = 0
    for doc_rows in documents:
        if term in doc_rows:
            count += 1
    idf = math.log((len(documents)/count), 10)
    term_idfs[term] = idf

# calculate tf-idf
i = 1
for doc in stemmed_rows:
    row = []
    doc_split = doc.split()
    row.append(i)
    i += 1
    for term in terms:
        tf = doc_split.count(term) / len(doc_split)
        tf_idf = tf * term_idfs[term]
        row.append(tf_idf)
    docTermMatrix.append(row)

#Printing the document-term matrix.
#--> add your Python code here
print(tabulate(docTermMatrix, headers='firstrow', tablefmt='fancy_grid'))