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


# FIGURE 1: COUNT GLOBAL COLLECTIVISTIC AND INDIVIDUALISTIC ORIENTATIONS IN EACH SITUATION

fig = px.bar(counts_fav, x="level_0", y="How_many",color= "1_Indiv_2_Collect", template = "gridon",opacity = 0.5, 
             labels={
                     "How_many": "Collectivistic/invidualistic",
                     "level_0": "CONTEXT"
                     
                 },
             title = "Situation Exposed and type of response")
fig.show()

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

#LARGE-SCALE COVID-19

px.parallel_categories(dfplot4, color = dfplot4['Large-scale_COVID19'],
                       color_continuous_scale = plotly.colors.sequential.Blackbody, 
                       labels={"Large-scale_COVID19":""},
                       title = "Large Scale COVID-19: 1) Individualistic and 2) Collectivistic per subject")

#LARGE-SCALE NEUTRAL

px.parallel_categories(dfplot2, color = dfplot2['Large-scale_NEUTRAL'], color_continuous_scale = px.colors.sequential.Inferno,
                      labels={"Large-scale_NEUTRAL":""},
                       title = "Large-scale_NEUTRAL: 1) Individualistic and 2) Collectivistic per subject"
                   )



#SMALL-SCALE COVID-19
px.parallel_categories(dfplot3, color = dfplot3['Small-scale_COVID19'], color_continuous_scale = plotly.colors.sequential.Blackbody,
                       labels={"Small-scale_COVID19":""},
                       title = "Small- Scale COVID-19: 1) Individualistic and 2) Collectivistic per subject"
                   )

#SMALL-SCALE NEUTRAL
px.parallel_categories(dfplot1, color = dfplot1["Small-scale_NEUTRAL"], color_continuous_scale = px.colors.sequential.Inferno,
                        labels={"Small-scale_NEUTRAL":""},
                       title = "Small-scale_NEUTRAL: 1) Individualistic and 2) Collectivistic per subject"
                   )




