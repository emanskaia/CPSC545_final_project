#Correlation analysis
import scipy.stats as stats
csv_file_path = '/home/emanskaia/Desktop/dataset_DD_original/1ERR/iteration_1/combined_output_modified.csv'
df = pd.read_csv(csv_file_path)
    x_column = 'Rank_dp'
    y_column = 'Rank_dd'
    x = df[x_column]
y = df[y_column]
correlation_coefficient, p_value = stats.pearsonr(x,y)
print(f"Pearson correlation coefficient: {correlation_coefficient}")
print(f"p_value: {p_value}")


1ERR
Pearson correlation coefficient: 0.01104
P-value: 5.394833077647444e-28
