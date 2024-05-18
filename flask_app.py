import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor



dataset = pd.read_csv('flask_test/House_Rent_Dataset.csv')
delhi_data = dataset[dataset['City']=="Delhi"]
X = delhi_data[['BHK','Size','Bathroom']]
Y = delhi_data['Rent']

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2)
RFR = RandomForestRegressor() 
model = RFR.fit(X_train,y_train)


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict([data['features']])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
