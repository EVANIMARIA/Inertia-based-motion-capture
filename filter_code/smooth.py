import numpy as np


def smooth(data, window):
    if (window % 2) == 0:
        return "No Even!"
    else:
    	for x in range(len(data)):
    		if x<window:
    			pass