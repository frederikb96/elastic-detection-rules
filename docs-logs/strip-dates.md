# Strip Dates Option

A new `strip_dates` flag was added to the rule export workflow. When enabled via the
`--strip-dates` command line option or the `strip_dates` field in `_config.yaml`,
`creation_date` and `updated_date` are removed before writing the rule TOML.
This helps avoid noisy diffs when exporting rules from Kibana and re-importing
them across clusters.

