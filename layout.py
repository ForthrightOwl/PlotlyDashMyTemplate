from dash import html, dcc, dash_table
from dash.dependencies import Input, Output
from app import app
import styling as sty
import pandas as pd
import plotly.express as px

styling_theme = sty.dark_theme

#Styling the line graph
df = pd.DataFrame({ "x":[1,2,3,4,5],
                    "y":[3,5,9,11,18],
                    "z":[1,8,-7,25,17],
                    "a":[5,2,9,23,14]})
fig = px.line(df, x="x", y=["y","z","a"],
              color_discrete_sequence=styling_theme["color_map"],
              )
fig.update_layout(
    font_family=styling_theme["title_font_type"],
    font_color=styling_theme["title_font_color"],
    title_font_family=styling_theme["title_font_type"],
    title_font_color=styling_theme["title_font_color"],
    plot_bgcolor = styling_theme["box_background_color"],
    paper_bgcolor = styling_theme["box_background_color"]
)
fig.update_xaxes(showgrid=False)
fig.update_yaxes(gridwidth=3, gridcolor=styling_theme["background_color"])
fig.update_traces(line=dict(width=3))
fig.update_layout(legend=dict(
    orientation="h"
))

app_layout = html.Div(children=[


        #Title on the very top of the page
        html.Div(children=["TITLE OF THE PROJECT GOES HERE"],
                    style={"font-family":styling_theme["title_font_type"],
                           "color":styling_theme["title_font_color"],
                           "text-align":"left",
                           "margin-left":"3%",
                           "margin-top":"1%",
                           "margin-bottom":"1%",
                           "background-color":styling_theme["title_background_color"],
                           "font-size":styling_theme["title_font_size"],
                           "font-style":"normal"}),

        #Tab selection below the title
        html.Div(
                dcc.Tabs(id="tab-bar", value="tab1", children=[
                        dcc.Tab(label="TAB 1", value="tab1",
                                style={"font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "padding-top":styling_theme["tabs_padding"],
                                       "padding-bottom":styling_theme["tabs_padding"]
                                       },
                                selected_style={
                                       "font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "border-bottom":"solid 7px #9adfd2",
                                       "padding-top":styling_theme["tabs_padding"],
                                       "padding-bottom":styling_theme["tabs_padding"]
                                       }),

                        dcc.Tab(label="TAB 2", value="tab2",
                                style={"font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "margin-left":"1%",
                                       "padding-top":styling_theme["tabs_padding"],
                                       "padding-bottom":styling_theme["tabs_padding"]},
                                selected_style={
                                       "font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "border-bottom":"solid 7px #9adfd2",
                                       "margin-left":"1%",
                                       "padding-top":styling_theme["tabs_padding"],
                                       "padding-bottom":styling_theme["tabs_padding"]
                                       }
                                ),
                        dcc.Tab(label="TAB 3", value="tab3",
                                style={"font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "margin-left":"1%",
                                       "padding-top":styling_theme["tabs_padding"],
                                       "padding-bottom":styling_theme["tabs_padding"]},
                                selected_style={
                                       "font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "border-bottom":"solid 7px #9adfd2",
                                       "margin-left":"1%",
                                       "padding-top":styling_theme["tabs_padding"],
                                       "padding-bottom":styling_theme["tabs_padding"]
                                       }),
                        dcc.Tab(label="TAB 4", value="tab4",
                                style={"font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "margin-left":"1%",
                                       "padding-top":styling_theme["tabs_padding"],
                                       "padding-bottom":styling_theme["tabs_padding"]},
                                selected_style={
                                       "font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "border-bottom":"solid 7px #9adfd2",
                                       "margin-left":"1%",
                                       "padding-top":styling_theme["tabs_padding"],
                                       "padding-bottom":styling_theme["tabs_padding"]
                                       })
                    ],
                         #Styles the dcc.Tabs
                         style={
                                "width":"94%",
                                "margin-left":"3%",
                                "height":"auto"
                         },

                #Closes the dcc.Tabs
                )
        #Closes the tab selection Div
        ),

        #First section beneath the tab bar
        html.Div(children=[

            #Title of the first section
            html.Div(
                children=["TITLE OF THE FIRST SUBSECTION"],
                style={"font-family": styling_theme["title_font_type"],
                       "color": styling_theme["title_font_color"],
                       "text-align": "left",
                       "margin-left": "3%",
                       "margin-top": "1%",
                       "margin-bottom": "1%",
                       "background-color": styling_theme["title_background_color"],
                       "font-size": styling_theme["subtitle_font_size"],
                       "font-style": "normal"}
            ),

            #The div containing two boxes
            html.Div([
                #The left box of the first div
                html.Div(
                    children=[
                        "Let's put some text in here just for the sake of it. "
                        "Let's put some text in here just for the sake of it. "
                        "Let's put some text in here just for the sake of it."
                    ],
                    style={"background-color":styling_theme["box_background_color"],
                       "font-family": styling_theme["title_font_type"],
                       "color": styling_theme["title_font_color"],
                       "font-size": styling_theme["body_font_size"],
                       "width":"29.5%",
                       "min-height":"100%",
                       "padding":"1%",
                        }
                ),

                    #The second Div on the right
                    html.Div(
                    children=[
                        #The title of the box
                        html.Div(children=["Title of the box"],
                                 style={"background-color": styling_theme["box_background_color"],
                                        "font-family": styling_theme["title_font_type"],
                                        "color": styling_theme["title_font_color"],
                                        "padding": "1%",
                                        "font-color":styling_theme["title_font_color"],
                                        "font-size":styling_theme["box_font_size"],
                                        "display":"inline-flex"
                                        }
                                 ),

                        #The graph
                        dcc.Graph(id="mygraph", figure=fig)

                    ],
                    style={"background-color":styling_theme["box_background_color"],
                       "font-family": styling_theme["title_font_type"],
                       "color": styling_theme["title_font_color"],
                       "width":"65%",
                       "margin-left":"1%",
                        "padding":"1%"
                        }
                ),


            ],
            #Styling the first section
            style={"margin-left":"3%",
                   "width":"94%",
                   "display":"inline-flex",
                   "align":"top"
                   }
            )

        ],

        #Styles the first section beneath the tab bar
        style={
            "margin-top":"2%",
            "background-color":styling_theme["background_color"]
        }
        ),

        html.Div(children=[],
                 style={"background-color":styling_theme["background_color"],
                        "height":"5cm"
                        })
#Closes the opening Div
],
style={"background-color":styling_theme["title_background_color"]}

)


