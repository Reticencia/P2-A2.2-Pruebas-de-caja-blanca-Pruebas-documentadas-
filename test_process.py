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


@pytest.mark.branch
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2], ["positivo", "par"]),   # D1=V, D2=V
        ([-3], []),                   # D1=F, D2=F
        ([3], ["positivo"]),          # D1=V, D2=F
        ([-2], ["par"]),              # D1=F, D2=V
        ([], []),                     # el ciclo no entra
    ],
    ids = ["CP2_A", "CP2_B", "CP2_C", "CP2_D", "CP2_E"],
)
def test_branch_coverage(values, expected):
    assert process(values) == expected
