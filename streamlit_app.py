# import os
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


if __name__ == "__main__":
    st.title("DATAVIEW")
    # allow the user to insert the file    
    f = st.file_uploader(label="Let the magic happen")
    "---"

    col_1, col_2 = st.columns([0.5, 0.5], border=True)
    container = st.container(border=True)
    # if the file exists, proceed to get the extension
    if f:
        f_ext = f.name.split(".")[-1]

        # retrieve dataframe with the desired extension
        try:
            with col_1:
                st.title("Your Base DataFrame")
                st.divider()
                df = eval(f"pd.read_{f_ext}(f)")
                df, f"'{f.name}' shape is -> {df.shape}"


            # select multiple columns to create a new desired dataframe
            with col_2:
                st.title("Your New DataFrame")
                columns = st.multiselect("", df.columns, placeholder="Select your COLUMNS in the desired order: ")

                # display the desired dataframe
                if len(columns):
                    columns = [col for col in columns if col in columns]
                    df[columns], f"new shape is -> {df[columns].shape}"
            
            with container:
                st.title("Select data to plot")
                st.write("X axis", st.selectbox(df.columns))
                st.write("Y axis")

        # error handling if the extension is not correct 
        except:
            st.write(f"Incompatible extension -> {f_ext}")
            st.write("Please make sure that the file extension is included in the following list:")
            st.write("[ CSV, XLSX, TXT, JSON, HTML, LaTeX, XML, SQL ]")
        
    

