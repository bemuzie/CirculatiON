__author__ = 'denis'
import numpy as np
from PyQt4 import QtGui,QtCore
from scipy import stats
import sys
from Model import CSmodel
import networkx as nx

class Body:
    def __init__(self):
        self._node_attributes=[]
        self._graph_attributes=[]
        self._compartments={}



    def set_node_attributes(self,*attr):
        self._node_attributes.extend(attr)
    def set_graph_attributes(self,*attr):
        self._graph_attributes.extend(attr)


    def add_node(self,name,determinated=False,**attr):
        self._compartments[name]=({},{})

        for attr_name in self._node_attributes:
            try:
                self._compartments[name][0].__setitem__(attr_name, attr[attr_name])
            except KeyError,key:
                print "You should add attribute %s"%key
                break


    def remove_node(self,name):
        self._compartments.__delitem__(name)

    def change_node_attributes(self,nodename,**attributes):
        for attr_name,attr_value in attributes.items():
            self._compartments[nodename][0].__setitem__(attr_name,attr_value)
    def add_edge(self,predessor,successor,weight=1):
        if not predessor in self._compartments.keys():
            raise ValueError("Predessor is invalid. There is not such node - %s."%predessor)
        if not successor in self._compartments.keys():
            raise ValueError("Successor is invalid. There is not such node - %s."%successor)
        self._compartments[successor][1].__setitem__(predessor,weight)
    def remove_edge(self,predessor,successor):
        self._compartments[successor][1].__delitem__(predessor)

    def nodes(self):
        return self._compartments.keys()
    def node_attributes(self,name):
        return self._compartments[name][0]
    def node_predessors(self,name):
        return self._compartments[name][1]
    def node_successors(self,name):
        successors=[]
        for n in self._compartments.keys():
            if name in self.node_predessors(n):
                successors.append(n)
        return successors

    def edges(self,weight=False):
        edges=[]
        for node in self._compartments.keys():
            [edges.append([node,successor ]) for successor in self.node_successors(node)]
        return edges


    def normilize_weights(self,node):
        coeff=1./sum(self.node_predessors(node).values())
        for pred in self.node_predessors(node).keys():
            self._compartments[node][1][pred]*=coeff





    def __str__(self):
        output=''

        for nodename in self.nodes():
            output+=nodename+'\n'
            for pred,weight in self.node_predessors(nodename).items():
                output+="  |-------"+pred+' weight:'+str(weight)+'\n'
        return output

class Circmodel(nx.DiGraph):
    def __init__(self):
        nx.DiGraph.__init__(self)

    def set_time(self,duration,resolution):
        self.graph['time']=np.arange(0,duration,resolution)

    def update_profiles(self):
        for i in self.nodes():
            if not self.node[i]['distribution']=='delta':
                func=getattr(stats,self.node[i]['distribution'])
                if self.node[i]['distribution']=='norm':
                    self.node[i]['profile']=func.pdf(self.graph['time'], self.node[i]['loc'], self.node[i]['scale'])
                if self.node[i]['distribution']=='gamma':
                    self.node[i]['profile']=func.pdf(self.graph['time'], self.node[i]['loc'], self.node[i]['scale'], self.node[i]['smth'])
                self.node[i]['profile']/=np.sum(self.node[i]['profile'])
                self.node[i]['conc']=np.zeros(self.graph['time'].size)

            else:
                self.node[i]['conc']=np.zeros(self.graph['time'].size)
                self.node[i]['conc'][self.node[i]['loc']/self.graph['time'][1] : self.node[i]['scale']/self.graph['time'][1]] =self.node[i]['smth']
    def make_profiles(self):
        for i in self.nodes():
            self.node[i]['profile']=stats.gamma.pdf(self.graph['time'],*self.node[i]['pars'])


    def arraytoparams(self,array):
        self.correspondence=[]




    def flow(self,node):
        thisnode=self.node[node]
        if self.predecessors(node)==[]:
            pass
        else:
            inputconc=np.sum( [self.node[inputs]['conc'] * self.edge[inputs][node]['weight']
                               for inputs in self.predecessors_iter(node)],axis=0)
            concnew=np.convolve( thisnode['profile'], inputconc)[:self.graph['time'].size]
            diff=thisnode['conc']-concnew
            thisnode['conc']=concnew
            if np.sum(diff*diff)>0.000000000001:
                for i in self.successors_iter(node):
                    self.flow(i)


