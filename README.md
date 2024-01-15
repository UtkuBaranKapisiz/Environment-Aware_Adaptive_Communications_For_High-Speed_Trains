# Overview
This project includes a Jupyter Notebook file, Model_selection.ipynb, which compares the performance of various models by training them on the data. The selected models, namely Decision Tree, Random Forest, Gradient Boosting, and Neural Network, are saved for future use using the model_save.py script.

## Files
### 1. Model_selection.ipynb
A Jupyter Notebook file that trains different models on the data and compares their performances.
Utilizes Decision Tree, Random Forest, Gradient Boosting, and Neural Network models.
### 2. model_save.py
Python script to save the selected models (Decision Tree, Random Forest, Gradient Boosting, Neural Network) for future use.
### 3. interface.py
Python script using the Streamlit library to create an interface.
Utilizes the functions defined in functions.py for real-time data prediction.
Displays the predictions on the interface.
### 4. functions.py
Python script containing custom functions used by the interface.py script for real-time data prediction.
# Usage
Run Model_selection.ipynb to train and compare models.
Use model_save.py to save the selected models.
Run interface.py to launch the Streamlit interface for real-time data prediction.
# Dependencies
Ensure you have the necessary dependencies installed. You can install them using the following command:
bash

pip install -r requirements.txt
