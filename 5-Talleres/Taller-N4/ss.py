import pandas as pd
import numpy as np

# === 1. Cargar el dataset original ===
df = pd.read_csv("dataset_futbol_suciov7.csv")

# === 2. Asegurar tipos numéricos en columnas clave ===
numeric_cols = [
    'Goals', 'Assists', 'Minutes_Played', 'Matches_Played',
    'Shots_On_Target', 'Pass_Accuracy_Percent', 'Player_Rating_Avg',
    'Expected_Goals_xG', 'Expected_Assists_xA', 'Goals_Per_90',
    'Distance_Covered_km', 'Sprints', 'Top_Speed_kmh'
]
numeric_cols = [c for c in numeric_cols if c in df.columns]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# === 3. Crear correlaciones realistas ===
# Ejemplo: jugadores con más minutos suelen tener más goles, asistencias y mejor rating
if {'Minutes_Played','Goals','Assists'}.issubset(df.columns):
    df['Goals'] = (df['Minutes_Played'] / df['Minutes_Played'].max() * 15 + np.random.randn(len(df))*2).clip(0)
    df['Assists'] = (df['Goals'] * 0.4 + np.random.randn(len(df))).clip(0)
    df['Player_Rating_Avg'] = (60 + df['Goals']*0.8 + df['Assists']*0.6 + np.random.randn(len(df))*3).clip(50,100)
    df['Expected_Goals_xG'] = df['Goals'] * np.random.uniform(0.9,1.1)
    df['Expected_Assists_xA'] = df['Assists'] * np.random.uniform(0.9,1.1)

# === 4. Crear una métrica de rendimiento sintético ===
df["Performance_Score"] = (
    0.4 * df["Goals"] +
    0.3 * df["Assists"] +
    0.2 * df["Minutes_Played"] / df["Minutes_Played"].max() +
    0.1 * df["Player_Rating_Avg"]
)

# === 5. Generar el target (1 = alto rendimiento) ===
threshold = df["Performance_Score"].mean() + 0.5 * df["Performance_Score"].std()
df["High_Performance"] = (df["Performance_Score"] > threshold).astype(int)

# === 6. Mantener estructura: 1000 filas × 100 columnas ===
# Si ya tiene más de 100 columnas, eliminamos la auxiliar "Performance_Score"
if df.shape[1] > 100:
    df = df.drop(columns=["Performance_Score"])

# Si tiene menos de 100 columnas, rellenamos con columnas dummy
while df.shape[1] < 100:
    df[f"Extra_{df.shape[1]}"] = np.random.randn(len(df))

# Limitar a 1000 filas y 100 columnas
df = df.iloc[:1000, :100]

# === 7. Guardar el archivo final ===
df.to_csv("datasetFutbolSucio.csv", index=False)
print("✅ Dataset generado correctamente: datasetFutbolSucio.csv")
print("Shape final:", df.shape)
print("Columnas principales:", list(df.columns[:10]))
