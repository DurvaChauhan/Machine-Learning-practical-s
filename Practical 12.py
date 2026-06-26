#Simulate Green Hydrogen v/s Ammonia Fuel Requirement for Cargo Ships using necessary python libraries. 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Energy demand for cargo ship (kWh)
energy_demand = 500000

# Fuel properties
hydrogen_energy_density = 33.3  # kWh/kg
ammonia_energy_density = 5.17   # kWh/kg

# Conversion efficiencies
hydrogen_efficiency = 0.60
ammonia_efficiency = 0.45

# Fuel required (kg)
hydrogen_required = energy_demand / (
    hydrogen_energy_density * hydrogen_efficiency
)

ammonia_required = energy_demand / (
    ammonia_energy_density * ammonia_efficiency
)

# Create DataFrame
df = pd.DataFrame({
    "Fuel": ["Green Hydrogen", "Ammonia"],
    "Fuel Required (kg)": [hydrogen_required, ammonia_required]
})

print(df)

# Visualization
plt.figure(figsize=(8, 5))
plt.bar(df["Fuel"], df["Fuel Required (kg)"])
plt.title("Fuel Requirement for Cargo Ship")
plt.ylabel("Fuel Required (kg)")
plt.xlabel("Fuel Type")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Multiple voyage simulation
voyages = np.arange(100000, 1000001, 100000)

hydrogen_fuel = voyages / (
    hydrogen_energy_density * hydrogen_efficiency
)

ammonia_fuel = voyages / (
    ammonia_energy_density * ammonia_efficiency
)

plt.figure(figsize=(10, 6))
plt.plot(voyages, hydrogen_fuel, marker='o',
         label='Green Hydrogen')
plt.plot(voyages, ammonia_fuel, marker='s',
         label='Ammonia')

plt.title("Fuel Requirement vs Energy Demand")
plt.xlabel("Energy Demand (kWh)")
plt.ylabel("Fuel Required (kg)")
plt.legend()
plt.grid(True)
plt.show()