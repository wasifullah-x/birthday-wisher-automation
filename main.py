from datetime import date
import pandas as pd
from sendmail import send_email

df = pd.read_excel("Book1.xlsx")

today_str = date.today().strftime("%Y-%m-%d")

filtered_df = df[(df["birthday_date"].astype(str) == today_str) & (df["has_wished"] == "no")]

for index, row in filtered_df.iterrows():
    send_email(
        subject="Happy Birthday Wish",
        reciever_email=row["email"],
        name=row["name"],
        age=row["age"],
        birthday_date=row["birthday_date"],
    )
