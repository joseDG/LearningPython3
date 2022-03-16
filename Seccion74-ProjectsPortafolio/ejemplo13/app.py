import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# These might be helpful:
#from iso3166 import countries
from datetime import datetime, timedelta


data = pd.read_csv("mission_launches.csv")
#company = data.Organisation
names = data.groupby("Organisation")
months = data.groupby("Organisation").count()
values = months["Unnamed: 0.1"]
print(values)

month = data.Date
month_dict = {

}
month_list = []
for i in month:
    mon = i.split()
    month_list.append(mon[1])

for names in month_list:
    new = month_list.count(names)
    month_dict[names] = new

print(month_dict)



#company = data.Organisation
status = data.groupby("Mission_Status").count()
stat = status["Rocket_Status"]
print(stat)

plt.plot(values.index, values)
plt.show()