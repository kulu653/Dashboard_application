
import dash_daq as daq
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import dash_bootstrap_components as dbc
from app import app

############ Loading Datasets ################

master_df = pd.read_csv('/database_dashboard/assets/data.txt', delimiter=" ")

########### Chart, Graphs and Tables assignment ############

chart4_local_db_region = px.histogram(master_df, x="assay")
chart5_local_db_country = px.histogram(master_df, x="assay")
chart6_local_db_continent = px.histogram(master_df, x="assay")
table2_local_db = dash_table.DataTable()
table_country_top_50_args = dash_table.DataTable()
table_continent_top_50_args = dash_table.DataTable()


####################### Setting Graphs as HTML Children ##############

graph4 = dcc.Graph(
    id='graph4',
    figure=chart4_local_db_region,
    style={'display': 'inline-block'}
)


graph5 = dcc.Graph(
    id='graph5',
    figure=chart5_local_db_country,
    style={'display': 'inline-block'}
)


graph6 = dcc.Graph(
    id='graph6',
    figure=chart6_local_db_continent,
    style={'display': 'inline-block'},
)

table2 = html.Table(table2_local_db,
                    id='table2'
                    )

table_country = html.Table(table_country_top_50_args,
                           id='table_country'
                           )

table_continent = html.Table(table_continent_top_50_args,
                             id='table_continent'
                             )


############### Creating Widgets For Each Graph #########################


sample_options_localdb = master_df["sample_type"].unique()
country_options_localdb = master_df["country"].unique()
region_options_localdb = master_df["region"].unique()
continent_options_localdb = master_df["continent"].unique()


dropdown5_histogram = dcc.Dropdown(
    id="dropdown5_histogram",
    options=[{"value": label, "label": label}
             for label in country_options_localdb] + [{'label': 'Select all', 'value': "all"}],
    placeholder="Select country",
    clearable=False,
    style=dict(width='50%', margin="auto"),
)

dropdown6_histogram = dcc.Dropdown(
    id="dropdown6_histogram",
    options=[{"value": label, "label": label}
             for label in sample_options_localdb] + [{'label': 'Select all', 'value': "all"}],
    placeholder="Select sample type",
    clearable=False,
    style=dict(width='80%', margin="auto"),
)

dropdown1_table2 = dcc.Dropdown(
    id="dropdown1_table2",
    options=[{"value": label, "label": label}
             for label in region_options_localdb] + [{'label': 'Select all', 'value': "all"}],
    placeholder="Select geographical region",
    clearable=False,
    style=dict(width='50%', margin="auto")

)

dropdown_table_country = dcc.Dropdown(
    id="dropdown_table_country",
    options=[{"value": label, "label": label}
             for label in country_options_localdb] + [{'label': 'Select all', 'value': "all"}],
    placeholder="Select country",
    clearable=False,
    style=dict(width='50%', margin="auto")
)

dropdown_table_continent = dcc.Dropdown(
    id="dropdown_table_continent",
    options=[{"value": label, "label": label}
             for label in continent_options_localdb] + [{'label': 'Select all', 'value': "all"}],
    placeholder="Select continent",
    clearable=False,
    style=dict(width='50%', margin="auto")
)

dropdown7_histogram = dcc.Dropdown(
    id="dropdown7_histogram",
    options=[
       {'label': 'Class of antibiotics', 'value': 'class_of_antibiotics'},
       {'label': 'MGE and Integrons', 'value': 'mge_and_integrons'},
       {'label': 'Pathogens', 'value': 'taxanomic'},
    ],
    placeholder="Select assay type",
    clearable=False,
    style=dict(width='80%', margin="auto")
)

log_switch = daq.BooleanSwitch(
    on=False,
    label="Log scale",
    labelPosition="top",
    id="log_switch"
)


######################### Laying out Charts & Widgets to Create App Layout ##########

