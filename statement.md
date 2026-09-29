# Project Statement

## Project Title
**Hostel Complaint Management System**

---

## Problem Statement
In most hostel setups, maintenance issues—whether it's broken plumbing, faulty electrical points, or spotty Wi-Fi—are handled through physical registers or verbal requests. This manual approach quickly leads to lost complaints, zero accountability, and students constantly having to follow up in person just to get an update.

The **Hostel Complaint Management System** is a lightweight Python command-line utility built to digitize this workflow. It gives residents a structured way to report issues, generates unique tracking IDs, and lets students look up their complaint's status instantly.

---

## Core Objectives
* **Streamline Reporting:** Provide a quick CLI flow for students to submit complaints without administrative delays.
* **Traceability:** Assign an auto-generated, unique Complaint ID to every submission for accurate tracking.
* **Structured Records:** Capture critical context (student details, room numbers, categories, descriptions) systematically.
* **Instant Status Lookups:** Allow residents to check their issue status directly using their Complaint ID.
* **Practical Python Application:** Apply foundational Python concepts to solve a practical, everyday campus problem.

---

## System Architecture & Features

### 1. Main Navigation
Simple terminal-based interactive menu with clear paths for registration, status checks, and exit execution.

### 2. Issue Registration Workflow
1. Capture student credentials (Name, Roll Number) and room location.
2. Categorize the issue (Electricity, Water, Internet, Cleanliness, Maintenance).
3. Record a detailed problem description.
4. Auto-generate a unique Complaint ID.
5. Initialize the ticket state to **Pending**.

### 3. Status Lookup Engine
1. Prompt user for their unique Complaint ID.
2. Search stored records for a match.
3. Display ticket metadata alongside current resolution status.

---

## Tech Stack & Core Concepts

* **Environment & Tools:** Python 3.x, Visual Studio Code, Git, GitHub

### Python Concepts Implemented
* **Control Flow:** `if`/`elif`/`else` structures for menu routing and validation; `while` loops for session continuity.
* **Data Structures:** Lists and Dictionaries for memory-based storage and fast lookup of complaint objects.
* **Modular Code:** Functions to segregate input handling, storage logic, and status lookups into clean components.
* **String Processing:** Formatting and manipulation for unique ID generation and display outputs.

---

## Expected Outcome
A fully operational, lightweight CLI application that replaces paper register books with a reliable digital workflow. It gives hostel residents peace of mind through clear tracking IDs while demonstrating clean, structured Python code.