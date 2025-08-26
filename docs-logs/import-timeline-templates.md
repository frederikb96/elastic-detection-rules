# Import timeline templates

## Summary
- allow `kibana import-rules` to upload timeline templates referenced in rules
- add `--overwrite-timeline-templates` flag to force replacing existing templates

## Implementation
- added `TimelineTemplateResource.get`, `delete`, and `import_template` helpers for `/api/timeline` endpoints
- extended rule import workflow to load template files, skip existing ones unless overwritten, and report missing templates
