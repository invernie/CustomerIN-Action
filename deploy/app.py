#import libraries

import pandas as pd
import numpy as np
import streamlit as st

from PIL import Image
import pickle

import warnings
warnings.filterwarnings('ignore')



st.set_page_config(
    layout='wide',
    page_title = 'Customer In-Action',
    page_icon = 'img/icon.png',
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: shown;}
            footer {visibility: hidden;}
            footer:after {
                          content:'Created by Edith | Samuel | Samson'; 
                          visibility: visible;
                          display: block;
                          position: relative;
                          #background-color: white;
                          padding: 4px;
                          top: 2px;
                          }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#st.sidebar.image("img/side_img.jpg", width=250)

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
#set_background('')
st.title('Customer In-Action')
image = Image.open('./img/header.png')
st.image(image, caption='Photo from Antavo Website')


#load data
new_df = pd.read_csv('./data/new_opt_out_df.csv')
out_prob = pd.read_csv('./data/out_prob.csv')



#load in pipeline
filename = './pipeline/model.pkl'
model = pickle.load(open(filename,'rb'))


def intro():
    import streamlit as st

    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a Page above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


def main():
    
    # get data
    with st.form(key='my_form'):
        col1, col2 = st.columns(2)
        
        with col1:
            last_step = st.selectbox('last_step',['Joined the Program'])
        
        with col2:
            next_step = st.selectbox('recomended_next_step',['level_up','profile'])
        
        submit_button = st.form_submit_button(label='Submit')
        
    
    #add proposed last step to points_at_opt_out
    new_df['proposed_last_step'] = np.round(out_prob[out_prob['action'] == next_step]['last_action'].values[0],5)

    #set X and y
    X = new_df[['days','points_at_opt_out','proposed_last_step']]
    y = new_df['opt_out_prob']
    
    
    # predictions
    new_df['preds'] = model.predict(X)
    
    #calculate probability
    disp = new_df.groupby('action').agg({'opt_out_prob':'mean',"preds": "mean"}).reset_index()
    disp = disp.rename(columns={'opt_out_prob':'previous_churn_probability',
                        'preds':'new_churn_probability'})
    
    if submit_button:
        st.success("Find below the churn probability of next steps")
        disp['recommended_next_step'] = next_step
        disp = disp[['action','recommended_next_step','previous_churn_probability','new_churn_probability']]
        st.table(disp[disp['action'] == last_step].reset_index(drop=True))
        


#main()


page_names_to_funcs = {
    "introduction": intro,
    "Recommender System": main
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
