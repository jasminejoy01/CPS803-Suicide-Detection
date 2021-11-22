# Suicide Detection (CPS803)
### Abstract 
Project uses ML techniques in detecting a probable suicide message based on social media posts. 
For this purpose, we will train and test classifiers such as Naïve Bayes, Support Vector Model and Logistic Regression to distinguish Reddit posts that indicate suicide and non-suicide. 
The word associations derived from each method is used to identify posts with suicidal tendencies.

### Procedure
![Untitled Diagram drawio](https://user-images.githubusercontent.com/55416635/142925329-23ffc099-be9a-44a6-9583-97bd35442513.png)

### Preliminary Results
#### sample_10 <br>
LR Prediction Score: 50.0 % <br>
SVM Prediction Score: 50.0 % <br>
Bernoulli Naive Bayes Prediction Score: 50.0 % <br>
Gaussian Naive Bayes Prediction Score: 50.0 % <br>

#### sample_20 <br>
LR Prediction Score: 63.16 % <br>
SVM Prediction Score: 63.16 % <br>
Bernoulli Naive Bayes Prediction Score: 63.16 % <br>
Gaussian Naive Bayes Prediction Score: 47.37 % <br>

#### sample_100 <br>
LR Prediction Score: 65.22 % <br>
SVM Prediction Score: 65.22 % <br>
Bernoulli Naive Bayes Prediction Score: 63.04 % <br>
Gaussian Naive Bayes Prediction Score: 52.17 % <br>

#### suicide_notes <br>
LR Prediction Score: 59.5 % <br>
SVM Prediction Score: 59.04 % <br>
Bernoulli Naive Bayes Prediction Score: 52.86 % <br>
Gaussian Naive Bayes Prediction Score: 22.88 % <br>

#### reddit_depression_suicidewatch <br>
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
            <td><i>Sample 100</i></td>
            <td>probably a coward, way of life, bad things, better go, don’t want to feel sorry anymore, want to take their life, felling hurt, lost things, can’t find meaning in their life</td>
            <td>really like to go on a date, struggling to ask someone out, asking a friend out, way of life, things were simpler back in school, mentions words like "girlfriend" & "past"</td>
            <td>anyone want to talk, loneliness, depression, thoughts of suicide, therapists</td>
        </tr>
        <tr>
            <td><i>Suicide Notes</i></td>
            <td>mentions caring for family and friends (people around them), thoughts to kills oneself</td>
            <td></td>
            <td>hurt, afraid and wondering about pain and death, sorry, want to cry, wondering if someone hears them, sad hours</td>
        </tr>
            <tr>
            <td><i>r/depression r/SuicideWatch</i></td>
            <td>believe they will never be happy, would like to see their family happy, better if they are dead, wishing life ended, feel useless, wishing things could change or were different</td>
            <td>depressed, hating life, recent, way of life, references to the past</td>
            <td>anxiety, panicking, use of medications, call for help</td>
        </tr>
    </tbody>
  </table>

### Themes <br>
| Datasets                     | True Positives        | False Positives | False Negatives         |
| -----------------------------|:---------------------:| ---------------:| -----------------------:|
| *Sample 100*                 | regret                | social anxiety  | loneliness & depression |
| *Suicide Notes*              | goodbye notes         |                 | loneliness & anxiety    |
| *r/depression r/SuicideWatch*| regret & goodbye notes| social anxiety  | loneliness & anxiety    |

