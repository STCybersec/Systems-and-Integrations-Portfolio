# 📊 Systems & Integration Portfolio

**Author:** Sanele Siyabonga Thusi
**Contact:** thusisanelelele@gmail.com
**GitHub:** [STCybersec](https://github.com/STCybersec)

---

## 📌 Project Overview

This project demonstrates core systems and integration capabilities mapped to real multi-branch distribution operations. It simulates a distribution environment covering **MS SQL Server, Power BI, Python, Power Automate Desktop (PAD/BPA), and UiPath (RPA)** - connected into one automated pipeline.

> *"From raw database to automated executive email - zero manual steps."*

---

## 🏗️ End-to-End Architecture

<img width="956" height="823" alt="end_to_end_flow" src="https://github.com/user-attachments/assets/aaa4ed9c-7d33-4973-ab5a-fd014a366721" />

---

## 📁 Project Structure

```
inventory-systems-and-integration/
│
├── 01.SQL/
│   └── inventory_business_queries.sql     <- 8 operational queries
│
├── 02.PowerBI/
│   ├── real-time-interactive-dashboard/
│   │   └── inventory_dashboard.pbix       <- Live interactive dashboard
│   └── screenshots/
│       ├── 01. executive_summary.png
│       ├── 02. inventory_details.png
│       └── 03. delivery_monitor.png
│
├── 03.Automation/
│   ├── PAD/
│   │   ├── pad_flow_documentation.md
│   │   ├── screenshots/
│   │   │   ├── 01. pad_canvas_part1.png
│   │   │   ├── 02. pad_canvas_part2.png
│   │   │   ├── 03. Daily Email Alert.png
│   │   │   └── 04. Display_Message -1.png
│   │   ├── recordings/
│   │   │   └── pad_flow_demo.mp4
│   │   └── evidence/
│   │       └── confirmation.txt
│   └── UiPath/
│       ├── uipath_bot_documentation.md
│       ├── screenshots/
│       │   ├── uipath_canvas.png
│       │   └── low_stock_log.png
│       └── recordings/
│           └── uipath_bot_demo.mp4
│
├── 04.Python_Pipeline/
│   └── inventory_pipeline.py
│
└── 05.Integration_Summary/
    └── architecture.md
```

---

## 🗄️ 1 - SQL Server (MS SQL / T-SQL)

**Database:** `inventory_supply`
**Tables:** `branches` · `products` · `inventory` · `deliveries`

### 💼 Business Workflow

```
Raw Data -> SQL Queries -> Operational Insights -> Management Decisions
```

### 📈 Step-by-Step

| Step | Query | What It Achieves |
|------|-------|-----------------|
| 1 | Product catalogue by price | Know your cost base |
| 2 | Stock quantity per branch | Where is stock sitting |
| 3 | Stock value in Rands per branch | Financial exposure - R1.35M total across 3 branches |
| 4 | Low stock alerts (< 50 units) | 12 items need urgent action |
| 5 | Brand performance across branches | Sales intelligence - TradeMax total value at R71,500 - indicating strongest sales velocity among brands |
| 6 | Delivery status + action flags | Logistics monitoring - 1 failed, 2 in transit |
| 7 | Delivery exceptions monitoring | Continuous monitoring - days outstanding per delivery |
| 8 | Executive summary (1 query) | CEO/Exec reporting - full picture in a single result set |

### 🤔💭 Key Insight
> *Stock value is directly proportional to quantity. Higher stock = lower sales velocity. Cape Town at R378K indicates stronger market movement than North Reef at R526K - assuming constant restocking conditions (ceteris paribus).*

📄 [`01.SQL/inventory_business_queries.sql`](01.SQL/inventory_business_queries.sql)

---

## 📊 2 - Power BI Dashboard

**3-page executive dashboard connected live to SQL Server.**

### Business Workflow

```
SQL Server → Power BI Desktop → 3-Page Dashboard → Executive Decisions
```

### Page 1 - Executive Summary

**What this achieves:** Single-page snapshot for CEO/Exec/Operations Manager morning review.

| Visual | Insight Delivered |
|--------|------------------|
| KPI Card - Total Stock Value | R1,350,300 across all branches |
| KPI Card - Total Units | 1,420 units in network |
| KPI Card - Low Stock Items | 12 product lines below threshold |
| KPI Card - Failed Deliveries | 1 delivery requires investigation |
| Bar Chart - Branch Stock Value | North Reef R526K · Durban R446K · Cape Town R378K |
| Line Chart + Average | Visual trend with R450,100 average benchmark |
| Delivery Status Donut | 33% delivered · 33% in transit · 17% failed · 17% pending |
| City + Branch Slicers | Filter entire dashboard by location |

📸 *Screenshot:*
<img width="1425" height="798" alt="01  Executive Summary" src="https://github.com/user-attachments/assets/c0513112-35f4-4ab2-b2a1-268d6829a8c8" />

---

### Page 2 - Inventory Details

**What this achieves:** Brand and category-level stock analysis for operations managers.

| Visual | Insight Delivered |
|--------|------------------|
| Grouped Bar Chart | Units per brand per branch - red bars = low stock |
| Brand Details Table | Brand · Category · Total Units · Stock Value · % of Total |
| City Bar Chart | Johannesburg 550 · Durban 470 · Cape Town 400 |
| Category Slicer | Filter by Automotive · Premium · Export/Industrial |

📸 *Screenshot:*
<img width="1469" height="796" alt="02  Inventory Details" src="https://github.com/user-attachments/assets/2339e545-4c40-481a-93a2-1b0d95f8e67f" />


---

### Page 3 - Delivery Monitor

**What this achieves:** Real-time delivery tracking with action flags for logistics teams.

| Visual | Insight Delivered |
|--------|------------------|
| Delivery Status Donut | Overall delivery health at a glance |
| Delivery by Brand Donut | Which brands have active delivery issues |
| Delivery Table | Branch · Brand · Status · Action Flag per delivery |

📸 *Screenshot:*
<img width="1553" height="799" alt="03  Delivery Monitor" src="https://github.com/user-attachments/assets/d5c1c479-21c7-4938-ae63-8d4a34dde230" />


📂 [`02.PowerBI/Real-time-interactive-dashboard/`](02.PowerBI/Real-time-interactive-dashboard/)

---

## 🤖 3 - Automation (BPA + RPA)

### Business Workflow

```
Python generates report → PAD orchestrates pipeline → Email sent to management
                                    ↓
                          UiPath scans inventory → Low stock log created
```

---

### 3a - Power Automate Desktop (BPA)

**Role:** End-to-end business process orchestration - runs the entire daily pipeline automatically.

### Step-by-Step Flow

| Step | Action | Why |
|------|--------|-----|
| 1 | Get current date and time | Creates timestamp for email subject and log |
| 2 | Run Python script | Generates fresh Inventory Report.xlsx silently |
| 3 | Wait 5 seconds | Ensures Python finishes writing before Excel opens |
| 4 | Launch Excel | Opens Inventory Report.xlsx |
| 5 | Set active worksheet → Branch Summary | Targets correct data sheet |
| 6 | Read all values from worksheet | Loads 3 rows × 4 columns into BranchData |
| 7 | Close Excel | Releases file lock before email attachment |
| 8 | Create list → AlertMessages | Empty container for alert strings |
| 9 | For Each branch in BranchData | Loops through all 3 branches |
| 10 | If low_stock_items > 0 | Evaluates each branch for alerts |
| 11 | Add to AlertMessages | Builds alert string per branch |
| 12 | Launch Outlook | Opens PAD-controlled Outlook instance |
| 13 | Wait 5 seconds | Ensures Gmail account fully loads in Outlook |
| 14 | Send email through Outlook | Dispatches alert email with Excel attached |
| 15 | Display message | On-screen confirmation of alert content |
| 16 | Write to confirmation.txt | Timestamped audit log of every run |

**What this achieves:**
- Zero manual reporting
- Management receives branch health email every morning
- Every run logged with timestamp for audit purposes
- Conditional logic - only alerts when thresholds are breached

**Critical fixes that made it work:**
- Close Excel before Send Email - file was locked preventing attachment
- Wait 5 seconds after Launch Outlook - account needed time to load

📸 *Screenshots:*

<img width="1144" height="973" alt="01  pad_canvas_screenshot" src="https://github.com/user-attachments/assets/0d2f7be9-50f9-4a99-a48d-3f2dcb85d25f" />
<img width="1152" height="979" alt="02  pad_canvas_screenshot" src="https://github.com/user-attachments/assets/23bbccdc-9d45-4066-90e5-b442f2ed9b86" />
<img width="1484" height="770" alt="03  Daily Email Alert" src="https://github.com/user-attachments/assets/e89f5547-01fc-4269-b87e-37b4023e751b" />

🎥 *Recording:*
[▶ Watch PAD Flow Demo](https://github.com/STCybersec/Systems-and-Integrations-Portfolio/issues/2)

📋 *Audit Log Evidence:*
```
2026/05/14 14:02:28 - Pipeline completed. Alerts sent: 3
```
[📄 View confirmation.txt](03.Automation/PAD/evidence/confirmation.txt)

📄 [`View PAD Documentation`](03.Automation/PAD/pad_flow_documentation.md)

---

### 3b - UiPath Community Edition (RPA)

**Role:** Targeted row-level automation - scans every inventory record and logs exceptions.

### Step-by-Step Bot

| Step | Activity | What It Does |
|------|----------|-------------|
| 1 | Read Range Workbook | Reads Full Inventory sheet into InventoryData table |
| 2 | For Each Row | Iterates through all 12 inventory records |
| 3 | Assign stockStatus | Extracts stock_status value from current row |
| 4 | If stockStatus Contains "LOW STOCK" | Evaluates each row against threshold |
| 5 | Append Line -> low_stock_log.txt | Writes flagged row: branch · brand · qty · status |
| 6 | Message Box | Confirms scan completion |

**What this achieves:**
- Individual product-level scanning - not just branch summaries
- Structured log file for operations team review
- Demonstrates row-by-row RPA capability distinct from PAD

**Output - low_stock_log.txt:**
```
North Reef | ApexCell | Qty: 40 | ⚠️ LOW STOCK
North Reef | TradeMax | Qty: 30 | ⚠️ LOW STOCK
Cape Town  | ApexCell | Qty: 25 | ⚠️ LOW STOCK
Cape Town  | TradeMax | Qty: 20 | ⚠️ LOW STOCK
Durban     | ApexCell | Qty: 35 | ⚠️ LOW STOCK
Durban     | TradeMax | Qty: 15 | ⚠️ LOW STOCK
```

**PAD vs UiPath - why both:**

| | PAD | UiPath |
|---|---|---|
| **Type** | BPA - full process orchestration | RPA - targeted task automation |
| **Scope** | End-to-end pipeline | Single repeatable task |
| **Output** | Management email + audit log | Product-level exception log |
| **Trigger** | Scheduled daily | Runs after PAD generates report |

📸 *Screenshots:*

![UiPath Canvas]
<img width="1919" height="1020" alt="01 uipath_canvas" src="https://github.com/user-attachments/assets/fdb66e79-3923-4239-adc9-8ab87c490cd3" />

![Low Stock Log]
<img width="1127" height="483" alt="02 low_stock_log" src="https://github.com/user-attachments/assets/09f0ad48-f03b-4174-afbf-844f41f961c2" />

🎥 *Recording:*
[▶ Watch UiPath Bot Demo](https://github.com/STCybersec/Systems-and-Integrations-Portfolio/issues/3)

📄 [`View UiPath Documentation`](03.Automation/UiPath/uipath_bot_documentation.md)

---

## 🐍 4 - Python Pipeline

**Role:** Data processing engine - transforms raw inventory data into structured Excel report.

### Business Workflow

```
Raw Data → Python → Calculations → Flagging → 4-Sheet Excel Report
```

### Step-by-Step

| Step | What Happens | Output |
|------|-------------|--------|
| 1 | Load inventory data | 12 rows × 6 columns DataFrame |
| 2 | Calculate stock value | quantity × unit_cost_rand per row |
| 3 | Flag low stock items | ⚠️ LOW STOCK if quantity < 50 |
| 4 | Branch summary | Total units, total value, low stock count per branch |
| 5 | Brand summary | Total units, total value per brand across all branches |
| 6 | Export to Excel | 4-sheet workbook saved to shared path |

**Output Sheets:**

| Sheet | Contents |
|-------|----------|
| Full Inventory | All 12 rows with flags and calculated values |
| Branch Summary | 3 branches - units, value, low stock count |
| Brand Performance | 4 brands - total units and total value |
| Low Stock Alerts | Only the 6 flagged rows for urgent review |


📄 [`View Inventory_Pipeline`](04.Python_Pipeline/inventory_pipeline.py)

---

## 🔗 5 - Integration Architecture

**Full end-to-end system connecting all tools.**

### What Each Tool Covers

| Tool | Layer | Responsibility |
|------|-------|---------------|
| SQL Server | Data | Central source of truth |
| Python | Processing | Transform, calculate, flag, export |
| Power BI | Visualisation | Executive dashboards, KPIs, trends |
| PAD | BPA | Orchestrate pipeline, alert, log |
| UiPath | RPA | Row-level scanning, exception logging |

### Azure-Ready Design

This architecture is designed to scale to cloud:

| Current | Azure Equivalent |
|---------|-----------------|
| SQL Server (local) | Azure SQL Database |
| PAD (desktop) | Power Automate Cloud |
| Python (local) | Azure Functions |
| Power BI Desktop | Power BI Service |

📄 [`05.Integration_Summary/architecture.md`](05.Integration_Summary/architecture.md)

---

## ✅ Requirements Coverage

| Requirement | Implementation | Status |
|-------------|---------------|--------|
| MS SQL Databases | Full schema + 8 business queries | ✅ |
| Workflow Design | Documented 16-step PAD flow + 6-step UiPath bot | ✅ |
| System Integration | SQL → Python → PAD → Email pipeline | ✅ |
| Business Process Automation | PAD daily orchestration flow | ✅ |
| Robotic Process Automation | UiPath inventory scanner | ✅ |
| Continuous Monitoring | Delivery exceptions query + confirmation.txt audit log | ✅ |
| Stakeholder Communication | Automated Gmail alert with Excel attachment | ✅ |
| Power BI / Analytics | 3-page dashboard with DAX measures | ✅ |
| Azure Ready | Architecture designed for cloud migration | ✅ |

---

## 🎓 About the Author

BCom Information Technology Management — Mancosa (2026–2029)
Hybrid specialist in Cybersecurity, Data Analytics, and Automation.

- 🛡️ [Cybersecurity Portfolio](https://github.com/STCybersec/Wazuh-Endpoint-Security)
- 📊 [Data Analytics & BI Portfolio](https://github.com/STCybersec/Data-Analysis-BI---Portfolio)
- 📧 thusisanelelele@gmail.com

> *"Logs don't lie — data tells the truth."*