class QBodyModel(QtCore.QAbstractTableModel, nx.DiGraph):
    def __init__(self,parent=None):
        nx.DiGraph.__init__(self)
        QtCore.QAbstractTableModel.__init__(self, parent)
    def set_time(self,duration,resolution):
        self.graph['time']=np.arange(0,duration,resolution)
    def update_profiles(self):
        for i in self.nodes():
            if not self.node[i]['distribution']=='delta':
                func=getattr(stats,self.node[i]['distribution'])
                if self.node[i]['distribution']=='norm':
                    self.node[i]['profile']=func.pdf(self.graph['time'], self.node[i]['loc'], self.node[i]['scale'])
                if self.node[i]['distribution']=='gamma':
                    self.node[i]['profile']=func.pdf(self.graph['time'], self.node[i]['loc'], self.node[i]['scale'], self.node[i]['smth'])

                self.node[i]['profile']/=np.sum(self.node[i]['profile'])
                self.node[i]['conc']=np.zeros(self.graph['time'].size)

            else:
                self.node[i]['conc']=np.zeros(self.graph['time'].size)

                self.node[i]['conc'][self.node[i]['loc']/self.graph['time'][1] : self.node[i]['scale']/self.graph['time'][1]] =self.node[i]['smth']
    def up_gamma_fast(self):
        for i in self.nodes():
            if not self.node[i]['distribution']=='delta':

                newprofile = np.vstack(stats.gamma.pdf(t, self.node[i]['loc'], self.node[i]['scale'], self.node[i]['smth'])
                                                   for t in self.graph['time'])


                self.node[i]['profile']= newprofile/ np.sum(newprofile)
                self.node[i]['conc']=np.zeros(self.graph['time'].size)
            else:
                self.node[i]['conc']=np.zeros(self.graph['time'].size)
                self.node[i]['conc'][self.node[i]['loc']/self.graph['time'][1] : self.node[i]['scale']/self.graph['time'][1]] =self.node[i]['smth']
    def flow(self,node):
        thisnode=self.node[node]
        predecessors=self.predecessors(node)
        if predecessors==[]:
            pass
        else:
            inputconc=np.sum( [self.node[inputs]['conc'] * self.edge[inputs][node]['weight']
                               for inputs in predecessors],axis=0)
            concnew=np.convolve( thisnode['profile'], inputconc)[:self.graph['time'].size]
            diff=thisnode['conc']-concnew
            thisnode['conc']=concnew
            if np.sum(np.abs(diff))>0.000001:
                for i in self.successors_iter(node):
                    self.flow(i)
    def fitting_func(self,attrs):
        for node,a in zip(self.linklist,attrs):
            self.node[node[0]][node[1]] = a
        self.update_profiles()
        self.flow('RV')
        return self.node['RV']['conc']

    def setnodeattrslinks(self,linklist):
        self.linklist=linklist


    def rowCount(self, parent):

        return len(self.nodes())

    def columnCount(self, parent):
        return 5

    def data(self, index, role):
        if role==QtCore.Qt.DisplayRole or role==QtCore.Qt.EditRole:
            nodename=self.nodes()[index.row()]
            if index.column()==0:
                return QtCore.QString(nodename)
            if index.column()==1:
                return QtCore.QString(self.node[nodename]['distribution'])
            if index.column()==2:
                return self.node[nodename]['loc']
            if index.column()==3:
                return self.node[nodename]['scale']
            if index.column()==4:
                return self.node[nodename]['smth']


    def headerData(self, p_int, Qt_Orientation, int_role=None):
        pass

    def flags(self,index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable

    def setData(self,qtindex,value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            if qtindex.column()==0:
                if not value.toString()=='' or value.toString()==self.nodes()[qtindex.row()]:
                    oldnode=self.nodes()[qtindex.row()]
                    oldnodeattr=self.node[oldnode]
                    predeccessors=self.predecessors(oldnode)
                    successors=self.successors(oldnode)
                    newnodename=str(value.toString())
                    self.add_node(newnodename,oldnodeattr)
                    for pred in predeccessors:
                        self.add_edge(pred, newnodename, weight=self.edge[pred][oldnode]['weight'])
                    for succ in successors:
                        self.add_edge(newnodename, succ, weight=self.edge[oldnode][succ]['weight'])
                    self.remove_node(oldnode)
                    return True
            if qtindex.column()==2:
                self.add_node(self.nodes()[qtindex.row()],loc=value.toDouble()[0])
                return True
            if qtindex.column()==3:
                self.add_node(self.nodes()[qtindex.row()],scale=value.toDouble()[0])
                return True
            if qtindex.column()==4:
                self.add_node(self.nodes()[qtindex.row()],smth=value.toDouble()[0])
                return True

        return False


    def insertRow(self, index=QtCore.QModelIndex(), *args, **kwargs):

        self.beginInsertRows(index,len(self.nodes()),len(self.nodes()))
        self.add_node(kwargs['nodename'],kwargs['attrs'])
        self.endInsertRows()

        return True
    def removeRow(self, idx, parent=QtCore.QModelIndex(), *args, **kwargs):
        self.beginRemoveRows(parent, idx.row(),idx.row())
        self.remove_node(self.nodes()[idx.row()])
        self.endRemoveRows()
        print 'row removed'
        return True


class QEdgeModel(QtCore.QAbstractTableModel):
    def __init__(self,qBodyModel, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.model=qBodyModel

        self._nodename='RV'
    def nodename(self):
        return self._nodename
    def change_nodename(self, index):
        if type(index)==QtCore.QModelIndex:
            self._nodename=self.model.nodes()[index.row()]
        elif type(index)==int:
            self._nodename=self.model.nodes()[index]
        self.reset()
        self.beginInsertRows(QtCore.QModelIndex(),0,len(self.model.predecessors(self._nodename)))
        self.endInsertRows()


    def rowCount(self,parent):
        return len(self.model.predecessors(self._nodename))

    def columnCount(self, parent):
        return 2
    def data(self, index, role):
        if role==QtCore.Qt.DisplayRole or role==QtCore.Qt.EditRole:
            pred=self.model.predecessors(self._nodename)
            if not pred==[]:
                if index.column()==0:
                    return QtCore.QString(pred[index.row()])
                if index.column()==1:
                    return QtCore.QString(str(self.model.edge [pred[index.row()]] [self._nodename]['weight']))
    def setData(self,qtindex,value,role=QtCore.Qt.EditRole):
        if role==QtCore.Qt.EditRole:
            if qtindex.column()==1:
                value=value.toDouble()[0]
                if value>0 or value<1:
                    self.model.add_edge(self.model.predecessors(self._nodename)[qtindex.row()],
                                        self._nodename,
                                        weight=value)
                    return True
        return False

    def flags(self,index):
        if index.column()==0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable
    def header(self):
        pass
    def removeRow(self, idx, parent=QtCore.QModelIndex(), *args, **kwargs):
        self.beginRemoveRows(parent,idx,idx)
        self.model.remove_edge(self.model.predecessors(self._nodename)[idx],self._nodename)
        self.endRemoveRows()

    def insertRow(self, idx, parent=QtCore.QModelIndex(), *args, **kwargs):
        self.beginInsertRows(parent,idx,idx)
        self.model.add_edge(kwargs['node'],self._nodename,weight=kwargs['weight'])
        self.endInsertRows()



