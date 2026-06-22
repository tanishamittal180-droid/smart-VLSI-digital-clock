# AI Smart VLSI Digital Clock using Verilog + Icarus Verilog + Streamlit + Machine Learning

## Project Overview

AI Smart VLSI Digital Clock is an advanced digital clock system built using Verilog HDL and simulated using Icarus Verilog and GTKWave. The project integrates a Python-based AI dashboard with machine learning features, real-time alarm configuration, smart recommendations, and interactive controls.

The system combines hardware design concepts with software and AI integration to create an industry-style project suitable for FPGA learning, internships, GitHub portfolios, and placement preparation.

---

## Features

### Core Verilog Features

✔ Digital clock functionality

✔ Hours, Minutes, Seconds counter

✔ Alarm functionality

✔ Multiple alarm support

✔ Stopwatch

✔ Date display

✔ AM/PM mode

✔ 12-hour and 24-hour mode

✔ Buzzer output

✔ Fast simulation mode

✔ Self-checking testbench

---

### AI Features

✔ Smart alarm recommendation using machine learning

✔ Natural language command parsing

Example:

Set alarm at 6:45

Set alarm at 22:30

✔ Usage analytics

✔ Alarm prediction engine

✔ Real-time system monitoring

---

### Dashboard Features

✔ Live digital clock

✔ Real PC time synchronization

✔ Alarm enable/disable

✔ Stopwatch control

✔ Wake-up analytics graph

✔ Alarm notifications

✔ System logs

✔ Simulation status

✔ Interactive UI

---

## Project Architecture

Clock Input

↓

Clock Divider

↓

Time Counter

↓

Date Counter

↓

Multiple Alarm Logic

↓

Stopwatch

↓

Buzzer

↓

Verilog Testbench

↓

Python Backend

↓

AI Prediction Engine

↓

Streamlit Dashboard

---

## Project Structure

VLSI-Digital-Clock-Alarm/

rtl/

├── clk_divider.v

├── time_counter.v

├── alarm_comparator.v

├── multi_alarm.v

├── stopwatch.v

├── buzzer.v

├── date_counter.v

├── top.v

tb/

├── clock_tb.v

interface/

├── dashboard.py

├── backend.py

├── ai_engine.py

waveforms/

reports/

README.rd

---

## Software Requirements

### Hardware Description

* Verilog HDL
* Icarus Verilog
* GTKWave

### Python Libraries

* Streamlit
* Pandas
* Matplotlib
* Scikit-learn
* NumPy

---

## Installation

### Install Icarus Verilog

Windows:

iverilog -V

If not installed:

winget install IcarusVerilog.IcarusVerilog

---

### Install GTKWave

winget install GTKWave.GTKWave

---

### Install Python Packages

pip install streamlit

pip install pandas

pip install matplotlib

pip install scikit-learn

pip install numpy

---

## Running Verilog Simulation

Compile project:

iverilog -o clock rtl/*.v tb/*.v

Run simulation:

vvp clock

Open waveform:

gtkwave clock.vcd

---

## Running Dashboard

Go to interface folder:

cd interface

Run dashboard:

streamlit run dashboard.py

---

## Dashboard Usage

### Set Alarm

Method 1:

Use sidebar controls

Alarm Hour = 6

Alarm Minute = 45

Enable Alarm = True

Method 2:

Use smart command:

Set alarm at 6:45

---

## Expected Outputs

Clock Output:

00:00:00

↓

00:00:01

↓

00:00:02

↓

...

Alarm Output:

Alarm Waiting

↓

Alarm Time Match

↓

Alarm Ringing

Stopwatch:

0

↓

1

↓

2

↓

...

---
## Screenshots
<img width="1366" height="768" alt="Screenshot 2026-06-22 105519" src="https://github.com/user-attachments/assets/21881fda-ef88-4e34-afb7-5dfe52c473ca" />
<img width="1366" height="768" alt="Screenshot 2026-06-22 105532" src="https://github.com/user-attachments/assets/5d017973-cef7-4510-a3f4-91606ba24ee5" />
<img width="1366" height="768" alt="Screenshot 2026-06-22 105546" src="https://github.com/user-attachments/assets/f65fc9ba-e572-4d43-a28d-6f0696739726" />
<img width="1366" height="768" alt="Screenshot 2026-06-22 105601" src="https://github.com/user-attachments/assets/e97eeb28-d49f-4264-9724-5c798e9b5b73" />
<img width="1366" height="768" alt="Screenshot 2026-06-22 105508" src="https://github.com/user-attachments/assets/fe12d78a-e639-41b3-964c-ead7959cc840" />

## Applications

* Smart alarm systems
* Embedded systems
* FPGA projects
* VLSI education
* Digital clocks
* Smart assistants
* AI-assisted scheduling systems

---

## Future Enhancements

* Voice assistant integration

* AI schedule planner

* FPGA deployment

* Mobile application integration

* Cloud synchronization

* Email reminders

* Calendar integration

* Face recognition login

---

## Skills Used

Verilog HDL

RTL Design

Icarus Verilog

GTKWave

Python

Machine Learning

Streamlit

Data Visualization

Digital Electronics

VLSI Concepts

---

## Author

Tanisha Mittal

AI Smart VLSI Digital Clock Project

---

## License

This project is intended for educational and learning purposes.
