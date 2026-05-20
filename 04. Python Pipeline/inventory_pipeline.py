"""
CompanyConnect Supply Chain Data Pipeline
Author: Sanele Siyabonga Thusi
Purpose: Automated data processing, flagging, and reporting
Tools: Python, pandas, pyodbc, openpyxl
Data source: SQL Server - inventory_supply database
"""

import pandas as pd
import pyodbc
from datetime import date


conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=LT-COE1\\SQLEXPRESS;"
    "DATABASE=inventory_supply;"
    "Trusted_Connection=yes;"
)

df = pd.read_sql("""
    SELECT
        b.branch_name,
        p.brand,
        p.category,
        i.quantity,
        p.unit_cost_rand,
        i.last_updated
    FROM dbo.inventory i
    JOIN dbo.branches b ON b.branch_id = i.branch_id
    JOIN dbo.products p ON p.product_id = i.product_id
    ORDER BY b.branch_name, p.brand
""", conn)

conn.close()


df["stock_value_rand"] = df["quantity"] * df["unit_cost_rand"]


df["stock_status"] = df["quantity"].apply(
    lambda q: "LOW STOCK" if q < 50 else "OK"
)


branch_summary = (
    df.groupby("branch_name")
    .agg(
        total_units     = ("quantity",         "sum"),
        total_value     = ("stock_value_rand", "sum"),
        low_stock_items = ("stock_status", lambda x: (x == "LOW STOCK").sum())
    )
    .reset_index()
    .sort_values("total_value", ascending=False)
)


brand_summary = (
    df.groupby(["brand", "category"])
    .agg(
        total_units = ("quantity",         "sum"),
        total_value = ("stock_value_rand", "sum")
    )
    .reset_index()
    .sort_values("total_value", ascending=False)
)


low_stock = df[df["stock_status"] == "LOW STOCK"].copy()


print("=" * 55)
print("   CompanyConnect SUPPLY CHAIN REPORT -", date.today())
print("=" * 55)

print("\nFULL INVENTORY WITH FLAGS:")
print(df[["branch_name","brand","quantity","stock_value_rand","stock_status"]].to_string(index=False))

print("\nBRANCH SUMMARY:")
print(branch_summary.to_string(index=False))

print("\nBRAND PERFORMANCE:")
print(brand_summary.to_string(index=False))

print(f"\nLOW STOCK ALERTS: {len(low_stock)} items require attention")
print(low_stock[["branch_name","brand","quantity"]].to_string(index=False))


output_path = r"C:\Users\Administrator\Downloads\systems-specialist-demo\To-send-through-Github\Inventory Report.xlsx"

with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    df.to_excel(writer,             sheet_name="Full Inventory",    index=False)
    branch_summary.to_excel(writer, sheet_name="Branch Summary",    index=False)
    brand_summary.to_excel(writer,  sheet_name="Brand Performance", index=False)
    low_stock.to_excel(writer,      sheet_name="Low Stock Alerts",  index=False)

print(f"\nReport exported to: {output_path}")
print("Sheets: Full Inventory | Branch Summary | Brand Performance | Low Stock Alerts")
