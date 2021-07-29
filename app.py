import joblib
import streamlit as st

#Load the model
model = joblib.load('Model')

def predict_car_price(present_price, kms_driven, fuel_type, seller_type, transmission, owner, car_age):
    prediction = model.predict([[present_price, kms_driven, fuel_type, seller_type, transmission, owner, car_age]])
    return prediction[0]

def main():

    with st.sidebar.beta_expander('About'):
        st.write('This Machine learning app uses XGBoost Regressor to predict the selling price of used cars. The model was trained on vehicle dataset which contains 301 rows of car details from cardekho.com. The front end is built using Streamlit😊')

    with st.sidebar.beta_expander('Contact'):
        st.write('[GitHub](https://github.com/VaisakNair7/Used-Car-Price-Prediction)')
        st.write('[LinkedIn](https://www.linkedin.com/in/vaisaksnair/)')
        st.write('Mail : vaisaksnair98@gmail.com')
    
    html_temp = """
    <div style="background-color:#88B04B;padding:10px">
    <h1 style="color:white;text-align:center;">Used Car Price Predictor</h1>
    </div>
    <br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    present_price = st.text_input('Current ex-showroom price of the car (Lakhs)')
    kms_driven = st.text_input('Kilometers Driven')
    fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
    seller_type = st.selectbox('Seller Type', ['Dealer', 'Individual'])
    transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])   
    owner = st.selectbox('Number of owners the car previously had', [0, 1, 2])
    car_age = st.slider('Years since bought', min_value = 0, max_value = 25)

    if st.button('Predict'):
        if not present_price or not kms_driven:
            st.error('Please fill the required fields')
        else:
            price = predict_car_price(present_price, kms_driven, fuel_type, seller_type, transmission, owner, car_age)
            st.success('Predicted selling price: {} {:.2f} Lakhs'.format(u"\u20B9", price))
    

if __name__ == '__main__':
    main()

