from pyscript import display, document
import numpy as np
import matplotlib

matplotlib.set_loglevel("error")
import matplotlib.pyplot as plt

days = np.array(['Mon','Tue','Wed','Thurs','Fri'])
absences = np.zeros(5, dtype=int)

def Wallahi(e):
    day = document.getElementById("DayOfTheWeek").value
    index = list(days).index(day)

    value = int(document.getElementById("absences").value or 0)
    absences[index] += value

    document.getElementById("output").innerHTML = ""

    plt.close()
    plt.figure()
    plt.bar(days, absences)
    plt.title("Absences Plot")
    plt.xlabel("days")
    plt.ylabel("absences")
    plt.grid()

    display(plt, target="output")

 
