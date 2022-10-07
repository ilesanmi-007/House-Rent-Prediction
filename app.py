import pickle
import streamlit as st

pickle_in = open('modelmodel.pkl', 'rb')

clf = pickle.load(pickle_in)


@st.cache()

def make_prediction(bhk, Bathroom, Size, City):
    if City == 'Mumbai':
        city_enc = 5
    elif City == 'Chennai':
        city_enc = 1
    elif City == 'Banglore':
        city_enc = 0
    elif City == 'Hyderabad':
        city_enc = 3
    elif City == 'Delhi':
        city_enc = 2
    elif City == 'Kolkota':
        city_enc = 4
    
    prediction = clf.predict([[bhk, Bathroom, Size, city_enc]])[0]
    return prediction


def main():
    #front end elements
    html_temp = """
    <div style = "background-color:green;padding:13px">
    <h1 style = "color:blue;text-align:center;"> House Prices Prediction by Ilesanmi </h1>
    </div>
    """

    #front end 
    #st.markdown("![](https://miro.medium.com/max/640/1*D6s2K1y7kjE14swcgITB1w.png)")
    
    st.markdown(html_temp, unsafe_allow_html = True)

    #following lines create the visuals
    City = st.selectbox('City', (' Mumbai','Chennai','Bangalore','Hyderabad','Delhi','Kolkata'))    
    Bathroom = st.number_input('Enter number of Bathroom')
    Size = st.number_input('Enter Size of the Land')
    bhk = st.number_input('Enter number of BHK')

    #when 'predict' is clicked, make prediction
    if st.button('Make Prediction'):
        result = make_prediction(bhk, Bathroom, Size, City)
        st.success('The price is mostlikely: {}'.format(result))
        print('Just test')

if __name__ == '__main__':
    main()


