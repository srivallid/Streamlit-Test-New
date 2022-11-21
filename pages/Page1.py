import streamlit as st
import pandas as pd
from password_check import check_password
import os
import zipfile
import pickle
import janitor

if check_password():
    st.set_page_config(page_title="Page1", page_icon="⚙️")
    st.write("This is a test page")
    df = pd.DataFrame({'a' : [1,2,3,4,5,6],
                       'b' : [2,3,4,5,6,7]})
    df = df.clean_names()
    df
    archive = zipfile.ZipFile('models//testregmodel.zip', 'r')
    lr = pickle.loads(archive.open('testregmodel.sav').read())
    st.write(lr)
    
    
    

