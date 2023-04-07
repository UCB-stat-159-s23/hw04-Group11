# 4 tests on readligo.py

from ligotools import readligo as rl
import pytest
import numpy as np

# Loaddata
strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
strain_L1, time_L1, chan_dict_L1 = rl.loaddata("data/L-L1_LOSC_4_V2-1126259446-32.hdf5", 'L1')

# Read_Hdf5
strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_hdf5("data/H-H1_LOSC_4_V2-1126259446-32.hdf5")

def test_loaddata_H1type():
    assert isinstance(strain_H1, np.ndarray)
    assert isinstance(time_H1, np.ndarray)
    assert isinstance(chan_dict_H1, dict)
    
def test_loaddata_L1type():
    assert isinstance(strain_L1, np.ndarray)
    assert isinstance(time_L1, np.ndarray)
    assert isinstance(chan_dict_L1, dict)
    
def test_dimensions():
    assert len(strain_H1) == 131072
    assert len(strain_L1) == 131072
    assert len(time_H1) == 131072
    assert len(time_L1) == 131072
    assert len(chan_dict_H1) == 13
    assert len(chan_dict_L1) == 13

def test_read_hdf5_H1():
    assert strain is not None
    assert gpsStart is not None
    assert ts is not None
    assert shortnameList is not None
    assert qmask is not None
    assert injmask is not None
    assert injnameList is not None

