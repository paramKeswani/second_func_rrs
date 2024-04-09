from flask import Flask, render_template, request
import pandas as pd
import helper
import json

import plotly

app = Flask(__name__)

# Read the CSV file
df = pd.read_excel('data.xlsx')
# df = pd.read_csv("final.csv")

# Extract unique state, city, and restaurant names and sort them
unique_states = "karnataka"
unique_cities = "Bangalore"
restaurant_name1 = sorted(df['res_name'].unique())
restaurant_name2 = sorted(df['res_name'].unique())

# Define routes
@app.route('/')
def index():
    return render_template('restaurant_comparison.html',
                           unique_states=unique_states,
                           unique_cities=unique_cities,
                           restaurant_name1=restaurant_name1,
                           restaurant_name2=restaurant_name2)


@app.route('/', methods=['POST'])
def submit():
    selected_state = request.form['state']
    selected_city = request.form['city']

    rest_1 = request.form['restaurant1']
    rest_2 = request.form['restaurant2']

    rest1 = df[df.res_name == rest_1]['id']
    if not rest1.empty:
        rest1 = rest1.reset_index(drop=True)[0]
    else:
        # Handle case when no matching restaurant is found
        return "Restaurant 1 not found."

    rest2 = df[df.res_name == rest_2]['id']
    if not rest2.empty:
        rest2 = rest2.reset_index(drop=True)[0]
    else:
        # Handle case when no matching restaurant is found
        return "Restaurant 2 not found."

    fig1 = helper.res_rating_com(df, rest1, rest2)
    fig2 = helper.res_cost_com(df, rest1, rest2)

    n1 = list(df[df.id == rest1]['res_name'])[0]
    n2 = list(df[df.id == rest2]['res_name'])[0]

    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON1)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON2)

    return render_template('restaurant_comparison.html',
                           graphJSON1=graphJSON1,
                           graphJSON2=graphJSON2,
                           restaurant1=n1,
                           restaurant2=n2,
                           selected_state=selected_state,
                           selected_city=selected_city,
                           selected_restaurant1=rest_1,
                           selected_restaurant2=rest_2)


if __name__ == '__main__':
    app.run(debug=True)
