'''
Dash apps for the demonstration of functionality

Copyright (c) 2018 Gibbs Consulting and others - see CONTRIBUTIONS.md

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# pylint: disable=no-member

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from django_plotly_dash.dash_wrapper import DjangoDash

from morpheme.models import MorphemeAnalysisModel

# pylint: disable=too-many-arguments, unused-argument, unused-variable


app = DjangoDash("PieChartSentence")


def app_layout():
    return (
        html.Div([
            dcc.Tabs(
                style={
                    'backgroundColor': '#ccc',
                    'width': '100%',
                    'fontFamily': 'Sans-Serif',
                    "displaylogo": False,
                },
                children=[
                    dcc.Tab(label='키워드 차트 보기', value=1),
                    dcc.Tab(label='태그 차트 보기', value=2),
                ],
                value=1,
                id='tabs'
            ),
            html.Div(id='output-tab', style={'border': '1px solid #ccc'})
        ])
    )


app.layout = app_layout()


@app.callback(dash.dependencies.Output('output-tab', 'children'), [dash.dependencies.Input('tabs', 'value')])
def display_content(value):
    group_key = None

    if value == 1:
        group_key = 'keyword'
    elif value == 2:
        group_key = 'tag'

    # if groupby_key != 'render':
    queryset = MorphemeAnalysisModel.objects.only('raw_sentence').order_by('-auto_increment_id').first()
    df = pd.read_json(queryset.raw_sentence)
    df = df.groupby([group_key]).size().rename('size').reset_index()
    df = df.sort_values(by=['size'], ascending=False)
    label_list = df[group_key].values.tolist()
    percent_list = df['size'].values.tolist()

    data = [
        {
            'labels': [label_list[:10]][0],
            'values': [percent_list[:10]][0],
            'type': 'pie',
        },
    ]

    return html.Div(
        children=[
            html.H3('마지막으로 분석된 결과', style={'text-align': 'center'}),
            dcc.Graph(
                id='graph',
                figure={
                    'data': data,
                    'layout': {
                        'margin': {
                            'l': 30,
                            'r': 30,
                            'b': 30,
                            't': 30
                        },
                        'legend': {'x': '0', 'y': '1'},
                        'paper_bgcolor': '#00ff0000',  # svg-main
                    }
                },

                config={
                    "displaylogo": False,
                    "scrollZoom": True,
                }
            )
        ])
