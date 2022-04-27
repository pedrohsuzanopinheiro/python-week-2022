from beerlog.cli import main
from typer.testing import CliRunner

runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Skol", "Korn Pale Ale", "--flavor=1", "--image=1", "--cost=1"]
    )
    assert result.exit_code == 0
    assert "Beer added" in result.stdout
