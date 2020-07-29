import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly
import plotly.express as px
import plotly.io as pio
#import figures



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



def to_string(x):
#To have string data for visualizations
    if x == 1:
        return "Individualistic orientation"
    if x == 2:
        return "Collectivistic orientation"
    
def countryres(x):
# To have countries in string for better visualization
    if x == 1:
        return "Germany"
    elif x == 2:
        return "Italy"
    elif x==3:
        return "France"
    elif x== 4:
        return "Spain"
    elif x== 5:
        return "Poland"

df = pd.read_csv("../__thoughts__/workingdf.csv", index_col=0)

df["String_SSN"] = df["Small-scale_NEUTRAL"].apply(to_string)
df["String_LSN"]  = df["Large-scale_NEUTRAL"].apply(to_string)
df["String_SSC"]  = df["Small-scale_COVID19"].apply(to_string)
df["String_LSC"]  = df["Large-scale_COVID19"].apply(to_string)
df["Country"] = df["Country of residence"].apply(countryres)

counts_fav = pd.read_csv("../__thoughts__/globalcontext.csv", index_col=0)
counts_fav["1_Indiv_2_Collect"] = counts_fav["level_1"].astype(str)

# FIGURES 2 to 5: FEATURES (VI) AND TARGETS(VD). COMPARISONS BETWEEN SITUATIONS AND EACH SUBJECT FOLLOWS 


small_scaleN = df[['Gender', 'Age (in years)', 'Country of residence', 'Living area',
       'Children', 
       'Total conform', 'Risk6', 'Education_cat', 'Job', 'Small-scale_NEUTRAL',"String_SSN", "Country" ]]
df1=small_scaleN
dfplot1 = df[["Country",'Gender', 'Age (in years)', 'Living area',
       'Children', 
        'Risk6', 'Education_cat', 'Job', "Small-scale_NEUTRAL"]]

large_scaleN = df[['Gender', 'Age (in years)', 'Country of residence', 'Living area',
       'Children', 
       'Total conform', 'Risk6', 'Education_cat', 'Job','Large-scale_NEUTRAL', "String_LSN", "Country"]]
df2 = large_scaleN
dfplot2=df[["Country",'Gender', 'Age (in years)', 'Living area',
       'Children', 
        'Risk6', 'Education_cat', 'Job', 'Large-scale_NEUTRAL']]

small_scaleC = df[['Gender', 'Age (in years)', 'Country of residence', 'Living area',
       'Children', 
       'Total conform', 'Risk6', 'Education_cat', 'Job','Small-scale_COVID19', "String_SSC", "Country"]]
df3 = small_scaleC
dfplot3=df[["Country",'Gender', 'Age (in years)', 'Living area',
       'Children', 
        'Risk6', 'Education_cat', 'Job', 'Small-scale_COVID19']]

large_scaleC = df[['Gender', 'Age (in years)', 'Country of residence', 'Living area',
       'Children', 
       'Total conform', 'Risk6', 'Education_cat', 'Job','Large-scale_COVID19', "String_LSC", "Country"]]
df4= large_scaleC
dfplot4=df[["Country",'Gender', 'Age (in years)', 'Living area',
       'Children', 
        'Risk6', 'Education_cat', 'Job', 'Large-scale_COVID19']]

# FIGURE 1: COUNT GLOBAL COLLECTIVISTIC AND INDIVIDUALISTIC ORIENTATIONS IN EACH SITUATION



fig1 = px.bar(counts_fav, x="level_0", y="How_many",color= "1_Indiv_2_Collect", template = "gridon",opacity = 0.5, 
             labels={
                     "How_many": "Collectivistic/invidualistic",
                     "level_0": "CONTEXT"
                     
                 },
             title = "Situation Exposed and type of response")

fig2 = px.parallel_categories(dfplot4, color = dfplot4['Large-scale_COVID19'],
                       color_continuous_scale = plotly.colors.sequential.Blackbody, 
                       labels={"Large-scale_COVID19":""},
                       title = "Large Scale COVID-19: 1) Individualistic and 2) Collectivistic per subject")

fig3 = px.parallel_categories(dfplot2, color = dfplot2['Large-scale_NEUTRAL'], color_continuous_scale = px.colors.sequential.Inferno,
                      labels={"Large-scale_NEUTRAL":""},
                       title = "Large-scale_NEUTRAL: 1) Individualistic and 2) Collectivistic per subject"
                   )


