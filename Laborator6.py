import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool

data = pd.read_csv('data.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Funcție pentru conversia valutelor
def convert_currency(value):
    if pd.isna(value):
        return 0
    value = value.replace('€', '').replace('K', '000').replace('M', '000000')
    try:
        return float(value)
    except:
        return 0

data['Wage_num'] = data['Wage'].apply(convert_currency)
data['Value_num'] = data['Value'].apply(convert_currency)

# 1. Primii 10 jucători cu vârstă > 40
print("Primii 10 jucători cu vârstă > 40:")
filtered1 = data[data['Age'] > 40].head(10)
print(filtered1)

# 2. Toți jucătorii cu Overall ≥ 85 și Age < 25
print("\nToți jucătorii cu Overall ≥ 85 și Age < 25:")
filtered2 = data[(data['Overall'] >= 85) & (data['Age'] < 25)]
print(filtered2)

# 3. Sortează jucătorii după Skill Moves descrescător
print("\nJucătorii sortați după Skill Moves descrescător:")
sorted_data = data.sort_values(by='Skill Moves', ascending=False)
print(sorted_data)

# 4. Filtrați jucătorii care au contractul până în 2021
print("\nJucătorii cu contract până în 2021:")
filtered3 = data[data['Contract Valid Until'] == '2021']
print(filtered3)

# 5. Câte rânduri și coloane are setul de date. Câți jucători unici avem?
print(f"\nSetul de date are {data.shape[0]} rânduri și {data.shape[1]} coloane.")
unique_players = data['Name'].nunique()
print(f"Avem {unique_players} jucători unici.")

# 6. Cea mai frecventă naționalitate și top 5
print("\nTop 5 naționalități:")
top_nat = data['Nationality'].value_counts().head(5)
print(top_nat)

# 7. Pie chart pentru top 5 naționalități
plt.figure(figsize=(8, 8))
plt.pie(top_nat.values, labels=top_nat.index, autopct='%1.1f%%')
plt.title('Proporția jucătorilor pe naționalități (Top 5)')
plt.show()

# 8. Media SprintSpeed și Acceleration per naționalitate
print("\nMedia SprintSpeed și Acceleration per naționalitate:")
avg_attributes = data.groupby('Nationality')[['SprintSpeed', 'Acceleration']].mean()
print(avg_attributes)

# 9. Completați valorile lipsă în Position cu "Unknown"
data['Position'].fillna('Unknown', inplace=True)
print("\nValori lipsă în Position completate cu 'Unknown'.")

# 10. Clubul cu cea mai mare medie Overall
club_avg = data.groupby('Club')['Overall'].mean().idxmax()
print(f"\nClubul cu cea mai mare medie Overall: {club_avg}")

# 11. Câți jucători au Value > Wage
count = (data['Value_num'] > data['Wage_num']).sum()
print(f"\n{count} jucători au valoare de transfer mai mare decât salariul.")

# 12. Coloană nouă "is_underpaid"
data['is_underpaid'] = data['Wage_num'] < data['Value_num'] / 100
print("\nColoană 'is_underpaid' adăugată.")

# 13. Scor general
data['Score'] = 0.3 * data['Overall'] + 0.3 * data['Potential'] + 0.2 * data['SprintSpeed']
print("\nColoană 'Score' adăugată.")

# 14. Jucători care reprezintă o "afacere bună"
print("\nJucătorii care reprezintă o afacere bună (diferență Value - Wage descrescătoare):")
new_df = data[['Name', 'Wage', 'Value']].copy()
new_df['difference'] = data['Value_num'] - data['Wage_num']
new_df = new_df[new_df['difference'] > 0]
new_df = new_df.sort_values(by='difference', ascending=False)
print(new_df)

# Grafic scatterplot interactiv cu Bokeh pentru vizualizare
print("\nCrearea graficului scatterplot interactiv cu Bokeh...")
source = ColumnDataSource(data)
p = figure(title="Scatterplot: Age vs Overall", x_axis_label='Age', y_axis_label='Overall')
p.circle('Age', 'Overall', size=5, source=source)
hover = HoverTool()
hover.tooltips = [("Name", "@Name"), ("Age", "@Age"), ("Overall", "@Overall"), ("Club", "@Club")]
p.add_tools(hover)
output_file("scatter.html")
show(p)