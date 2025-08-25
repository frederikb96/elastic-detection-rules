import click
from click.testing import CliRunner

from detection_rules.cli_utils import multi_collection
from detection_rules.rule_loader import RuleCollection


@click.command()
@multi_collection
def _cmd(rules: RuleCollection) -> None:
    click.echo("|".join(sorted(r.name for r in rules)))


def test_rule_name_exact():
    runner = CliRunner()
    result = runner.invoke(
        _cmd,
        [
            "-d",
            "rules-test/rules",
            "--rule-name",
            "Test01 - Windows Event Log Cleared",
            "--no-tactic-filename",
        ],
    )
    assert result.exit_code == 0
    assert result.output.strip() == "Test01 - Windows Event Log Cleared"


def test_rule_name_wildcard():
    runner = CliRunner()
    result = runner.invoke(
        _cmd,
        [
            "-d",
            "rules-test/rules",
            "--rule-name",
            "test01*cleared",
            "--no-tactic-filename",
        ],
    )
    assert result.exit_code == 0
    assert result.output.strip() == "Test01 - Windows Event Log Cleared"


def test_multiple_rule_name():
    runner = CliRunner()
    result = runner.invoke(
        _cmd,
        [
            "-d",
            "rules-test/rules",
            "--rule-name",
            "Test01*",
            "--rule-name",
            "Test02*",
            "--no-tactic-filename",
        ],
    )
    assert result.exit_code == 0
    names = result.output.strip().split("|")
    assert sorted(names) == [
        "Test01 - Windows Event Log Cleared",
        "Test02 - Windows Event Log Modified",
    ]


def test_rule_name_conflict_with_id():
    runner = CliRunner()
    result = runner.invoke(
        _cmd,
        [
            "-d",
            "rules-test/rules",
            "--rule-name",
            "Test01*",
            "--rule-id",
            "de7a3fda-0ef5-e8a0-ad54-f8e1fd2d1dbf",
            "--no-tactic-filename",
        ],
    )
    assert result.exit_code != 0
    assert "Cannot use --rule-id and --rule-name together" in result.output
