import pickle
import streamlit as st

pickle_in = open('modelmodel2.pkl', 'rb')

clf = pickle.load(pickle_in)


@st.cache()

def make_prediction(bhk, Bathroom, Size, City):
    if City == 'Mumbai':
        city_enc = 5
    elif City == 'Chennai':
        city_enc = 1
    elif City == 'Bangalore':
        city_enc = 0
    elif City == 'Hyderabad':
        city_enc = 3
    elif City == 'Delhi':
        city_enc = 2
    elif City == 'Kolkata':
        city_enc = 4
    
    prediction = clf.predict([[bhk, Bathroom, Size, city_enc]])[0]
    return prediction


def main():
    #front end elements
    html_temp = """
    <div style = "background-color:green;padding:10px">
    <h1 style = "color:white;text-align:center;"> House Prices Prediction by Ilesanmi </h1>
    </div>
    """

    #front end 
    st.markdown("![](https://cdn.modernghana.com/story_/780/420/424201721206_6_222124n01_0.jpg)")
    
    st.markdown(html_temp, unsafe_allow_html = True)

    #following lines create the visuals
    City = st.selectbox('City', ('Mumbai','Chennai','Bangalore','Hyderabad','Delhi','Kolkata'))    
    Bathroom = st.number_input('Enter number of Bathroom')
    Size = st.number_input('Enter Size of the Land in square Feet (900 sqm is a plot)')
    bhk = st.number_input('Enter number of Bedroom, Hall and Kitchen')

    #when 'predict' is clicked, make prediction
    if st.button('Make Prediction'):
        result = make_prediction(bhk, Bathroom, Size, City)
        st.success('The price is mostlikely: {}'.format(result))
        print('Just test')

if __name__ == '__main__':
    main()


