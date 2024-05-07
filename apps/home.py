from dash import html
import dash_bootstrap_components as dbc


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to Database dashboard",
                    className="text-center"), className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(
                children='Press "GO" to select database', className="text-center"), className="mb-5")
        ]),

        dbc.Row([dbc.Col(dbc.Button(children="GO", href="/local_database",
                                    color="primary"),  style={'textAlign': 'center'}, className="mt-3")])
    ])])
