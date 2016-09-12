import copy,os,glob
import netCDF4 as nc
import numpy as np
from mpl_toolkits.basemap import Basemap

def mapping(latlim):
        '''
    This function is used to create a circle region centered on the north pole.
    ===========================================================================
    arg:  boundinglat: the latitude circle boundinglat (default is set to be 67). 
    type: boundinglat: can be either floats or interger
    '''
        Bathy=nc.Dataset(
    '/ocean/xiaoxiny/research/data/Jasper/ANHA4_bathy_etopo1_gebco1_smoothed_coast_corrected_mar10.nc')
        bathy=Bathy.variables['Bathymetry'][400:,:]
        nav_lon=Bathy.variables['nav_lon'][400:,:]
        nav_lat=Bathy.variables['nav_lat'][400:,:]

        m = Basemap(projection='npstere',boundinglat=latlim,lon_0=0,resolution='l',round='True')
        m.drawcoastlines()
        m.fillcontinents(color = '0.85',alpha=0.5)
        m.drawparallels(np.arange(-90.,90.,15.),labels=[0, 0, 0, 0])
        m.drawmeridians(np.arange(-180.,180.,60.),labels=[1, 1, 1, 1])
        x_lon, y_lat = m(nav_lon[:], nav_lat[:])
        m.plot(x_lon[::20,::20],y_lat[::20,::20],x_lon[::20,::20].T,y_lat[::20,::20].T,color='black',linewidth=0.2,alpha=0.7)
        m.contour(x_lon,y_lat,bathy,linewidth=0.075,colors='black',alpha=0.2)
        return m,x_lon,y_lat


def section(x0,y0,length,xi,yi):
    '''
    This function is to find the lat/lon for interested sections
    ============================================================================
    arg:  x0, y0: the starting point of the section.  
    type: x0, y0: interger
    
    arg:  length: length of the section  (Longer the section, bigger this number)
    type: length: interger
    
    arg:  xi, yi: slope  example: xi  =  0.5 then x0 + 0.5 * i
    type: xi, yi: floats/interger 
                 (If choose floats, index could be floats as well but it will Round to nearest integer)
    
    '''
    a = [] #index for the first dimension
    b = [] #index for the second dimension
    for i in range (length):
        a.append(x_lon[x0 + xi*i,y0 + yi*i])
        b.append(y_lat[x0 + xi*i,y0 + yi*i])
    return a,b

def section_hovmoller(data,layer,x0,y0,length,xi,yi):
    '''load data for vertical profiles, return to tracer/cooridination 
     ================================================================
     
    arg:  data: 4-dimension model result from NEMO model 
    type: data: np.array
    
    arg:  layer: for a desired depth of the field
    type: layer: interger
    
    arg:  length: length of the section  (Longer the section, bigger this number)
    type: length: interger   
    
    arg:  x0, y0: the starting point of the section.  
    type: x0, y0: interger

    arg:  xi, yi: slope  example: xi  =  0.5 then x0 + 0.5 * i
    type: xi, yi: floats/interger 
                 (If choose floats, index could be floats as well but it will Round to nearest integer)

    '''
    a = np.empty([yearnum,length]);  # array to hold cross-section data over the model period
    coordinate = np.empty(length)    # array to contain coordinate for that section
    signx = xi
    signy = yi
    for i in range (length):
        temp = data[:,layer,x0 + signx*i,y0 + signy*i]
        temp = np.ma.masked_where(tmask[layer,x0 + signx*i,y0 + signy*i]< = 0,temp)
        a[:,i] = temp
        coordinate[i] = lon[x0 + signx*i,y0 + signy*i]
    return a,coordinate



