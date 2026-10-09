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


@pytest.mark.path
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2, 2],   ["positivo", "par", "positivo", "par"]),   # A-A
        ([2, 3],   ["positivo", "par", "positivo"]),          # A-B
        ([2, -2],  ["positivo", "par", "par"]),               # A-C
        ([2, -3],  ["positivo", "par"]),                      # A-D
        ([3, 2],   ["positivo", "positivo", "par"]),          # B-A
        ([3, 3],   ["positivo", "positivo"]),                 # B-B
        ([3, -2],  ["positivo", "par"]),                      # B-C
        ([3, -3],  ["positivo"]),                             # B-D
        ([-2, 2],  ["par", "positivo", "par"]),               # C-A
        ([-2, 3],  ["par", "positivo"]),                      # C-B
        ([-2, -2], ["par", "par"]),                           # C-C
        ([-2, -3], ["par"]),                                  # C-D
        ([-3, 2],  ["positivo", "par"]),                      # D-A
        ([-3, 3],  ["positivo"]),                             # D-B
        ([-3, -2], ["par"]),                                  # D-C
        ([-3, -3], []),                                       # D-D
    ],
    ids=[f"CP{i}_{r}" for i, r in enumerate(
        ["A-A", "A-B", "A-C", "A-D", "B-A", "B-B", "B-C", "B-D",
         "C-A", "C-B", "C-C", "C-D", "D-A", "D-B", "D-C", "D-D"], start=1)],
)
def test_path_coverage(values, expected):
    assert process(values) == expected