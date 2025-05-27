<div style="text-align: center;">
  
# WARP Production Optimization
</div>

This repository contains all materials and code required to optimize the WARP Shoe Company’s production schedule. The project demonstrates:

- **Data Extraction** from Microsoft Access (*.mdb) databases (via Python pyodbc).
- **Mathematical Modeling** of the production problem in AMPL.
- **Optimization** using the Gurobi solver to maximize profits while respecting constraints.
- **Scenario Investigations**, such as adjusting machine availability, raw material budgets, or adding warehouse space.

## Project Organization

```
warp-production-optimization/  
├── .gitignore  
├── README.md  
├── requirements.txt       
├── reports/                 
│   └── Case Study Report.pdf  
├── datax
│   ├── processed/
│   └── raw/      
│       └── warp_demands.mdb  
│ 
└── src/  
    ├── __init__.py  
    ├── extract_demand.py  
    └── model/           
        ├── ampl.mod  
        ├── ampl.dat   
        └── ampl.run  
```

## Table of Contents
- [Project Overview](#project-overview)
- [Dependencies and Setup](#dependencies-and-setup)
- [AMPL Model Details](#ampl-model-details)
- [Troubleshooting](#troubleshooting)
- [Acknowledgments](#acknowledgments)

## Project Overview
In February 2006, a major competitor of the WARP Shoe Company went bankrupt, significantly increasing the demand for WARP’s shoes. This project develops and solves a Mixed-Integer Programming (MIP) model to help WARP:

- **Forecast Demand** by extracting and averaging historical data for February, then scaling it.
- **Maximize Profit** by determining optimal production quantities of different shoe types while accounting for raw material costs, machine constraints, warehouse capacities, labor costs, and unmet demand penalties.
- **Investigate Scenarios** such as limited machine hours, additional warehouse space, and increased budgets.

**Key Features:**
- **Data Extraction:** Python scripts using pyodbc to pull data from .mdb files.
- **AMPL model** (`.mod` + `.dat` + `.run` file) defining sets, parameters, variables, constraints, and the objective function.
- **Solver:** Gurobi solver integration for efficiently solving the IP model. 
- **Analysis:** Slack & Shadow Price Analysis and “What-If” scenario explorations.

## Dependencies and Setup

**1. Python**
- ```pyodbc``` to connect to ```.mdb``` files.
- ```pandas``` for data manipulation.

**2. AMPL**
- Obtain and install AMPL (with a valid license).
- Ensure AMPL is accessbile from your command line or integrated into your workflow.

**3. Gurobi Solver**
- Install Gurobi and confirm you have a valid license.
- Make sure ```gurobi.sh``` (on Linux/Unix) or the Gurobi bin directory (Windows) is in your PATH so AMPL can invoke it.

**4. Microsoft Access ODBC Driver (for Windows**)
- This is required for reading from ```.mdb```.

## AMPL Model Details
We needed rapid prototyping and focus  on pure optimization modeling, therefore a language like AMPL was ideal. 

The AMPL model is found in files such as:
- ```ampl.mod```: Contains sets, paramters, decision variables, objective, and constraints:
- ```ampl.dat```: Specifies how AMPL reads data from tables in WARP2011W.mdb
- ```ampl.run```: A script to reset, load the modal and data, set solve to gurobi, solve and display results.

## Troubleshooting

**ODBC Connection Issues**
- Confirm the correct DSN or connection string in ```.dat``` or Python.
- Ensure you have the right driver (e.g., Microsoft Access Driver (```*.mdb```, ```*.accdb```)) installed.

**AMPL Table Syntax Errors**
- Verify table names and column names match exactly what’s in the Access database.
- AMPL is case-sensitive for some table references.

**Gurobi License Problems**
- Make sure the ```GRB_LICENSE_FILE``` environment variable is set or Gurobi is otherwise activated.

## Acknowledgments
University of Toronto: Original concept, data (```WARP2011W.mdb```) for academic demonstration.

**Contributors:**
- Ahmed Khan