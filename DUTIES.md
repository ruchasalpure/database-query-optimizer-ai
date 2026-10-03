# Duties and Responsibilities for Database Query Optimizer Agent

## Dual-Control Architecture
Maker:
index-synthesizer

Checker:
planner-cost-checker

## Operational Workflow
1. The Maker (index-synthesizer) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (planner-cost-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
