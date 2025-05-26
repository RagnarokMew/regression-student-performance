import sys
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

##################
## Load dataset ##
##################

csv_path = sys.argv[1]

df = pd.read_csv(csv_path)

numeric = df.select_dtypes(include='number')

features = [ col for col in numeric.columns if col != 'exam_score' ]

###########################
## Plotting scatterplots ##
## ########################

for feature in features:
    sns.scatterplot(data=numeric, x=feature, y='exam_score', hue='exam_score', palette='coolwarm')
    plt.title(f'{feature} by exam_score')
    plt.legend(title='exam_score', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small', title_fontsize='medium') # put outside the plot bc it covered important info
    plt.tight_layout()
    plt.savefig(f"../../raw/scatter_{feature}.png")
    plt.close()