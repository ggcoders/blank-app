import streamlit as st
import pandas as pd
import matplotlib

# basic page configuration
st.set_page_config(
    layout="wide", 
    page_icon="images/logo.png", 
    page_title="Datalize"
    )

def get_df(file) -> pd.DataFrame | None:
    '''
    get_df(file) is going to return a dataframe if possible. \n
    The file extension will be retrieved by itself and if it's included in the pandas library it will be opened. \n
    All of this will be possible thanks to the extension retrieving and the eval() function.
    '''
    # if the file exists, proceed to get the extension
    f_ext = file.name.split(".")[-1]

    # retrieve dataframe with the desired extension
    try:
        data = eval(f"pd.read_{f_ext}(f)")

    # error handling if the extension is not correct formatting
    except: 
        st.write(f"Incompatible extension -> {f_ext}")
        st.write("Please make sure that the file extension is included in the following list:")
        st.code("[ CSV, XLSX, TXT, JSON, HTML, LaTeX, XML, SQL ]")
        st.write("If the extension is in the list, please make sure that the file is formatted correctly")
        
        return None
    
    return data


if __name__ == "__main__":
    st.markdown(
        '''
        # Datalize
        #### Data Analytics, :rainbow[but simple]
        '''
    )
    
    # allow the user to upload the file
    f = st.file_uploader(label="Please input your file here to continue", )
    st.divider()

    df = None

    if f:
        df = get_df(f)

    if df is not None:
        # segments creations for later
        col_1, col_2 = st.columns([0.5, 0.5], border=True)
        plotting_container = st.container(border=True)

        # showcasing the main dataframe in the dedicated column
        with col_1:
            st.markdown(
                '''
                # Your Main Dataframe
                ---
                '''
            )
            df.style.background_gradient(cmap='plasma'), 
            f"'{f.name}' current shape is -> {df.shape}"

        # select multiple columns to create a new desired dataframe
        with col_2: 
            st.markdown(
                '''
                # Your :rainbow[New Dataframe]
                '''
            )
            columns = st.multiselect(
                label="new_df selector",
                options=df.columns, 
                placeholder="Select your COLUMNS in the desired order: ",
                label_visibility="hidden"
                )
            
            # display the desired dataframe
            if len(columns) > 2: 
                new_df = df[columns]
                columns = [col for col in columns if col in columns]
                new_df.style.background_gradient(cmap='plasma'), 
                f"new shape is -> {new_df.shape}"
        

        with plotting_container:
            st.markdown(
                '''
                # Select the data you want to plot
                '''
            )
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
            
            row_selector = st.slider(
                label="Select your range // Leave blank if not specific",
                min_value=0,
                max_value=len(df.index - 1),
                value=(0, len(df.index - 1))
            )

            st.code(f"X = '{x_axis}' // Y = {y_axis} // Chart type = '{chart_type}' // Rows selected = '{row_selector}'")

            if (x_axis and y_axis and chart_type and row_selector):
                prompt = f'st.{chart_type}(data=df[{row_selector[0]}:{row_selector[1]}], x="{x_axis}", y={y_axis})'
                eval(prompt)
                st.code(prompt)
            else:
                st.code("please be sure that you have selected all of the data needed to process your chart")
