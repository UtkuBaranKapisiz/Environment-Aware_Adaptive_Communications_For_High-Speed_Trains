import time
import streamlit as st
import functions as func

# Streamlit app layout
st.title('Metrics And Prediction')

# Display placeholders for DataFrame and text
dataframe_placeholder = st.empty()
text_placeholder = st.empty()

# Model Selection
model_names = ["Decision Tree", "Random Forest", "Gradient Boosting", "Neural Network"]
selected_model = st.sidebar.selectbox("Makine Öğrenmesi Modeli Seçin:", model_names)
# Train Selection
train_options = ['1 Nolu Tren', '2 Nolu Tren']
selected_train = st.sidebar.selectbox("Tren Seçin:", train_options)


while True:

    df1, df2 = func.get_all_df()
    features_df1 = df1.iloc[:, 2:8]
    features_df2 = df2.iloc[:, 2:8]
    predictions1 = func.get_predictions(features_df1)[0]
    predictions2 = func.get_predictions(features_df2)[0]
    if selected_train == '1 Nolu Tren':
        if selected_model == "Decision Tree":
            df1["Role"] = predictions1[0]
        elif selected_model == "Random Forest":
            df1["Role"] = predictions1[1]
        elif selected_model == "Gradient Boosting":
            df1["Role"] = predictions1[2]
        elif selected_model == "Neural Network":
            df1["Role"] = predictions1[3]

        with text_placeholder:
            st.write('## Additional Text:')
            if df1.at[0, "Role"] == 1:
                st.write(f'The {selected_model} predicts to use relays ')
            elif df1.at[0, "Role"] == 2:
                st.write(f'The {selected_model} predicts to NOT use relays ')        
        with dataframe_placeholder:
            st.write('## Displaying DataFrame:')
            st.write(df1.T)        
    elif selected_train == '2 Nolu Tren':
        if selected_model == "Decision Tree":
            df2["Role"] = predictions2[0]
        elif selected_model == "Random Forest":
            df2["Role"] = predictions2[1]
        elif selected_model == "Gradient Boosting":
            df2["Role"] = predictions2[2]
        elif selected_model == "Neural Network":
            df2["Role"] = predictions2[3]
            
        with text_placeholder:
            st.write('## Additional Text:')
            if df2.at[0, "Role"] == 1:
                st.write(f'The {selected_model} predicts to use relays ')
            elif df2.at[0, "Role"] == 2:
                st.write(f'The {selected_model} predicts to NOT use relays ')        
        with dataframe_placeholder:
            st.write('## Displaying DataFrame:')
            st.write(df2.T)          


    time.sleep(1)  # Wait for 5 seconds before updating again