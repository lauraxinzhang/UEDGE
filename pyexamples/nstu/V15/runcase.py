#-import uedge
from uedge import *

#-import hdf5 routines
from uedge.hdf5 import *

#-import graphics, math, etc.
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os

#-import some utilities for using OS
###execfile(os.path.join(os.environ['HOME'], 'utils/python/osfun.py'))
PYLIB = '/u/xzhang/UEDGE/pylib'

#-in .bashrc: "export PYLIB=/home/umansky1/PyUEDGE/uedge/pylib"
execfile(PYLIB+"/plotmesh.py")
execfile(PYLIB+"/plotcontour.py")
execfile(PYLIB+"/plotvar.py")
execfile(PYLIB+"/paws.py")
execfile(PYLIB+"/osfun.py")

plt.ion()


#-read UEDGE settings
execfile("rd_nstu_V15.py")


#-do a quick preliminary run to set all internals
bbb.restart=0; bbb.ftol=1e10; bbb.dtreal = 1e-6; bbb.exmain()

#-show grid
#plotmesh(iso=1)
#wait = raw_input("PAUSING, PRESS ENTER TO CONTINUE...")


#-run to steady state
bbb.restart=1; bbb.ftol=1e-10; 
bbb.isbcwdt=1
bbb.dtreal = 1e-14; bbb.itermx=30; bbb.exmain()
bbb.t_stop=1e0
bbb.rundt()
bbb.dtreal=1e20; bbb.isbcwdt=0; bbb.exmain()


#-show some results
#plotvar(bbb.te/bbb.ev)
#wait = raw_input("PAUSING, PRESS ENTER TO CONTINUE...")

#-show some results
savedir = './'
ext = '.pdf'
limiter = '../' + 'NSTX_limiter.dat'

plotvar(bbb.te/bbb.ev, savedir + 'te' + ext, False, title = "Electron Temperature (eV)", limiter = limiter)
#wait = raw_input("press enter")
plotvar(bbb.ti/bbb.ev, savedir + 'ti' + ext, False, title = "Ion Temperature (eV)", limiter = limiter)
#wait = raw_input("press enter")
plotvar(bbb.ne, savedir + 'ne' + ext, False, title = r"Electron Density ($m^{-3}$)", limiter = limiter)
plotvar(bbb.up, savedir + 'up' + ext, False, title = "Fluid Velocity (m/s)", limiter = limiter)
plotvar(bbb.phi, savedir + 'phi' + ext, False, title = "Potential (V)",limiter = limiter)
plotvar(bbb.ng, savedir + 'ng'+ext, False, title = r'Neutral Density ($m^{-3})$', limiter =limiter)


#-export the solution in hdf5 file
hdf5_save('nstu_V15.h5')

#-can be imported with this command
#hdf5_restore('mycase.h5')


###-refine the grid, interpolate to new grid, and restart:
#com.nxleg[0,0]=20; bbb.newgeo=1; bbb.icntnunk=0
#bbb.dtreal = 1e-14; bbb.isbcwdt=1; bbb.itermx=30; bbb.exmain()

###-time advance by another second
#bbb.t_stop=2e0; bbb.rundt()

###-now to steady state (infinite time)
#bbb.dtreal=1e20; bbb.isbcwdt=0; bbb.exmain()

###-show some results
#plotvar(bbb.te/bbb.ev)
