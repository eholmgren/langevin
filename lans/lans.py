import argparse

#defaults
ENERGY = r'.\tests\potential_example.txt'
POSITION = 0.0
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


def read_energy(input_file):
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
                    idx.append(new_data[0])
                    pos.append(new_data[1])
                    pot.append(new_data[2])
                    force.append(new_data[3])
                else:
                    print('Bad data in line', line_num)

    return idx, pos, pot, force

def write_output(output_file, index, time, position, velocity):
    '''Writes an output file'''
    with open(output_file,'w') as f:
        print('Writing output data to file:', output_file)
        line_num = 0
        for line in range(len(index)):
            f.write('{0} {1:0.06f} {2:0.06f} {3:0.06f}\n'.format(index[line], time[line], position[line], velocity[line])) #TODO fancier float format

def main():
    args = get_arguments()
    idx, pos, pot, force = read_energy(args.energy)
    print(args)
    print(pos[5])

if __name__ == '__main__':
    main()


