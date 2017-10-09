import lans
import io
import numpy as np
from os import path
test_dir = path.join(path.dirname(__file__), '../tests')

def test_read_energy_file():
    '''Tests if the function can read mock file'''

    test_file = test_dir+r'\potential_example.txt'
    idx, pos, pot, force = lans.read_energy(test_file)

def test_read_energy_plot():
    '''Tests if the function can plot energy'''

    test_file = test_dir+r'\potential_example.txt'
    idx, pos, pot, force = lans.read_energy(test_file,plot=True)

def test_read_energy_sorted():
    '''Asserts that an error is thrown unless the positions are ordered'''
    
    test_file = test_dir+r'\potential_unsorted.txt'

    #idx, pos, pot, force = lans.read_energy(test_file)
    #assertRaises(AssertionError, lans.read_energy, test_file) #TODO this doesn't work right. How do I check if code raises assertion error when it should?

def test_write_output_format():
    '''Tests if the function can write up a mock file'''

    output_file = test_dir+r'\output_example.txt'
    index = [1, 2, 3, 4, 5]
    time = [0, .1, .2, .3, .4]
    position = [0.04, -1, 9.33, .00000002, 0]
    velocity = [0.6, -.34, -0.12, 7.7, 0.0]

    lans.write_output(output_file, index, time, position, velocity)

    with open(output_file,'r') as f:
        attempt = f.read()
    with open(test_dir+r'\output_correct_example.txt','r') as g:
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

def test_step_calculate():
    '''Tests whether the velocity of a single timestep is calculated correctly'''
    
    class args:
        def __init__():
            pass

        timestep = .1
        totaltime = 100.0
        energy = test_dir+r'\potential_example.txt'
        position = 1.0
        velocity = 0.0
        damping = 0.0
        temperature = 0.0

    xi = 0.0
    vi = 0.1
    idx,pos,pot,force = lans.read_energy(args.energy)
    a,b=lans.step(xi,vi,pos,pot,force,args)
    assert(np.isclose(a,0.01)) #checks if position is correct
    assert(np.isclose(b,0.0886525)) #checks if velocity is correct in this case

def test_run_iters():
    '''Tests whether the simulation runs the correct number of iterations based on the time parameters'''

    class args:
        def __init__():
            pass

        timestep = .1
        totaltime = 100.0
        energy = test_dir+r'\potential_example.txt'
        position = 1.0
        velocity = 0.0
        damping = 1.0
        temperature = 100.0
        output = test_dir+r'\output_example.txt'
        
    xi,vi = lans.run(args)
    assert len(xi) == 1001

def test_run_plot():
    '''Tests whether the trajectory can be plotted'''

    class args:
        def __init__():
            pass

        timestep = .1
        totaltime = 100.0
        energy = test_dir+r'\potential_example.txt'
        position = 1.0
        velocity = 0.0
        damping = 10.0
        temperature = 1.0
        output = test_dir+r'\output_example.txt'
        
    xi,vi = lans.run(args,plot=True)