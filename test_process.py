import pytest 
from process import process

@pytest.mark.state
@pytest.mark.parametrize(
    "values, expected", 
    [
        ([2], ["positivo", "par"])
    ],
    ids = ["CP1_A"],
)

def test_statement_coverage(values, expected):
    assert process(values) == expected