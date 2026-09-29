# Hostel Complaint Management System

A lightweight, CLI-based Python application that simplifies how hostel complaints are logged and tracked. Built to replace manual, messy register entries with a structured digital workflow for students.

---

## Key Features

* **Student Data Logging:** Captures essential student details before registering an issue.
* **Auto-Generated IDs:** Assigns a unique tracking ID to every submitted complaint.
* **Status Tracking:** Quick lookups using the generated ID to check current status.
* **Clean CLI Navigation:** Simple, menu-driven command-line interface.
* **Basic Input Guardrails:** Simple checks to prevent invalid entries and crashes.

---

## Tech Stack & Tools

* **Language:** Python 3.x
* **IDE:** Visual Studio Code
* **Version Control:** Git & GitHub

---

## Project Structure

```text
Hostel-Complaint-Management-System/
│
├── main.py          # Entry point; handles UI menus and application flow
├── student.py       # Handles student data structures and validation
├── complaint.py     # Manages complaint logic, ID generation, and state
├── statement.md     # Problem statement, scope, and target audience
└── README.md        # Project documentation

