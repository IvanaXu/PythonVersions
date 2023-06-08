import os
import pandas as pd
from config.date import Ldate

path = "Version/"
data = []
fTASK = lambda x: tuple([int(i) for i in x.split(".")])
TASK = sorted(
    [
        i for i in os.listdir(path) 
        if "3." in i and os.path.exists(f"{path}{i}/py{i}.log")
    ], key=fTASK
)
print(TASK)

for t in TASK:
    t1, t2, tdata = "", "", {}
    with open(f"{path}{t}/py{t}.log") as f:
        for i in f:
            i = i.strip("\n")
            
            if "###" in i:
                t1 = i.replace("###", "").replace(" ", "")
            if "Mean" in i:
                t2 = i.replace("Mean +- std dev: ", "")
                tdata[t1] = t2

                t1, t2 = "", ""

    tdata = pd.DataFrame(
        [[_k, _v] for _k, _v in tdata.items()],
        columns=["Task", t]
    )
    data.append(tdata)

sdata = pd.DataFrame()
for tdata in data:
    if len(sdata) == 0:
        sdata = tdata
    else:
        sdata = pd.merge(sdata, tdata, on="Task", how="outer")


def fchange(string):
    if pd.isna(string):
        return string
    string = str(string).split("+-")[0]

    result = -999999
    if "sec" in string:
        result = float(string.replace("sec", ""))*1000
    elif "ms" in string:
        result = float(string.replace("ms", ""))
    elif "us" in string:
        result = float(string.replace("us", ""))/1000
    elif "ns" in string:
        result = float(string.replace("ns", ""))/1000/1000
    return round(result, 4)

def change(df):
    _df = df[df["Task"] != "pprint_safe_repr"].copy()
    for icol in TASK:
        _df[icol] = _df[icol].apply(fchange)
    return _df

cdata = change(sdata)
cdata0 = cdata.copy()
cdata.loc["SUM"] = [""] + [round(cdata0[icol].sum(), 4) for icol in  TASK]
cdata.loc["AVG"] = [""] + [round(cdata0[icol].mean(), 4) for icol in  TASK]
_max = max([cdata0[icol].sum() for icol in  TASK])
cdata.loc["UP%"] = [""] + [f"{_max/cdata0[icol].sum():.4%}" for icol in  TASK]
Lup = cdata[cdata.index == "UP%"].to_dict()


FIRST = """
### 0.Readme
#### (1) Python Versions
> https://www.python.org/downloads/
#### (2) Running Environment
* Docker gcc library/gcc

<p align="center">
<img src="./environment/M1-ENV.png" width=300>
</p>

#### (3) Test Software
* [Pyperformance](https://github.com/python/pyperformance)

"""

with open("README.md", "w") as f:
    f.write(FIRST)


    f.write("### 1.Versions\n")
    idf = pd.DataFrame(TASK, columns=["version"])
    idf["date"] = idf["version"].apply(lambda x: Ldate.get(x, ""))
    idf["UP%"] = idf["version"].apply(lambda x: Lup.get(x, {}).get("UP%", ""))

    # TOP = 5
    # idf["Rank"] = idf["UP%"].rank(ascending=False).apply(lambda x: max(TOP-int(x)+1, 0) * "🌹")
    # idf["Rank"] = idf["UP%"].rank(ascending=True).apply(lambda x: int(x) * "+")
    
    TOP = 5
    idf["Progress"] = idf["UP%"].apply(lambda x: int(float(x[:-1])/100 * TOP) * ">.")
    idf["rank"] = idf["version"].apply(fTASK)
    idf.sort_values("rank", inplace=True)
    print(idf)

    for i in idf[["version", "date", "UP%", "Progress"]].to_markdown(index=None):
        f.write(i)
    f.write("\n\n")


    f.write("### 2.Details\n")
    for i in sdata.fillna("/").to_markdown():
        f.write(i)
    f.write("\n\n")


    f.write("### 3.Calculation(UNIT: ms)\n")
    for i in cdata.fillna("/").to_markdown():
        f.write(i)
    f.write("\n\n")



