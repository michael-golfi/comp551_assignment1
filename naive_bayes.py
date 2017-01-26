import pandas as pd
import numpy as np
import math

# Enumerate all combinations of possible features for double checking
# Some are duplicated due to generator output.
columnChoices3 = [["2015", "Sex", "Age Category"],
["2015", "Sex", "Rank"],
["2015", "Sex", "TotalRaces"],
["2015", "Sex", "LastRace"],
["2015", "Age Category", "Sex"],
["2015", "Age Category", "Rank"],
["2015", "Age Category", "TotalRaces"],
["2015", "Age Category", "LastRace"],
["2015", "Rank", "Sex"],
["2015", "Rank", "Age Category"],
["2015", "Rank", "TotalRaces"],
["2015", "Rank", "LastRace"],
["2015", "TotalRaces", "Sex"],
["2015", "TotalRaces", "Age Category"],
["2015", "TotalRaces", "Rank"],
["2015", "TotalRaces", "LastRace"],
["2015", "LastRace", "Sex"],
["2015", "LastRace", "Age Category"],
["2015", "LastRace", "Rank"],
["2015", "LastRace", "TotalRaces"],
["Sex", "2015", "LastRace"],
["Sex", "2015", "Age Category"],
["Sex", "2015", "Rank"],
["Sex", "2015", "TotalRaces"],
["Sex", "Age Category", "LastRace"],
["Sex", "Age Category", "2015"],
["Sex", "Age Category", "Rank"],
["Sex", "Age Category", "TotalRaces"],
["Sex", "Rank", "LastRace"],
["Sex", "Rank", "2015"],
["Sex", "Rank", "Age Category"],
["Sex", "Rank", "TotalRaces"],
["Sex", "TotalRaces", "LastRace"],
["Sex", "TotalRaces", "2015"],
["Sex", "TotalRaces", "Age Category"],
["Sex", "TotalRaces", "Rank"],
["Sex", "LastRace", "TotalRaces"],
["Sex", "LastRace", "2015"],
["Sex", "LastRace", "Age Category"],
["Sex", "LastRace", "Rank"],
["Age Category", "2015", "TotalRaces"],
["Age Category", "2015", "LastRace"],
["Age Category", "2015", "Sex"],
["Age Category", "2015", "Rank"],
["Age Category", "Sex", "TotalRaces"],
["Age Category", "Sex", "LastRace"],
["Age Category", "Sex", "2015"],
["Age Category", "Sex", "Rank"],
["Age Category", "Rank", "TotalRaces"],
["Age Category", "Rank", "LastRace"],
["Age Category", "Rank", "2015"],
["Age Category", "Rank", "Sex"],
["Age Category", "TotalRaces", "Rank"],
["Age Category", "TotalRaces", "LastRace"],
["Age Category", "TotalRaces", "2015"],
["Age Category", "TotalRaces", "Sex"],
["Age Category", "LastRace", "Rank"],
["Age Category", "LastRace", "TotalRaces"],
["Age Category", "LastRace", "2015"],
["Age Category", "LastRace", "Sex"],
["Rank", "2015", "Age Category"],
["Rank", "2015", "TotalRaces"],
["Rank", "2015", "LastRace"],
["Rank", "2015", "Sex"],
["Rank", "Sex", "Age Category"],
["Rank", "Sex", "TotalRaces"],
["Rank", "Sex", "LastRace"],
["Rank", "Sex", "2015"],
["Rank", "Age Category", "Sex"],
["Rank", "Age Category", "TotalRaces"],
["Rank", "Age Category", "LastRace"],
["Rank", "Age Category", "2015"],
["Rank", "TotalRaces", "Sex"],
["Rank", "TotalRaces", "Age Category"],
["Rank", "TotalRaces", "LastRace"],
["Rank", "TotalRaces", "2015"],
["Rank", "LastRace", "Sex"],
["Rank", "LastRace", "Age Category"],
["Rank", "LastRace", "TotalRaces"],
["Rank", "LastRace", "2015"],
["TotalRaces", "2015", "Sex"],
["TotalRaces", "2015", "Age Category"],
["TotalRaces", "2015", "Rank"],
["TotalRaces", "2015", "LastRace"],
["TotalRaces", "Sex", "2015"],
["TotalRaces", "Sex", "Age Category"],
["TotalRaces", "Sex", "Rank"],
["TotalRaces", "Sex", "LastRace"],
["TotalRaces", "Age Category", "2015"],
["TotalRaces", "Age Category", "Sex"],
["TotalRaces", "Age Category", "Rank"],
["TotalRaces", "Age Category", "LastRace"],
["TotalRaces", "Rank", "2015"],
["TotalRaces", "Rank", "Sex"],
["TotalRaces", "Rank", "Age Category"],
["TotalRaces", "Rank", "LastRace"],
["TotalRaces", "LastRace", "2015"],
["TotalRaces", "LastRace", "Sex"],
["TotalRaces", "LastRace", "Age Category"],
["TotalRaces", "LastRace", "Rank"],
["LastRace", "2015", "TotalRaces"],
["LastRace", "2015", "Sex"],
["LastRace", "2015", "Age Category"],
["LastRace", "2015", "Rank"],
["LastRace", "Sex", "TotalRaces"],
["LastRace", "Sex", "2015"],
["LastRace", "Sex", "Age Category"],
["LastRace", "Sex", "Rank"],
["LastRace", "Age Category", "TotalRaces"],
["LastRace", "Age Category", "2015"],
["LastRace", "Age Category", "Sex"],
["LastRace", "Age Category", "Rank"],
["LastRace", "Rank", "TotalRaces"],
["LastRace", "Rank", "2015"],
["LastRace", "Rank", "Sex"],
["LastRace", "Rank", "Age Category"],
["LastRace", "TotalRaces", "Rank"],
["LastRace", "TotalRaces", "2015"],
["LastRace", "TotalRaces", "Sex"],
["LastRace", "TotalRaces", "Age Category"]]

