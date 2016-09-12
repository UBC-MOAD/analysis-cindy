import netCDF4 as nc
from mpl_toolkits.basemap import Basemap

def mapping():
	'''This function aim at making maps for Arctic'''
	bathy=nc.Dataset(
    '/ocean/xiaoxiny/research/data/Jasper/ANHA4_bathy_etopo1_gebco1_smoothed_coast_corrected_mar10.nc')
	bathy=bathy.variables['Bathymetry'][400:,:]
	nav_lon=ptrc.variables['nav_lon'][:]
	nav_lat=ptrc.variables['nav_lat'][:]

	m = Basemap(projection='npstere',boundinglat=70,lon_0=0,resolution='l',round='True')
	m.drawcoastlines()
	m.fillcontinents(color = '0.85',alpha=0.5)
	m.drawparallels(np.arange(-90.,90.,15.),labels=[0, 0, 0, 0])
	m.drawmeridians(np.arange(-180.,180.,60.),labels=[1, 1, 1, 1])
	x_lon, y_lat = m(nav_lon[:], nav_lat[:])
	m.plot(x_lon[::20,::20],y_lat[::20,::20],x_lon[::20,::20].T,y_lat[::20,::20].T,color='black',linewidth=0.2,alpha=0.7)
	m.contour(x_lon,y_lat,bathy,linewidth=0.075,colors='black',alpha=0.2)
	return m
