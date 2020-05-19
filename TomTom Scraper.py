import matplotlib.pyplot as plt
import pandas as pd
import json
import requests

# retrieve json file
url_ = "https://api.midway.tomtom.com/ranking/live/CHN_shanghai"
italy_req = requests.get(url_)
italy_json = italy_req.json()

#expand output to display more rows
pd.set_option("display.max_rows", False)

# create empty lists of append data
live_traffic = []
time = []

count = len(italy_json["data"])-1

# append each item in the json file to the empty lists
i = 0
while i <= count:
    live_traffic.append(italy_json["data"][i]["TrafficIndexLive"])
    time.append(italy_json["data"][i]["UpdateTime"])
    i += 1

# create dataframe with the traffic data
df = pd.DataFrame({"Live Traffic": live_traffic}, index=time)
df.index = pd.to_datetime(df.index, unit="ms")
df.index.name = "Time"
print(df.head(5))

plt.style.use("ggplot")
ax = df.plot(color="Green")
plt.title("Shanghai Traffic")
plt.legend(loc=2)
plt.show()