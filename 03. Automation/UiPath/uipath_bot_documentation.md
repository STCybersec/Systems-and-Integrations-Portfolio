# UiPath Community Edition - RPA Bot Documentation

**Author:** Sanele Siyabonga Thusi
**Tool:** UiPath Studio Community Edition - free
**Project name:** Inventory-Low-Stock-Bot
**Type:** Robotic Process Automation (RPA)

---

## ✔ What This Bot Does

This bot performs targeted row-level automation - simulating how a human would
manually scan through an inventory report and flag every low stock item.

Unlike PAD which orchestrates the full pipeline, this bot executes one specific
repeatable task: read every product row, evaluate its status, and log exceptions.

---

## ✔ Activities Used - Step by Step

| Step | Activity | Configuration | Output |
|------|----------|--------------|--------|
| 1 | Sequence | Main container | Holds all activities |
| 2 | Read Range Workbook | File: Inventory Report.xlsx / Sheet: Full Inventory / Range: "" | InventoryData (DataTable) |
| 3 | For Each Row in Data Table | DataTable: InventoryData | CurrentRow variable |
| 4 | Assign | stockStatus = currentRow("stock_status").ToString | stockStatus (String) |
| 5 | If | Condition: stockStatus.Contains("LOW STOCK") | Branches to Then or skips |
| 6 | Append Line | File: low_stock_log.txt / Text: branch + brand + qty + status | Row written to file |
| 7 | Message Box | Text: "Low stock scan complete. Results saved to low_stock_log.txt" | Confirmation popup |

---

## ⚖️ Key Decisions During Development

### 🤔 Why Assign before If
UiPath uses VB.NET expressions. Nested quotes inside a condition field cause
syntax errors. Storing the value in a variable first removes the nesting problem.
 
**❌ Would not work:**
I tried this:
```
currentRow("stock_status").ToString.Contains("LOW STOCK")
```

**✅ Works correctly:**
```
stockStatus = currentRow("stock_status").ToString
stockStatus.Contains("LOW STOCK")
```

### 💭 Why string concatenation uses & not + (AI agent was instrumental in creating this string)
UiPath uses VB.NET - not Python or JavaScript. String joining uses & operator.

```
Correct: currentRow("branch_name").ToString & " | " & currentRow("brand").ToString
Wrong:   currentRow("branch_name").ToString + " | " + currentRow("brand").ToString
```

---

## 💡 Output - low_stock_log.txt

```
North Reef | ApexCell | Qty: 40 | LOW STOCK
North Reef | TradeMax | Qty: 30 | LOW STOCK
Cape Town  | ApexCell | Qty: 25 | LOW STOCK
Cape Town  | TradeMax | Qty: 20 | LOW STOCK
Durban     | ApexCell | Qty: 35 | LOW STOCK
Durban     | TradeMax | Qty: 15 | LOW STOCK
```

<img width="526" height="202" alt="Low stocks" src="https://github.com/user-attachments/assets/2a0c005c-6b79-4177-8924-3a783c3ba311" />


6 rows written. 12 rows scanned. 6 skipped (OK status). Zero errors.

---

## PAD vs UiPath - Role Distinction

| | PAD | UiPath |
|---|---|---|
| Type | BPA - Business Process Automation | RPA - Robotic Process Automation |
| Scope | End-to-end pipeline orchestration | Single targeted repeatable task |
| Trigger | Scheduled daily at 07:00 | Runs after PAD generates report |
| Reads from | Branch Summary sheet (3 rows) | Full Inventory sheet (12 rows) |
| Output | Management email + audit log | Product-level exception log |
| Detail level | Branch summary (North Reef has 2 alerts) | Individual product (ApexCell Qty: 40) |

---

## Tools Used

| Tool | Cost | Purpose |
|------|------|---------|
| UiPath Studio Community | Free | Bot design and execution |
| UiPath.Excel.Activities | Free - included | Read Range Workbook activity |
| UiPath.System.Activities | Free - included | For Each Row, Assign, If, Append Line |

**Total licensing cost: R0**
