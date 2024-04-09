from flask import Flask, render_template, request
import pandas as pd
import plotly.graph_objs as go


from trial import restaurant_name1

import helper
app = Flask(__name__)

# Read the CSV file
df = pd.read_csv('final.csv')

# restaurant_names = df['name'].sort_values().unique().tolist()

# Extract unique restaurant names and sort them

# Define routes
# @app.route('/')
# def index():
#     # Handle form submission
#     selected_state = request.form['state']
#     selected_city = request.form['city']
#
#     rest_1 = request.form['restaurant1']
#     rest_2 = request.form['restaurant2']
#
#     rest1 = df[df.name == rest_1]['res_id']
#     rest1 = rest1.reset_index(drop=True)
#     rest1 = rest1[0]
#     rest2 = df[df.name == rest_2]['res_id']
#     rest2 = rest2.reset_index(drop=True)
#     rest2 = rest2[0]
#     # st.subheader('Rating Comparision')
#     fig1 = helper.res_rating_com(df, rest1, rest2)
#     # st.plotly_chart(fig)
#     # st.subheader('Average cost for two Comparision')
#     fig2 = helper.res_cost_com(df, rest1, rest2)
#     # st.plotly_chart(fig)
#
#     rating1 = df[df['name'] == rest_1]['aggregate_rating']
#     rating2 = df[df['name'] == rest_2]['aggregate_rating']
#
#     if rating1 is not None and rating2 is not None:
#         # Create bar graph
#         fig = go.Figure(data=[go.Bar(x=[rest_1, rest_2], y=[rating1, rating2])])
#         graph = fig.to_html(full_html=False)
#
#     # Pass the generated Plotly charts to the HTML template
#     return render_template('restaurant_comparison.html', fig_rating_comparison=fig1,
#                            fig_cost_comparison=fig2, restaurant_names=restaurant_name1, graph=graph)
#

@app.route('/')
def submit():
    # Handle form submission
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
    # st.plotly_chart(fig)

    rating1 = df[df['name'] == rest_1]['aggregate_rating']
    rating2 = df[df['name'] == rest_2]['aggregate_rating']

    if rating1 is not None and rating2 is not None:
        # Create bar graph
        fig = go.Figure(data=[go.Bar(x=[rest_1, rest_2], y=[rating1, rating2])])
        graph = fig.to_html(full_html=False)




    # Pass the generated Plotly charts to the HTML template
    return render_template('restaurant_comparison.html', fig_rating_comparison=fig1,
                           fig_cost_comparison=fig2,restaurant_names= restaurant_name1 ,graph =graph)

    # {{graph | safe}} in jinja template

    # Perform any necessary backend logic here

    # Return a response or render a template with the results
    return f"Selected State: {selected_state}, Selected City: {selected_city}, Restaurant 1: {restaurant1}, Restaurant 2: {restaurant2}"


if __name__ == '__main__':
    app.run(debug=True)
