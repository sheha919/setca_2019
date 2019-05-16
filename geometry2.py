#this is my geometry analysis
"""
Functions an d script for geometry analysis
"""
import numpy
import os
import sys
def calculate_distance(atom1,atom2):
    """
    Calculate the distance between two atoms.
    Parameters
    ----------
    atom1:list
        A  list of coordinates[x,y,z]
    atom2:list
        A  list of coordinates[x,y,z]
    Returns
    -------
    bond_length : float
        The distance between atoms
    Examples
    --------
    >>> calculate_distance([0,0,0],[0,0,1])
    1.0
    """
    x_distance=atom1[0]-atom2[0]
    y_distance=atom1[1]-atom2[1]
    z_distance=atom1[2]-atom2[2]
    distance=numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance
def bond_check(bond_distance,minimum_value=0,maximum_value=1.5):
    """
    check if distance is a bond.

    Parameters
    ----------
    atom_distance: float
        The distance between atoms
    minimum_length: float
        The minimum distance for a bond
    maximum_value_length: float
        The maximum distance for a bond
    Returns
    -------
    True if bond
    False if not a bond
    """
    # Check that atom_distance is a file_location
    if not isinstance(bond_distance,float):
        raise TypeError(F'atom_distance must be type float. {bond_distance}')
    if bond_distance>minimum_value and bond_distance<maximum_value:
        return True
    else:
        return False

def open_xyz(filename):
    xyz_file= numpy.genfromtxt(fname=file_location,skip_header=2,dtype='unicode')
    symbols = xyz_file[:,0]
    coordinates =  xyz_file[:,1:]
    coordinates=coordinates.astype(numpy.float)
    return symbols,coord


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise IndexError('No file name given. Script requires an xyz file')

    xyzfilename = sys.argv[1]

    symbols, coord = open_xyz(xyzfilename)

    for numA, atomA in enumerate (coordinates):
        for numB, atomB in enumerate (coordinates):
            if numB< numA:
                distance_AB = calculate_distance(atomA,atomB)
                if bond_check(distance_AB,1.0,1.6) is True:
                    print(F'{symbols[numA]} to {symbols[numB]}: {distance_AB:.3f}')
