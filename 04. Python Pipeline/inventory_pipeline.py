"""
CompanyConnect Supply Chain Data Pipeline
Purpose: Automated data processing, flagging, and reporting
Tools: Python, pandas, openpyxl
"""

import pandas as pd
from datetime import date
import os


data = {
    "branch_name":  ["North Reef","North Reef","North Reef","North Reef",
                     "Cape Town", "Cape Town", "Cape Town", "Cape Town",
                     "Durban",    "Durban",    "Durban",    "Durban"],
    "brand":        ["PowerCore","VoltDrive","ApexCell","TradeMax"] * 3,
    "category":     ["Automotive","Automotive","Premium Automotive","Export/Industrial"] * 3,
    "quantity":     [120,85,40,30, 95,60,25,20, 110,75,35,15],
    "unit_cost_rand":[850,920,1250,1100] * 3,
    "last_updated": [date(2026,5,1)] * 12
}

df = pd.DataFrame(data)


df["stock_value_rand"] = df["quantity"] * df["unit_cost_rand"]


df["stock_status"] = df["quantity"].apply(
    lambda q: "⚠️ LOW STOCK" if q < 50 else "✔ OK"
)


branch_summary = (
    df.groupby("branch_name")
    .agg(
        total_units   = ("quantity",        "sum"),
        total_value   = ("stock_value_rand","sum"),
        low_stock_items = ("stock_status", lambda x: (x == "⚠️ LOW STOCK").sum())
    )
    .reset_index()
    .sort_values("total_value", ascending=False)
)


brand_summary = (
    df.groupby(["brand","category"])
    .agg(
        total_units = ("quantity",         "sum"),
        total_value = ("stock_value_rand", "sum")
    )
    .reset_index()
    .sort_values("total_value", ascending=False)
)


print("=" * 55)
print("   CompanyConnect SUPPLY CHAIN REPORT —", date.today())
print("=" * 55)

print("\n📦 FULL INVENTORY WITH FLAGS:")
print(df[["branch_name","brand","quantity","stock_value_rand","stock_status"]].to_string(index=False))

print("\n🏢 BRANCH SUMMARY:")
print(branch_summary.to_string(index=False))

print("\n🔋 BRAND PERFORMANCE:")
print(brand_summary.to_string(index=False))

low_stock = df[df["stock_status"] == "⚠ LOW STOCK"]
print(f"\n🚨 LOW STOCK ALERTS: {len(low_stock)} items require attention")
print(low_stock[["branch_name","brand","quantity"]].to_string(index=False))

output_path = r"C:\Users\Administrator\Downloads\systems-specialist-demo\To-send-through-Github\Inventory Report.xlsx"

with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    df.to_excel(writer,             sheet_name="Full Inventory",   index=False)
    branch_summary.to_excel(writer, sheet_name="Branch Summary",   index=False)
    brand_summary.to_excel(writer,  sheet_name="Brand Performance", index=False)
    low_stock.to_excel(writer,      sheet_name="Low Stock Alerts",  index=False)

print(f"\n✅ Report exported to: {output_path}")
print("   Sheets: Full Inventory | Branch Summary | Brand Performance | Low Stock Alerts")

