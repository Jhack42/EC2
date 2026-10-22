import pandas as pd

# 1. Leer CSV
df = pd.read_csv(
    "C:\\Users\\tucta\\Downloads\\DATASET_CEXTERNA_2015_2022_0.csv",
    sep=";",
    dtype={"UBIGEO": "string"}
)


# 2. Eliminar espacios en columnas de texto
columnas_texto = [
    "SES_DESRED",
    "SES_DESCAS",
    "DES_GRU",
    "DES_ACT",
    "DES_SER",
    "DEPARTAMENTO",
    "PROVINCIA",
    "DISTRITO",
    "UBIGEO"
]

for columna in columnas_texto:
    # Quitar espacios en los nombres de columnas y en los valores
    df.columns = df.columns.str.strip()
    df[columna] = df[columna].astype("string").str.strip()

# 3. Convertir cadenas vacías a NULL
df[columnas_texto] = df[columnas_texto].replace("", pd.NA)

# 4. Estandarizar texto
for columna in columnas_texto:
    df[columna] = df[columna].str.upper()

# 5. Convertir cantidad a número
df["CANTIDAD"] = pd.to_numeric(
    df["CANTIDAD"],
    errors="coerce"
)

# 6. Convertir fecha
df["FECHA_CORTE"] = pd.to_datetime(
    df["FECHA_CORTE"],
    format="%Y%m%d",
    errors="coerce"
)

# 7. Crear año y mes
df["AÑO"] = df["PERIODO"].astype(str).str[:4].astype(int)
df["MES"] = df["PERIODO"].astype(str).str[4:6].astype(int)

# 8. Eliminar duplicados
df = df.drop_duplicates()

# 9. Guardar archivo limpio
df.to_csv(
    "C:\\Users\\tucta\\Downloads\\datos_limpios.csv",
    sep=";",
    index=False
)