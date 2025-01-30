# import os
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


if __name__ == "__main__":
    st.title("DATALIZE")
    st.subheader("Visualizing data, made simple")
    
    f = st.file_uploader(label="Please input your file here to continue") # allow the user to upload the file  
    
    st.divider()

    if f:
        col_1, col_2 = st.columns([0.5, 0.5], border=True) # preparation
        plotting_container = st.container(border=True)

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
            # x axis data selector
            x_axis = st.selectbox(
                label="Select your data to be plotted on the X Axis",
                options=df.columns,
                index=None,
                placeholder="X Axis value",
            )

            # y axis data selector
            y_axis = st.multiselect(
                label="Select your data to be plotted on the Y Axis",
                options=df.columns,
                placeholder="Y Axis value // You can choose multiple values to be displayed"
            )

            # chart type selector
            chart_type = st.selectbox(
                label="Select the type of chart to plot",
                options=["area_chart", "line_chart", "bar_chart", "scatter_chart"],
                index=None,
                placeholder="Chart type"
            )
            
            st.code(f"X = '{x_axis}' // Y = {y_axis} // Chart type = '{chart_type}'")

            if (x_axis and y_axis and chart_type):
                eval(f'st.{chart_type}(data=df, x="{x_axis}", y={y_axis})')
            else:
                st.code("please be sure that you have selected all of the data needed to process your chart")
