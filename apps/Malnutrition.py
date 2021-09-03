import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from app import app
from urllib.request import urlopen
import joblib
import pathlib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#with urlopen('https://storage.googleapis.com/ds4all-test-bd1/Modelo_malnutrition.sav') as response:
#    modelo_malnutrition = joblib.load(response)

#base_malnutrition = pd.read_csv('https://storage.googleapis.com/ds4all-test-bd1/base_malnutrition.csv').drop(
#    ["IdBeneficiario", "Unnamed: 0", "Unnamed: 0.1"], axis=1)

#top10_df = top10table.createTable_top(modelo_malnutrition, base_malnutrition)
#img = SHAP_Val.plotShapValuesTop(modelo_malnutrition, top10_df)

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Img(src='/assets/long_child.jpg', height="200px"), width=12)
    ], align="center",
    )
], fluid=True)