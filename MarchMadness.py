import pandas as pd
import matplotlib.pyplot as plt
import sys
import random

oeffD1 = 104.7
tempoD1 = 67.7


pd.set_option("display.max_rows", None, "display.max_columns", None)
teamA = sys.argv[1]
teamB = sys.argv[2]
dfa = pd.read_csv("Teams/" + teamA + ".csv")
dfb = pd.read_csv("Teams/" + teamB + ".csv")

ptsA = round(float(dfa.iloc[0]["PTS"]))
defptsA = round(float(dfa.iloc[2]["PTS"]))
ptsB = round(float(dfb.iloc[0]["PTS"]))
defptsB = round(float(dfb.iloc[2]["PTS"]))

tempoA = (
    round(float(dfa.iloc[0]["FGA"]))
    + 0.475 * round(float(dfa.iloc[0]["FTA"]))
    - round(float(dfa.iloc[0]["ORB"]))
    + round(float(dfa.iloc[0]["TOV"]))
)
deftempoA = (
    round(float(dfa.iloc[2]["FGA"]))
    + 0.475 * round(float(dfa.iloc[2]["FTA"]))
    - round(float(dfa.iloc[2]["ORB"]))
    + round(float(dfa.iloc[2]["TOV"]))
)
tempoB = (
    round(float(dfb.iloc[0]["FGA"]))
    + 0.475 * round(float(dfb.iloc[0]["FTA"]))
    - round(float(dfb.iloc[0]["ORB"]))
    + round(float(dfb.iloc[0]["TOV"]))
)
deftempoB = (
    round(float(dfb.iloc[2]["FGA"]))
    + 0.475 * round(float(dfb.iloc[2]["FTA"]))
    - round(float(dfb.iloc[2]["ORB"]))
    + round(float(dfb.iloc[2]["TOV"]))
)

oeffA = tempoA / ptsA * 100
deffA = deftempoA / defptsA * 100
oeffB = tempoB / ptsB * 100
deffB = deftempoB / defptsB * 100

adjustedpos = (tempoA - tempoD1 + tempoB - tempoD1) + tempoD1
adjustedoeffA = (oeffA - oeffD1 + deffB - oeffD1) + oeffD1
adjustedoeffB = (oeffB - oeffD1 + deffA - oeffD1) + oeffD1


luckA = random.randint(-2, 2)
luckB = random.randint(-2, 2)

# Turnover Rate (lower is better)
tovRateA = round(float(dfa.iloc[0]["TOV"])) / (tempoA + 1)  # Avoid division by zero
tovRateB = round(float(dfb.iloc[0]["TOV"])) / (tempoB + 1)

# Offensive Rebound Advantage (higher is better)
rebAdvA = round(float(dfa.iloc[0]["ORB"])) - round(float(dfa.iloc[2]["DRB"]))
rebAdvB = round(float(dfb.iloc[0]["ORB"])) - round(float(dfb.iloc[2]["DRB"]))

# Adjust prediction with new factors
predictionA = ptsA + luckA - tovRateA * 2 + rebAdvA * 0.5
predictionB = ptsB + luckB - tovRateB * 2 + rebAdvB * 0.5

print("Prediction for " + teamA + ": " + str(round(predictionA)))
print("Prediction for " + teamB + ": " + str(round(predictionB)))