columnChoices4 = [["2015", "Sex", "Age Category", "Rank"],
["2015", "Sex", "Age Category", "TotalRaces"],
["2015", "Sex", "Age Category", "LastRace"],
["2015", "Sex", "Rank", "Age Category"],
["2015", "Sex", "Rank", "TotalRaces"],
["2015", "Sex", "Rank", "LastRace"],
["2015", "Sex", "TotalRaces", "Age Category"],
["2015", "Sex", "TotalRaces", "Rank"],
["2015", "Sex", "TotalRaces", "LastRace"],
["2015", "Sex", "LastRace", "Age Category"],
["2015", "Sex", "LastRace", "Rank"],
["2015", "Sex", "LastRace", "TotalRaces"],
["2015", "Age Category", "Sex", "LastRace"],
["2015", "Age Category", "Sex", "Rank"],
["2015", "Age Category", "Sex", "TotalRaces"],
["2015", "Age Category", "Rank", "LastRace"],
["2015", "Age Category", "Rank", "Sex"],
["2015", "Age Category", "Rank", "TotalRaces"],
["2015", "Age Category", "TotalRaces", "LastRace"],
["2015", "Age Category", "TotalRaces", "Sex"],
["2015", "Age Category", "TotalRaces", "Rank"],
["2015", "Age Category", "LastRace", "TotalRaces"],
["2015", "Age Category", "LastRace", "Sex"],
["2015", "Age Category", "LastRace", "Rank"],
["2015", "Rank", "Sex", "TotalRaces"],
["2015", "Rank", "Sex", "LastRace"],
["2015", "Rank", "Sex", "Age Category"],
["2015", "Rank", "Age Category", "TotalRaces"],
["2015", "Rank", "Age Category", "LastRace"],
["2015", "Rank", "Age Category", "Sex"],
["2015", "Rank", "TotalRaces", "Age Category"],
["2015", "Rank", "TotalRaces", "LastRace"],
["2015", "Rank", "TotalRaces", "Sex"],
["2015", "Rank", "LastRace", "Age Category"],
["2015", "Rank", "LastRace", "TotalRaces"],
["2015", "Rank", "LastRace", "Sex"],
["2015", "TotalRaces", "Sex", "Age Category"],
["2015", "TotalRaces", "Sex", "Rank"],
["2015", "TotalRaces", "Sex", "LastRace"],
["2015", "TotalRaces", "Age Category", "Sex"],
["2015", "TotalRaces", "Age Category", "Rank"],
["2015", "TotalRaces", "Age Category", "LastRace"],
["2015", "TotalRaces", "Rank", "Sex"],
["2015", "TotalRaces", "Rank", "Age Category"],
["2015", "TotalRaces", "Rank", "LastRace"],
["2015", "TotalRaces", "LastRace", "Sex"],
["2015", "TotalRaces", "LastRace", "Age Category"],
["2015", "TotalRaces", "LastRace", "Rank"],
["2015", "LastRace", "Sex", "TotalRaces"],
["2015", "LastRace", "Sex", "Age Category"],
["2015", "LastRace", "Sex", "Rank"],
["2015", "LastRace", "Age Category", "TotalRaces"],
["2015", "LastRace", "Age Category", "Sex"],
["2015", "LastRace", "Age Category", "Rank"],
["2015", "LastRace", "Rank", "TotalRaces"],
["2015", "LastRace", "Rank", "Sex"],
["2015", "LastRace", "Rank", "Age Category"],
["2015", "LastRace", "TotalRaces", "Rank"],
["2015", "LastRace", "TotalRaces", "Sex"],
["2015", "LastRace", "TotalRaces", "Age Category"],
["Sex", "2015", "LastRace", "Rank"],
["Sex", "2015", "LastRace", "TotalRaces"],
["Sex", "2015", "LastRace", "Age Category"],
["Sex", "2015", "Age Category", "Rank"],
["Sex", "2015", "Age Category", "TotalRaces"],
["Sex", "2015", "Age Category", "LastRace"],
["Sex", "2015", "Rank", "Age Category"],
["Sex", "2015", "Rank", "TotalRaces"],
["Sex", "2015", "Rank", "LastRace"],
["Sex", "2015", "TotalRaces", "Age Category"],
["Sex", "2015", "TotalRaces", "Rank"],
["Sex", "2015", "TotalRaces", "LastRace"],
["Sex", "Age Category", "LastRace", "2015"],
["Sex", "Age Category", "LastRace", "Rank"],
["Sex", "Age Category", "LastRace", "TotalRaces"],
["Sex", "Age Category", "2015", "LastRace"],
["Sex", "Age Category", "2015", "Rank"],
["Sex", "Age Category", "2015", "TotalRaces"],
["Sex", "Age Category", "Rank", "LastRace"],
["Sex", "Age Category", "Rank", "2015"],
["Sex", "Age Category", "Rank", "TotalRaces"],
["Sex", "Age Category", "TotalRaces", "LastRace"],
["Sex", "Age Category", "TotalRaces", "2015"],
["Sex", "Age Category", "TotalRaces", "Rank"],
["Sex", "Rank", "LastRace", "TotalRaces"],
["Sex", "Rank", "LastRace", "2015"],
["Sex", "Rank", "LastRace", "Age Category"],
["Sex", "Rank", "2015", "TotalRaces"],
["Sex", "Rank", "2015", "LastRace"],
["Sex", "Rank", "2015", "Age Category"],
["Sex", "Rank", "Age Category", "TotalRaces"],
["Sex", "Rank", "Age Category", "LastRace"],
["Sex", "Rank", "Age Category", "2015"],
["Sex", "Rank", "TotalRaces", "Age Category"],
["Sex", "Rank", "TotalRaces", "LastRace"],
["Sex", "Rank", "TotalRaces", "2015"],
["Sex", "TotalRaces", "LastRace", "Age Category"],
["Sex", "TotalRaces", "LastRace", "Rank"],
["Sex", "TotalRaces", "LastRace", "2015"],
["Sex", "TotalRaces", "2015", "Age Category"],
["Sex", "TotalRaces", "2015", "Rank"],
["Sex", "TotalRaces", "2015", "LastRace"],
["Sex", "TotalRaces", "Age Category", "2015"],
["Sex", "TotalRaces", "Age Category", "Rank"],
["Sex", "TotalRaces", "Age Category", "LastRace"],
["Sex", "TotalRaces", "Rank", "2015"],
["Sex", "TotalRaces", "Rank", "Age Category"],
["Sex", "TotalRaces", "Rank", "LastRace"],
["Sex", "LastRace", "TotalRaces", "2015"],
["Sex", "LastRace", "TotalRaces", "Age Category"],
["Sex", "LastRace", "TotalRaces", "Rank"],
["Sex", "LastRace", "2015", "TotalRaces"],
["Sex", "LastRace", "2015", "Age Category"],
["Sex", "LastRace", "2015", "Rank"],
["Sex", "LastRace", "Age Category", "TotalRaces"],
["Sex", "LastRace", "Age Category", "2015"],
["Sex", "LastRace", "Age Category", "Rank"],
["Sex", "LastRace", "Rank", "TotalRaces"],
["Sex", "LastRace", "Rank", "2015"],
["Sex", "LastRace", "Rank", "Age Category"],
["Age Category", "2015", "TotalRaces", "Rank"],
["Age Category", "2015", "TotalRaces", "LastRace"],
["Age Category", "2015", "TotalRaces", "Sex"],
["Age Category", "2015", "LastRace", "Rank"],
["Age Category", "2015", "LastRace", "TotalRaces"],
["Age Category", "2015", "LastRace", "Sex"],
["Age Category", "2015", "Sex", "Rank"],
["Age Category", "2015", "Sex", "TotalRaces"],
["Age Category", "2015", "Sex", "LastRace"],
["Age Category", "2015", "Rank", "Sex"],
["Age Category", "2015", "Rank", "TotalRaces"],
["Age Category", "2015", "Rank", "LastRace"],
["Age Category", "Sex", "TotalRaces", "2015"],
["Age Category", "Sex", "TotalRaces", "Rank"],
["Age Category", "Sex", "TotalRaces", "LastRace"],
["Age Category", "Sex", "LastRace", "2015"],
["Age Category", "Sex", "LastRace", "Rank"],
["Age Category", "Sex", "LastRace", "TotalRaces"],
["Age Category", "Sex", "2015", "LastRace"],
["Age Category", "Sex", "2015", "Rank"],
["Age Category", "Sex", "2015", "TotalRaces"],
["Age Category", "Sex", "Rank", "LastRace"],
["Age Category", "Sex", "Rank", "2015"],
["Age Category", "Sex", "Rank", "TotalRaces"],
["Age Category", "Rank", "TotalRaces", "LastRace"],
["Age Category", "Rank", "TotalRaces", "2015"],
["Age Category", "Rank", "TotalRaces", "Sex"],
["Age Category", "Rank", "LastRace", "TotalRaces"],
["Age Category", "Rank", "LastRace", "2015"],
["Age Category", "Rank", "LastRace", "Sex"],
["Age Category", "Rank", "2015", "TotalRaces"],
["Age Category", "Rank", "2015", "LastRace"],
["Age Category", "Rank", "2015", "Sex"],
["Age Category", "Rank", "Sex", "TotalRaces"],
["Age Category", "Rank", "Sex", "LastRace"],
["Age Category", "Rank", "Sex", "2015"],
["Age Category", "TotalRaces", "Rank", "Sex"],
["Age Category", "TotalRaces", "Rank", "LastRace"],
["Age Category", "TotalRaces", "Rank", "2015"],
["Age Category", "TotalRaces", "LastRace", "Sex"],
["Age Category", "TotalRaces", "LastRace", "Rank"],
["Age Category", "TotalRaces", "LastRace", "2015"],
["Age Category", "TotalRaces", "2015", "Sex"],
["Age Category", "TotalRaces", "2015", "Rank"],
["Age Category", "TotalRaces", "2015", "LastRace"],
["Age Category", "TotalRaces", "Sex", "2015"],
["Age Category", "TotalRaces", "Sex", "Rank"],
["Age Category", "TotalRaces", "Sex", "LastRace"],
["Age Category", "LastRace", "Rank", "2015"],
["Age Category", "LastRace", "Rank", "Sex"],
["Age Category", "LastRace", "Rank", "TotalRaces"],
["Age Category", "LastRace", "TotalRaces", "2015"],
["Age Category", "LastRace", "TotalRaces", "Sex"],
["Age Category", "LastRace", "TotalRaces", "Rank"],
["Age Category", "LastRace", "2015", "TotalRaces"],
["Age Category", "LastRace", "2015", "Sex"],
["Age Category", "LastRace", "2015", "Rank"],
["Age Category", "LastRace", "Sex", "TotalRaces"],
["Age Category", "LastRace", "Sex", "2015"],
["Age Category", "LastRace", "Sex", "Rank"],
["Rank", "2015", "Age Category", "TotalRaces"],
["Rank", "2015", "Age Category", "LastRace"],
["Rank", "2015", "Age Category", "Sex"],
["Rank", "2015", "TotalRaces", "Age Category"],
["Rank", "2015", "TotalRaces", "LastRace"],
["Rank", "2015", "TotalRaces", "Sex"],
["Rank", "2015", "LastRace", "Age Category"],
["Rank", "2015", "LastRace", "TotalRaces"],
["Rank", "2015", "LastRace", "Sex"],
["Rank", "2015", "Sex", "Age Category"],
["Rank", "2015", "Sex", "TotalRaces"],
["Rank", "2015", "Sex", "LastRace"],
["Rank", "Sex", "Age Category", "2015"],
["Rank", "Sex", "Age Category", "TotalRaces"],
["Rank", "Sex", "Age Category", "LastRace"],
["Rank", "Sex", "TotalRaces", "2015"],
["Rank", "Sex", "TotalRaces", "Age Category"],
["Rank", "Sex", "TotalRaces", "LastRace"],
["Rank", "Sex", "LastRace", "2015"],
["Rank", "Sex", "LastRace", "Age Category"],
["Rank", "Sex", "LastRace", "TotalRaces"],
["Rank", "Sex", "2015", "LastRace"],
["Rank", "Sex", "2015", "Age Category"],
["Rank", "Sex", "2015", "TotalRaces"],
["Rank", "Age Category", "Sex", "LastRace"],
["Rank", "Age Category", "Sex", "2015"],
["Rank", "Age Category", "Sex", "TotalRaces"],
["Rank", "Age Category", "TotalRaces", "LastRace"],
["Rank", "Age Category", "TotalRaces", "2015"],
["Rank", "Age Category", "TotalRaces", "Sex"],
["Rank", "Age Category", "LastRace", "TotalRaces"],
["Rank", "Age Category", "LastRace", "2015"],
["Rank", "Age Category", "LastRace", "Sex"],
["Rank", "Age Category", "2015", "TotalRaces"],
["Rank", "Age Category", "2015", "LastRace"],
["Rank", "Age Category", "2015", "Sex"],
["Rank", "TotalRaces", "Sex", "Age Category"],
["Rank", "TotalRaces", "Sex", "LastRace"],
["Rank", "TotalRaces", "Sex", "2015"],
["Rank", "TotalRaces", "Age Category", "Sex"],
["Rank", "TotalRaces", "Age Category", "LastRace"],
["Rank", "TotalRaces", "Age Category", "2015"],
["Rank", "TotalRaces", "LastRace", "Sex"],
["Rank", "TotalRaces", "LastRace", "Age Category"],
["Rank", "TotalRaces", "LastRace", "2015"],
["Rank", "TotalRaces", "2015", "Sex"],
["Rank", "TotalRaces", "2015", "Age Category"],
["Rank", "TotalRaces", "2015", "LastRace"],
["Rank", "LastRace", "Sex", "2015"],
["Rank", "LastRace", "Sex", "Age Category"],
["Rank", "LastRace", "Sex", "TotalRaces"],
["Rank", "LastRace", "Age Category", "2015"],
["Rank", "LastRace", "Age Category", "Sex"],
["Rank", "LastRace", "Age Category", "TotalRaces"],
["Rank", "LastRace", "TotalRaces", "2015"],
["Rank", "LastRace", "TotalRaces", "Sex"],
["Rank", "LastRace", "TotalRaces", "Age Category"],
["Rank", "LastRace", "2015", "TotalRaces"],
["Rank", "LastRace", "2015", "Sex"],
["Rank", "LastRace", "2015", "Age Category"],
["TotalRaces", "2015", "Sex", "Rank"],
["TotalRaces", "2015", "Sex", "LastRace"],
["TotalRaces", "2015", "Sex", "Age Category"],
["TotalRaces", "2015", "Age Category", "Rank"],
["TotalRaces", "2015", "Age Category", "LastRace"],
["TotalRaces", "2015", "Age Category", "Sex"],
["TotalRaces", "2015", "Rank", "Age Category"],
["TotalRaces", "2015", "Rank", "LastRace"],
["TotalRaces", "2015", "Rank", "Sex"],
["TotalRaces", "2015", "LastRace", "Age Category"],
["TotalRaces", "2015", "LastRace", "Rank"],
["TotalRaces", "2015", "LastRace", "Sex"],
["TotalRaces", "Sex", "2015", "Age Category"],
["TotalRaces", "Sex", "2015", "Rank"],
["TotalRaces", "Sex", "2015", "LastRace"],
["TotalRaces", "Sex", "Age Category", "2015"],
["TotalRaces", "Sex", "Age Category", "Rank"],
["TotalRaces", "Sex", "Age Category", "LastRace"],
["TotalRaces", "Sex", "Rank", "2015"],
["TotalRaces", "Sex", "Rank", "Age Category"],
["TotalRaces", "Sex", "Rank", "LastRace"],
["TotalRaces", "Sex", "LastRace", "2015"],
["TotalRaces", "Sex", "LastRace", "Age Category"],
["TotalRaces", "Sex", "LastRace", "Rank"],
["TotalRaces", "Age Category", "2015", "LastRace"],
["TotalRaces", "Age Category", "2015", "Sex"],
["TotalRaces", "Age Category", "2015", "Rank"],
["TotalRaces", "Age Category", "Sex", "LastRace"],
["TotalRaces", "Age Category", "Sex", "2015"],
["TotalRaces", "Age Category", "Sex", "Rank"],
["TotalRaces", "Age Category", "Rank", "LastRace"],
["TotalRaces", "Age Category", "Rank", "2015"],
["TotalRaces", "Age Category", "Rank", "Sex"],
["TotalRaces", "Age Category", "LastRace", "Rank"],
["TotalRaces", "Age Category", "LastRace", "2015"],
["TotalRaces", "Age Category", "LastRace", "Sex"],
["TotalRaces", "Rank", "2015", "Age Category"],
["TotalRaces", "Rank", "2015", "LastRace"],
["TotalRaces", "Rank", "2015", "Sex"],
["TotalRaces", "Rank", "Sex", "Age Category"],
["TotalRaces", "Rank", "Sex", "LastRace"],
["TotalRaces", "Rank", "Sex", "2015"],
["TotalRaces", "Rank", "Age Category", "Sex"],
["TotalRaces", "Rank", "Age Category", "LastRace"],
["TotalRaces", "Rank", "Age Category", "2015"],
["TotalRaces", "Rank", "LastRace", "Sex"],
["TotalRaces", "Rank", "LastRace", "Age Category"],
["TotalRaces", "Rank", "LastRace", "2015"],
["TotalRaces", "LastRace", "2015", "Sex"],
["TotalRaces", "LastRace", "2015", "Age Category"],
["TotalRaces", "LastRace", "2015", "Rank"],
["TotalRaces", "LastRace", "Sex", "2015"],
["TotalRaces", "LastRace", "Sex", "Age Category"],
["TotalRaces", "LastRace", "Sex", "Rank"],
["TotalRaces", "LastRace", "Age Category", "2015"],
["TotalRaces", "LastRace", "Age Category", "Sex"],
["TotalRaces", "LastRace", "Age Category", "Rank"],
["TotalRaces", "LastRace", "Rank", "2015"],
["TotalRaces", "LastRace", "Rank", "Sex"],
["TotalRaces", "LastRace", "Rank", "Age Category"],
["LastRace", "2015", "TotalRaces", "Rank"],
["LastRace", "2015", "TotalRaces", "Sex"],
["LastRace", "2015", "TotalRaces", "Age Category"],
["LastRace", "2015", "Sex", "Rank"],
["LastRace", "2015", "Sex", "TotalRaces"],
["LastRace", "2015", "Sex", "Age Category"],
["LastRace", "2015", "Age Category", "Rank"],
["LastRace", "2015", "Age Category", "TotalRaces"],
["LastRace", "2015", "Age Category", "Sex"],
["LastRace", "2015", "Rank", "Age Category"],
["LastRace", "2015", "Rank", "TotalRaces"],
["LastRace", "2015", "Rank", "Sex"],
["LastRace", "Sex", "TotalRaces", "Age Category"],
["LastRace", "Sex", "TotalRaces", "Rank"],
["LastRace", "Sex", "TotalRaces", "2015"],
["LastRace", "Sex", "2015", "Age Category"],
["LastRace", "Sex", "2015", "Rank"],
["LastRace", "Sex", "2015", "TotalRaces"],
["LastRace", "Sex", "Age Category", "2015"],
["LastRace", "Sex", "Age Category", "Rank"],
["LastRace", "Sex", "Age Category", "TotalRaces"],
["LastRace", "Sex", "Rank", "2015"],
["LastRace", "Sex", "Rank", "Age Category"],
["LastRace", "Sex", "Rank", "TotalRaces"],
["LastRace", "Age Category", "TotalRaces", "2015"],
["LastRace", "Age Category", "TotalRaces", "Sex"],
["LastRace", "Age Category", "TotalRaces", "Rank"],
["LastRace", "Age Category", "2015", "TotalRaces"],
["LastRace", "Age Category", "2015", "Sex"],
["LastRace", "Age Category", "2015", "Rank"],
["LastRace", "Age Category", "Sex", "TotalRaces"],
["LastRace", "Age Category", "Sex", "2015"],
["LastRace", "Age Category", "Sex", "Rank"],
["LastRace", "Age Category", "Rank", "TotalRaces"],
["LastRace", "Age Category", "Rank", "2015"],
["LastRace", "Age Category", "Rank", "Sex"],
["LastRace", "Rank", "TotalRaces", "Age Category"],
["LastRace", "Rank", "TotalRaces", "2015"],
["LastRace", "Rank", "TotalRaces", "Sex"],
["LastRace", "Rank", "2015", "Age Category"],
["LastRace", "Rank", "2015", "TotalRaces"],
["LastRace", "Rank", "2015", "Sex"],
["LastRace", "Rank", "Sex", "Age Category"],
["LastRace", "Rank", "Sex", "TotalRaces"],
["LastRace", "Rank", "Sex", "2015"],
["LastRace", "Rank", "Age Category", "Sex"],
["LastRace", "Rank", "Age Category", "TotalRaces"],
["LastRace", "Rank", "Age Category", "2015"],
["LastRace", "TotalRaces", "Rank", "Sex"],
["LastRace", "TotalRaces", "Rank", "Age Category"],
["LastRace", "TotalRaces", "Rank", "2015"],
["LastRace", "TotalRaces", "2015", "Sex"],
["LastRace", "TotalRaces", "2015", "Age Category"],
["LastRace", "TotalRaces", "2015", "Rank"],
["LastRace", "TotalRaces", "Sex", "2015"],
["LastRace", "TotalRaces", "Sex", "Age Category"],
["LastRace", "TotalRaces", "Sex", "Rank"],
["LastRace", "TotalRaces", "Age Category", "2015"],
["LastRace", "TotalRaces", "Age Category", "Sex"],
["LastRace", "TotalRaces", "Age Category", "Rank"]]

