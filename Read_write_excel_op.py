
import pandas as pd
print(pd.__version__)

## Read Excel File
df = pd.read_excel(r"C:\Users\santosh.b\OneDrive - Brillio\Desktop\Python_Learning\sales_data.xlsx")
print(df)

##read specific sheet
df_orders = pd.read_excel(r"C:\Users\santosh.b\OneDrive - Brillio\Desktop\Python_Learning\sales_data.xlsx", sheet_name="Orders")
print(df_orders)

df_customers=pd.read_excel(r"C:\Users\santosh.b\OneDrive - Brillio\Desktop\Python_Learning\sales_data.xlsx",sheet_name="Customers")
print(df_customers)

# If multiple sheets:
all_sheets=pd.read_excel(r"C:\Users\santosh.b\OneDrive - Brillio\Desktop\Python_Learning\sales_data.xlsx",sheet_name=None)
print(all_sheets)

##Data Transformation
#Select / Slice Columns
df_orders[['Product','Amount']]

#Filter Data
df_orders[df_orders['Amount'] > 30000]

#Convert Data Types
df_orders['Amount'] = df_orders['Amount'].astype(int)

#Date Formatting 
df_orders['OrderDate'] = pd.to_datetime(df_orders['OrderDate'], errors='coerce')

#Convert format:
df_orders['OrderDate'] = df_orders['OrderDate'].dt.strftime("%Y-%m-%d")

#Add New Column
df_orders['GST'] = df_orders['Amount'] * 0.18
#print (df_orders)

#Remove Columns
df_orders = df_orders.drop(columns=['Product'])
print(df_orders)

#Add Column again
#df_orders['Product'] = df_orders['Product']
#print (df_orders)

#Rename Column
df_orders.rename(columns={'Amount': 'Price'}, inplace=True)
#print(df_orders)

#Handle Null Values
df_orders.fillna(0, inplace=True)
#print(df_orders)

#Sorting
#df_orders.sort_values(by='Amount', ascending=False)
print(df_orders.columns)

#print(df_orders)

#GroupBy
#df_orders.groupby('Product')['Amount'].sum()

#Save Transformed File
df_orders.to_excel("output.xlsx", index=False)
df_orders.to_csv("output.csv", index=False)

#Read CSV & JSON
# Read Csv
#df_csv = pd.read_csv("data.csv")

#Read JSON
#df_json = pd.read_json("data.json")

#Load Data to SQL Server


