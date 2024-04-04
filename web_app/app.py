import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Title of our app
st.title("Visualization for Sensor Data collected from BME680 Sensor and SCD41 Sensor")

csvFile = pd.read_csv('./sensor_data.csv')

df = pd.DataFrame(csvFile)

data = {
    "Sensor": [],
    "Pressure (hPa)": [],
    "Gas Resistance (ppm)": [],
    "Temperature (C)": [],
    "Humidity (%)": [],
    "CO2": [],
    "Created At": []

}

data_temperature = {
    "sensor_id": [],
    "temperature": [],
    "created_at": []
}

data_humidity = {
    "sensor_id": [],
    "humidity": [],
    "created_at": []
}

data_pressure = {
    "sensor_id": [],
    "pressure": [],
    "created_at": []
}

data_gas_resistance = {
    "sensor_id": [],
    "gas_resistance": [],
    "created_at": []
}

data_co2 = {
    "sensor_id": [],
    "co2": [],
    "created_at": []
}

for index, row in df.iterrows():
    if (row['created_at']):
        row['created_at'] = datetime.fromtimestamp(row['created_at']/1000).strftime("%d/%m/%Y %H:%M:%S")
        data['Created At'].append(row['created_at'])
    if (row['sensor_id']):
        data['Sensor'].append(row['sensor_id'])
    # print(row['sensor_id'])
    if (row['temperature']):
        data_temperature['sensor_id'].append(row['sensor_id'])
        data_temperature['temperature'].append(row['temperature'])
        data_temperature['created_at'].append(row['created_at'])
        data['Temperature (C)'].append(row['temperature'])
    if (row['humidity']):
        data_humidity['sensor_id'].append(row['sensor_id'])
        data_humidity['humidity'].append(row['humidity'])
        data_humidity['created_at'].append(row['created_at'])
        data['Humidity (%)'].append(row['humidity'])
    if (row['pressure']):
        data_pressure['sensor_id'].append(row['sensor_id'])
        data_pressure['pressure'].append(row['pressure'])
        data_pressure['created_at'].append(row['created_at'])
        data['Pressure (hPa)'].append(row['pressure'])
    if (row['gas']):
        data_gas_resistance['sensor_id'].append(row['sensor_id'])
        data_gas_resistance['gas_resistance'].append(row['gas'])
        data_gas_resistance['created_at'].append(row['created_at'])
        data['Gas Resistance (ppm)'].append(row['gas'])
    if (row['co2']):
        data_co2['sensor_id'].append(row['sensor_id'])
        data_co2['co2'].append(row['co2'])
        data_co2['created_at'].append(row['created_at'])
        data['CO2'].append(row['co2'])


dfTemperature = pd.DataFrame(data_temperature)
dfHumidity = pd.DataFrame(data_humidity)
dfPressure = pd.DataFrame(data_pressure)
dfGasResistance = pd.DataFrame(data_gas_resistance)
dfCO2 = pd.DataFrame(data_co2)
dfData = pd.DataFrame(data)

# Displaying a table with Streamlit
st.header("Displaying Sensor Data from CSV")
st.write(dfData.head(200))

# Using line_chart to visualize the data
st.header("Data Visualization for Temperature (C)")
st.line_chart(dfTemperature, x="created_at", y="temperature", color="sensor_id")

st.header("Data Visualization for Humidity (%)")
st.line_chart(dfHumidity, x="created_at", y="humidity", color="sensor_id")

st.header("Data Visualization for Pressure (hPa)")
st.line_chart(dfPressure, x="created_at", y="pressure", color="sensor_id")

st.header("Data Visualization for Gas Resistance (ppm)")
st.line_chart(dfGasResistance, x="created_at", y="gas_resistance", color="sensor_id")

st.header("Data Visualization for CO2 (ppm)")
st.line_chart(dfCO2, x="created_at", y="co2", color="sensor_id")

