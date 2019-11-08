#
#
###########################################################################
# DESCRIPTION OF PROBLEM (d3dHsm) from FACETS test suite:
# DIII-D single-null geometry with 5 variables (ni,upi,te,ti,ng) and a
# (16+2)*(8+2)=18x10 [poloidal*radial] mesh yielding 900 variables.
# Solver used is Newton Krylov (svrpkg="nksol") and preconditioner uses a
# direct banded solver for the LU decomposition (premeth="banded"). Iterates
# to steady-state solution from an initial profile file (HF5).
###########################################################################
###import uedge
from uedge import *

# Set the geometry
bbb.mhdgeo = 1 		        #=1 use MHD equilibrium files
com.geometry = "dnull"
#flx.aeqdskfname = "aeqdsk"   #name of EFIT 'a' file for flux-surface mesh
#flx.geqdskfname = "neqdsk"   #name of EFIT 'g' or 'n' file for flux-sur mesh
flx.psi0min1 = 0.8		#normalized flux on core bndry
flx.psi0min2 = 0.9		#normalized flux on pf bndry
flx.psi0sep = 1.00001	        #normalized flux at separatrix
flx.psi0max = 1.22		#normalized flux on outer wall bndry
bbb.ngrid = 1		        #number of mesh sequenc. (always set to 1)
com.nxleg[0,0]  = 25		#pol. mesh pts from inner plate to x-point
com.nxcore[0,0] = 25		#pol. mesh pts from x-point to top on inside
com.nxcore[0,1] = 25		#pol. mesh pts from top to x-point on outside
com.nxleg[0,1]  = 25		#pol. mesh pts from x-point to outer plate
com.nysol[0]    = 24		#rad. mesh pts in SOL
com.nycore[0]   = 7		#rad. mesh pts in core

# Finite-difference algorithms (upwind, central diff, etc.)
bbb.methn = 33		#ion continuty eqn
bbb.methu = 33		#ion parallel momentum eqn
bbb.methe = 33		#electron energy eqn
bbb.methi = 33		#ion energy eqn
bbb.methg = 33		#neutral gas continuity eqn

# Core Boundary conditions
bbb.iflcore = 1         # power boundary condition
bbb.pcoree = 2.0e6
bbb.pcorei = 2.0e6
bbb.isnicore[0] = 3     # switch for ion-density core BC
bbb.ncore = 3.0e19      # is isnicore = 1, set core ni BC.
bbb.ngcore[0] = 0       # Neutral density is 0 at psi = 0.8
bbb.curcore[0] = 64.0   # Core current. if isnicore = 0
	
bbb.isnwcono = 3            #=3 for (1/n)dn/dy = 1/lyni
bbb.isnwconi = 3            # switch for private-flux wall
bbb.lyni[0] = 0.05          # PF density radial scale length
bbb.lyni[1] = 0.02          # outer wall density rad scale length (m)
bbb.isnwcono[0]=1           # switch for outer wall BC. =1 for fixed density array
bbb.nwallo=3.5e18           # outer wall density (m**-3)
	
bbb.istepfc = 3             # =3 for (1/Te)dTe/dy=1/lyte on pf wall
bbb.istipfc = 3             # =3 ditto for Ti on pf wall
bbb.istewc = 1              # =3 ditto for Te on vessel wall
bbb.istiwc = 1              # =3 ditto for Ti on vessel wall
bbb.lyte[0] = 0.05          # scale length for Te PF bc
bbb.lyti[0] = 0.05          # scale length for Ti PF bc
bbb.lyte[1] = 0.05          # scale length for Te wall bc
bbb.lyti[1] = 0.05          # scale length for Ti wall bc
	        
bbb.tedge = 2.              # fixed wall,pf Te,i if istewc=1, etc.
bbb.tewallo= 10.
bbb.tiwallo= 15.
	
bbb.isupcore = 1            #=1 sets d(up)/dy=0
bbb.isplflxl = 1            #=0 for no flux limit (te & ti) at plate
bbb.isngcore[0]=0           #zero local density flux (if albedoc=1)


# Neutral Boundary Conditions

