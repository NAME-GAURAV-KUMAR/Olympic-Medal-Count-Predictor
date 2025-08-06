
from flask import Flask, request, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model and the dataset
model = joblib.load('olympics_model.joblib')
teams_data = pd.read_csv('teams.csv')

# Function to get the 'prev_medals' for a given country
def get_prev_medals(country_name):
    # Filter data for the specified country
    country_df = teams_data[teams_data['team'] == country_name]
    if country_df.empty:
        # If country is new or not in our data, assume 0 previous medals
        return 0
    
    # Find the most recent entry before our prediction year (e.g., 2012)
    # and get its medal count.
    # Here, we just find the most recent year in the dataset for simplicity.
    latest_year = country_df['year'].max()
    prev_medals = country_df[country_df['year'] == latest_year]['medals'].values[0]
    return prev_medals


@app.route('/')
def home():
    # Get a list of unique country names for the dropdown
    countries = sorted(teams_data['team'].unique())
    return render_template('index.html', countries=countries)


@app.route('/predict', methods=['POST'])
def predict():
    # Get user inputs from the form
    country = request.form['country']
    athletes = float(request.form['athletes'])

    # --- This is the "smart" part ---
    # Automatically find the previous medals for the selected country
    prev_medals = get_prev_medals(country)

    # Create the feature array for the model
    # It must be in the same order as your 'predictors' list: ['athletes', 'prev_medals']
    features = np.array([[athletes, prev_medals]])

    # Make prediction
    prediction = model.predict(features)
    output = round(prediction[0])
    
    # Get a list of unique country names for the dropdown
    countries = sorted(teams_data['team'].unique())

    # Return the result to the page
    return render_template(
        'index.html', 
        countries=countries,
        selected_country=country,
        prediction_text=f'Predicted Medals for {country}: {output}',
        details_text=f'(Based on {int(athletes)} athletes and {int(prev_medals)} previous medals found in data)'
    )

if __name__ == "__main__":
    app.run(debug=True)