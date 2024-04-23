# -*- coding: utf-8 -*-


# pip install nltk

# pip install newspaper3k

from newspaper import Article
import random , string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#Downloader !!
nltk.download('punkt')

#Download content !!
article=Article("https://www.drdo.gov.in/drdo/about-drdo")
article.download()
article.parse()
article.nlp()
corpus=article.text

#Display corpus!!
print(corpus)

# List of sentences!!
text=corpus
sentence_list=nltk.sent_tokenize(text)
# print(sentence_list)
# print("lenght of sentence_list: ",len(sentence_list))

#Bot Greetings Response!!
def bot_greetings(user_input):
  user_input=user_input.lower()

  bot_greetings=['hi','hello','hola','glad to see you','wassup']
  user_greetings=['hi','hello','hola','hey','greetings']

  for word in user_input.split():
    if word in user_greetings:
      return random.choice(bot_greetings)

def index_sort(list_var):
  length=len(list_var)
  index_list=list(range(0,length))

  var=list_var
  for i in range(length):
    for j in range(length):
      if var[index_list[i]]>var[index_list[j]]:
        temp=index_list[i]
        index_list[i]=index_list[j]
        index_list[j]=temp
  return index_list

#Bot Response!!
def bot_response(user_input):
  user_input=user_input.lower()
  sentence_list.append(user_input)
  bot_response=''
  cnt_mat=CountVectorizer().fit_transform(sentence_list)
  similarity_scores=cosine_similarity(cnt_mat[-1],cnt_mat)
  similarity_scores_list=similarity_scores.flatten()
  index=index_sort(similarity_scores_list)
  index =index[1:]
  response_flag=0

  redundant_response=0
  for i in range(len(index)):
    if similarity_scores_list[index[i]]>0.0:
      response_flag=1
      bot_response=bot_response+''+sentence_list[index[i]]
      redundant_response+=1

    if redundant_response >2:
      break

  if response_flag == 0:
    bot_response=bot_response+''+'I apologize, I dont understand :( )'
  sentence_list.remove(user_input)

  return bot_response

#Commence Conversation!!

print("COMET_GPT: I am COMET , I will answer your queries about DRDO(DEFENSE,RESEARCH AND DEVELOPMENT ORGANIZATION) .IF you want to exit type BYE.")
exit_list=['exit','stop','terminate','bye','see you later','quit','break']
while(True):
  user_input=input()
  if user_input.lower() in exit_list:
    print("COMET_GPT: Chat with you later , take care <3")
    break
  else:
    if bot_greetings(user_input) !=None:
      print("COMET_GPT: ",bot_greetings(user_input))
    else:
      print("COMET_GPT: ",bot_response(user_input))
