# aws-network-logic-python

AWS Network Logic (Python)
This repository contains small Python utilities that simulate AWS‑style network reasoning.

The goal is to demonstrate the ability to:

- parse AWS‑like JSON

- find objects by ID

- evaluate routing logic

- simulate Transit Gateway reachability

- write clean, testable Python functions


These patterns match real AWS networking tasks such as:

- checking if two subnets can communicate

- determining TGW attachment relationships

- evaluating route table entries

- validating network paths



Contents
data/sample_topology.json — Example AWS‑style topology

- src/find_by_id.py — Utility to find objects in lists

- src/reachability.py — Logic to determine subnet‑to‑subnet reachability

- src/tgw_logic.py — Transit Gateway attachment evaluation



Skills Demonstrated
- Python (loops, conditions, dicts, lists)

- JSON parsing

- AWS networking concepts (VPC, Subnets, TGW, Route Tables)

- Network automation mindset

- Clean code structure



How to run:
- python3 src/reachability.py
