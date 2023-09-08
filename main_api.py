
import pandas as pd
import numpy as np
import pickle
from flask import Flask,request,jsonify

model=pickle.load(open('linear_model.pkl','rb'))
columns=pickle.load(open('columns.pkl','rb'))

app=Flask(__name__)

@app.route('/predictionprice', methods=['POST'])

def predictprice():
    data=request.form
    vector=np.zeros(246)
    location=data['location']
    print(location)
    location_list=columns.get('columns')[4:].tolist()
    print(location_list)
    location_index=location_list.index(location)
    vector[location_index]==1
    vector[0]=data['size']
    vector[1]=data['bath']
    vector[2]=data['balcony']
    vector[3]=data['total_sqft_clean']
    # vector[4]=data['price_per_sqft']
    input=[vector]

    prediction = model.predict(input)

    return ('Your house estimate price is Rs.{} lakhs'.format(prediction))

if __name__== "__main__":
    app.run(debug=True)