layout = html.Div([dbc.Container([


    dbc.Row([
            dbc.Col(html.H1("Welcome to Local Database Dashboard",
                    className="text-center"), className="mb-5 mt-5")
            ]),


    dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='AMR- prevalence in continent and regional level',
                                 className="text-center text-primary"), body=True, color="Thistle"), className="mt-4 mb-4")
    ]),


    dbc.Row([
        dbc.Col(dropdown6_histogram),
        dbc.Col(dropdown7_histogram),

    ]),
    dbc.Row([
        dbc.Col(log_switch, width="auto", align="center")
    ]),

    dbc.Row([
            
            dbc.Col(graph6, width="auto", align="center"),
            dbc.Col(graph4, width="auto", align="center")


            ], justify="center"),


    dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='AMR-prevalence in country level',
                                 className="text-center text-primary"), body=True, color="Thistle"), className="mt-4 mb-4")
    ]),

    dbc.Row(dbc.Col(dropdown5_histogram)),
    dbc.Row(dbc.Col(graph5, width="auto", align="center"), justify="center"),

    dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='Top 50 most abundant ARGs in selected sample type on regional level',
                                 className="text-center text-primary"), body=True, color="Thistle"), className="mt-4 mb-4")]),

    dbc.Row(dbc.Col(dropdown1_table2), style={"height": "150px"}),

    dbc.Row(dbc.Col(table2, width="auto"), justify="center"),

    dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='Top 50 most abundant ARGs in selected sample type on continent level',
                                 className="text-center text-primary"), body=True, color="Thistle"), className="mt-4 mb-4")]),

    dbc.Row(dbc.Col(dropdown_table_continent), style={"height": "150px"}),

    dbc.Row(dbc.Col(table_continent, width="auto"), justify="center"),


    dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='Top 50 most abundant ARGs in selected sample type on country level',
                                 className="text-center text-primary"), body=True, color="Thistle"), className="mt-4 mb-4")]),

    dbc.Row(dbc.Col(dropdown_table_country), style={"height": "150px"}),

    dbc.Row(dbc.Col(table_country, width="auto"), justify="center"),

])
])


############### Setting App Layout ########################################


app.layout = dbc.Container(layout, fluid=True)


@app.callback([Output('graph4', 'figure'),
               Output('graph5', 'figure'),
               Output('graph6', 'figure'),
               Output('table2', 'children'),
               Output('table_country', 'children'),
               Output('table_continent', 'children'),

               ],
              [Input("log_switch", "on"),
              Input('dropdown5_histogram', 'value'),
              Input('dropdown6_histogram', 'value'),
              Input('dropdown7_histogram', 'value'),
              Input('dropdown1_table2', 'value'),
              Input('dropdown_table_country', 'value'),
              Input('dropdown_table_continent', 'value'),


               ])
