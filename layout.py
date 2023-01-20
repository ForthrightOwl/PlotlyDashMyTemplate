from dash import html, dcc, dash_table
from dash.dependencies import Input, Output
from app import app
import styling as sty


styling_theme = sty.dark_theme



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
                                       "border":"none"
                                       },
                                selected_style={
                                       "font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "border-bottom":"solid 7px #9adfd2"
                                       }),

                        dcc.Tab(label="TAB 2", value="tab2",
                                style={"font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "margin-left":"1%"},
                                selected_style={
                                       "font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "border-bottom":"solid 7px #9adfd2",
                                       "margin-left":"1%"
                                       }
                                ),
                        dcc.Tab(label="TAB 3", value="tab3",
                                style={"font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "margin-left":"1%"},
                                selected_style={
                                       "font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "border-bottom":"solid 7px #9adfd2",
                                       "margin-left":"1%"
                                       }),
                        dcc.Tab(label="TAB 4", value="tab4",
                                style={"font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "margin-left":"1%"},
                                selected_style={
                                       "font-family":styling_theme["tabs_font_type"],
                                       "font":styling_theme["tabs_font_color"],
                                       "background-color":styling_theme["tabs_background_color"],
                                       "font-size":styling_theme["tabs_font_size"],
                                       "color":styling_theme["tabs_font_color"],
                                       "border":"none",
                                       "border-bottom":"solid 7px #9adfd2",
                                       "margin-left":"1%"
                                       })
                    ],
                         #Styles the dcc.Tabs
                         style={
                                "width":"94%",
                                "margin-left":"3%",
                                "height":"3%"
                         },

                #Closes the dcc.Tabs
                )
        #Closes the tab selection Div
        ),



#Closes the opening Div
],
style={"background-color":styling_theme["title_background_color"]}

)


