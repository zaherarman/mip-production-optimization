set Y;
set M;

# Sets
set I;  # Raw materials
set J;  # Products
set N;  # Warehouses
set K;  # Machines

# Parameters
param Demand{J};   # Demand parameter indexed by product and month
param s{J};          # Sales price per product
param d{J};          # Demand for each product
param rmc{I};        # Cost of raw material

param avgdur{J,K} default 0;

param rmq{I};        # Available raw materials
param opm{K};        # Machine operating cost
param capw{N};       # Warehouse capacity
param opcw{N};       # Warehouse operating cost
param rm{I,J} default 0;

# Decision Variables
# var m{K} binary;        # Machine usage
var w{N} binary;        # Warehouse usage
var a{J} >= 0;  # Number of products to produce
# var amtw{N} >= 0;       # Amount stored in warehouse

maximize z:
    sum {j in J} s[j] * a[j] -
    sum {i in I, j in J} rmc[i] * rm[i,j] * a[j]
    - sum {k in K} sum{j in J} opm[k] * avgdur[j,k]*a[j]*1/60 -
    25 * sum{j in J} sum {k in K} 1/3600*avgdur[j,k]*a[j]
    - sum {n in N} opcw[n]*w[n] - 10 * sum {j in J} ( 2*d[j] - a[j] );

#Constraints
# 1) raw material constraint
subject to cons1: sum{i in I} sum{j in J} rmc[i]*rm[i,j]*a[j] <= 10000000;

# 2) Demand constraint
subject to cons2{j in J}:
    a[j] <= 2*d[j];

# 3) warehouse capacity
subject to cons3:
    sum {j in J} a[j] <= sum{n in N} capw[n]*w[n];

# 4) Raw material availability
subject to cons4 {i in I}:
    sum{j in J} rm[i,j]*a[j] <= rmq[i];

# 5) Machine Operating Time
subject to cons5 {k in K}:
    sum{j in J} avgdur[j,k]*a[j] <= 1209600;