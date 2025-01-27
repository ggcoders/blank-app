# import os
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


if __name__ == "__main__":
    st.title("DATAVIEW")  
    
    f = st.file_uploader(label="Let the magic happen") # allow the user to upload the file  
    "---"

    col_1, col_2 = st.columns([0.5, 0.5], border=True)
    plotting_container = st.container(border=True)
    

    if f:
        f_ext = f.name.split(".")[-1] # if the file exists, proceed to get the extension

        try: # retrieve dataframe with the desired extension
            df = eval(f"pd.read_{f_ext}(f)")

        except: # error handling if the extension is not correct formatting
            st.write(f"Incompatible extension -> {f_ext}")
            st.write("Please make sure that the file extension is included in the following list:")
            st.write("[ CSV, XLSX, TXT, JSON, HTML, LaTeX, XML, SQL ]")
    

        with col_1: # showcasing the main dataframe
            st.title("Your Base DataFrame")
            st.divider()
            df, f"'{f.name}' shape is -> {df.shape}"

        
        with col_2: # select multiple columns to create a new desired dataframe
            st.title("Your New DataFrame")
            columns = st.multiselect("", df.columns, placeholder="Select your COLUMNS in the desired order: ")
            
            if len(columns): # display the desired dataframe
                new_df = df[columns]
                columns = [col for col in columns if col in columns]
                new_df, f"new shape is -> {new_df.shape}"
        

        with plotting_container:
            st.title("Select data to plot")
            x_axis = st.selectbox(
                "Select your data to be plotted on the X Axis",
                options=df.columns,
                index=None,
                placeholder="X Axis value"
            )
            y_axis = st.selectbox(
                "Select your data to be plotted on the Y Axis",
                options=df.columns,
                index=None,
                placeholder="Y Axis value"
            )
