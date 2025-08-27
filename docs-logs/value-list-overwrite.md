Bug Fix: Correct value list overwrite behavior and improve error handling.

Previously `kibana import-rules --overwrite-value-lists` attempted to delete
and recreate value lists before importing their items. When a list was in use,
Kibana rejected the delete request, causing the import to append duplicate
items.

Implementation:
- Introduced `clear_list_items` to remove existing list items without deleting
  the list.
- Simplified value list, exception list and timeline template helpers to rely
  on Kibana's native error responses.
- Updated `kibana import-rules` to collect and display errors for list
  operations while continuing with the import.
