import lans
import io
import numpy as np

def test_read_energy_read():
    '''Tests if the function reads and returns for given input file'''

    test_file = '''
    #test input energy
    #x energy
    0   -2
    1   -1
    2   0
    3   0
    4   3

    '''

    test_file = io.StringIO(test_string)
    pos, energy = lans.read_energy(test_file)
    assert np.isclose(pos, [0, 1, 2, 3, 4])
    assert np.isclose(energy, [-2, -1, 0, 0, 3])
    