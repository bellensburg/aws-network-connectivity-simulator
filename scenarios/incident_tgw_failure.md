# Incident: TGW Routing Failure

## Problem
Service in VPC-A cannot reach backend in VPC-B.

## Investigation Steps
1. Checked subnet route table → TGW route exists ✅
2. Checked TGW attachments → both VPCs attached ✅
3. Checked TGW route table → missing destination ❌

## Root Cause
Transit Gateway route table was not propagating the destination CIDR.

## Fix
Added correct route to TGW route table.

## Prevention
- Implement automated validation of TGW routes
- Monitor route propagation changes
``
