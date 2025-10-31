import sys
from pathlib import Path
import pytest
import numpy as np

parent_dir = str(Path(__file__).parent.parent)  # Adjust based on your structure
print(parent_dir)
sys.path.insert(0, parent_dir)

from assignment1 import find_period

def test1_find_period(capsys):
    args1  = (9,12)
    args2  = (8,16)
    args3  = (9,13)
    args4  = (7,16)
    args5  = (8,19)

    args = [args1, args2, args3, args4, args5]
    
    results = ["""When L =  9.0 m, T = 6.0 s
When L = 10.0 m, T = 6.3 s
When L = 11.0 m, T = 6.7 s
When L = 12.0 m, T = 6.9 s
""",
        """When L =  8.0 m, T = 5.7 s
When L =  9.0 m, T = 6.0 s
When L = 10.0 m, T = 6.3 s
When L = 11.0 m, T = 6.7 s
When L = 12.0 m, T = 6.9 s
When L = 13.0 m, T = 7.2 s
When L = 14.0 m, T = 7.5 s
When L = 15.0 m, T = 7.8 s
When L = 16.0 m, T = 8.0 s
""",
        """When L =  9.0 m, T = 6.0 s
When L = 10.0 m, T = 6.3 s
When L = 11.0 m, T = 6.7 s
When L = 12.0 m, T = 6.9 s
When L = 13.0 m, T = 7.2 s
""",
"""When L =  7.0 m, T = 5.3 s
When L =  8.0 m, T = 5.7 s
When L =  9.0 m, T = 6.0 s
When L = 10.0 m, T = 6.3 s
When L = 11.0 m, T = 6.7 s
When L = 12.0 m, T = 6.9 s
When L = 13.0 m, T = 7.2 s
When L = 14.0 m, T = 7.5 s
When L = 15.0 m, T = 7.8 s
When L = 16.0 m, T = 8.0 s
""",
"""When L =  8.0 m, T = 5.7 s
When L =  9.0 m, T = 6.0 s
When L = 10.0 m, T = 6.3 s
When L = 11.0 m, T = 6.7 s
When L = 12.0 m, T = 6.9 s
When L = 13.0 m, T = 7.2 s
When L = 14.0 m, T = 7.5 s
When L = 15.0 m, T = 7.8 s
When L = 16.0 m, T = 8.0 s
When L = 17.0 m, T = 8.3 s
When L = 18.0 m, T = 8.5 s
When L = 19.0 m, T = 8.7 s
"""
    ]

    for i in range(len(args)):
        find_period(args[i][0], args[i][1])
        captured = capsys.readouterr()
        
        assert captured.out == results[i]


def test2_find_period():
    args1  = (9,12)
    args2  = (8,16)
    args3  = (9,13)
    args4  = (7,16)
    args5  = (8,19)

    args = [args1, args2, args3, args4, args5]

    results = [[6.018200042131942, 6.9492188287237875],
               [5.67401341377155, 8.02426672284259],
               [6.018200042131942, 7.232976279302086],
               [5.307553550573187, 8.02426672284259],
               [5.67401341377155, 8.744241935221787]]

    for i in range(len(args)):
        output = find_period(args[i][0], args[i][1])

        assert output[0] == results[i][0]
        assert output[1] == results[i][1]

"""
@pytest.fixture
def get_results():
    num_arr = np.loadtxt("tests/num_arr.csv", delimiter=",")
    return num_arr

def test_values_arr(get_results):
    num_arr = get_results
    num_arr = np.int64(num_arr)
    
    for i in num_arr:
        test_a = np.int64(np.loadtxt("tests/test_a"+str(i)+".csv", delimiter=","))
        test_b = np.int64(np.loadtxt("tests/test_b"+str(i)+".csv", delimiter=","))
        true_res = np.int64(np.loadtxt("tests/true_res"+str(i)+".csv", delimiter=","))
        res = find_circumference(test_a, test_b)

        assert res.all() == true_res.all()
"""
