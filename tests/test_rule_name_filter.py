from pathlib import Path

from detection_rules.rule_loader import RuleCollection


def test_filter_by_name_patterns() -> None:
    rc = RuleCollection()
    rc.load_files(
        [
            Path("rules-test/rules/test01_windows_event_log_cleared.toml"),
            Path("rules-test/rules/test02_windows_event_log_modified.toml"),
        ]
    )
    filtered = rc.filter_by_name(["Test01*Cleared"])
    assert len(filtered) == 1
    assert next(iter(filtered)).contents.data.name == "Test01 - Windows Event Log Cleared"

    filtered_multi = rc.filter_by_name(["*Cleared", "*Modified"])
    assert len(filtered_multi) == 2
