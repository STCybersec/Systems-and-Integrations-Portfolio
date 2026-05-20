# End-to-End Integration Architecture

**Author:** Sanele Siyabonga Thusi
**Purpose:** Documents how all tools connect into one automated pipeline

---

## Architecture

<img width="773" height="675" alt="end_to_end_systems_architecture" src="https://github.com/user-attachments/assets/0d4b0248-e721-4761-b6ed-347efa0f1d1b" />

---

## Tool Responsibilities

| Tool | Layer | Input | Output | Responsibility |
|------|-------|-------|--------|---------------|
| SQL Server | Data | Raw business data | Structured tables | Central source of truth |
| Python | Processing | Live SQL query | 4-sheet Excel report | Connect, transform, calculate, flag, export |
| Power BI | BI | SQL Server live connection | 3-page dashboard | Executive visualisation |
| PAD | Automation | Python Excel output | Email + audit log | End-to-end orchestration |
| UiPath | Automation | Python Excel output | Exception log | Row-level scanning |

---

## Morning Pipeline - Step by Step

```
1.  PAD fires automatically via Windows Task Scheduler at 07:00
2.  PAD runs inventory_pipeline.py
3.  Python connects to SQL Server - inventory_supply database
4.  Python queries live inventory, branches, products and deliveries data
5.  Python calculates stock values, flags low stock items
6.  Python exports Inventory Report.xlsx with 4 sheets
7.  PAD opens Excel - switches to Branch Summary sheet
8.  PAD reads branch alert data into BranchData variable
9.  PAD closes Excel - releases file lock
10. PAD evaluates each branch for low stock threshold
11. PAD launches Outlook - waits 5 seconds for account to load
12. PAD sends email to management with Excel attached
13. PAD writes timestamp to confirmation.txt
14. UiPath opens Inventory Report.xlsx
15. UiPath reads every row in Full Inventory sheet
16. UiPath flags rows where stock_status contains LOW STOCK
17. UiPath writes each flagged row to low_stock_log.txt
18. UiPath confirms completion via Message Box
```

---

Any change made in SQL Server automatically flows through Python into the Excel report, the PAD email, and the UiPath log - on the next scheduled run.

---

## File Paths

| File | Created by | Read by |
|------|-----------|---------|
| inventory_pipeline.py | Manual | PAD |
| Inventory Report.xlsx | Python (from SQL) | PAD + UiPath |
| confirmation.txt | PAD | Manual review |
| low_stock_log.txt | UiPath | Manual review |

---

## Python - SQL Connection

Python connects directly to SQL Server using pyodbc:

```python
import pyodbc
import pandas as pd

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
```

This makes Python, PAD email reports, and UiPath logs all reflect live SQL data — identical to what Power BI shows on the dashboard.

---

## PAD - UiPath Connection

Currently PAD and UiPath run as separate automations. The connection between them:

PAD triggers UiPath using the Run Application action after generating the report:

```
PAD Step 13 (after confirmation.txt is written):
Action: Run Application
Application path: C:\Users\Administrator\AppData\Local\UiPath\app-[version]\UiPath.Studio.exe
Arguments: --execute "C:\path\to\Inventory-Low-Stock-Bot\project.json"
Wait for completion: Yes
```

This makes the full pipeline sequential:
```
PAD runs Python -> PAD emails management -> PAD triggers UiPath -> UiPath scans rows -> UiPath logs exceptions
```

---

## Azure-Ready Design

| Current (local) | Azure equivalent |
|----------------|-----------------|
| SQL Server | Azure SQL Database |
| Python script | Azure Functions |
| PAD | Power Automate Cloud |
| Power BI Desktop | Power BI Service |
| Local file paths | Azure Blob Storage |

Migration path: move SQL first, then Python, then Power Automate Cloud.
Each step is independent - the architecture supports incremental migration.

---

## Licensing - Total Cost: R0

| Tool | License |
|------|---------|
| SQL Server Express | Microsoft free tier |
| Power BI Desktop | Microsoft free |
| Power Automate Desktop | Built into Windows |
| Python | Open source |
| UiPath Studio Community | UiPath free tier |
