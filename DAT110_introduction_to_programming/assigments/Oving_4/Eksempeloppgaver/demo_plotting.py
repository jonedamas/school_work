import matplotlib.pyplot as plt

# List comprehension: liste av alle elementene fra og med 0, til men ikke med 20
x_koordinater = [x for x in range(0, 20)]

# List comprehension: For hvert element i x-koordinater, regn ut x**2 og sett
# inn i den nye lista.
y_koordinater = [x**2 for x in x_koordinater]

plt.plot(x_koordinater, y_koordinater, label="x**2")
plt.title("Tester plotting")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.plot(x_koordinater, y_koordinater, "o")
y_koordinater_2 = [5*x for x in x_koordinater]
plt.plot(x_koordinater, y_koordinater_2, label="5*x")
plt.legend()
plt.show()
