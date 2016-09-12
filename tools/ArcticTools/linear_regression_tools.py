import pandas as pd
import numpy as np



#combining stations before perform linear regressions
def group_stations(filename,fileindex,fliter_dep=2000 ,string1='230Th part.',string2='230Th diss.'):
    err_=[]
    x_=[]
    y_=[]

    for j in (fileindex):
        data=pd.read_csv(filename[j])
        if j==8:
            start=1
        else:
            start=0
        y= data['depth'][start:].values;
        x=data[string1][start:]+data[string2][start:];

        x=np.ma.masked_where(y<=0,x)
        y=np.ma.masked_where(y<=0,y)

        x=np.ma.masked_where(y>=fliter_dep,x)
        y=np.ma.masked_where(y>=fliter_dep,y) 
        x=x.compressed()
        y=y.compressed()
        if j<12:
            name= data['name'][0];    
#        plt.plot(x,y,'-o',lw=2,color=col[j],marker=mark[i],label=name)
#        i+=1
    
    
        for num in range (len(x)):
            #err_.append(err[num])
            x_.append(x[num])
            y_.append(y[num])

        return x_,y_
