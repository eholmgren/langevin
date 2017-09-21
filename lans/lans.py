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
                print(new_data)
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