def update_histogram(on, drop5, drop6, drop7, drop8, drop9, drop10):
    if on:
        master_df["log_relative"] = np.log10(master_df["relative"])
    else:
        master_df["log_relative"] = master_df["relative"]

    if drop6 == "all":
        local_db_df = master_df
    else:
        local_db_df = master_df[master_df.sample_type == drop6]

    if drop7 == "class_of_antibiotics":
        local_db_df1 = local_db_df.loc[~local_db_df["class"].isin(
            ["16S rRNA", "MGE", "Integrons", "Taxanomic"])]
        legend_name = "Class of Antibiotics"
    elif drop7 == "mge_and_integrons":
        local_db_df1 = local_db_df.loc[local_db_df["class"].isin([
            "MGE", "Integrons"])]
        legend_name = "MGE and Integrons"
    else
        local_db_df1 = local_db_df.loc[local_db_df["class"].isin([
                                                                 "Taxanomic"])]
        legend_name = "Pathogens"
    

    if drop5 == "all":
        local_db_df2 = local_db_df1
    else:
        local_db_df2 = local_db_df1[local_db_df1.country == drop5]

    chart6_local_db_continent = px.box(local_db_df1, labels={
        "log_relative": "abundance, relative to 16S rRNA gene",
        "continent": "continent",
        "class": "Assay type: %s" % (legend_name)},
        x="continent",
        y="log_relative",
        color="class",
        color_discrete_sequence=px.colors.qualitative.Pastel,
        height=450, width=800,
        hover_data={'assay': True,
                    'gene': True,
                    "class": False,
                    "continent": False,


                    }
    )
    chart6_local_db_continent.update_traces(
        dict(marker_line_width=0))
    chart6_local_db_continent.update_layout(legend=dict(
        title_font_family="Times New Roman", font=dict(size=10)))
   

    chart4_local_db_region = px.box(local_db_df1, labels={
        "log_relative": "abundance, relative to 16S rRNA gene",
        "region": "region",
        "class": "Assay type: %s" % (legend_name)},
        x="region",
        y="log_relative",
        color="class",
        color_discrete_sequence=px.colors.qualitative.Pastel,
        height=450, width=800,
        hover_data={'assay': True,
                    "class": False,
                    "region": False,


                    }
    )
    chart4_local_db_region.update_traces(dict(marker_line_width=0))
    chart4_local_db_region.update_layout(legend=dict(
        title_font_family="Times New Roman", font=dict(size=10)))

    chart5_local_db_country = px.box(local_db_df2, labels={
        "log_relative": "abundance, relative to 16S rRNA gene",
        "class": "Assay type: %s" % (legend_name)},
        x="country",
        y="log_relative",
        color="class",
        color_discrete_sequence=px.colors.qualitative.Pastel,
        height=450, width=1200,
        hover_data={'assay': True,
                    'gene': True,
                    "class": False,
                    "country": False,


                    }
    )

    chart5_local_db_country.update_traces(dict(marker_line_width=0))
    chart5_local_db_country.update_yaxes(automargin=True)
    chart5_local_db_country.update_layout(legend=dict(
        title_font_family="Times New Roman", font=dict(size=10)))
   
    #

    sample_type_df_region = master_df[master_df.sample_type == drop6]

    if drop8 == "all":
        regional_df = sample_type_df_region

    else:
        regional_df = sample_type_df_region[sample_type_df_region.region == drop8]

    top_50_region = regional_df.groupby('assay').agg(
        {'relative': ['median', 'min', 'max', 'count', ]}).relative.sort_values(
        by='median', ascending=False).nlargest(50, 'median').round(decimals=10)
    top_50_region.reset_index(inplace=True)
    top_50_region_no_zero = regional_df[regional_df['relative'] != 0].groupby("assay").agg(
        {'relative': 'count'})
    top_50_region_no_zero.reset_index(inplace=True)
    top_50_region_merged = pd.merge(
        top_50_region, top_50_region_no_zero, how="inner", on="assay")
    top_50_region_merged["relative"] = top_50_region_merged["relative"].fillna(
        0)

    top_50_region_new = top_50_region_merged.rename(columns={'index': 'assay', 'median': 'relative abundance (median)', 'min': 'relative abundance (miminum)',
                                                    'max': 'relative abundance (maximum)', 'count': 'number of times ARG was assayed', "relative": "number of times ARG was detected"})

    gene_names = pd.read_excel(
        "/Users/datalab/Documents/kul_database_dashboard/assets/gene.xlsx")
    top_50_region_new = pd.merge(gene_names, top_50_region_new, how='inner',
                                 on='assay')
    top_50_region_new = top_50_region_new.sort_values(
        by=['relative abundance (median)'], ascending=False)
    table2_local_db = dash_table.DataTable(top_50_region_new.to_dict('records'), [{'name': i, 'id': i} for i in top_50_region_new.columns],
                                           row_selectable="multi",
                                           row_deletable=True,
                                           editable=True,
                                           filter_action="native",
                                           filter_options={
        'case': 'insensitive'},
        sort_action="native",
        style_header={
        'backgroundColor': '#2E86C1', 'padding': '10px', 'color': '#FFFFFF'},
        style_cell={'textAlign': 'left', 'backgroundColor': '#FDEDEC', 'maxWidth': 325,
                    'font_size': '14px', 'whiteSpace': 'normal', 'height': 'auto'},

    )

    #

    sample_type_df_country = master_df[master_df.sample_type == drop6]

    if drop9 == "all":
        country_df = sample_type_df_country

    else:
        country_df = sample_type_df_country[sample_type_df_country.country == drop9]

    top_50_country = country_df.groupby('assay').agg({'relative': ['median', 'min', 'max', 'count']}).relative.sort_values(
        by='median', ascending=False).nlargest(50, 'median').round(decimals=10)
    top_50_country.reset_index(inplace=True)
    top_50_country_no_zero = country_df[country_df['relative'] != 0].groupby("assay").agg(
        {'relative': 'count'})
    top_50_country_no_zero.reset_index(inplace=True)
    top_50_country_merged = pd.merge(
        top_50_country, top_50_country_no_zero, how="inner", on="assay")
    top_50_country_merged["relative"] = top_50_country_merged["relative"].fillna(
        0)

    top_50_country_new = top_50_country_merged.rename(columns={'index': 'assay', 'median': 'relative abundance (median)', 'min': 'relative abundance (miminum)',
                                                               'max': 'relative abundance (maximum)', 'count': 'number of times ARG was assayed', "relative": "number of times ARG was detected"})

    gene_names = pd.read_excel(
        "/Users/datalab/Documents/kul_database_dashboard/assets/gene.xlsx")
    top_50_country_new = pd.merge(gene_names, top_50_country_new, how='inner',
                                  on='assay')
    top_50_country_new = top_50_country_new.sort_values(
        by=['relative abundance (median)'], ascending=False)
    table_country = dash_table.DataTable(top_50_country_new.to_dict('records'), [{'name': i, 'id': i} for i in top_50_country_new.columns],
                                         row_selectable="multi",
                                         row_deletable=True,
                                         editable=True,
                                         filter_action="native",
                                         filter_options={
        'case': 'insensitive'},
        sort_action="native",
        style_header={
        'backgroundColor': '#2E86C1', 'padding': '10px', 'color': '#FFFFFF'},
        style_cell={'textAlign': 'left', 'backgroundColor': '#FDEDEC', 'maxWidth': 325,
                    'font_size': '14px', 'whiteSpace': 'normal', 'height': 'auto'},

    )

    #

    sample_type_df_continent = master_df[master_df.sample_type == drop6]

    if drop10 == "all":
        continent_df = sample_type_df_continent

    else:
        continent_df = sample_type_df_continent[sample_type_df_continent.continent == drop10]

    top_50_continent = continent_df.groupby('assay').agg({'relative': ['median', 'min', 'max', 'count']}).relative.sort_values(
        by='median', ascending=False).nlargest(50, 'median').round(decimals=3)
    top_50_continent.reset_index(inplace=True)
    top_50_continent_no_zero = continent_df[continent_df['relative'] != 0].groupby("assay").agg(
        {'relative': 'count'})
    top_50_continent_no_zero.reset_index(inplace=True)
    top_50_continent_merged = pd.merge(
        top_50_continent, top_50_continent_no_zero, how="inner", on="assay")
    top_50_continent_merged["relative"] = top_50_continent_merged["relative"].fillna(
        0)

    top_50_continent_new = top_50_continent_merged.rename(columns={'index': 'assay', 'median': 'relative abundance (median)', 'min': 'relative abundance (miminum)',
                                                                   'max': 'relative abundance (maximum)', 'count': 'number of times ARG was assayed', "relative": "number of times ARG was detected"})
    gene_names = pd.read_excel(
        "/Users/datalab/Documents/kul_database_dashboard/assets/gene.xlsx")
    top_50_continent_new = pd.merge(gene_names, top_50_continent_new, how='inner',
                                    on='assay')
    top_50_continent_new = top_50_continent_new.sort_values(
        by=['relative abundance (median)'], ascending=False)
    table_continent = dash_table.DataTable(top_50_continent_new.to_dict('records'), [{'name': i, 'id': i} for i in top_50_continent_new.columns],
                                           row_selectable="multi",
                                           row_deletable=True,
                                           editable=True,
                                           filter_action="native",
                                           filter_options={
        'case': 'insensitive'},
        sort_action="native",
        style_header={
        'backgroundColor': '#2E86C1', 'padding': '10px', 'color': '#FFFFFF'},
        style_cell={'textAlign': 'left', 'backgroundColor': '#FDEDEC', 'maxWidth': 325,
                    'font_size': '14px', 'whiteSpace': 'normal', 'height': 'auto'},

    )

    return chart4_local_db_region, chart5_local_db_country, chart6_local_db_continent, table2_local_db, table_country, table_continent
