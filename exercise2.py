# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

weekday_in_order = ['Saturday', 'Sunday']
counts_in_order = [160613, 154225, 155175, 150819, 146014, 215725, 203483]
bike_s = [52642, 50812, 51866, 50913, 49740, 71586, 68147]
ped_n = [26884, 26444, 25876, 24368, 23403, 36894, 32792]


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Delannah Collins-Wright'),
    html.Div(children='''
    '''),

dcc.Graph(
    id='example-graph',
        figure={
            # configure the data
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': weekday_in_order, 'y': counts_in_order, 'type': 'bar:', 'name': 'Total'},
                {'x': weekday_in_order, 'y': bike_s, 'type': 'bar:', 'name': 'Bike_s'},
                {'x': weekday_in_order, 'y': ped_n, 'type': 'bar:', 'name': 'Ped_n'},

            ],

            'layout': {
                'title': 'Comparing Bike S and Ped N to Total'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)







# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.
