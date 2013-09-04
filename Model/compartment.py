__author__ = 'denest'

from scipy import stats
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(50000)
class Compartment(object):
    def __init__(self,name):
        self.name = name
        self.successors = {}
        self.predecessors = {}
        self.pdf = stats.gamma.pdf
        self.treshold = 0.0000001

        self.i=0
    def __call__(self):
        
        inputs = np.sum([pred.concentration*weight for pred,weight in self.predecessors.items()],axis=0)
        newconc = signal.fftconvolve(self.profile, inputs)[:self.time.__len__()]
        diff = self.concentration - newconc
        self.concentration = newconc
        if np.sum(diff*diff)>self.treshold:
            for s in self.successors:
                s()

    def __repr__(self):
        output = self.name + '\n'
        for pred in self.predecessors:
            output += '  - ' + pred.name + " : " + str(self.predecessors[pred])+'\n'
        return output
    def set_attrs(self,*args):
        self.a, self.loc, self.scale = args
        
    def add_successor(self,compartment,weight=1):
        self.successors[compartment]=weight
        compartment.predecessors[self]=weight

    def set_time(self,duration,resolution):
        self.time=np.arange(0,duration,resolution)

    def add_predecessor(self,compartment,weight=1):
        self.predecessors[compartment]=weight
        compartment.successors[self]=weight

    def reset_concentration(self):
        self.concentration=np.zeros(self.time.__len__())

    def make_delta(self):
        #attrs:
        #a - amp
        #loc - duration
        #scale - delay
        self.concentration=np.zeros(self.time.__len__())
        self.concentration[int(self.scale / self.time[1]) : int(self.loc / self.time[1]) ]=self.a

    def make_profile(self):
        # Make PDF of compartment transit times
        self.profile = self.pdf(self.time, self.a, self.loc, self.scale)
        self.profile /= np.sum(self.profile)
        self.concentration = np.zeros( self.time.__len__() )
    def plot(self,color=''):
        plt.plot(self.time,self.concentration,'%s'%color)
class Compartment_fft(object):
    """
    Make compartment with single profile using FFT to convolve during calculation of concentration
    """
    def __init__(self,name):
        self.name = name
        self.successors = {}
        self.predecessors = {}
        self.concentartion = []
        self.pdf = stats.gamma.pdf
        self.time = np.arange(0,10,1)
        self.treshold = 1

        self.i=0
    def __call__(self):     
        #Calculate concentration in compartment   
        inputs = np.sum([pred.concentration*weight for pred,weight in self.predecessors.items()],axis=0)
        inputs_fft = np.fft.fft(inputs,self.fsize)
        print inputs_fft

        newconc = np.fft.ifft(inputs_fft * self.profile_fft).real[:self.time.__len__()]
        diff = np.allclose(self.concentration, newconc,rtol=0.2)
        self.concentration = newconc
        if not diff:
            for s in self.successors:
                s()
    def __repr__(self):
        output = self.name + '\n'
        for pred in self.predecessors:
            output += '  - ' + pred.name + " : " + str(self.predecessors[pred])+'\n'
        return output
    def set_attrs(self,*args):
        self.a, self.loc, self.scale = args
        
    def add_successor(self,compartment,weight=1):
        """
        Adding successor to compartment(and compartment to successor predecessors list). 
        
        compartment should be instance of Compartment class.
        weight is the ratio compartment flow to the whole successor's income flow
        """
        if weight<0 or weight>1:
            raise ValueError
        self.successors[compartment]=weight
        compartment.predecessors[self]=weight

    def set_time(self,duration,resolution):

        self.time=np.arange(0,duration,resolution)
        self.fsize= int(2 ** np.ceil(np.log2( self.time.__len__()*2-1 )))
        print self.fsize
    def add_predecessor(self,compartment,weight=1):
        
        self.predecessors[compartment]=weight
        compartment.successors[self]=weight

    def reset_concentration(self):
        self.concentration=np.zeros(self.time.__len__())

    def make_delta(self):
        """
        attrs:
        a - amp
        loc - duration
        scale - delay
        """
        self.concentration=np.zeros(self.time.__len__())
        self.concentration[int(self.scale / self.time[1]) : int(self.loc / self.time[1]) ]=self.a

    def make_profile(self):
        # Make PDF of compartment transit times
        self.profile = self.pdf(self.time, self.a, self.loc, self.scale)
        self.profile /= np.sum(self.profile)
        self.profile_fft=np.fft.fft(self.profile,self.fsize)
        self.concentration = np.zeros( self.time.__len__() )
    def plot(self,color=''):
        plt.plot(self.time,self.concentration,'%s'%color)
