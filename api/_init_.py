from sodapy import Socrata

# Conectar a la API (puedes usar app_token para mayor rendimiento)
client = Socrata("www.datos.gov.co", None )

# Obtener los primeros 1000 registros de un conjunto de datos
results = client.get("n8mc-b4w4", limit=1000)

# Si lo prefieres, convertir a un DataFrame de pandas
import pandas as pd
df = pd.DataFrame.from_records(results)

print(df.head()) 