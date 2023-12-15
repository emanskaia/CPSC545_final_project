#Correlation analysis
import scipy.stats as stats
csv_file_path = '~/home/result_experiment2.csv' #replace with actual path to your file '~/home/result_experiment1.csv' 
df = pd.read_csv(csv_file_path)
    x_column = 'Rank_dp'
    y_column = 'Rank_dd'
    x = df[x_column]
y = df[y_column]
correlation_coefficient, p_value = stats.pearsonr(x,y)
print(f"Pearson correlation coefficient: {correlation_coefficient}")
print(f"p_value: {p_value}")