def crossS_vel_hov(layer,length,x0,y0,xi,yi):
    '''cross-section velocity (m/s), return to cross-section velocity/cooridination 
    ===============================================================================
    arg:  layer: for a desired depth of the field
    type: layer: interger
    
    arg:  length: length of the section  (Longer the section, bigger this number)
    type: length: interger   
    
    arg:  x0, y0: the starting point of the section.  
    type: x0, y0: interger

    arg:  xi, yi: slope  example: xi  =  0.5 then x0 + 0.5 * i
    type: xi, yi: floats/interger 
                 (If choose floats, index could be floats as well but it will round to nearest integer)

    '''
    a = np.empty([length]);             # array to restore cross-section data (for just one time step)
    coordinate = np.empty(length)       # array to contain coordinate for that section


    signx = xi;signy = yi
    zi = (yi**2 + xi**2)**0.5
    hold = np.empty([yearnum,length]);  # array to hold cross-section data over the model period
    for j in range (yearnum):
        u = vel(keyword = 'U',T = 1958 + j,ENG = 'ENG3')[layer,:,:]
        v = vel(keyword = 'V',T = 1958 + j,ENG = 'ENG3')[layer,:,:]
        
        for i in range (length):
                # u,v --> cross-section velocity
                temp = u[x0 + signx*i,y0 + signy*i]*yi/zi - v[x0 + signx*i,y0 + signy*i]*xi/zi
                # mask
                temp = np.ma.masked_where(tmask[layer,x0 + signx*i,y0 + signy*i]< = 0,temp)
                a[i] = temp
                coordinate[i] = lon[x0 + signx*i,y0 + signy*i]
        hold[j,:] = a[:]
    return hold,coordinate


def alongS_vel_hov(layer,length,x0,y0,xi,yi):
    '''Along-section velocity (m/s), return to along-section velocity/cooridination 
    ===============================================================================
    arg:  layer: for a desired depth of the field
    type: layer: interger
    
    arg:  length: length of the section  (Longer the section, bigger this number)
    type: length: interger   
    
    arg:  x0, y0: the starting point of the section.  
    type: x0, y0: interger

    arg:  xi, yi: slope  example: xi  =  0.5 then x0 + 0.5 * i
    type: xi, yi: floats/interger 
                 (If choose floats, index could be floats as well but it will Round to nearest integer)

    '''
    a = np.empty([length]); 
    coordinate = np.empty(length)


    signx = xi;signy = yi
    zi = (yi**2 + xi**2)**0.5
    hold = np.empty([yearnum,length]);
    for j in range (yearnum):
        u = vel(keyword = 'U',T = 1958 + j,ENG = 'ENG3')[layer,:,:]
        v = vel(keyword = 'V',T = 1958 + j,ENG = 'ENG3')[layer,:,:]
        for i in range (length):
                # u,v --> Along-section velocity
                temp = u[x0 + signx*i,y0 + signy*i]*xi/zi + v[x0 + signx*i,y0 + signy*i]*yi/zi
                temp = np.ma.masked_where(tmask[layer,x0 + signx*i,y0 + signy*i]< = 0,temp)
                a[i] = temp
                coordinate[i] = lon[x0 + signx*i,y0 + signy*i]
        hold[j,:] = a[:]
    return hold,coordinate


def vel(keyword,T,ENG = 'ENG3'):
    '''
    This function is designed to obtain velocity field
    ======================================================
    arg:  keyword: three options. can choose 'U', 'V' or 'W'
    type: keyword: string
    
    arg:  T: calender year 
    type: T: string
    
    arg:  ENG: choose run series, for example, ENG3, ENG4, EXH001, EXH005
    type: ENG: string
    '''
    if keyword  == 'U':
        nc_filename = sorted(glob.glob('/ocean/xiaoxiny/research/result_jasper/data_eng3/*%s*U*%s.nc'%(ENG,T)))
        uvel = nc.Dataset(nc_filename[0])
        data  = uvel.variables['vozocrtx'][0,:,400:,:]
    elif keyword  == 'V':
        nc_filename = sorted(glob.glob('/ocean/xiaoxiny/research/result_jasper/data_eng3/*%s*V*%s.nc'%(ENG,T)))
        vvel = nc.Dataset(nc_filename[0])
        data  = vvel.variables['vomecrty'][0,:,400:,:]
    else:
        nc_filename = sorted(glob.glob('/ocean/xiaoxiny/research/result_jasper/data_eng3/*%s*W*%s.nc'%(ENG,T)))
        wvel = nc.Dataset(nc_filename[0])
        data  = wvel.variables['vovecrtz'][0,:,400:,:]
    data  = np.ma.masked_where(tmask == 0,data)
    return data
