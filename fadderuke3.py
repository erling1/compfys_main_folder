import pandas as pd

df = pd.read_csv("./fil.csv")


#df = pd.read_csv("./data/filmer.csv")
#display(df)

#df = df.drop_duplicates("Name[2]")
#print(df)





print(df.drop(columns = ["Name","Author"]))

print(df[df["Author"]!="Jen Sincero"])
#df["Name"]
