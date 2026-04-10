# 🏛️ Module 2: Python Data Fundamentals (Cisco PCAP)

This directory houses the complete technical breakdown of **Module 2** from the Cisco Networking Academy. I have structured this module into six tactical sectors, focusing on high-level data management and security-oriented programming.

---

## 🚦 Course Progress Tracker
- [x] **Sector 1:** Advanced I/O & Print Formatting
- [x] **Sector 2:** Literals & Alternative Number Bases (Hex/Octal)
- [x] **Sector 3:** Operators, Expressions, and Priority Logic
- [x] **Sector 4:** Variables & Assignment Shortcuts
- [x] **Sector 5:** Professional Documentation & PEP 8 Standards
- [x] **Sector 6:** Type Casting & Data Transformation
- [x] **Capstone Project:** Student Financial Planner (Synthesis of all concepts)
- [x] **Module 2 Summary Test** (Status: *Complete*)

---

## 📂 Modular Sector Breakdown

| Sector | Technical Focus | Applied Student Example | File Link |
| :--- | :--- | :--- | :--- |
| **01** | **Output Control** | Simulated system progress bars using `end` and `sep`. | [sector_1_io.py](./sector_1_io.py) |
| **02** | **Data Atoms** | Handling **Hex (0x)** for memory and **Octal (0o)** for permissions. | [sector_2_literals.py](./sector_2_literals.py) |
| **03** | **Logic Ops** | Using **Modulo (%)** for packet load-balancing logic. | [sector_3_operators.py](./sector_3_operators.py) |
| **04** | **Memory** | Managing state with dynamic typing and `+=` increments. | [sector_4_variables.py](./sector_4_variables.py) |
| **05** | **Standards** | Implementing professional **Docstrings** and `TODO` tags. | [sector_5_comments.py](./sector_5_comments.py) |
| **06** | **Interactivity** | Safe transformation of user input into computational data. | [sector_6_interaction.py](./sector_6_interaction.py) |

---

## 🧠 Theory & Concept Repository
In addition to the practical sectors, I have developed a **Concept Notebook** to document the underlying logic of the Python language.

* [**Data Types & Casting**](./Module-2-Concepts/Data_Types_Reference.py): Deep dive into float precision and dynamic typing.
* [**Math & PEMDAS**](./Module-2-Concepts/Arithmetic_Operators.py): Exploration of operator precedence and integer division.
* [**String Replication**](./Module-2-Concepts/String_Operations.py): Using arithmetic operators on string objects.
* [**Bitwise Logic**](./Module-2-Concepts/Bitwise_Basics.py): Manipulating data at the binary level (Networking Prep).

---

## 🚀 Featured Project: Student Financial Planner
**File:** `Module_2_Capstone_Project.py`

This project serves as a synthesis of Module 2. It takes raw user input to generate a formatted financial report, calculating daily budgets and savings distributions using floating-point arithmetic and modulo operators.

---

## 🛠️ Key Technical Implementations

### 1. The "Security" Literals
I moved beyond standard integers to master **Alternative Bases**. 
* **Hexadecimal:** Essential for representing MAC addresses and memory offsets.
* **Octal:** Crucial for understanding Linux file system permissions (e.g., `0o755`).

### 2. Computational Efficiency
Implemented **Shortcut Operators** (`+=`, `-=`). This demonstrates a transition toward PEP 8 "Clean Code" standards, reducing verbosity in the source code.

### 3. Data Integrity
Focus on **Safe Casting**. By wrapping inputs in `try-except` blocks or specific `float()` calls, I ensured that the program maintains integrity even when handling unpredictable user data.

---

## 📈 Learning Outcomes
* **Modularization:** Developed the ability to split a large curriculum into testable, isolated files.
* **Documentation:** Mastered the use of comments to make code "Audit-Ready" for academic reviews.
* **Precision:** Gained a deep understanding of how Python stores data in memory versus how it displays to the user.

---
**Current Status:** `Module-02-COMPLETE`  
**Next Objective:** `Module-03: Control Flow & Logic`

*Maintained by [@byaman-dev](https://github.com/byaman-dev) for MEXT Scholarship Portfolio.*
