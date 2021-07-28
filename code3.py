import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
hello = px.scatter(df, x = "Population", y = "Per capita", size = "Percentage", color = "Country", size_max = 60)
hello.show()