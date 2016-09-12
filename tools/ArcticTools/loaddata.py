import netCDF4 as nc
import glob
import numpy as np

tmask=nc.Dataset(
        '/ocean/xiaoxiny/research/NEMO-code/NEMOGCM/CONFIG/myANHA/EXP00/crop.nc')
#mbathy=tmask.variables['mbathy'][0,400:,:]
tmask=tmask.variables['tmask'][0,:,400:,:]

def ice(year):
    Ice = nc.Dataset('/ocean/xiaoxiny/research/data/forcing/Ice_nt/ANHA4-ENG3_icemod_y%sm09.nc'%year)
    ice = Ice.variables['ileadfra'][400:,:]
    return ice

def vel(keyword,T,ENG):
    '''design to obtain velocity field;
     keyword: should be U, V, W;
     T is the year to plot, for example, 1991;
     ENG is the name of ANHA run, for example, ENG3, ENG4,EXH001'''
    if keyword =='U':
        nc_filename=sorted(glob.glob('/ocean/xiaoxiny/research/result_jasper/data_eng3/*%s*U*%s*.nc'%(ENG,T)))
        #print nc_filename
        uvel=nc.Dataset(nc_filename[0])
        data =uvel.variables['vozocrtx'][0,:,400:,:]
    elif keyword =='V':
        nc_filename=sorted(glob.glob('/ocean/xiaoxiny/research/result_jasper/data_eng3/*%s*V*%s*.nc'%(ENG,T)))
        vvel=nc.Dataset(nc_filename[0])
        data =vvel.variables['vomecrty'][0,:,400:,:]
    else:
        nc_filename=sorted(glob.glob('/ocean/xiaoxiny/research/result_jasper/data_eng3/*%s*W*%s*.nc'%(ENG,T)))
        wvel=nc.Dataset(nc_filename[0])
        data =wvel.variables['vovecrtz'][0,:,400:,:]
    data =np.ma.masked_where(tmask==0,data)
    return data
