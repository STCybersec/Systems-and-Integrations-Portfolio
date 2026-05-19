# Power Automate Desktop - BPA Flow Documentation

**Author:** Sanele Siyabonga Thusi
**Tool:** Power Automate Desktop (PAD) - free, built into Windows 10/11
**Flow name:** Inventory Daily Report - Automated
**Type:** Business Process Automation (BPA)

---

## ✔ What This Flow Does

This flow runs the entire daily inventory reporting pipeline automatically - from
generating the Excel report to sending a management email - with zero manual steps.

Every morning it:
1. Triggers the Python pipeline to generate a fresh Excel report
2. Reads branch-level data from the report
3. Evaluates which branches have low stock
4. Sends a conditional alert email to management with the report attached
5. Logs every run with a timestamp for audit purposes

---

## 📶 Flow Steps - Full Documentation

| Step | Action | Purpose |
|------|--------|---------|
| 1 | Get current date and time | Creates %CurrentDateTime% for email subject and log entry |
| 2 | Run application - Python script | Runs inventory_pipeline.py silently in background |
| 3 | Wait - 5 seconds | Ensures Python finishes writing Excel before next step reads it |
| 4 | Launch Excel | Opens Inventory Report.xlsx - stores as %ExcelInstance% |
| 5 | Set active Excel worksheet | Switches to Branch Summary tab - avoids reading wrong sheet |
| 6 | Read all values from worksheet | Reads Branch Summary with column names as headers |
| 7 | Close Excel | Releases file lock - critical before email attachment step |
| 8 | Create new list | Creates empty %AlertMessages% list |
| 9 | For each row in BranchData | Loops through all 3 branch rows |
| 10 | If low_stock_items > 0 | Evaluates each branch against threshold |
| 11 | Add item to list | Builds alert string per branch |
| 12 | Launch Outlook | Opens PAD-controlled Outlook instance |
| 13 | Wait - 5 seconds | Allows Gmail account to fully load in Outlook |
| 14 | Send email through Outlook | Dispatches alert email with Excel attached |
| 15 | Display message | On-screen confirmation showing alert content |
| 16 | Write text to file | Appends timestamped entry to confirmation.txt |

<img width="641" height="857" alt="pad_workflow_BPA" src="https://github.com/user-attachments/assets/a3bfe5d1-4686-4ae7-81d2-2c1451e260cb" />

---

## ⚙️ Critical Fixes done/encounted - What Made It Work

### Fix 1 - Close Excel before Send Email
**Problem:** PAD could not attach the Excel file to the email.
**Cause:** Excel had the file open (locked) - the email action could not access it.
**Fix:** Added Close Excel action between reading data and sending email.
**Lesson:** Always release file locks before referencing a file in another action.

### Fix 2 - Wait 5 seconds after Launch Outlook
**Problem:** PAD returned "failed to find account" error.
**Cause:** PAD fired the Send Email action before Outlook had fully loaded the Gmail account.
**Fix:** Added Wait 5 seconds between Launch Outlook and Send Email.
**Lesson:** External applications need time to initialise before automation interacts with them.

### Fix 3 - App Password for Gmail in Outlook
**Problem:** Gmail account would not authenticate in Outlook.
**Cause:** Google blocks direct password access for third-party apps by default.
**Fix:** Generated a 16-character App Password from myaccount.google.com - Security - App Passwords.
**Lesson:** Google requires App Passwords for any third-party app accessing Gmail via IMAP/SMTP.

---

## 📧 Email Output

**Subject:** Daily Inventory Alert - 2026/05/14 14:02:28
**From:** sanele Thusi (thusisanelelele@gmail.com)
**To:** thusisanelelele@gmail.com
**Attachment:** Inventory Report.xlsx


**Body:**
```
Good morning,

The automated inventory scan has detected the following alerts:

North Reef has 2 low stock items
Durban has 2 low stock items
Cape Town has 2 low stock items

Full report attached.

- Inventory Systems Monitor (Automated)
```

<img width="1484" height="770" alt="03  Daily Email Alert" src="https://github.com/user-attachments/assets/ed052ddd-0c19-4e58-9e6c-52e9ed87922c" />

---

## 📝 Audit Log - confirmation.txt

Every run appends one line:
```
2026/05/14 14:02:28 - Pipeline completed. Alerts sent: 3
```

<img width="777" height="486" alt="confirmation" src="https://github.com/user-attachments/assets/1fad9732-937a-45ee-91af-841df2ac0938" />

---

## 📅 Scheduling for Production

To run this flow automatically every morning at 07:00:

1. Open Windows Task Scheduler
2. Create Basic Task - name it "Inventory Daily Report"
3. Trigger - Daily at 07:00
4. Action - Start a program
5. Program: "C:\Program Files\Power Automate Desktop\PAD.Console.Host.exe"
6. Arguments: /flow "Inventory Daily Report - Automated"

---

## 🛠️ Tools Used

| Tool | Cost | Purpose |
|------|------|---------|
| Power Automate Desktop | Free - built into Windows | Flow orchestration |
| Microsoft Outlook | Free with Microsoft account | Email dispatch |
| Gmail App Password | Free - generated in Google account | Authentication |
| Windows Task Scheduler | Free - built into Windows | Scheduling |

**Total licensing cost: R0**
