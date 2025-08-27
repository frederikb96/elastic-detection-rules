# Exception list ID handling

## Summary
- ensure rule imports update exception list references with existing IDs
- look up lists using namespace type from the file to avoid duplicates

## Implementation
- `detection_rules/kbwrap.py`
  - fetch existing exception lists with their `namespace_type`
  - update rule and container IDs so rules reference the correct list
