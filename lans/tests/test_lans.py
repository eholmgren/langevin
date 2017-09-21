import lans
import io
import numpy as np

def test_read_energy_read():
    '''Tests if the function reads and returns for given input file'''

    test_string = '''
    #test input energy
    #i x U(x) F(x)
    0 -2 3 5
    1 -1 .234 -1
    2 0 1.5 -.3
    3 0 2 -5
    4 3 1 1
    '''

    test_file = io.StringIO(test_string) #something funky with this line, fails test
    idx, pos, pot, force = lans.read_energy(test_file)
    assert np.isclose(idx, [0, 1, 2, 3, 4])
    assert np.isclose(pos, [-2, -1, 0, 0, 3])
    assert np.isclose(pot, [3, .234, 1.5, 2, 1])
    assert np.isclose(force, [5, -1, -.3, -5, 1])

def test_read_energy_file():
    '''Tests if the function can read mock file'''

    test_file = r'.\lans\tests\potential_example.txt'
    idx, pos, pot, force = lans.read_energy(test_file)

def test_write_output_format():
    '''Tests if the function can write up a mock file'''

    output_file = r'.\lans\tests\output_example.txt'
    index = [1, 2, 3, 4, 5]
    time = [0, .1, .2, .3, .4]
    position = [0.04, -1, 9.33, .00000002, 0]
    velocity = [0.6, -.34, -0.12, 7.7, 0.0]

    lans.write_output(output_file, index, time, position, velocity)

    with open(output_file,'r') as f:
        attempt = f.read()
    with open(r'.\lans\tests\output_correct_example.txt','r') as g:
        correct = g.read()

    assert(attempt==correct)


    