import matplotlib.pyplot as plt
import numpy as np

Testmarks = [98,78, 68, 73, 72, 97, 88, 60, 94, 95, 80, 73, 82, 80, 99, 91, 74, 88, 70, 94, 86, 81, 100, 99, 84, 93, 94, 79]
myStd=np.std(Testmarks)
mymean=np.mean(Testmarks)

print(myStd)

cities=['East London', 'Cape Town', 'Kimberley', 'Durban']
rainfall= [140,  200, 120, 157]
x_pos = [i for i, _ in enumerate(cities)] #labels on the x-axis
#labeling and visuals
plt.bar(x_pos, rainfall, color='green')
plt.xlabel("cities")
plt.ylabel("Rainfall in (mm)")
plt.title("Rainfall for the 4 main cities in SA")
plt.xticks(x_pos, cities)
plt.show()

x = np.array([14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5])
y = np.array([200, 330, 190, 340, 410, 445, 415])

m, b = np.polyfit(x, y, 1)
plt.plot(x, y, 'o')
plt.plot(x, m*x + b)
