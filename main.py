
from pyscript import display, document
import numpy as np
import logging
logging.getLogger('Matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt
plt.figure()
plt.plot([0,1], [0,1])
plt.close()

days = np.array(['Mon','Tue','Wed','Thurs','Fri'])

absences = np.zeros(5, dtype=int)

def Wallahi(e):
    day = document.getElementById("DayOfTheWeek").value
    index = list(days).index(day)

    value = int(document.getElementById("absences").value)

    absences[index] += value

    plt.clf()
    plt.bar(days, absences)
    plt.title("Absences Plot")
    plt.xlabel("days")
    plt.ylabel("absences")
    plt.grid()
    plt.show()

 