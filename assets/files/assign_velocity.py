import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import healpy as hp

############################################################
# User defined variables
############################################################
N_shell = 10 #number of shells in velocity distribution
Nside = 2 #The number of directions in each shell will be 12*Nside**2
z = 20 #redshift
g_nu = 6 #magnitude of the neutrino degeneracy. 3 neutrino species + 3 anti-neutrino species

############################################################
# Constants
############################################################
c = 299792458 #[m/s] speed of light
k_b = 1.38064852e-23 #[m^2 kg s^{-2} K^{-1}] boltzman constant
T_nu = 1.95 # [K] neutrino temperature today
h_p =  6.62607004e-34#[m^2 kg s^{-1}] plancks constant


############################################################
#Step 1a: divide Fermi-Dirac distribution into shells
############################################################
#Note x = (pc)/(k_B*T) and T = T_nu*(1+z)
x_max = 12 # maximum value... see Fig 1 in Banjeree et al. 2018
x = np.linspace(0,x_max,1000)
fermi_dirac = (4*np.pi*g_nu)/h_p**3 * 1/(np.exp(x) + 1)
p2f = integrate.cumtrapz(x*x*fermi_dirac, x, initial=0) # integral x^2*f(x) from 0 to x
dV = p2f[-1]/N_shell #volume of each shell
x_edges = np.interp(dV*np.arange(0,N_shell+1),p2f,x) #find the edges of the shells


############################################################
#Step 1b: set magnitude for each shell
############################################################
p4f = integrate.cumtrapz(x**4*fermi_dirac, x, initial=0) # integral x^4*f(x) from 0 to x
p4f_i = np.interp(x_edges,x,p4f)
p2f_i = np.interp(x_edges,x,p2f)
p_i = np.sqrt((p4f_i[1:]-p4f_i[:-1]) /(p2f_i[1:]-p2f_i[:-1]))


############################################################
#Make a plot to check momentum values
############################################################
y=x*x*fermi_dirac
plt.plot(x,y,'k')
plt.xlabel('$pc/k_B T$')
plt.ylabel('$x^2 f(x)$')
for xx in x_edges:
    plt.plot((xx,xx),(0,np.interp(xx,x,y)),'k')
for xx in p_i:
    plt.plot((xx,xx),(0,np.interp(xx,x,y)),':k')
plt.savefig('velocityshells.png')

############################################################
#Step 2: Assign angular direction
############################################################
x,y,z = hp.pix2vec(Nside,np.arange(12*Nside**2))

############################################################
#Make a plot to check momentum directions
############################################################

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z,'o')
plt.savefig('velocitydirections.png')
