# Skip existing rules when importing without overwrite

## Summary
- detection_rules now checks for rule existence before import and skips them when `--overwrite` isn't provided

## Implementation
- added `RuleResource.get` helper using `/api/detection_engine/rules` to fetch by `rule_id`
- `kibana import-rules` omits existing rules from the import payload and reports them as skipped
