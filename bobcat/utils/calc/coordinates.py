## coordinate_converter.py contains the code for the coord_converter function. This function allows you to 
## convert the coordinates from J2000 ra and dec in the units of hmsdms to J2000 ra and dec in the units of 
## degrees. 


######
# Import the need libraries and modules for the function to work.
import numpy as np
from astropy.coordinates import SkyCoord 
######


####################
def coord_converter(ra, dec): 
    '''
    Convert J2000 ra and dec with units of hmsdms into J2000 ra and dec with units of degrees.

    Inputs:
        ra = J2000 right ascension, units = hms
        dec = J2000 declination, units = dms 

    Outputs:
        ra = J2000 right ascension, units = degrees
        dec = J2000 declination, units = degrees
    '''

    # Make sure the ra and dec passed to the function are strings, i.e. they're most likely in hmsdms units. 
    # If not raise an error.
    if not isinstance(ra, str) or not isinstance(dec, str):
        raise TypeError("ra and dec must be strings.")
    
    # Try to convert the coordinates into decimal degrees.
    try:
        # Convert the coordinates into degrees.
        coords_arr = SkyCoord(ra, dec)

        # Split the ra and dec and return them.
        ra_deg, dec_deg = np.array([coords_arr.ra.degree, coords_arr.dec.degree]) 
        return ra_deg, dec_deg
    # If something goes wrong in the above code block it is most likely because the ra and dec passed to the 
    # function weren't entered exactly correctly. Therefore, raise an error.
    except:
        raise SystemError("Make sure ra and dec are entered correctly.")
######################


## coordinate_finder.py contains the code for the coord_finder() function. This function will take the name
## of an astronomical object and query the astropy database with the name. The name used in this function does
## NOT have to be the NED name of the object. The function will return the J2000 ra and dec of the object 
## in units of hmsdms as long so the object is found within astropy.


######
# Import the need libraries and modules for the function to work.
from astropy.coordinates import SkyCoord
######


#################
def coord_finder(name):
    '''
    Use astropy search library to determine J2000 ra and dec of an object.

    Inputs:
        name = string of the name of the object the coordinates are needed for

    Outputs:
        ra = J2000 right ascension, units = hms
        dec = J2000 declination, units = dms 
    '''

    # First we need to check that the name given is actually a string.
    # If it isn't a string we could change it into a string but it is probably better to raise an error to
    # make sure the user is aware of what is wanted for the function.
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")

    # Try to find the name in the astropy databases.
    try:
        # Search for the coordinates of the object given the name. 
        coords = SkyCoord.from_name(name, parse = True).to_string('hmsdms').split()

        # Assign the ra and dec variables.
        ra = coords[0]
        dec = coords[1]

        # Return an array of the ra and dec.
        return (ra, dec)
    
    # If the name is not in the astropy databases then raise an error. 
    # (There will most likely be another error raised by the query failing that says the same thing).
    except:
        raise SystemError("Name of source is in shorthand or not in an established database.")
###############