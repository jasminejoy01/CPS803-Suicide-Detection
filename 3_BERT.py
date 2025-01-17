'''
- Using BERT
- Training Dataset: Suicide_Detection
- Test Datasets: reddit_depression_suicidewatch, suicide_notes
- Input folder: tokenized_datasets
- Output folder: predicted_datasets
'''
import pandas as pd
import numpy as np
from sklearn import metrics
import utils 

'''Import Training Data'''
train_name = 'Suicide_Detection_tokens'
df = pd.read_csv("tokenized_datasets/"+train_name+'.csv') 
train_df = df.loc[df['limit'] == 0] #filter records where tokens <512

'''Import Test Data'''
#test_name = 'suicide_notes_tokens' 
test_name = 'reddit_depression_suicidewatch_tokens'
test_df = pd.read_csv("tokenized_datasets/"+test_name+'.csv') 

'''Training Dataframes'''
index = train_df['id']
notes = train_df['text']
classfication = train_df['class']
notesCleaned = train_df['notesCleaned']
classfication_int = train_df['classification_int']
tokens = train_df['tokens']
max_count = train_df['max_count']

test_index = test_df['id']
test_notes = test_df['text']
test_classfication = test_df['class']
test_notesCleaned = test_df['notesCleaned']
test_classfication_int = test_df['classification_int']
test_tokens = test_df['tokens']
test_max_count = test_df['max_count']

'''Constants'''
if max_count[0] > 512 or test_max_count[0]:
    padding = 512
else:
    padding = max(max_count[0], test_max_count[0])

train_matrix = utils.create_matrix(tokens, padding)
test_matrix = utils.create_matrix(test_tokens, padding)

print(test_name)
'''LR Classification'''
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=0, tol=1e-5, max_iter=100000, dual=False)
clf.fit(train_matrix, classfication_int)
predictLR = clf.predict(test_matrix)
scoreLR = metrics.accuracy_score(test_classfication_int, predictLR)
print('Accuracy for Logistic Regression model: {:.4f}'.format(scoreLR))

'''Bernoulli Naive Bayes Classification'''
from sklearn.naive_bayes import BernoulliNB
bnb = BernoulliNB()
bnb = bnb.fit(train_matrix, classfication_int)
predictionsNB = bnb.predict(test_matrix)
scoreNB = metrics.accuracy_score(test_classfication_int, predictionsNB)
print('Accuracy for Bernoulli NB model: {:.4f}'.format(scoreNB))

'''Multinomial Naive Bayes Classification'''
from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb = mnb.fit(train_matrix, classfication_int)
predictionsMNB = mnb.predict(test_matrix)
scoreMNB = metrics.accuracy_score(test_classfication_int, predictionsMNB)
print('Accuracy for Multinomial NB model: {:.4f}'.format(scoreMNB))

'''SVM Classification'''
from sklearn.svm import LinearSVC
svm = LinearSVC(random_state=0, tol=1e-5, max_iter=100000, dual=False)
svm = svm.fit(train_matrix, classfication_int)
predictionsSVM = svm.predict(test_matrix)
scoreSVM = metrics.accuracy_score(test_classfication_int, predictionsSVM)
print('Accuracy for SVC model: {:.4f}'.format(scoreSVM))

'''MLP Classification'''
from sklearn.neural_network import MLPClassifier
mlp_clf = MLPClassifier()
mlp_clf = mlp_clf.fit(train_matrix, classfication_int)
predictionsMLP = mlp_clf.predict(test_matrix)
scoreMLP = metrics.accuracy_score(test_classfication_int, predictionsSVM)
print('Accuracy for MLP model: {:.4f}'.format(scoreMLP))

'''Export predictions as CSV'''
#test_df['predictionsLR'] = predictLR         #Logistic Regression
#test_df['predictionsSVM'] = predictionsSVM   #SVM
#test_df['predictionsNB'] = predictionsNB     #Naive Bayes
#test_df['predictions'] = predictionsMNB   #Multinomial Naive Bayes
#test_df['predictionsLR'] = predictionsMLP    #MLP
#test_df.to_csv("predicted_datasets/"+test_name+'_BERT.csv', index=False)

test_df['predictions'] = predictionsMLP    #MLP
test_df.to_csv('predicted_datasets/'+test_name+'_MLP_BERT.csv', index=False)