bbb.nwsor=2                 # number of source regions on each wall
bbb.issorlb[0:2]=1          # measure source positions from left plate
# at HFS outer wall --
bbb.jxsoro[0]=1
bbb.igaso[0]=0.             # no puff at outer boundary
bbb.xgaso[0]=0.
bbb.wgaso[0]=1000.
bbb.albdso[0]=1.
bbb.matwso[0]=1             # material wall b.c. is ON
# at LFS outer wall --
bbb.jxsoro[1]=2
bbb.igaso[1]=0.             # no puff at outer boundary
bbb.xgaso[1]=0.
bbb.wgaso[1]=1000.
bbb.albdso[1]=1.
bbb.matwso[1]=1             # material wall b.c. is ON

# at lower PF wall --
bbb.jxsori[0]=1
bbb.xgasi[0]=0.0
bbb.wgasi[0]=1000.
bbb.igasi[0]=0.             # no puff at inner boundary
bbb.albdsi[0]=1.            # neutral pumping on inner boundary
bbb.matwsi[0]=1             # material wall b.c. is ON
# at upper PF wall --
bbb.jxsori[1]=2
bbb.xgasi[1]=0.0
bbb.wgasi[1]=1000.
bbb.igasi[1]=0.             # no puff at inner boundary
bbb.albdsi[1]=1.            # neutral pumping on inner boundary
bbb.matwsi[1]=1             # material wall b.c. is ON

bbb.recycw = 0.5

bbb.recycp = .95 # deuterium recycling coeff. at plates

# Centerstack gas puff
bbb.nwsor = 3
bbb.jxsoro[2] = 1           # gas source on inside outer wall
bbb.igaso[2] = 500.         # amps (as if neutral has charge e)
bbb.xgaso[2] = 1.5          # position (in m) of source
bbb.wgaso[2] = .2           # width (in m) of source
bbb.albdso[2] = bbb.albdso[0]
bbb.jxsori[2] = 1; 
bbb.albdsi[2] = bbb.albdsi[0]


# Parallel neutral momentum equation
bbb.isupgon[0] = 0
#bbb.ngsp = 1
bbb.isngon[0] = 1
bbb.cngflox = 1.
bbb.cngfloy = 1.
bbb.cngmom[0] = 1.
bbb.cmwall[0] = 1.


# Neutral Gas Properties
bbb.ingb = 2
bbb.ngbackg = 1.e13
bbb.rtg2ti[0] = 1.
bbb.ineudif = 2

# Transport coefficients (m**2/s)
bbb.difni[0] = 1.	#D for radial hydrogen diffusion
bbb.kye = 5		#chi_e for radial elec energy diffusion
bbb.kyi = 5.    	#chi_i for radial ion energy diffusion
bbb.travis[0] = 1.	#eta_a for radial ion momentum diffusion
bbb.difutm = 1.


# Flux limits
bbb.flalfe = 0.21       #electron parallel thermal conduct. coeff
bbb.flalfi = 0.21	#ion parallel thermal conduct. coeff
bbb.flalfv = .5		#ion parallel viscosity coeff
bbb.flalfgx = 1.	#neut. gas in poloidal direction
bbb.flalfgy = 1.	#neut. gas in radial direction
bbb.flalfgxy = 1.
bbb.flalftgx = 1.       #limit x thermal transport
bbb.flalftgy = 1.       #limit y thermal transport
lgmax = 0.05            #maximum scale-length for gas particle diffusion
lgtmax = 0.1            #maximum scale-length for thermal diffusion



# Solver package
bbb.svrpkg = "nksol"	#Newton solver using Krylov method
bbb.premeth = "banded"	#Solution method for precond. Jacobian matrix
#bbb.mfnksol = 3
#nurlx = 1.e7


# Restart from a HDF5 or PDB savefile
bbb.restart = 1	    #Begin from savefile, not estimated profiles
#bbb.allocate()      #allocates storage for arrays



#from uedge.hdf5 import *
#hdf5_restore("d3dHsm.h5")

if (0):
    ue.restore("d3dHsm.h5")
    bbb.dtreal = 1e20; bbb.exmain()
else:
    #-set up some initial state
    ###ev=1.6022e-19
    bbb.ng=1e14
    bbb.ni=1e20 
    bbb.up=0.0
    bbb.te=bbb.ev
    bbb.ti=bbb.ev




# Atomic data switches
com.istabon = 0            #-analytic rates
###com.istabon = 10        #=10 specifics hydrogen data file ehr2.dat
