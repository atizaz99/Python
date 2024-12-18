import numpy as np

r = 6371
# convert degrees to radians
def deg_to_rad(degrees):
    return degrees*(np.pi/180)

def dist_calculate(lat1, lon1, lat2, lon2):
    d_lat = deg_to_rad(lat2-lat1)
    d_lon = deg_to_rad(lon2-lon1)
    a = np.sin(d_lat/2)**2 + np.cos(deg_to_rad(lat1))*np.cos(deg_to_rad(lat2)*np.sin(d_lon/2))**2
    c = 2*np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return r*c

print(dist_calculate(22.222, 75.88888, 22.76, 98.9999))