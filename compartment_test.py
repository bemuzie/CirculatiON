__author__ = 'denest'
from Model.compartment import *
from Model.genetic import *
import matplotlib.pyplot as plt
import hotshot
import os

timeduration=100
timeresolution=1
time_array=np.arange(0,100,1)
#np.append(np.arange(0,22,2),np.arange(26,100,6))
sys.setrecursionlimit(50000)
timeaxis=np.arange(0,100,1)
#make reference body model
reference_model={}
for nodename in ['Legs','SVC','Lungs','Kidneys','GI']:
    node=Compartment(nodename)
    node.time=timeaxis
    reference_model[nodename]=node
reference_model['Legs'].set_attrs(7,10,6)
reference_model['Kidneys'].set_attrs(4,2,2)
reference_model['GI'].set_attrs(7,5,6)
reference_model['SVC'].set_attrs(3,3,6)
reference_model['Lungs'].set_attrs(4,8,3)

for node in reference_model.values():
    node.make_profile()

reference_model['Injection']=Compartment('Injection')
reference_model['Injection'].set_attrs(6000,12,2)
reference_model['Injection'].time=timeaxis
reference_model['Injection'].make_delta()
for node in reference_model.values():
    print node.name, node.a,node.loc,node.scale
    print stats.gamma.mean(node.a,node.loc,node.scale)

#------------------------------------------------------
reference_model['Legs'].add_successor(      reference_model['Lungs'],   0.3)
reference_model['Kidneys'].add_successor(      reference_model['Lungs'],   0.2)
reference_model['GI'].add_successor(      reference_model['Lungs'],   0.2)
reference_model['Injection'].add_successor(reference_model['Lungs'],   0.1)
reference_model['SVC'].add_successor(      reference_model['Lungs'],   0.3)

reference_model['Lungs'].add_successor(    reference_model['Legs'],     1)
reference_model['Lungs'].add_successor(    reference_model['GI'],     1)
reference_model['Lungs'].add_successor(    reference_model['Kidneys'],     0.9)
reference_model['Lungs'].add_successor(    reference_model['SVC'],     1)
#ResetBody-------------------------------------------------------

reference_model['Lungs']()
aimresult = reference_model['Lungs'].concentration
"""
plt.plot(reference_model['Lungs'].time,reference_model['Lungs'].concentration,'k-o')
plt.show()
"""
#----------------------------------------------------------------
#make test body compartment
bodytest={}
for nodename in ['IVC','SVC','Lungs','GI']:
    node=Compartment_array_fft(nodename)
    node.set_time(timearray = time_array)
    bodytest[nodename]=node

injectiontest=Compartment_array_fft('Injection')
injectiontest.set_time(timearray=time_array)
injectiontest.set_attrs(0,12,2)


bodytest['IVC'].add_successor(  bodytest['Lungs'],  0.3)
bodytest['GI'].add_successor(  bodytest['Lungs'],   0.4)
bodytest['SVC'].add_successor(  bodytest['Lungs'],  0.3)
bodytest['Lungs'].add_successor(bodytest['IVC'],    1)
bodytest['Lungs'].add_successor(bodytest['SVC'],    1)
bodytest['Lungs'].add_successor(bodytest['GI'],     1)
injectiontest.add_successor(    bodytest['Lungs'],  0.1)


def makelinklist(model,injection_node):
    links=[]
    i=0
    for nodename,attr in [ (model['IVC'], 'a'), (model['IVC'], 'loc'), (model['IVC'], 'scale'),
                            (model['SVC'], 'a'), (model['SVC'], 'loc'), (model['SVC'], 'scale'),
                           (model['Lungs'], 'a'), (model['Lungs'], 'loc'), (model['Lungs'], 'scale'),
                           (model['GI'], 'a'), (model['GI'], 'loc'), (model['GI'], 'scale'),
                           (injection_node, 'a') ]:
        links.append( (nodename,attr,(Ellipsis,i) ))
        i+=1
    return links
links=makelinklist(bodytest,injectiontest)


#------------------------------------------------

def makebody(population):
    
    l=makelinklist(reference_model,reference_model['Injection'])
    setattrs_from_array2(population,l)
    for node in reference_model.values():
        if not node.name == 'Injection':
            node.make_profile()

    reference_model['Injection'].make_delta()
    """
    for node in reference_model.values():
        print node.name, node.a,node.loc,node.scale
    """
    reference_model['Lungs']()
    return reference_model['Lungs'].concentration

def makebody_array(population):
    
    setattrs_from_array(population,links)
    for node in bodytest.values():
        node.make_profile()
    injectiontest.make_delta()
    bodytest['Lungs']()
    return bodytest['Lungs'].concentration
def plotdistributions(chromosome_c,chromosome_p,*args):
  time=time_array
  
  concentration_c=makebody_array(chromosome_c)
  concentration_p=makebody_array(chromosome_p)

  conc=plt.subplot(121)
  pr=plt.subplot(122)
  conc.hold(False)
  pr.hold(False)

  conc.plot(time,aimresult,'-k')
  #pr.plot(range(args[0].__len__()),args[0])
  #pr.plot(timeaxis,reference_model['SVC'].profile,'--k')
  #pr.plot(range(args[0].__len__()),args[0],'k')
  conc.hold(True)
  pr.hold(True)

  #pr.plot(range(args[1].__len__()),args[1],'r')
  #pr.plot(timeaxis,reference_model['IVC'].profile,'--k')
  #pr.plot(timeaxis,reference_model['Lungs'].profile,'--k')

  for c in concentration_c:
    conc.plot(time,c,'r',alpha=0.2)
    plt.pause(0.0001)  
  for c in concentration_p:
    conc.plot(time,c,color='g',alpha=0.2)
    plt.pause(0.0001)  
  
  plt.draw()


def test(loops):
    plt.ion()
    
    gf=GenneticFit(values_intervals = [(2,20)]*12+[(1000,10000)],
                   fenotype_function = makebody_array,
                   aimresult = aimresult,
                   population_size = 100,
                   selection_ratio = 50,
                   output=plotdistributions
                   )
    gf.outputrate=300
    gf.crossover_method='shuffle'
    gf.selection_strategy='elite'
    gf.parent_ratio=25
    fittness_function='ssd'
    gf.fit()
    print 'finished'
    
    plt.ioff()
    plt.plot(reference_model['Lungs'].time,reference_model['Lungs'].concentration,'k-o')
    for i in gf.stats('population'):
        c=makebody(i)
        plt.plot(bodytest['Lungs'].time,c,alpha=0.1)

    
    plt.plot(bodytest['Lungs'].time, makebody(gf.stats('best')), 'r-o')
    for node in reference_model.values():
        print node.name, node.a,node.loc,node.scale
        print stats.gamma.mean(node.a,node.loc,node.scale)
    plt.plot(bodytest['Lungs'].time, makebody(gf.stats('average')), 'b-o')
    

    plt.show()
    
    



test(100000)


"""
prof=hotshot.Profile('CompartmentFittingProfile.prof')
prof.runcall(test,100)
prof.close()
os.system('hotshot2calltree CompartmentFittingProfile.prof > CompartmentFittingProfile_fft.out')
"""