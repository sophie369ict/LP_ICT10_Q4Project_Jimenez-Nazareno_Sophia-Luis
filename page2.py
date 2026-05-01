from pyscript import document, display
import numpy as np

# Suppress matplotlib font logs
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt
import io
import base64
from matplotlib.ticker import MaxNLocator

# Store data globally
weeks_dict = {f"Week{i}": i for i in range(1, 16)}
week_absences = {}

def addgraph(e):
    week = document.getElementById('Select_Day').value
    absence = int(document.getElementById('Future_profession').value)

    # Save data (accumulate if multiple entries for same week)
    if week in week_absences:
        week_absences[week] += absence
    else:
        week_absences[week] = absence

    # Sort data by week number
    sorted_weeks = sorted(week_absences.keys(), key=lambda w: weeks_dict[w])
    sorted_nums = [weeks_dict[w] for w in sorted_weeks]
    sorted_absences = [week_absences[w] for w in sorted_weeks]

    # Clear previous plot
    plt.clf()

    # Create graph
    plt.plot(sorted_nums, sorted_absences, marker='o')
    plt.title("Absences Over Weeks")
    plt.xlabel("Week")
    plt.ylabel("Number of Absences")
    plt.xticks(sorted_nums, sorted_weeks, rotation=45)  # Set x-ticks to week names with rotation
    plt.grid()
    plt.ylim(0, 6)  # Limit y-axis from 0 to 6
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))  # Force integer y-ticks

    # Save plot to base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    document.getElementById('graphforplot').src = f'data:image/png;base64,{img_str}'

    plt.close()

# Initialize empty graph
plt.figure()
plt.title("Absences Over Weeks")
plt.xlabel("Week")
plt.ylabel("Number of Absences")
plt.xlim(0.5, 15.5)  # Center the ticks
plt.ylim(0, 6)  # Limit y-axis from 0 to 6
plt.xticks(range(1,16), [f'Week{i}' for i in range(1,16)], rotation=45)
plt.grid()
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
img_str = base64.b64encode(buf.read()).decode('utf-8')
document.getElementById('graphforplot').src = f'data:image/png;base64,{img_str}'
plt.close()