fig4 = px.parallel_categories(dfplot3, color = dfplot3['Small-scale_COVID19'], color_continuous_scale = plotly.colors.sequential.Blackbody,
                       labels={"Small-scale_COVID19":""},
                       title = "Small- Scale COVID-19: 1) Individualistic and 2) Collectivistic per subject"
                   )



fig5 = px.parallel_categories(dfplot1, color = dfplot1["Small-scale_NEUTRAL"], color_continuous_scale = px.colors.sequential.Inferno,
                        labels={"Small-scale_NEUTRAL":""},
                       title = "Small-scale_NEUTRAL: 1) Individualistic and 2) Collectivistic per subject"
                   )

fig6 = px.scatter(df4, x=df4['Total conform'], y=df4["Age (in years)"], color=df4["String_LSC"],  
                    size=df4['Risk6'], template="ggplot2", facet_col = df4['Country'], 
                    title="Collectivistic vs Individualistic choices: Large Scale Covid19 Context")

fig7 = px.scatter(df2, x=df2['Total conform'], y=df2["Age (in years)"], color=df2["String_LSN"],  
                    size=df2['Risk6'], facet_col = df2['Country'], 
                    title="Collectivistic vs Individualistic choices: Large Scale Neutral Context", 
                     color_discrete_map={
                         "Collectivistic orientation": "#61CFBE",
                         "Individualistic orientation": "#AAA8AD",
                         })

fig8 = px.scatter(df3, x=df3['Total conform'], y=df3["Age (in years)"], 
                        color=df3["String_SSC"],  size=df3['Risk6'], template="ggplot2", facet_col = df3['Country'], opacity = 0.7
                    , title="Collectivistic vs Individualistic choices: Small Scale Covid19 Context")

fig9 = px.scatter( df1, x=df1['Total conform'], y=df1["Age (in years)"], color=df1["String_SSN"],  
                    size=df1['Risk6'], template="ggplot2", facet_col = df1['Country'], opacity = 0.7
                    , color_discrete_map={
                 "Collectivistic orientation": "#61CFBE",
                    "Individualistic orientation": "#AAA8AD",
                }, title="Collectivistic vs Individualistic choices: Small Scale Neutral Context", 
)

app.layout = html.Div(children=[
    html.H1(children='GLOBAL APPROACH '),

    html.Div(children='''
        Global Orientation
    '''),

    dcc.Graph(
        id='graph1',
        figure=fig1
    )

    ,html.H1(children='RELATIONSHIPS BETWEEN FEATURES AND TARGETS '),

    html.Div(children='''
        SITUATION LARGE SCALE COVID
    '''),

    dcc.Graph(
        id='graph2',
        figure=fig2
    )
    ,html.H1(children=''),

    html.Div(children='''
        SITUATION LARGE SCALE NEUTRAL
    '''),

    dcc.Graph(
        id='graph3',
        figure=fig3
    ),html.H1(children=''),

    html.Div(children='''
        SITUATION SMALL SCALE COVID
    '''),

    dcc.Graph(
        id='graph4',
        figure=fig4
    ),html.H1(children=''),

    html.Div(children='''
        SITUATION SMALL SCALE NEUTRAL
    '''),

    dcc.Graph(
        id='graph5',
        figure=fig5
    ),
      html.H1(children='RISK PERCEPTION, CONFORMITI, AGE AND CHOICE '),

    html.Div(children='''
       LARGE SCALE COVID19
    '''),

    dcc.Graph(
        id='graph6',
        figure=fig6
    ),
  html.H1(children=''),

    html.Div(children='''
        LARGE SCALE NEUTRAL
    '''),

    dcc.Graph(
        id='graph7',
        figure=fig7
    ),
  html.H1(children=''),

    html.Div(children='''
        SMALL SCALE COVID19
    '''),

    dcc.Graph(
        id='graph8',
        figure=fig8
    ),
  html.H1(children=' '),

    html.Div(children='''
        SMALL SCALE NEUTRAL
    '''),

    dcc.Graph(
        id='graph9',
        figure=fig9
    )

])




if __name__ == '__main__':
    app.run_server(debug=True)
