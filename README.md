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
 <table>
    <thead>
      <tr>
        <th>Datasets</th>
        <th>True Positives</th>
        <th>False Positives</th>
        <th>False Negatives</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <td>Sample 100</td>
            <td>consider themselves a coward, mentions taking own life, feeling lost and hurt</td>
            <td>struggling to ask someone out, mentiones "girlfriend" & "past"</td>
            <td>loneliness, depression, throughs of suicide, call for help</td>
        </tr>
        <tr>
            <td>Suicide Notes</td>
            <td>mentions caring for family and friends (people around them), thoughts to kills oneself</td>
            <td></td>
            <td>hurt, afraid and wondering about pain and death, sorry, want to cry, wondering if someone hears them, sad hours</td>
        </tr>
            <tr>
            <td>r/depression r/SuicideWatch</td>
            <td>believe they will never be happy, would like to see their family happy, better if they are dead, wishing life ended, feel useless, wishing things could change or were different</td>
            <td>depressed, hating life, recent, way of life, references to the past</td>
            <td>anxiety, panicking, use of medications, call for help</td>
        </tr>
    </tbody>
  </table>

### Themes <br>
| Datasets                    | True Positives        | False Positives  |  False Negatives         |
| --------------------------- |:---------------------:| ----------------:| ------------------------:|
| Sample 100                  | regret                | social anxiety   | loneliness & depression  |
| Suicide Notes               | goodby notes          |                  | loneliness & anxiety     |
| r/depression r/SuicideWatch | regret & goodbyenotes | social anxiety   | loneliness & anxiety     |

