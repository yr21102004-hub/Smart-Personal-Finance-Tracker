import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def file_load(path_file):# open the Dataset
    try:
     df = pd.read_csv(path_file)
     return df
    except FileNotFoundError:
       print("File not found! Check path.")
       return None
def clean_data(df):# Data Cleaning
   if df is None:
      return None
   if (df.isnull().sum().sum())>0 or (df.duplicated().sum())>0:
      df.dropna(subset=["amount"])
      df.drop_duplicates(inplace=True)
   if df["date"].dtype == "object":
      df["date"] = pd.to_datetime(df["date"], errors="coerce")
   return df
"""Analysis"""
def Total_Spending(df):
   if df is None:
    return None
   else:
    ts = df["amount"].sum()
    return ts
def Average_Spending(df):
   if df is None:
      return None
   else:
     s = np.mean(df["amount"])
   return s
def Daily_Expense_Calculation(df):
   if df is None:
      return None
   else:
      DES = df.groupby("date")["amount"].sum()
   return DES
def Daily_Average(df):
   if df is None:
      return None
   else:
    DA = df.groupby("date")["amount"].sum()
   return DA.mean()
def Category_Analysis(df):
  Food = df[df["category"] == "Food"]["amount"].sum()
  b = f"Total cost of Food = {Food}\n"
  Shopping = df[df["category"] == "Shopping"]["amount"].sum()
  c = f"Total cost of Shopping = {Shopping}\n"
  Transport = df[df["category"] == "Transport"]["amount"].sum()
  d = f"Total cost of Transport = {Transport}\n"
  Bills = df[df["category"] == "Bills"]["amount"].sum()
  e = f"Total cost of Bills = {Bills}\n"
  Entertainment = df[df["category"] == "Entertainment"]["amount"].sum()
  f = f"Total cost of Entertainment = {Entertainment}\n"
  return b + c + d + e + f
def strongest_and_weakest_day(df):
   a = df.groupby("date")["amount"].sum().idxmax()
   b = f"The most costly day is{a}\n"
   c = df.groupby("date")["amount"].sum().idxmin()
   d = f"The Least costly day is{c}\n"
   return b,d
def Forecasting(df):
   a = df.groupby("date")["amount"].sum()
   return f"If the same exchange rate continues, the expected ≈ {(np.mean(a))*30}"
def Budget(df):
   a = df.groupby("date")["amount"].sum()
   expected = a.mean() * 30   
   budget = 7000             
   if expected > budget:
      return f"Over Budget by {expected - budget}"
   else:
      return f"Under Budget by {budget - expected}"
def Trend_Analysis(df):
   if df is None:
      return None
   else:
      if df["date"].dtype == type(str):
         df["date"] = pd.to_datetime(df["date"])
      df = df.dropna(subset=["amount"])# Removing empty values
      a = df.groupby("date")["amount"].sum()
      b = a.sort_index()
      if b.iloc[-1] > b.iloc[0]:
         trend = "upward trend ⬆️"
      elif b.iloc[-1] < b.iloc[0]:
         trend = "downward trend ⬇️"
      else:
         trend = "Fixed ➖"
      ups = 0
      downs = 0
      for i in range(len(b) - 1):
         if b.iloc[i+1] > b.iloc[i]:
            ups += 1
         elif b.iloc[i+1] < b.iloc[i]:
            downs += 1
      if ups > 0 and downs > 0:
         return "Fluctuating 🔄 with " + trend
      else:
         return "Not Fluctuating ➖ with " + trend
"""Visualization"""
def kde_plot(df):
    plt.figure()
    sns.kdeplot(data=df, x="amount", fill=True)
    plt.title("Distribution of Expenses (KDE Plot)")
    plt.xlabel("Amount")
    plt.ylabel("Density")
    plt.savefig("KDE Plot.png")
    plt.show()
def bar_plot(df):
   x = df.groupby("category")["amount"].sum()
   x.plot.bar()
   plt.xlabel("Category")
   plt.ylabel("Amount")
   plt.title("The relationship between categories and expenses")
   plt.savefig("Bar Chart.png")
   plt.show()
def line_plot(df):
    x = df.groupby("date")["amount"].sum().sort_index()
    x.plot.line()
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Expenses over time")
    plt.savefig("Line Plot.png")
    plt.show()
def pie_chart(df):
    x = df.groupby("category")["amount"].sum()
    plt.figure()
    plt.pie(x, labels=x.index, autopct="%1.1f%%")
    plt.title("Expenses Distribution by Category")
    plt.savefig("Pie Chart.png")
    plt.show()
def heatmap(df):
    plt.figure()
    corr = df[["amount"]].corr()  # أو أي أعمدة رقمية عندك
    sns.heatmap(corr, annot=True)
    plt.title("Correlation Heatmap")
    plt.savefig("Heatmap.png")
    plt.show()
def rug_plot(df):
    plt.figure()
    sns.rugplot(data=df, x="amount")
    plt.title("Rug Plot for Amount")
    plt.savefig("Rug Plot.png")
    plt.show()
def violin_plot(df):
    plt.figure()
    sns.violinplot(data=df, x="category", y="amount")
    plt.title("Violin Plot by Category")
    plt.savefig("Violin Plot.png")
    plt.show()
def swarm_plot(df):
    plt.figure()
    sns.swarmplot(data=df, x="category", y="amount")
    plt.title("Swarm Plot by Category")
    plt.xticks(rotation=45)
    plt.savefig("Swarm Plot.png")
    plt.show()
def pair_plot(df):
    sns.pairplot(df.select_dtypes(include=["number"]))
    plt.savefig("Pair Plot.png")
    plt.show()
def box_plot(df):
    plt.figure()
    sns.boxplot(data=df, x="category", y="amount")
    plt.title("Box Plot of Amount by Category")
    plt.xticks(rotation=45)
    plt.savefig("Box Plot.png")
    plt.show()
def main():
   file_path = r"E:\Computer Scienes\My Projects\My Teskes\Smart Personal Finance Tracker\Smart Personal Finance Tracker.csv.txt"
   df = file_load(file_path)
   if df is None:
      return
   if df.empty:
      print("The Dataset Is Empty")
   else:
      print(df)
      df = clean_data(df)
      print(f"Total Spending Is {Total_Spending(df)}")
      print(f" Average Spending Is {Daily_Average(df)}")
      print(f"Daily Expense Calculation Is {Daily_Expense_Calculation(df)}")
      print(Category_Analysis(df))
      print(strongest_and_weakest_day(df))
      print(Forecasting(df))
      print(Budget(df))
      print(Trend_Analysis(df))
      kde_plot(df)
      rug_plot(df)
      violin_plot(df)
      swarm_plot(df)
      pair_plot(df)
      bar_plot(df)
      line_plot(df)
      pie_chart(df)
      heatmap(df)
      box_plot(df)
if __name__ == "__main__":
   main()