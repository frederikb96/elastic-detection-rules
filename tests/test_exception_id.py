from pathlib import Path

import pytoml

from detection_rules.rule import TOMLRule, TOMLRuleContents


def make_test_rule(tmp_path: Path) -> TOMLRule:
    data = {
        "metadata": {
            "creation_date": "2024/01/01",
            "updated_date": "2024/01/01",
            "maturity": "development",
        },
        "rule": {
            "author": ["Elastic"],
            "description": "test",
            "rule_id": "00000000-0000-0000-0000-000000000000",
            "risk_score": 21,
            "severity": "low",
            "type": "query",
            "language": "kuery",
            "query": "process.name: test",
            "name": "Test Rule",
            "exceptions_list": [
                {"id": "abc", "list_id": "abc", "namespace_type": "single", "type": "detection"}
            ],
        },
    }
    contents = TOMLRuleContents.from_dict(data)
    path = tmp_path / "rule.toml"
    return TOMLRule(contents=contents, path=path)


def test_strip_exception_id(tmp_path: Path):
    rule = make_test_rule(tmp_path)
    rule.save_toml(strip_exception_list_id=True)
    loaded = pytoml.load((tmp_path / "rule.toml").open())
    exc = loaded["rule"]["exceptions_list"][0]
    assert "id" not in exc
