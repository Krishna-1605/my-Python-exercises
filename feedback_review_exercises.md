# Python Exercises - Real World Problem Statements

These exercises are designed based on the concepts practiced in this repository. Each project combines multiple Python fundamentals to create practical, real-world applications.

---
these exercises are addressed in project1.py, project2.py, project3.py,

## Exercise 1: Student Grade Management System

### Problem Statement
Build a system that manages student records for a small coaching center.

### Requirements
1. **Store student data** using dictionaries with the following structure:
   ```python
   student = {
       "name": "Krishna",
       "age": 20,
       "subjects": ["math", "python", "science"],
       "marks": {"math": 85, "python": 92, "science": 78}
   }
   ```

2. **Maintain a list** of all students enrolled

3. **Calculate grades** based on average marks:
   - A: >= 90
   - B: >= 75
   - C: >= 60
   - D: >= 40
   - F: < 40

4. **Use sets** to track unique subjects offered across all students

5. **Generate a formatted report card** using string formatting (f-strings)

### Features to Implement
- [ ] Add a new student
- [ ] Update student marks
- [ ] Calculate average and assign grade
- [ ] Display all students with their grades
- [ ] Show unique subjects offered
- [ ] Generate individual report card

### Concepts Used
| File Reference | Concept |
|----------------|---------|
| `dictionaries.py` | Storing student data |
| `python lists.py` | Managing student list |
| `if, elif, else statements.py` | Grade calculation |
| `loops.py` | Iterating through records |
| `sets.py` | Tracking unique subjects |
| `strings.py` | Report formatting |

### Sample Output
```
========== REPORT CARD ==========
Name: Krishna Nagini
Age: 20
---------------------------------
Subject         Marks
---------------------------------
Math            85
Python          92
Science         78
---------------------------------
Average: 85.0
Grade: B
=================================
```

---

## Exercise 2: Personal Expense Tracker

### Problem Statement
Create an expense tracking application that helps users manage their monthly budget.

### Requirements
1. **Store expenses as tuples** (immutable records):
   ```python
   expense = ("2025-01-15", "food", 250.50, "Lunch at restaurant")
   ```

2. **Categorize expenses** using a dictionary:
   ```python
   categories = {
       "food": [],
       "travel": [],
       "utilities": [],
       "entertainment": [],
       "other": []
   }
   ```

3. **Use lists** to maintain expense history

4. **Apply operators** to calculate:
   - Total spent
   - Category-wise totals
   - Budget remaining
   - Average daily expense

5. **Boolean conditions** to trigger alerts:
   - Warn if spending > 80% of budget
   - Alert if over budget

6. **Type casting** when reading user inputs

### Features to Implement
- [ ] Set monthly budget
- [ ] Add new expense with category
- [ ] View expenses by category
- [ ] Calculate total spent and remaining budget
- [ ] Show spending warnings
- [ ] Display expense summary

### Concepts Used
| File Reference | Concept |
|----------------|---------|
| `tuple.py` | Storing expense records |
| `dictionaries.py` | Categorizing expenses |
| `python lists.py` | Expense history |
| `operators.py` | Calculations |
| `boolean.py` | Budget alerts |
| `casting.py` | Input handling |
| `numbers.py` | Financial calculations |

### Sample Output
```
========== EXPENSE TRACKER ==========
Monthly Budget: ₹15,000

Category-wise Spending:
---------------------------------
Food:           ₹4,500 (30%)
Travel:         ₹2,000 (13%)
Utilities:      ₹3,500 (23%)
Entertainment:  ₹1,500 (10%)
---------------------------------
Total Spent:    ₹11,500
Remaining:      ₹3,500

⚠️ Warning: You've spent 77% of your budget!
=====================================
```

---

## Exercise 3: Event Calendar & Reminder System

### Problem Statement
Build a simple event management system that helps users organize and track their events.

### Requirements
1. **Use the calendar module** to display monthly calendars

2. **Store events in a dictionary** with dates as keys:
   ```python
   events = {
       "2025-01-20": [
           {"title": "Team Meeting", "time": "10:00", "priority": "high"},
           {"title": "Lunch with friend", "time": "13:00", "priority": "low"}
       ],
       "2025-01-25": [
           {"title": "Project Deadline", "time": "18:00", "priority": "high"}
       ]
   }
   ```

3. **Use sets** to track unique event types/categories

4. **Apply string operations** to:
   - Search events by keyword
   - Filter events by title

5. **Use loops** to list and process events

6. **Use if/elif/else** to:
   - Prioritize events (high, medium, low)
   - Show different alert levels

### Features to Implement
- [ ] Display monthly calendar
- [ ] Add event to a specific date
- [ ] View events for a specific date
- [ ] List all upcoming events (sorted by date)
- [ ] Search events by keyword
- [ ] Show high-priority events count
- [ ] Validate dates (check leap year, valid day)

### Concepts Used
| File Reference | Concept |
|----------------|---------|
| `calender.py` | Calendar display |
| `dictionaries.py` | Event storage |
| `sets.py` | Unique categories |
| `strings.py` | Search and formatting |
| `loops.py` | Event iteration |
| `if, elif, else statements.py` | Priority handling |

### Sample Output
```
========== JANUARY 2025 ==========
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
==================================

📅 Events for 2025-01-20:
---------------------------------
🔴 [HIGH] 10:00 - Team Meeting
🟢 [LOW]  13:00 - Lunch with friend
---------------------------------

📊 This Week Summary:
- Total Events: 5
- High Priority: 2
- Upcoming Today: 1
==================================
```

---

## Getting Started

### Recommended Order
1. **Start with Exercise 1** - It uses the most fundamental concepts
2. **Move to Exercise 2** - Adds financial calculations and type handling
3. **Complete Exercise 3** - Integrates external module (calendar) with all concepts

### Tips
- Start with basic functionality, then add features
- Test each feature before moving to the next
- Use comments to explain your logic
- Break down complex features into smaller functions

### File Naming Suggestions
```
exercises/
├── student_grade_system.py
├── expense_tracker.py
└── event_calendar.py
```

---

## Concepts Checklist

Mark the concepts as you use them in your projects:

- [ ] Variables and Data Types
- [ ] Numbers and Operators
- [ ] Strings and String Methods
- [ ] Boolean and Conditions
- [ ] If, Elif, Else Statements
- [ ] Lists and List Methods
- [ ] Tuples
- [ ] Dictionaries
- [ ] Sets
- [ ] Loops (for, while)
- [ ] Functions
- [ ] Type Casting
- [ ] Identity Operators

---

*Created on: December 14, 2025*
