# 🏅 Olympic Medal Predictor

A web application that predicts the number of medals a country will win at the Olympics based on its historical data and the number of participating athletes. This project combines a machine learning model (Linear Regression) with a user-friendly web interface built with Flask.

![Screenshot](screenshot.png)
<!-- Replace the image above with a screenshot of your running application -->

---

## ✨ Key Features

- **Smart Prediction:**  
  Users select a country and enter the number of athletes. The app automatically looks up the country's previous medal count from the dataset.

- **Interactive Web Interface:**  
  Clean, modern, and responsive frontend built with HTML & CSS.

- **Scikit-Learn Model:**  
  Utilizes a `LinearRegression` model to predict medal counts.

- **Flask Backend:**  
  Lightweight and robust backend serves the model and handles user requests.

- **Dynamic Dropdown:**  
  The list of countries is dynamically populated from the dataset, ensuring all available countries are included.

---

## ⚙️ How It Works

1. The user selects a country and inputs the number of athletes via the web form.
2. The Flask backend receives this information.
3. It queries an internal dataset (`teams.csv`) to find the most recent medal count for the selected country, which serves as the `prev_medals` feature.
4. The number of athletes and the retrieved `prev_medals` are fed into the pre-trained `LinearRegression` model.
5. The model predicts the total number of medals.
6. The prediction is sent back to the frontend and displayed to the user.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Frontend:** HTML, CSS
- **Model Persistence:** Joblib

---
<img width="1909" height="872" alt="Screenshot 2025-08-06 182352" src="https://github.com/user-attachments/assets/72dcc05f-710e-42ff-ae9c-23a3600599fe" />


## 📁 Project Structure

| File/Folder              | Description                                      |
|--------------------------|--------------------------------------------------|
| olympics_project/        | Project root directory                           |
| ├── app.py               | The main Flask application file                  |
| ├── trainModel.ipynb     | Script to train and save the ML model            |
| ├── olympics_model.joblib| The pre-trained and saved model file             |
| ├── teams.csv            | The dataset with historical Olympics data        |
| ├── requirements.txt     | A list of all required Python packages           |
| └── templates/           | Folder for HTML templates                        |
|     └── index.html       | The HTML file for the frontend                   |


---


## 🚀 Setup and Installation

To run this project on your local machine, follow these steps:

## Setup and Installation

To run this project on your local machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/olympic-medal-predictor.git
cd olympic-medal-predictor

2. Create and Activate a Virtual Environment (Recommended)
For Windows:
python -m venv venv
.\venv\Scripts\activate

For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Train the Model (If olympics_model.joblib is not present)
python train.py

5. Run the Flask Application
python app.py

6. Access the Application
Open your web browser and navigate to http://127.0.0.1:5000.
text


---

## 📖 How to Use
Select a country from the dropdown menu.
Enter the total number of athletes the country is sending.
Click the Predict button.
The predicted total medal count will be displayed below the button.


🔮 Future Improvements
 Deploy to a Cloud Service: Host the application on a platform like Render or PythonAnywhere to make it publicly accessible.
 Enhance Model Accuracy: Experiment with more complex models (e.g., RandomForestRegressor) or additional features (like country GDP) to improve prediction accuracy.
 Add Data Visualization: Display a chart of the country's historical medal performance.
 Improve UI/UX: Add country flags, dynamic backgrounds, and more interactive elements.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📄 License
This project is licensed under the MIT License.

🙏 Acknowledgements
Scikit-learn
Flask
Pandas
NumPy
