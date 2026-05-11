# 🔋 Systems and Integrations - Portfolio

**Author:** Sanele Siyabonga Thusi  
**Contact:** thusisanelelele@gmail.com  
**LinkedIn / GitHub:** STCybersec  

---

## 📌 Project Overview

This project demonstrates core systems and integration capabilities directly mapped to core integrations and business workflows. It simulates a multi-branch distribution environment - covering **MS SQL, Power BI, Python automation, Power Automate Desktop (PAD), UIPath (RPA) and systems integration architecture**.

---

## 🏗️ Architecture

```
SQL Server → Python Pipeline → Power Automate Desktop → Management Email
                ↓
           Power BI Dashboard
```

Full architecture diagram: [`5_Integration_Summary/architecture.md`](5_Integration_Summary/architecture.md)

---

## 📁 Project Structure

```
inventory-systems-and-integration/
│
├── 01.SQL/
│   ├── inventory_supply_schema.sql        ← Full DB schema + seed data
│   └── inventory_business_queries.sql     ← 8 operational queries
│
├── 02.PowerBI/
│   ├── powerbi_setup_guide.md             ← Connection + DAX measures
│   └── screenshots/                       ← Dashboard visuals
│
├── 03.Automation/
│   ├── PAD/
│   │   └── pad_flow_documentation.md      ← BPA: scheduled pipeline + email alert
│   └── UiPath/
│       └── uipath_bot_documentation.md    ← RPA: reads Excel, logs rows to text file
│
├── 04.Python_Pipeline/
│   └── inventory_pipeline.py              ← Automated reporting pipeline
│
└── 05.Integration_Summary/
    └── architecture.md                    ← End-to-end system design
```

---

## 🗄️ 1 - SQL Server (MS SQL / T-SQL)

**Database:** `inventory_supply`  
**Tables:** `branches` · `products` · `inventory` · `deliveries` · `system_alerts`

### Key Queries
| Query | Business Purpose |
|-------|-----------------|
| Product catalogue by price | Procurement reference |
| Stock quantity per branch | Operations overview |
| Stock value in Rands per branch | Financial exposure |
| Low stock alerts (< 50 units) | Replenishment trigger |
| Brand performance across branches | Sales intelligence |
| Delivery status + action flags | Logistics monitoring |
| Unresolved system alerts | IT uptime monitoring |
| Executive summary (1 query) | CEO reporting |

📄 [`01.SQL/inventory_business_queries.sql`](1_SQL/inventory_business_queries.sql)

---

## 📊 2 - Power BI Dashboard

**3-page executive dashboard:**

| Page | Content |
|------|---------|
| Executive Summary | KPI cards, branch value bar chart, branch slicer |
| Inventory Detail | Brand/category table, grouped bar chart, conditional formatting |
| Delivery Monitoring | Status donut, full delivery log with action flags |

**DAX Measures:** Total Stock Value · Low Stock Items · Failed Deliveries · Total Units

📄 [`02.PowerBI/powerbi_setup_guide.md`](2_PowerBI/powerbi_setup_guide.md)

---

## 🤖 3 - Automation (BPA + RPA)

### 3a - Power Automate Desktop (BPA)

**Role:** Orchestrates the entire daily reporting pipeline from end to end.

**Flow:**
1. Triggers Python pipeline at 07:00 daily
2. Validates the Excel report was successfully generated
3. Reads branch alert counts from the Branch Summary sheet
4. Sends conditional email to management with report attached - only fires if low stock or failed deliveries are detected
5. Logs every run with timestamp to a local log file

> Zero manual steps. Zero licensing cost.

📄 [`03.Automation/PAD/pad_flow_documentation.md`](3_Automation/PAD/pad_flow_documentation.md)

---

### 3b - UiPath Community Edition (RPA)

**Role:** Executes a specific, repeatable UI-based task - simulating how a human would manually process a report row by row.

**Bot Task:**
1. Opens the generated Excel inventory report
2. Reads each row from the Full Inventory sheet
3. Evaluates the stock status column
4. Logs every LOW STOCK row to a structured text file with branch, brand, quantity, and timestamp
5. Closes the file and confirms completion

**Why both PAD and UiPath?**

| | PAD | UiPath |
|---|---|---|
| **Type** | BPA - full process orchestration | RPA - targeted task automation |
| **Scope** | End-to-end pipeline management | Single repeatable UI task |
| **Trigger** | Scheduled (daily 07:00) | Triggered by PAD after report is generated |
| **Output** | Management email + run log | Low stock text log file |

Together they form a complete automation layer - PAD runs the process, UiPath handles the detail work inside it.

📄 [`03.Automation/UiPath/uipath_bot_documentation.md`](3_Automation/UiPath/uipath_bot_documentation.md)

---

## 🐍 4 - Python Pipeline

**Script:** `inventory_pipeline.py`

- Loads inventory data (simulates SQL export)
- Calculates stock value per line item
- Flags low stock items with status column
- Generates branch and brand summaries
- Exports 4-sheet Excel report for Power BI and email

**Output Sheets:** Full Inventory · Branch Summary · Brand Performance · Low Stock Alerts

```bash
pip install pandas openpyxl
python inventory_pipeline.py
```

📄 [`04.Python_Pipeline/inventory_pipeline.py`](4_Python_Pipeline/inventory_pipeline.py)

---

## 🔗 5 - Integration Architecture

End-to-end workflow connecting all tools into one operational system.  
Designed to be **Azure-ready** (SQL → Azure SQL, PAD → Power Automate Cloud).

📄 [`05.Integration_Summary/architecture.md`](5_Integration_Summary/architecture.md)

---

## ✅ Inventory JD Requirements Covered

| Requirement | Status |
|-------------|--------|
| MS SQL Databases | ✅ Full schema + 8 queries |
| Workflow Design Principles | ✅ Documented end-to-end |
| System Integration | ✅ SQL → Python → PAD → Email |
| Business Process Automation | ✅ PAD scheduled flow |
| RPA | ✅ PAD bot + UiPath (in progress) |
| Continuous Monitoring | ✅ system_alerts table + query |
| Stakeholder Communication | ✅ Automated management email |
| Azure (Advantageous) | ✅ Architecture is Azure-ready |

---

## 🎓 About the Author

BCom Information Technology Management student (Mancosa, 2026-2029).  
Hybrid specialist in **Cybersecurity, Data Analytics, and Automation**.

- 🛡️ [Cybersecurity Portfolio](https://github.com/STCybersec/Wazuh-Endpoint-Security)
- 📊 [Data & Automation Portfolio](https://github.com/STCybersec/Data-Analysis-BI---Portfolio)
- 📧 thusisanelelele@gmail.com
