import netCDF4 as nc
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from matplotlib.patches import Polygon
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


def mapping(latlim,ax='False',Bathykey ='True',Gridkey = 'True',LatlonKey='True',fontsize=10):
	'''This function aim at making maps for Arctic'''
	Bathy=nc.Dataset('/ocean/xiaoxiny/research/data/Jasper/ANHA4_bathy_etopo1_gebco1_smoothed_coast_corrected_mar10.nc')
	bathy=Bathy.variables['Bathymetry'][400:,:]
	nav_lon=Bathy.variables['nav_lon'][400:,:]
	nav_lat=Bathy.variables['nav_lat'][400:,:]
	if ax == 'False':
		m = Basemap(projection='npstere',boundinglat=latlim,lon_0=0,resolution='l',round='True')
	else:
		m = Basemap(projection='npstere',boundinglat=latlim,lon_0=0,resolution='l',round='True',ax=ax)
	m.drawcoastlines()
	m.fillcontinents(color = '0.85',alpha=0.5)
	m.drawparallels(np.arange(-90.,90.,20.),labels=[0, 0, 0, 0],fontsize=fontsize)
	if LatlonKey == 'True':
		m.drawmeridians(np.arange(0.,360.,60.) ,labels=[1, 1, 1, 1],fontsize=fontsize)
	else:
		m.drawmeridians(np.arange(0.,360.,60.) ,labels=[0, 0, 0, 0],fontsize=fontsize)
	x_lon, y_lat = m(nav_lon[:], nav_lat[:])
	if Gridkey == 'True':
		m.plot(x_lon[::20,::20],y_lat[::20,::20],x_lon[::20,::20].T,y_lat[::20,::20].T,color='black',linewidth=0.2,alpha=0.7)
	if Bathykey == 'True':
		m.contour(x_lon,y_lat,bathy,linewidth=0.075,colors='black',alpha=0.2)
	return m,x_lon,y_lat

def maponAR(ax, Bathykey = 'True', datakey='False',data=[],vlimkey='False',vlim=[]):
	'''The data comes in for pcolor
	vmin: has to be a list. inside, it should contain two numbers, vlim[vmin,vmax]
	data: has to be 2 dimension- the same as x_lon and y_lat'''
	Bathy=nc.Dataset('/ocean/xiaoxiny/research/data/Jasper/ANHA4_bathy_etopo1_gebco1_smoothed_coast_corrected_mar10.nc')
	bathy=Bathy.variables['Bathymetry'][400:,:]
	lon=Bathy.variables['nav_lon'][400:,:]
	lat=Bathy.variables['nav_lat'][400:,:]

	#fig, ax = plt.subplots(figsize=(10,5))
	m = Basemap(width =4e6,height =2e6,lon_0=-85, lat_0=85,
			projection='stere', resolution='l',ax=ax)
	m.drawcoastlines()
	m.fillcontinents(color='0.85')
	m.drawparallels(np.arange(-80.,81.,10.),labels=[1, 0, 0, 0])
	m.drawmeridians(np.arange(-180.,181.,30.),labels=[0, 0, 0, 1])
	x_lon,y_lat=m(lon,lat)
	if datakey !='False':
		if vlimkey == 'False':
			m.pcolor(x_lon,y_lat,data[:,:])
		else:
			m.pcolor(x_lon,y_lat,data[:,:],vmin=vlim[0],vmax=vlim[1],cmap='Spectral_r')
		m.colorbar()
	if Bathykey == 'True':
		m.contour(x_lon,y_lat,bathy,linewidth=0.075,colors='black',alpha=0.2)

	m.ax = ax

	#add inset
	axin = inset_axes(m.ax, width="30%", height="30%", loc=4)
	# Global inset map.
	inmap = Basemap(projection='npstere', lon_0=0,boundinglat=60, round="True", ax=axin)
	inmap.fillcontinents('grey')

	bx, by = inmap(m.boundarylons, m.boundarylats)
	xy = list(zip(bx, by))
	mapboundary = Polygon(xy, edgecolor='k', linewidth=1, fill=False)
	inmap.ax.add_patch(mapboundary)

	return m,ax,x_lon,y_lat

def maponCB(ax, width =1.8e6, height =1.8e6,lon_0=-145, lat_0=76.5, \
			Bathykey = 'True', datakey='False',data=[],vlimkey='False',vlim=[]):
	'''The data comes in for pcolor
	vmin: has to be a list. inside, it should contain two numbers, vlim[vmin,vmax]
	data: has to be 2 dimension- the same as x_lon and y_lat'''
	Bathy=nc.Dataset('/ocean/xiaoxiny/research/data/Jasper/ANHA4_bathy_etopo1_gebco1_smoothed_coast_corrected_mar10.nc')
	bathy=Bathy.variables['Bathymetry'][400:,:]
	lon=Bathy.variables['nav_lon'][400:,:]
	lat=Bathy.variables['nav_lat'][400:,:]

	#fig, ax = plt.subplots(figsize=(10,5))
	m = Basemap(width=width,height=height,lon_0=lon_0, lat_0=lat_0, projection='stere', resolution='i',ax=ax)
	m.drawcoastlines()
	m.fillcontinents(color='0.85')
	m.drawparallels(np.arange(-80.,81.,10.),labels=[1, 0, 0, 0])
	m.drawmeridians(np.arange(-180.,181.,30.),labels=[0, 0, 0, 1])
	x_lon,y_lat=m(lon,lat)
	if datakey !='False':
		if vlimkey == 'False':
			m.pcolor(x_lon,y_lat,data[:,:])
		else:
			m.pcolor(x_lon,y_lat,data[:,:],vmin=vlim[0],vmax=vlim[1],cmap='Spectral_r')
		m.colorbar()

	if Bathykey == 'True':
		m.contour(x_lon,y_lat,bathy,linewidth=0.075,colors='black',alpha=0.2)

	m.ax = ax

	#add inset
	axin = inset_axes(m.ax, width="25%", height="25%", loc=4)
	# Global inset map.
	inmap = Basemap(projection='npstere', lon_0=0,boundinglat=65, round="True", ax=axin)
	inmap.fillcontinents('grey')
	inx_lon,iny_lat=inmap(lon,lat)
	inmap.contour(inx_lon,iny_lat,bathy,linewidth=0.075,colors='black',alpha=0.2)

	bx, by = inmap(m.boundarylons, m.boundarylats)
	xy = list(zip(bx, by))
	mapboundary = Polygon(xy, edgecolor='k', linewidth=1, fill=False)
	inmap.ax.add_patch(mapboundary)

	return m,ax,x_lon,y_lat


