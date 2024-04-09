from flask import Flask, render_template, request
import pandas as pd

import helper

app = Flask(__name__)

# Read the CSV file
dfs = pd.read_excel('data.xlsx')

df = pd.read_csv("final.csv")



# Extract unique state, city, and restaurant names and sort them
unique_states = "karnataka"
unique_cities = "Bangalore"
restaurant_name1 = sorted(dfs['res_name'].unique())
restaurant_name2 = sorted(dfs['res_name'].unique())



# Define routes
@app.route('/')
def index():
    return render_template('restaurant_comparison.html',
                           unique_states=unique_states,
                           unique_cities=unique_cities,
                           restaurant_name1=restaurant_name1,
                           restaurant_name2=restaurant_name2)

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form submission
    # selected_state = request.form['restaurant1']
    # selected_city = request.form['restaurant1']
    # rest_1 = request.form['restaurant1']
    # rest_2 = request.form['restaurant2']
    #
    # rest1 = df[df.name == rest_1]['res_id']
    # rest1 = rest1.reset_index(drop=True)
    # rest1 = rest1[0]
    #
    # rest2 = df[df.name == rest_2]['res_id']
    # rest2 = rest2.reset_index(drop=True)
    # rest2 = rest2[0]
    #
    # fig_rating_comparison = helper.res_rating_com(df, rest1, rest2)
    # fig_cost_comparison = helper.res_cost_com(df, rest1, rest2)
    selected_state = request.form['state']
    selected_city = request.form['city']

    rest_1 = request.form['restaurant1']
    rest_2 = request.form['restaurant2']

    rest1 = df[df.name == rest_1]['res_id']
    rest1 = rest1.reset_index(drop=True)
    rest1 = rest1[0]
    rest2 = df[df.name == rest_2]['res_id']
    rest2 = rest2.reset_index(drop=True)
    rest2 = rest2[0]
    # st.subheader('Rating Comparision')
    fig1 = helper.res_rating_com(df, rest1, rest2)
    # st.plotly_chart(fig)
    # st.subheader('Average cost for two Comparision')
    fig2 = helper.res_cost_com(df, rest1, rest2)
    n1 = list(df[df.res_id == rest1]['name'])[0]
    n2 = list(df[df.res_id == rest2]['name'])[0]

    return render_template('restaurant_comparison.html',
                           fig_rating_comparison=fig1,
                           fig_cost_comparison=fig2,
                           restaurant1=n1,
                           restaurant2=n2,
                           selected_state=selected_state,
                           selected_city=selected_city,
                           selected_restaurant1=rest_1,
                           selected_restaurant2=rest_2)

if __name__ == '__main__':
    app.run(debug=True)