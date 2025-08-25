# Import rule name flag for `kibana import-rules`

## Summary
Adds a `--rule-name` (`-rn`) option to the `kibana import-rules` command to import only rules whose `rule.name` matches a given pattern. Patterns are case-insensitive and support shell wildcards like `*`. The flag can be repeated to match multiple patterns.

## Implementation details
- Introduced a `filter_by_name` method on `RuleCollection` that compiles glob patterns to regular expressions for efficient matching.
- Updated `kibana import-rules` to accept the new option, reject combinations with `--rule-id`, and filter the loaded rule files using the new helper.
- Documented the option in `CLI.md` and added unit tests verifying name filtering.