class Compartment_array(Compartment):
    """
    Make compartment with an array of profiles
    """
    def __call__(self,index=None):
        
        if index == None:
            for idx in range (self.profile.shape[0]):
                inputs = np.sum([pred.concentration[idx] * weight for pred,weight in self.predecessors.items()], axis=0)
                newconc = np.convolve(self.profile[idx] ,inputs)[:self.time.__len__()]
                diff = self.concentration[idx] - newconc
                self.concentration[idx] = newconc
                if np.sum(diff*diff) > self.treshold:
                    for s in self.successors:
                        s(idx)
        else:
            inputs = np.sum([pred.concentration[index]*weight for pred,weight in self.predecessors.items()], axis=0)
            newconc = np.convolve(self.profile[index] ,inputs)[:self.time.__len__()]
            diff = self.concentration[index] - newconc
            self.concentration[index] = newconc
            if np.sum(diff*diff)>self.treshold:
                for s in self.successors:
                    s(index)
    def make_delta(self):
        """
        attrs:
        a - amp
        loc - duration
        scale - delay
        """
        self.concentration = np.zeros(( self.a.__len__(), self.time.shape[0] ))
        self.concentration[ :,int(self.scale / self.time[1]) : int(self.loc / self.time[1]) ]=self.a
    def make_profile(self):
        # Make PDF of compartment transit times
        self.profile = self.pdf(self.time[np.newaxis, :], self.a, self.loc, self.scale)
        self.profile /= np.sum(self.profile, axis = 1)[:,np.newaxis]
        self.concentration = np.zeros(( self.profile.shape[0], self.time.__len__() ))
class Compartment_array_fft(Compartment):
    """
    Make compartment with array of profiles that use FFT to convolve durinf calculation of concentration
    """
    sys.setrecursionlimit(50000)
    def set_time(self,duration=None,resolution=None,timearray=None):
        if timearray==None:
            self.time=np.arange(0,duration,resolution)
        else:
            self.time = timearray
            

        self.fsize= int(2 ** np.ceil(np.log2( self.time.__len__()*2-1 )))#Length of the transformed axis of the FFT output.(copied from scipy.stats.fftconvolve) 

    def __call__(self,index=None):
        inputs = np.sum([pred.concentration * weight for pred,weight in self.predecessors.items()], axis=0)
        inputs_fft = np.fft.fft(inputs, self.fsize, axis = 1)
        newconc = np.fft.ifft(inputs_fft * self.profile_fft).real[:, :self.time.__len__()]
        diff = self.concentration - newconc
        self.concentration = newconc
        if np.sum(diff*diff) > self.treshold:
            for s in self.successors:
                s()
    def make_delta(self):
        """
        attrs:
        a - amp
        loc - duration
        scale - delay
        """
        self.concentration = np.zeros(( self.a.__len__(), self.time.shape[0] ))
        self.concentration[ :,int(self.scale / self.time[1]) : int(self.loc / self.time[1]) ] = self.a
    def make_profile(self):
        # Make PDF of compartment transit times
        self.profile = self.pdf(self.time[np.newaxis,:], self.a, self.loc, self.scale)
        self.profile /= np.sum(self.profile, axis = 1)[:,np.newaxis]
        self.profile_fft=np.fft.fft(self.profile, self.fsize, axis = 1)
        self.concentration = np.zeros(( self.profile.shape[0], self.time.__len__() ))

def setattrs_from_array(values,linklist):
    #
    #linklist - [(node,attribute,index_in_values),...]
    
    for node,attribute,index in linklist:
        setattr(node,attribute,values[index][:,np.newaxis])

def setattrs_from_array2(values,linklist):
    #
    #linklist - [(node,attribute,index_in_values),...]
    for node,attribute,index in linklist:
        setattr(node,attribute,values[index])


if __name__=='__main__':
    rv=Compartment_array('RV')
    lv=Compartment_array('LV')
    injection=Compartment_array('Injection')
    rv.add_predecessor(lv, 1)
    rv.add_predecessor(injection, 0.1)
    lv.add_predecessor(rv, 1)

    for compartment in [rv,lv]:
        compartment.set_time(100, 0.5)
        compartment.set_attrs(*[np.random.uniform(2, 7, 10)[:,np.newaxis] for i in range(3)])
        
        compartment.make_profile()
    injection.set_time(100, 0.5)
    injection.set_attrs(np.ones((10, 1))*[2000], 22, 2)
    injection.make_delta()
    
    plt.ion()
    
    rv()
    plt.ioff()
    for i in rv.concentration:
        plt.plot(rv.time,i)
    plt.plot(injection.time,injection.concentration[0])
    plt.show()
    