allColumns = [["Sex", "Age Category", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "Time", "Rank", "TotalRaces", "LastRace"]]

def gauss(x, mean, std):
    # Sometimes our stdev is zero in the case of last race where all have participated in 2015
    if std == 0:
        std = 1
    
    return (1 / (math.sqrt(2 * math.pi) * std)) * math.exp(-((x-mean**2)/(2*std**2)))

def predictDistribution(trueAvgStd, falseAvgStd, input):
    """
    Decision method: Will the input be participating or not?
    """    
    willParticipate = 1
    wontParticipate = 1

    for i in range(len(trueAvgStd)):
        mean,std = trueAvgStd[i]
        x = input[i]
        res = gauss(x, mean, std)
        
        willParticipate *= res

    for i in range(len(falseAvgStd)):
        mean,std = falseAvgStd[i]
        x = input[i]
        wontParticipate *= gauss(x, mean, std)

    if willParticipate > wontParticipate:
        return 1
    else:
        return 0

def runAll(trueAvgStd, falseAvgStd, instances):
    results = []
    for instance in instances:
        predict = predictDistribution(trueAvgStd, falseAvgStd, instance)
        results.append(predict)
    return results

def calculateAccuracy(prediction, test):
    trueInstances = 0
    testSize = len(test)
    for i in range(testSize):
        if prediction[i] == test[i][-1]:
            true += 1
    
    # Return an accuracy in percent
    return (trueInstances/float(testSize)) * 100.0

