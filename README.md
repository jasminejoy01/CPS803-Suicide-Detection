# CPS803-Suicide-Detection
### Abstract 
Project uses ML techniques in detecting a probable suicide message based on social media posts. 
For this purpose, we will train and test classifiers such as Naïve Bayes, Support Vector Model and Logistic Regression to distinguish Reddit posts that indicate suicide and non-suicide. 
The word associations derived from each method is used to identify posts with suicidal tendencies. 
The least biased method of identifying intent of suicide in text will be used to evaluate social media posts accumulate before and during the time of COVID-19.

### Preliminary Results
#### sample_10_tokens <br>
LR Prediction Score: 50.0 % <br>
SVM Prediction Score: 50.0 % <br>
Bernoulli Naive Bayes Prediction Score: 50.0 % <br>
Gaussian Naive Bayes Prediction Score: 50.0 % <br>

#### sample_20_tokens <br>
LR Prediction Score: 63.16 % <br>
SVM Prediction Score: 63.16 % <br>
Bernoulli Naive Bayes Prediction Score: 63.16 % <br>
Gaussian Naive Bayes Prediction Score: 47.37 % <br>

#### sample_100_tokens <br>
LR Prediction Score: 65.22 % <br>
SVM Prediction Score: 65.22 % <br>
Bernoulli Naive Bayes Prediction Score: 63.04 % <br>
Gaussian Naive Bayes Prediction Score: 52.17 % <br>

#### suicide_notes_tokens <br>
LR Prediction Score: 59.5 % <br>
SVM Prediction Score: 59.04 % <br>
Bernoulli Naive Bayes Prediction Score: 52.86 % <br>
Gaussian Naive Bayes Prediction Score: 22.88 % <br>

#### reddit_depression_suicidewatch_tokens <br>
LR Prediction Score: 44.98 % <br>
SVM Prediction Score: 44.86 % <br>
Bernoulli Naive Bayes Prediction Score: 45.02 % <br>
Gaussian Naive Bayes Prediction Score: 46.79 % <br>

### Key Concepts <br>
| Datasets                    | True Positives        | False Positives  |  False Negatives         |
| --------------------------- |:---------------------:| ----------------:| ------------------------:|
| Sample 100                  | regret                | social anxiety   | loneliness & depression  |
| Suicide Notes               | goodby notes          |                  | loneliness & anxiety     |
| r/depression r/SuicideWatch | regret & goodbyenotes | social anxiety   | loneliness & anxiety     |

### Themes <br>
| Datasets                    | True Positives        | False Positives  |  False Negatives         |
| --------------------------- |:---------------------:| ----------------:| ------------------------:|
| Sample 100                  | regret                | social anxiety   | loneliness & depression  |
| Suicide Notes               | goodby notes          |                  | loneliness & anxiety     |
| r/depression r/SuicideWatch | regret & goodbyenotes | social anxiety   | loneliness & anxiety     |

