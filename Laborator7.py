import pandas as pd
from sklearn.preprocessing import StandardScaler
data = pd.read_csv('StudentsPerformance.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
primele5 = data.head(5)
print(primele5)

# Analiza structurii dataset-ului (tipuri de date, număr de valori non-null)
print("\n=== Structura dataset-ului ===")
data.info()

# Calcularea statisticilor descriptive pentru variabilele numerice
print("\n=== Statistici descriptive pentru variabilele numerice ===")
print(data.describe())

# Identificarea valorilor lipsă
print("\n=== Valori lipsă ===")
print(data.isnull().sum())

# 2. Identificarea tipurilor de variabile
print("\n=== 2. Identificarea tipurilor de variabile ===")

# Variabilele categorice (tip object)
categorical_vars = data.select_dtypes(include=['object']).columns.tolist()
print(f"Variabile categorice: {categorical_vars}")

# Variabilele numerice (tip int64 sau float64)
numerical_vars = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
print(f"Variabile numerice: {numerical_vars}")

# Enumerați fiecare categorie identificată
print("\nCategorii pentru variabilele categorice:")
for var in categorical_vars:
    unique_values = data[var].unique().tolist()
    print(f"{var}: {unique_values}")

# 3. Curățarea datelor
print("\n=== 3. Curățarea datelor ===")

# Verificați existența valorilor lipsă
print("Verificare valori lipsă înainte de curățare:")
missing_before = data.isnull().sum()
print(missing_before)

# Dacă există valori lipsă
if missing_before.sum() > 0:
    # Înlocuiți valorile numerice lipsă cu mediana
    for col in numerical_vars:
        if data[col].isnull().sum() > 0:
            median_val = data[col].median()
            data[col].fillna(median_val, inplace=True)
            print(f"Înlocuit valorile lipsă în {col} cu mediana: {median_val}")
    
    # Înlocuiți valorile categorice lipsă cu „Unknown”
    for col in categorical_vars:
        if data[col].isnull().sum() > 0:
            data[col].fillna("Unknown", inplace=True)
            print(f"Înlocuit valorile lipsă în {col} cu 'Unknown'")
else:
    print("Nu există valori lipsă în dataset.")

# Verificați din nou dataset-ul pentru a confirma eliminarea valorilor lipsă
print("\nVerificare valori lipsă după curățare:")
missing_after = data.isnull().sum()
print(missing_after)

if missing_after.sum() == 0:
    print("Toate valorile lipsă au fost eliminate.")
else:
    print("Mai există valori lipsă.")

# 5. Crearea de caracteristici noi (Feature Engineering)
print("\n=== 5. Crearea de caracteristici noi (Feature Engineering) ===")

# Creați o variabilă nouă average_score ca medie a scorurilor
data['average_score'] = (data['math score'] + data['reading score'] + data['writing score']) / 3
print("Variabilă nouă 'average_score' creată ca medie a scorurilor.")

# Creați o variabilă categorială performance_level
def categorize_performance(score):
    if score < 50:
        return 'low'
    elif 50 <= score <= 70:
        return 'medium'
    else:
        return 'high'

data['performance_level'] = data['average_score'].apply(categorize_performance)
print("Variabilă categorială 'performance_level' creată.")

# Creați o variabilă binară is_prepared
data['is_prepared'] = data['test preparation course'].apply(lambda x: 1 if x == 'completed' else 0)
print("Variabilă binară 'is_prepared' creată.")

# Justificați utilitatea caracteristicilor create
print("\nJustificare utilitate caracteristici:")
print("- average_score: Oferă o măsură generală a performanței, simplificând analiza.")
print("- performance_level: Categorizează performanța pentru clasificare, facilitând predicția.")
print("- is_prepared: Indicǎ dacă studentul s-a pregătit, relevant pentru predicția scorurilor.")

# 6. Selectarea caracteristicilor (Feature Selection)
print("\n=== 6. Selectarea caracteristicilor (Feature Selection) ===")

# Lista tuturor coloanelor
all_columns = data.columns.tolist()
print(f"Toate coloanele: {all_columns}")

# Analizați fiecare coloană
relevant_features = []
removed_features = []

for col in all_columns:
    if col in ['math score', 'reading score', 'writing score']:
        # Scorurile individuale sunt relevante pentru predicție
        relevant_features.append(col)
        print(f"{col}: Păstrată - aduce informație relevantă despre performanță.")
    elif col == 'average_score':
        relevant_features.append(col)
        print(f"{col}: Păstrată - măsură generală a performanței.")
    elif col == 'performance_level':
        # Aceasta este ținta, deci păstrată
        relevant_features.append(col)
        print(f"{col}: Păstrată - variabila țintă.")
    elif col == 'is_prepared':
        relevant_features.append(col)
        print(f"{col}: Păstrată - indică pregătirea, relevantă pentru performanță.")
    elif col in ['gender', 'race/ethnicity', 'parental level of education', 'lunch']:
        # Acestea pot influența performanța, deci relevante
        relevant_features.append(col)
        print(f"{col}: Păstrată - poate aduce informație relevantă despre factori sociali.")
    elif col == 'test preparation course':
        # Redundantă cu is_prepared
        removed_features.append(col)
        print(f"{col}: Eliminată - redundantă cu 'is_prepared'.")
    else:
        removed_features.append(col)
        print(f"{col}: Eliminată - nu este relevantă.")

# Verificați existența coloanelor constante
constant_columns = [col for col in data.columns if data[col].nunique() == 1]
if constant_columns:
    print(f"Coloane constante găsite: {constant_columns}")
    for col in constant_columns:
        if col in relevant_features:
            relevant_features.remove(col)
        removed_features.append(col)
else:
    print("Nu există coloane constante.")

# Verificați coloanele redundante (corelate puternic)
# Calculați corelația pentru variabilele numerice
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = data[numerical_cols].corr()
print("\nMatricea de corelație:")
print(correlation_matrix)

# Identificați perechi cu corelație > 0.9
high_corr_pairs = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        if abs(correlation_matrix.iloc[i, j]) > 0.9:
            col1 = correlation_matrix.columns[i]
            col2 = correlation_matrix.columns[j]
            high_corr_pairs.append((col1, col2))
            print(f"Pereche redundantă: {col1} și {col2} (corelație: {correlation_matrix.iloc[i, j]:.2f})")

if not high_corr_pairs:
    print("Nu există perechi redundante puternic corelate.")
else:
    # Scorurile individuale sunt puternic corelate cu average_score, dar păstrăm pentru analiză detaliată
    print("Perechile redundante sunt notate, dar păstrăm toate pentru relevanță.")

# Eliminați caracteristicile considerate irelevante
data_selected = data[relevant_features].copy()
print(f"\nCaracteristici păstrate: {relevant_features}")
print(f"Caracteristici eliminate: {removed_features}")

# 7. Scalarea datelor
print("\n=== 7. Scalarea datelor ===")

# Selectați variabilele numerice relevante
numerical_features = [col for col in relevant_features if col in numerical_vars or col == 'average_score']
print(f"Variabile numerice pentru scalare: {numerical_features}")

# Valori înainte de scalare
print("\nValori înainte de scalare (primele 5 rânduri):")
print(data_selected[numerical_features].head())

# Aplicați StandardScaler
scaler = StandardScaler()
data_selected[numerical_features] = scaler.fit_transform(data_selected[numerical_features])

# Valori după scalare
print("\nValori după scalare (primele 5 rânduri):")
print(data_selected[numerical_features].head())

# Explicați de ce este necesară scalarea
print("\nExplicație scalare:")
print("Scalarea este necesară pentru algoritmii bazați pe distanță (ex. KNN, SVM) deoarece aceștia calculează distanțe între puncte.")
print("Fără scalare, variabilele cu valori mai mari (ex. scoruri) ar domina calculul distanței, ducând la rezultate incorecte.")

# 8. Pregătirea dataset-ului final
print("\n=== 8. Pregătirea dataset-ului final ===")

# Definiți matricea de caracteristici X (excludeți ținta)
X = data_selected.drop(columns=['performance_level'])
print(f"Matricea de caracteristici X: {X.shape}")

# Variabila țintă y
y = data_selected['performance_level']
print(f"Variabila țintă y: {y.shape}")

# Afișați dimensiunile finale
print(f"\nDimensiunile finale ale dataset-ului: {data_selected.shape}")