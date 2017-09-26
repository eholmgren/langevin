import lans
import io
import numpy as np
import unittest

def bad_test_read_energy_read():
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

    test_file = r'C:\Users\Eric\CHE477\Langevin\lans\tests\potential_example.txt'
    idx, pos, pot, force = lans.read_energy(test_file)

def test_read_energy_plot():

    test_file = r'C:\Users\Eric\CHE477\Langevin\lans\tests\potential_example.txt'
    idx, pos, pot, force = lans.read_energy(test_file,plot=True)

def test_read_energy_sorted():
    '''Asserts that an error is thrown unless the positions are ordered'''
    
    test_file = r'C:\Users\Eric\CHE477\Langevin\lans\tests\potential_unsorted.txt'

    #idx, pos, pot, force = lans.read_energy(test_file)
    #assertRaises(AssertionError, lans.read_energy, test_file) #TODO this doesn't work right

    #with assertRaises(AssertionError):
    #    lans.read_energy(test_file)

def test_write_output_format():
    '''Tests if the function can write up a mock file'''

    output_file = r'C:\Users\Eric\CHE477\Langevin\lans\tests\output_example.txt'
    index = [1, 2, 3, 4, 5]
    time = [0, .1, .2, .3, .4]
    position = [0.04, -1, 9.33, .00000002, 0]
    velocity = [0.6, -.34, -0.12, 7.7, 0.0]

    lans.write_output(output_file, index, time, position, velocity)

    with open(output_file,'r') as f:
        attempt = f.read()
    with open(r'C:\Users\Eric\CHE477\Langevin\lans\tests\output_correct_example.txt','r') as g:
        correct = g.read()

    assert(attempt==correct)


def test_lookup_interpolate():
    '''Tests if the function can read out an interpolated potential and force from the tabulated potential file'''
    positions = [-1.0,0,.1,.25,2.5]
    pos = [0.0,0.1,0.2,0.3,0.4,0.5]
    pot = [1.0,5.1,.36,0.0,-0.4,-0.4]
    force = [0.0,0.1,1.0,-0.5,-0.4,3.14]
    ux_corr = [1.0, 1.0, 5.1, 0.18, -0.4]
    fx_corr = [0.0, 0.0, 0.1, 0.25, 3.14]
    itr = 0
    for i in positions:
        ux, fx = lans.lookup(i, pos, pot, force)
        assert (np.isclose(ux,ux_corr[itr]))
        assert (np.isclose(fx,fx_corr[itr]))
        itr+=1

def test_step_xxxx(): #TODO have this actually test something
    class args:
        def __init__():
            pass

        timestep = .1
        totaltime = 100.0
        energy = r'C:\Users\Eric\CHE477\Langevin\lans\tests\potential_example.txt'
        position = 1.0
        velocity = 0.0
        damping = 1.0
        temperature = 0
    xi = 0.0
    vi = 0.0
    idx,pos,pot,force = lans.read_energy(args.energy)
    a,b=lans.step(xi,vi,pos,pot,force,args)
    print(a,b)
    #assert(np.isclose(a,6))

test_step_xxxx()

def test_run_iters():
    class args:
        def __init__():
            pass

        timestep = .1
        totaltime = 100.0
        energy = r'C:\Users\Eric\CHE477\Langevin\lans\tests\potential_example.txt'
        position = 1.0
        velocity = 0.0
        damping = 1.0
        temperature = 100.0
        
    xi,vi = lans.run(args)
    assert len(xi) == 1001
