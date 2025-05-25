import pandas as pd
from sklearn.model_selection import train_test_split

#####################
## Loading dataset ##
#####################

df = pd.read_csv("../../data/noised_student_habits_performance.csv")

#####################################
## Splitting dataset using sklearn ##
#####################################

target = df['exam_score']

df = df.drop(columns=['exam_score', 'student_id'])

X_train, X_test, y_train, y_test = train_test_split(
    df, target, test_size=0.25, random_state=1984
)

print(f"Train size: {X_train.shape}")
print(f"Train target size: {y_train.shape}")
print(f"Test size: {X_test.shape}")
print(f"Test target size: {y_test.shape}")

#####################################################
## Merging the features and targets for processing ##
#####################################################

df_train = pd.concat([X_train, y_train])
df_test = pd.concat([X_test, y_test])

df_train.to_csv("../../data/noised_train.csv", index=False)
df_test.to_csv("../../data/noised_test.csv", index=False)