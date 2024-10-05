import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def flowduration(Q):
    #create an array with values from 0 to 1, in increments of 0.01
    percs = np.arange(0,1.01,0.01)
    # calculate percentiles, but remove NaN first
    discharge = Q['Value'].dropna().quantile(percs)
    # create a new data frame
    flowduration = pd.DataFrame(index=percs,columns=['Exceedance Probability','Discharge']) 
    # reverse order of quantiles
    flowduration['Exceedance Probability'] = 100*(1-percs)
    flowduration['Discharge'] = discharge[-1::]
    #plot with log y axis
    fig,ax = plt.subplots()
    ax.semilogy(flowduration['Exceedance Probability'],flowduration['Discharge'],'-k')
    ax.grid()
    ax.set_xlabel('Exceedance probability')
    # use Latex formatting
    ax.set_ylabel(u'Q ($m^3/s$)') 
    return(flowduration,fig)