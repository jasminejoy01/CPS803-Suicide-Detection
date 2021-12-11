'''
- Using CountVectorize
- Splitting training and testing datasets
- Dataset: Suicide_Detection
- Input folder: tokenized_datasets
- Output folder: predicted_datasets
'''

import warnings
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
warnings.filterwarnings("ignore")

'''Import Dataset '''
name = 'Suicide_Detection'
df = pd.read_csv("tokenized_datasets/"+name+'_tokens.csv') 
df = df.loc[df['limit'] == 0] #filter records where tokens <512

''' Splitting Method '''
total_size=len(df)
train_size=int(np.floor(0.75*total_size))
train=df.head(train_size)
test=df.tail(len(df) - train_size)
#train.to_csv('tokenized_datasets/'+'train.csv')
#test.to_csv('tokenized_datasets/'+test.csv')

'''Import Training Data'''
train_name = 'train'
train_df = pd.read_csv('tokenized_datasets/'+train_name+'.csv', header=0)
#print(df.iloc[0])

train_df['notesCleaned'].replace('', np.nan, inplace=True)
train_df.dropna(subset=['notesCleaned'], inplace=True)
sentences_train = train_df['notesCleaned'].values
train_ex = sentences_train.shape[0]
y_train = np.zeros((train_ex))
y_train[train_df['class'] == 'suicide'] = 1

'''Import Test Data'''
test_name = 'test'
#'c_reddit_depression_suicidewatch'   ################ Replace Dataset 
test_df = pd.read_csv('tokenized_datasets/'+test_name+'.csv') 

test_df['notesCleaned'].replace('', np.nan, inplace=True)
test_df.dropna(subset=['notesCleaned'], inplace=True)
sentences_test = test_df['notesCleaned'].values
test_ex = sentences_test.shape[0]
y_test = np.zeros((test_ex))
y_test[test_df['class'] == 'suicide'] = 1
test_df['classification_int'] = y_test

'''Vectorize & tokenize'''
vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)
X_train = vectorizer.transform(sentences_train)
X_test  = vectorizer.transform(sentences_test)

'''LR Classification'''
from sklearn.linear_model import LogisticRegression
classifierLR = LogisticRegression().fit(X_train, y_train)
score = classifierLR.score(X_test, y_test)
print('Accuracy for Logistic Regression model: {:.4f}'.format(score))

''' Bernoulli Naive Bayes '''
from sklearn.naive_bayes import BernoulliNB
classifierBNB = BernoulliNB().fit(X_train, y_train)
score = classifierBNB.score(X_test, y_test)
print('Accuracy for Bernoulli NB model: {:.4f}'.format(score))

''' Multinomial Naive Bayes '''
from sklearn.naive_bayes import MultinomialNB
classifierMNB = MultinomialNB()
classifierMNB = classifierMNB.fit(X_train, y_train)
predictionsMNB = classifierMNB.predict(X_test)
scoreLR = metrics.accuracy_score(y_test, predictionsMNB)
print('Accuracy for Multinomial NB model: {:.4f}'.format(scoreLR))

''' SVM '''
from sklearn.svm import LinearSVC
classifierSVC = LinearSVC()
classifierSVC = classifierSVC.fit(X_train, y_train)
predictionsSVC = classifierSVC.predict(X_test)
scoreSVC = metrics.accuracy_score(y_test, predictionsSVC)
print('Accuracy for Linear SVC model: {:.4f}'.format(scoreSVC))

'''Export predictions as CSV'''
# test_df['predictions'] = predictLR         #Logistic Regression
# test_df['predictions'] = predictionsSVM    #SVM
# test_df['predictions'] = predictionsNB     #Naive Bayes
test_df['predictions'] = predictionsMNB    #Multinomial Naive Bayes
# test_df['predictions'] = predictionsMLP    #MLP
test_df.to_csv('predicted_datasets/'+test_name+'_CountVectorize.csv', index=False)