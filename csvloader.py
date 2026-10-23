import pandas as pd;
from pandas import isna
#Loading Excel File into Python
df = (pd.read_excel(r"C:\Users\ARYAN DEEP SINGH\Downloads\archive\Telco_customer_churn.xlsx"));
#Converting the Data Type of Total Charges from Text to Numeric
df["Total Charges"] = pd.to_numeric(df["Total Charges"], errors='coerce');
# Checking data type of Total Charges
# print(df["Total Charges"].dtypes);

#Printing the total number of missing values
print(df["Total Charges"].isna().sum())

#Filling these rows as O, means brand new customers with zero tenure
df["Total Charges"] = df["Total Charges"].fillna(0)


#Checking if duplicates exists
print(df.duplicated("Total Charges").sum())

#Dropping useless columns
df = df.drop(columns=["Count" , "Country", "Lat Long"])

#Grouping the Tenure into Groups

df["Tenure Group"] = pd.cut(df["Tenure Months"],
                            bins= [-1,12,24,48,72] ,
                            labels=["0-12 Months","13-24 Months","25-48 Months","49-72 Months"])

df.to_csv("Clean Churn.csv", index=False)

#  print(df["Churn Label"].value_counts(normalize=True)*100)

# print(df.duplicated().sum())
# print(df["CustomerID"].duplicated().sum())

print(df.groupby("Contract")["Churn Value"].mean()*100)
print(df["Contract"].value_counts())
print(df.groupby("Tenure Group")["Churn Value"].mean()*100)
print(df.groupby("Payment Method")["Churn Value"].mean()*100)
print(df["Churn Reason"].value_counts())


df.columns = df.columns.str.replace(" ", "_").str.lower()
print(df.columns)

df.to_csv("clean_churn.csv", index=False)