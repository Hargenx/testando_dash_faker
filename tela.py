import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from typing import Optional

# Carregar dados de exemplo
df = pd.read_csv('dados_exemplo.csv')
df['data'] = pd.to_datetime(df['data'])  # Convertendo a coluna 'data' para o tipo datetime

# Definir variáveis para filtros
especialidades = df['especialidade'].unique()
convenios = df['convenio'].unique()

# Layout da tela
app = dash.Dash(__name__, title='Sistema Clinica - Dashboard')

# Estilo do layout
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Dia da Semana', children=[
            html.Div([
                dcc.Input(id="pesquisa", type="text", placeholder="Digite nome do paciente", className="search-input"),
                dcc.Dropdown(id="especialidade", options=[{"label": i, "value": i} for i in especialidades],
                             placeholder="Selecione uma especialidade", className="dropdown"),
                dcc.Dropdown(id="convenio", options=[{"label": i, "value": i} for i in convenios],
                             placeholder="Selecione um convênio", className="dropdown"),
                dcc.Graph(id="grafico_dia_semana"),
            ], className="content"),
        ]),

        dcc.Tab(label='Paciente e Dia da Semana', children=[
            html.Div([
                dcc.Input(id="pesquisa", type="text", placeholder="Digite nome do paciente", className="search-input"),
                dcc.Dropdown(id="especialidade", options=[{"label": i, "value": i} for i in especialidades],
                             placeholder="Selecione uma especialidade", className="dropdown"),
                dcc.Dropdown(id="convenio", options=[{"label": i, "value": i} for i in convenios],
                             placeholder="Selecione um convênio", className="dropdown"),
                dcc.Graph(id="grafico_paciente_dia_semana"),
            ], className="content"),
        ]),

        dcc.Tab(label='Convênio', children=[
            html.Div([
                dcc.Input(id="pesquisa", type="text", placeholder="Digite nome do paciente", className="search-input"),
                dcc.Dropdown(id="especialidade", options=[{"label": i, "value": i} for i in especialidades],
                             placeholder="Selecione uma especialidade", className="dropdown"),
                dcc.Dropdown(id="convenio", options=[{"label": i, "value": i} for i in convenios],
                             placeholder="Selecione um convênio", className="dropdown"),
                dcc.Graph(id="grafico_convenio"),
            ], className="content"),
        ]),
    ]),

    html.Div(className="sidebar", children=[
        html.H2("Filtros Rápidos", className="sidebar-title"),
        html.Label("Dia da Semana", className="sidebar-label"),
        dcc.Checklist(
            id='checklist-dia-semana',
            options=[
                {'label': 'Segunda-feira', 'value': 'Monday'},
                {'label': 'Terça-feira', 'value': 'Tuesday'},
                {'label': 'Quarta-feira', 'value': 'Wednesday'},
                {'label': 'Quinta-feira', 'value': 'Thursday'},
                {'label': 'Sexta-feira', 'value': 'Friday'},
                {'label': 'Sábado', 'value': 'Saturday'},
                {'label': 'Domingo', 'value': 'Sunday'},
            ],
            value=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],  # Valor inicial
            className="checklist",
        ),
    ]),
])

# Função de filtro do dataframe
def construir_query(pesquisa: Optional[str], especialidade: Optional[str], convenio: Optional[str]) -> str:
    query_parts = []
    if pesquisa:
        query_parts.append(f"paciente.str.contains('{pesquisa}', case=False)")
    if especialidade:
        query_parts.append(f"especialidade == '{especialidade}'")
    if convenio:
        query_parts.append(f"convenio == '{convenio}'")

    return " & ".join(query_parts)

def filtrar_dataframe(df: pd.DataFrame, pesquisa: Optional[str], especialidade: Optional[str], convenio: Optional[str]) -> pd.DataFrame:
    query_string = construir_query(pesquisa, especialidade, convenio)
    if query_string:
        return df.query(query_string).copy()
    else:
        return df.copy()

# Callbacks
@app.callback(
    Output("grafico_dia_semana", "figure"),
    [Input("pesquisa", "value"), Input("especialidade", "value"), Input("convenio", "value")],
)
def atualizar_grafico_dia_semana(pesquisa: Optional[str], especialidade: Optional[str], convenio: Optional[str]):
    df_filtrado = filtrar_dataframe(df, pesquisa, especialidade, convenio)
    return px.bar(df_filtrado, x="data", y="numero_consultas", color="paciente", title="Consultas por Dia da Semana")

@app.callback(
    Output("grafico_paciente_dia_semana", "figure"),
    [Input("pesquisa", "value"), Input("especialidade", "value"), Input("convenio", "value")],
)
def atualizar_grafico_paciente_dia_semana(pesquisa: Optional[str], especialidade: Optional[str], convenio: Optional[str]):
    df_filtrado = filtrar_dataframe(df, pesquisa, especialidade, convenio)
    return px.scatter(df_filtrado, x="data", y="numero_consultas", color="paciente", trendline="ols", title="Consultas por Paciente e Dia da Semana")

@app.callback(
    Output("grafico_convenio", "figure"),
    [Input("pesquisa", "value"), Input("especialidade", "value"), Input("convenio", "value")],
)
def atualizar_grafico_convenio(pesquisa: Optional[str], especialidade: Optional[str], convenio: Optional[str]):
    df_filtrado = filtrar_dataframe(df, pesquisa, especialidade, convenio)
    return px.pie(df_filtrado, values="numero_consultas", names="convenio", title="Consultas por Convênio")

# Executar o aplicativo
if __name__ == "__main__":
    app.run_server(debug=True)
