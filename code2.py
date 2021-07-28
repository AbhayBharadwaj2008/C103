import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
hi = px.bar(df, x = "Country", y = "InternetUsers")
hi.show()