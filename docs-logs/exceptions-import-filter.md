# Filter exceptions during Kibana import

## Problem and fix

When invoking `python -m detection_rules import-rules --rule-file <file>` the old
implementation uploaded **all** exception lists found in the configured
`rules-test/exceptions` directory. This polluted Kibana with unrelated exceptions
and made it hard to test rules in isolation. The command now analyses the rules
being imported and collects the `list_id` values from their `exceptions_list`
sections. Only exception files containing these list IDs are sent to Kibana.

## Files and program flow

The filtering logic lives in `detection_rules/kbwrap.py` inside the
`kibana_import_rules` function. It iterates over the parsed rules, gathers the
referenced list IDs and filters the loaded exception objects before making the
API request. `detection_rules/misc.py` contains the helper function
`get_kibana_client` which is used for authentication, while
`detection_rules/remote_validation.py` provides a similar helper for remote
validation. These helpers were touched during development but no longer carry any
lint suppressions.