print "Loading training data"
train_x = pd.read_csv("output/train_x.csv")
train_y = pd.read_csv("output/train_y.csv")

print "Loading validation data"
test_x = pd.read_csv("output/test_x.csv")
test_y = pd.read_csv("output/test_y.csv")

training = train_x["LastRace"] == 4
train_x = train_x[training]
train_y = train_y[training]

didParticipate = (train_x.xs("2015", axis=1, drop_level=False) == 1).as_matrix()

for columns in allColumns:
    print "Finding those who participanted in 2016 and those who did not"
    participants2016 = train_x[columns][didParticipate].as_matrix()
    nonParticipants2016 = train_x[columns][~didParticipate].as_matrix()

    print "Zipped Averages and Standard Deviations as [(Average, StdDev), ...]"
    participatedAvg = participants2016.mean(axis=0)
    participatedStd = participants2016.std(axis=0, ddof=1)

    nonParticipatedAvg = nonParticipants2016.mean(axis=0)
    nonParticipatedStd = nonParticipants2016.std(axis=0, ddof=1)

    participatedVector = zip(participatedAvg, participatedStd)
    nonParticipatedVector = zip(nonParticipatedAvg, nonParticipatedStd)

    testX = test_x[columns].as_matrix()
    testY = test_y.as_matrix()

    print participatedVector
    results = runAll(participatedVector, nonParticipatedVector, testX)
    print results
    
    acc = calculateAccuracy(results, testY)
    print columns, acc
