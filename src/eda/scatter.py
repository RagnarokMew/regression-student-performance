import sys
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

csv_path = sys.argv[1]
df = pd.read_csv(csv_path)

numeric = df.select_dtypes(include='number')

features = [ col for col in numeric.columns if col != 'exam_score' ]

for feature in features:
    sns.scatterplot(data=numeric, x=feature, y='exam_score', hue='exam_score', palette='coolwarm')
    plt.title(f'{feature} by exam_score')
    plt.savefig(f"scatter_{feature}.png")
    plt.close()