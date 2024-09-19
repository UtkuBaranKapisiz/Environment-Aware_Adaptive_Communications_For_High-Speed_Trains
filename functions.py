import pandas as pd
import numpy as np
import requests
import random
import joblib


# # initial weather condition
hava_durumu = 5

# gets the data and returns arr[train, node]
def get_data():
    # Function to get the latest data from Flask API
    def get_latest_from_api():
        api_url = "https://<your_api>.pythonanywhere.com/get_latest"  # Replace with your actual Flask API URL, pythonanywhere is an option
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve data")
            return None

    # Fetch the latest data
    latest_data = get_latest_from_api()
    if latest_data is not None:
        node1 = latest_data['node_1']
        node2 = latest_data['node_2']
    
    arr = [node1, node2]
    
    return arr

# gets the data and returns arr[train, node]
def get_data2():
    # Function to get the latest data from Flask API
    def get_latest_from_api2():
        api_url = "https://<your_api>.pythonanywhere.com/get_latest2"  # Replace with your actual Flask API URL
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve data")
            return None

    # Fetch the latest data
    latest_data = get_latest_from_api2()
    if latest_data is not None:
        node3 = latest_data['node_3']
        node4 = latest_data['node_4']
    
    arr = [node3, node4]
    
    return arr

def generate_mesafe(node):
    if node == 0:
        return random.randint(5,8)
    elif node == 1:
        return random.randint(6,10) 
    elif node == 2:
        return random.randint(5,8)    
    elif node == 3:
        return random.randint(3,7)    
    elif node == 4:
        return random.randint(2,5)    
    elif node == 5:
        return random.randint(3,7)    
    elif node == 6:
        return random.randint(1,4)    
    elif node == 7:
        return random.randint(2,5)    
    elif node == 8:
        return random.randint(2,5)    
    elif node == 9:
        return random.randint(1,4)

def generate_los(node):
    if node == 0:
        return random.randint(6,9)
    elif node == 1:
        return random.randint(5,6) 
    elif node == 2:
        return random.randint(6,9)    
    elif node == 3:
        return random.randint(6,9)    
    elif node == 4:
        return random.randint(3,5)    
    elif node == 5:
        return random.randint(6,9)    
    elif node == 6:
        return random.randint(1,4)    
    elif node == 7:
        return random.randint(3,5)    
    elif node == 8:
        return random.randint(1,4)    
    elif node == 9:
        return random.randint(1,3)    

def generate_hava(hava_durumu):
    hava_durumu_current = hava_durumu + random.randint(-3,3)
    if hava_durumu_current < 1:
        hava_durumu_current = 3
    elif hava_durumu_current > 10:
        hava_durumu_current = 8
    
    return hava_durumu_current

def generate_speed(node):
    if node == 0:
        return random.randint(6,8)
    elif node == 1:
        return random.randint(7,10) 
    elif node == 2:
        return random.randint(6,8)    
    elif node == 3:
        return random.randint(1,4)    
    elif node == 4:
        return random.randint(3,5)    
    elif node == 5:
        return random.randint(1,4)    
    elif node == 6:
        return random.randint(5,8)    
    elif node == 7:
        return random.randint(6,9)    
    elif node == 8:
        return random.randint(4,7)    
    elif node == 9:
        return random.randint(5,8)       

def cografya_info(node):
    if node == 0:
        return 7
    elif node == 1:
        return 9
    elif node == 2:
        return 7    
    elif node == 3:
        return 5     
    elif node == 4:
        return 4   
    elif node == 5:
        return 6   
    elif node == 6:
        return 5   
    elif node == 7:
        return 5   
    elif node == 8:
        return 3    
    elif node == 9:
        return 1   

def tunel_info(node):
    if node == 0:
        return 9
    elif node == 1:
        return 9
    elif node == 2:
        return 9    
    elif node == 3:
        return 9     
    elif node == 4:
        return 1   
    elif node == 5:
        return 9   
    elif node == 6:
        return 9   
    elif node == 7:
        return 1   
    elif node == 8:
        return 9    
    elif node == 9:
        return 9 

def generate_array_for_node(node):
    global hava_durumu
    result_array = []
    result_array.append(cografya_info(node))
    result_array.append(tunel_info(node))
    hava_durumu = generate_hava(hava_durumu)
    result_array.append(hava_durumu)
    result_array.append(generate_mesafe(node))
    result_array.append(generate_los(node))
    result_array.append(generate_speed(node))
    
    array_new = np.array(result_array)
    array_new = array_new.reshape(1,6)
    
    return array_new

def get_predictions(features_df):
    # Load the models
    model5 = joblib.load(r'<your_dir>\decision_tree.joblib') # replace with your joblib dir
    model6 = joblib.load(r'<your_dir>\random_forest.joblib') # replace with your joblib dir
    model7 = joblib.load(r'<your_dir>\gradient_boosting.joblib') # replace with your joblib dir
    model8 = joblib.load(r'<your_dir>\random_forest.joblib') # replace with your joblib dir

    # List of models for convenience
    models = [model5, model6, model7, model8]
    model_names = ["Decision Tree", "Random Forest", "Gradient Boosting", "Neural Network"]


    all_predictions = []

    for model, name in zip(models, model_names):
        predictions = model.predict(features_df)
        all_predictions.append(predictions)

    # Convert the list of predictions to a NumPy array
    all_predictions = np.array(all_predictions)
    all_predictions = all_predictions.T
    # Print the array of predictions
    return all_predictions

def get_all_df():
    # train_node_array [train, node]
    temp = get_data()
    temp2 = get_data2()
    
    # 2 digit int
    train_1_node_1 = (temp[0] // 10)
    train_1_node_2 = (temp[1] // 10)
    train_2_node_3 = (temp2[0] // 10)
    train_2_node_4 = (temp2[1] // 10)
    
    # tempin ilk hanesine bak bir olanı curr diye yaz
    if ((temp[0] % 10) == 1):
        train_1_curr_node = train_1_node_1
    elif ((temp[1]  % 10) == 1):
        train_1_curr_node = train_1_node_2
    
    if ((temp2[0] % 10) == 1):
        train_2_curr_node = train_2_node_3
    elif ((temp2[1]  % 10) == 1):
        train_2_curr_node = train_2_node_4  
    
    # setting up the dataframe
    column_names = ["Cografya_zorlugu", "Tunel_sayisi", "Hava_kosulu_zorlugu", "Iletim_noktasi_uzaklik", "DurumLOS", "Bolge_tren_hizi"]
    df1 = pd.DataFrame((generate_array_for_node(train_1_curr_node)), columns=column_names)
    df2 = pd.DataFrame((generate_array_for_node(train_2_curr_node)), columns=column_names)
    df1.insert(loc=0, column="Train", value=(1))
    df1.insert(loc=1, column="Node", value=(train_1_curr_node))
    df2.insert(loc=0, column="Train", value=(2))
    df2.insert(loc=1, column="Node", value=(train_2_curr_node))
    
    return df1, df2

