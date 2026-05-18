# End-to-End Integration Architecture

**Author:** Sanele Siyabonga Thusi
**Purpose:** Documents how all tools connect into one automated pipeline

---

## Architecture 
<img width="956" height="823" alt="Screenshot 2026-05-18 100927" src="https://github.com/user-attachments/assets/baa2ad77-dfc8-4c62-98b4-a50265d2947d" />

## Tool Responsibilities

| Tool | Layer | Input | Output | Responsibility |
|------|-------|-------|--------|---------------|
| SQL Server | Data | Raw business data | Structured tables | Central source of truth |
| Python | Processing | Hardcoded data (SQL-ready) | 4-sheet Excel report | Transform, calculate, flag, export |
| Power BI | BI | SQL Server live connection | 3-page dashboard | Executive visualisation |
| PAD | Automation | Python Excel output | Email + audit log | End-to-end orchestration |
| UiPath | Automation | Python Excel output | Exception log | Row-level scanning |

---

## Morning Pipeline - Step by Step

```
1.  PAD fires automatically via Windows Task Scheduler at 07:00
2.  PAD runs inventory_pipeline.py
3.  Python processes inventory data
4.  Python exports Inventory Report.xlsx with 4 sheets
5.  PAD opens Excel - switches to Branch Summary sheet
6.  PAD reads branch alert data into BranchData variable
7.  PAD closes Excel - releases file lock
8.  PAD evaluates each branch for low stock threshold
9.  PAD launches Outlook - waits 5 seconds for account to load
10. PAD sends email to management with Excel attached
11. PAD writes timestamp to confirmation.txt
12. UiPath opens Inventory Report.xlsx
13. UiPath reads every row in Full Inventory sheet
14. UiPath flags rows where stock_status contains LOW STOCK
15. UiPath writes each flagged row to low_stock_log.txt
16. UiPath confirms completion via Message Box
```

---

## File Paths

| File | Created by | Read by |
|------|-----------|---------|
| inventory_pipeline.py | Manual | PAD |
| Inventory Report.xlsx | Python | PAD + UiPath |
| confirmation.txt | PAD | Manual review |
| low_stock_log.txt | UiPath | Manual review |

---

## Python - SQL Integration Note

Currently Python uses hardcoded data mirroring the SQL database.
In production, replace the data block with a live SQL connection:

```python
import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost;"
    "DATABASE=inventory_supply;"
    "Trusted_Connection=yes;"
)

df = pd.read_sql("""
    SELECT b.branch_name, p.brand, p.category,
           i.quantity, p.unit_cost_rand, i.last_updated
    FROM inventory i
    JOIN branches b ON i.branch_id = b.branch_id
    JOIN products p ON p.product_id = i.product_id
""", conn)
```

Any change in SQL Server then flows automatically through Python into Excel, Power BI, and the morning management email.

---

## Azure-Ready Design

| Current (local) | Azure equivalent |
|----------------|-----------------|
| SQL Server | Azure SQL Database |
| Python script | Azure Functions |
| PAD | Power Automate Cloud |
| Power BI Desktop | Power BI Service |
| Local file paths | Azure Blob Storage |

---

## Licensing - Total Cost: R0

| Tool | License |
|------|---------|
| SQL Server Express | Microsoft free tier |
| Power BI Desktop | Microsoft free |
| Power Automate Desktop | Built into Windows |
| Python | Open source |
| UiPath Studio Community | UiPath free tier |
