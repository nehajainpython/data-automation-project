import pandas as pd

df = pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\Python\data.csv")

# remove duplicates
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

# feature engineering
df["Email"] = df["Name"].apply(lambda x: x.lower() + "@gmail.com")
df["Website"] = df["Website"].apply(lambda x: "https://" + x)
df["Type"] = df["Location"].apply(lambda x: "Domestic" if x == "India" else "Foreign")


df.to_excel("final_output.xlsx", index=False)
df.to_csv("final_output.csv", index=False)
print(df.head())
print("Project completed successfully!")