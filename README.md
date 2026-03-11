# Student Marks Management System

A Python-based application for managing student academic records, featuring persistent storage and automated reporting.

## 🚀 Features

* [cite_start]**Data Persistence**: Uses a text-based database (`students.txt`) to store records[cite: 3].
* [cite_start]**Input Validation**: Uses `assert` to verify Student IDs [cite: 5] [cite_start]and a custom `InvalidMarksError` for scores[cite: 4, 6].
* [cite_start]**Recursive Logic**: Calculates total marks using a recursive function `calculate_average_recursive`[cite: 9].
* [cite_start]**Functional Programming**: Uses **Lambda expressions** to find the highest and lowest student averages[cite: 9, 10].
* [cite_start]**Reporting**: Generates a `summary_report.txt` with calculated averages and letter grades[cite: 1, 10].

## 📂 Project Structure

* **main.py**: The entry point of the application containing the menu loop.
* [cite_start]**utils.py**: The helper module containing all validation, file handling, and calculation logic[cite: 4].
* [cite_start]**students.txt**: The flat-file database for student records[cite: 3].

## 🛠️ Installation & Usage

### 1. Prerequisites
Ensure you have **Python 3.x** installed on your system.

### 2. Setup
Clone the repository and navigate to the project folder:
```bash
git clone [https://github.com/your-username/student-management-system.git](https://github.com/your-username/student-management-system.git)
cd student-management-system
