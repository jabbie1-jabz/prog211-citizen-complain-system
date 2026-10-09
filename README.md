# PROG211 – Citizen Complaint System

## Project overview
A Python console application for the PROG211 Object-Oriented Programming 1 individual assignment. It represents a government/public-service process for recording and tracking community complaints.

## Assignment concepts demonstrated
- **Classes and objects:** `Citizen` and `Complaint`.
- **Attributes:** citizen ID, name, ward, complaint category, description, reference number, and status.
- **Object interaction:** a Complaint object contains a Citizen object.
- **Python data structure:** a list named `complaints` stores Complaint objects.
- **Instance methods:** `display()` and `update_status()`.
- **Class method:** `Complaint.total_complaints()`.
- **Menu-driven program:** submit, view, search, update status, and summary.

## Features
1. Submit a complaint.
2. View all complaints.
3. Search by reference number.
4. Update status to Pending, In Progress, or Resolved.
5. View a summary by status.
6. Basic validation of required input and reference numbers.

## Requirements and running
Python 3 is required; no external packages are needed.
1. Open a terminal in the folder containing the program.
2. Run `python citizen_complaint_system.py` (Windows users can run `py citizen_complaint_system.py`).
3. Select a menu option.

Two demonstration complaints load when the program starts. Records are kept in memory only and will not persist after the program closes.

## Digital Public Goods considerations
The prototype uses plain-language prompts, a reusable structure, and sample data. It is an educational assignment, not a production government service and has not been independently certified as a Digital Public Good. Use fictional data when testing.

## Submission checklist
- [ ] Include the Python source code.
- [ ] Include this README.
- [ ] Capture genuine screenshots of the program running on your computer.
- [ ] Include/print the written documentation and repository URL as directed by the assignment brief.
- [ ] Invite the lecturer as a repository collaborator if required by the brief.
- [ ] Do not upload passwords, tokens, or unnecessary personal information.

Student Name: [Insert Student Name]  
Student ID: [Insert Student ID]  
Module: PROG211 – Object-Oriented Programming 1  
Project: Citizen Complaint System
