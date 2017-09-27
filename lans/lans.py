import argparse
import numpy as np
import matplotlib.pyplot as plt

#defaults
ENERGY = r'C:\Users\Eric\CHE477\Langevin\lans\tests\potential_example.txt'
POSITION =1.0
VELOCITY = 0.0
TEMPERATURE = 100.0
DAMPING = 1.0
TIMESTEP = 0.1
TOTALTIME = 100.0




def get_arguments():
    '''Get arguments from command line'''

    parser = argparse.ArgumentParser(description='Langevin Dynamics Simulator')
    parser.add_argument('--energy', type=str, default=ENERGY, help='File of Potential Energy')
    parser.add_argument('--position', type=float, default=POSITION, help='Initial position')
    parser.add_argument('--velocity', type=float, default=VELOCITY, help='Initial velocity')
    parser.add_argument('--temperature', type=float, default=TEMPERATURE, help='Temperature')
    parser.add_argument('--damping', type=float, default=DAMPING, help='Damping coefficient')
    parser.add_argument('--timestep', type=float, default=TIMESTEP, help='Time step')
    parser.add_argument('--totaltime', type=float, default=TOTALTIME, help='Total time')

    return parser.parse_args()


def read_energy(input_file,plot=False):
    '''Reads in the energy file and returns the data as series of lists''' 

    with open(input_file, 'r') as f:
        print('Reading input from file:', input_file)
        line_num = 0
        idx, pos, pot, force = [], [], [], []
        for line in f.readlines():
            line_num += 1
            if line[0] != '#':
                new_data = line.split()
                if len(new_data) == 4:
                    idx.append(int(new_data[0]))
                    pos.append(float(new_data[1]))
                    pot.append(float(new_data[2]))
                    force.append(float(new_data[3]))
                else:
                    print('Bad data in line', line_num)

    assert pos == sorted(pos), "Unsorted positions in Potential File"

    if plot==True:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax2 = ax.twinx()

        l1 = ax.plot(pos, pot, 'b', label='potential')
        l2 = ax2.plot(pos, force, 'g', label='force')

        ax.set_title('Potential Energy Profile')
        ax.set_xlabel('Position')
        ax.set_ylabel('Potential')
        ax2.set_ylabel('Force')

        lns = l1+l2
        labs = [l.get_label() for l in lns]
        ax.legend(lns, labs, loc=3)

        plt.show()


    return idx, pos, pot, force



def write_output(output_file, index, time, position, velocity):
    '''Writes an output file'''

    with open(output_file,'w') as f:
        print('Writing output data to file:', output_file)
        line_num = 0
        for line in range(len(index)):
            f.write('{0} {1:0.06f} {2:0.06f} {3:0.06f}\n'.format(index[line], time[line], position[line], velocity[line])) 

def lookup(x,pos,pot,force):
    '''Gives potential and force for a position. Interpolates if necessary'''
    
    x = float(x)
    ux = np.interp(x,pos,pot)
    fx = np.interp(x,pos,force)
    return ux, fx

def step(xi,vi,pos,pot,force,args):
    '''Calculate one timestep for x and v using Euler's Method'''

    drag = -1*args.damping*vi
    solvent = np.random.normal(0, 2*args.temperature*args.damping)
    _, fpotential = lookup(xi, pos, pot, force)

    dvdt = drag + solvent + fpotential
    vj = vi + dvdt*args.timestep
    xj = xi + vj*args.timestep
    return xj,vj

def run(args,plot=False):
    '''Runs all steps of the simulation'''

    iters = int(args.totaltime / args.timestep)
    idx, pos, pot, force = read_energy(args.energy, plot)

    xi,vi = args.position, args.velocity
    x,v = [xi],[vi]
    for s in range(iters):
        xi,vi = step(xi,vi,pos,pot,force,args)
        x.append(xi)
        v.append(vi)
        #print(xi,vi)

    if plot==True:
        fig = plt.figure()

        ax = fig.add_subplot(111)
        ax2 = ax.twinx()

        time = np.linspace(0, args.totaltime, len(x))
        l1 = ax.plot(time, x, 'b', label='position')
        l2 = ax2.plot(time, v, 'g', label='velocity')

        ax.set_title('Trajectory')
        ax.set_xlabel('Time')
        ax.set_ylabel('Position')
        ax2.set_ylabel('Velocity')

        lns = l1+l2
        labs = [l.get_label() for l in lns]
        ax.legend(lns, labs, loc=3)

        plt.show()


    return x,v



def start():
    print('STARTING...')
    
    sv = SimVis()
    start_server(sv)
    asyncio.ensure_future(main(sv))

    


def main():
    args = get_arguments()
    print(args)
    run(args,plot=True)

if __name__ == '__main__':
    main()


