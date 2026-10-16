import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

engine_rpm = 1400

# Load the diesel PV data
df = pd.read_excel('Diesel_PV_Data_1400RPM.xlsx')

# Load the petrol PV data
df2 = pd.read_excel('Petrol_PV_Data_1400RPM.xlsx')

# Convert data frames to numpy arrays
d_vol_data = df.iloc[:, 0].to_numpy()
d_prs_data = df.iloc[:, 1].to_numpy()

p_vol_data = df2.iloc[:, 0].to_numpy()
p_prs_data = df2.iloc[:, 1].to_numpy()

plt.figure(figsize=(8,6))
plt.plot(d_vol_data, d_prs_data, label=f'Diesel Cycle {engine_rpm} rpm')
plt.plot(p_vol_data, p_prs_data, label=f'Petrol Cycle {engine_rpm} rpm')

plt.title(f"Petrol and Diesel cycle overlay at {engine_rpm} rpm", fontsize=16)
plt.xlabel('Volume [m^3]')
plt.ylabel('Pressure [kPa]')

plt.grid(True)
plt.legend()
plt.show()