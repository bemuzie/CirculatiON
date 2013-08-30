__author__ = 'denest'
from PyQt4.QtCore import SIGNAL
from PyQt4 import QtCore
from PyQt4 import QtGui
from View import Editor2
from Model import CSmodel,qmodels
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt



class Current(Editor2.Ui_MainWindow):
    def __init__(self,Form):
        self.gui=Editor2.Ui_MainWindow()
        self.gui.setupUi(Form)
        self.bodymodel=CSmodel.Compartment()

        Form.connect(self.gui.spinBox_time,SIGNAL("valueChanged()"),self.setgraphtime)
        Form.connect(self.gui.doubleSpinBox_timeres,SIGNAL("valueChanged()"),self.setgraphtime)
        for element in [self.gui.doubleSpinBox_loc,self.gui.doubleSpinBox_scale,self.gui.doubleSpinBox_smth]:
            Form.connect(element,SIGNAL("valueChanged()"),self.updatenode)
        Form.connect(self.gui.comboBox_distribution,SIGNAL("currentIndexChanged(QString)"),self.updatenode)
        Form.connect(self.gui.comboBox_newnode,SIGNAL("currentIndexChanged(QString)"),self.updatenodeinfo)
        #Form.connect(self.gui.comboBox_newnode,SIGNAL("currentIndexChanged(QString)"),self.update_preccesscb)

        Form.connect(self.gui.pushButton_addNode,SIGNAL('clicked()'),self.addNode_clicked)
        Form.connect(self.gui.pushButton_removeNode,SIGNAL('clicked()'),self.removenode)
        Form.connect(self.gui.pushButton_redraw,SIGNAL('clicked()'),self.redraw)

        Form.connect(self.gui.pushButton_addPrecessor,SIGNAL('clicked()'),self.addedge)
        Form.connect(self.gui.tabWidget,SIGNAL('currentChanged(int)'),self.choosecanvas)
        Form.connect(self.gui.comboBox_graphlayout,SIGNAL('currentIndexChanged(QString)'),self.redraw)

        self.setgraphtime()

        self.graph_layouts={'Spring':nx.spring_layout,'Random':nx.random_layout,'Shell':nx.shell_layout,'Circular':nx.circular_layout}
        self.gui.comboBox_graphlayout.addItems([i for i in self.graph_layouts])

        self.nodes=QtCore.QStringList()
        self.nodes << self.bodymodel.nodes()
        self.GuiModel=QtGui.QStringListModel(self. nodes)

        Form.connect(self.GuiModel,SIGNAL('dataChanged()    '),self.modelchanged)

        self.gui.comboBox_nodesForPrecessor.setModel(self.GuiModel)
        self.gui.comboBox_newnode.setModel(self.GuiModel)
        self.gui.listView_nodestodraw.setModel(self.GuiModel)

    def addNode_clicked(self):
        self.updatenode()

        self.update_cbox([self.gui.comboBox_newnode])
        self.redraw()

    def modelchanged(self):
        print "model changed!!"

    def choosecanvas(self,i):
        print i
        if i==0:
            self.canvas=self.gui.mpl_graph.canvas
            self.draw_func=nx.draw(self.bodymodel,ax=self.canvas.ax)
        if i==1:
            self.canvas=self.gui.mpl_concentration.canvas

    def plotconcentration(self):
        nodestoplot=0
        plt.plot(self.bodymodel.graph['time'],)

        pass

    def addedge(self):
        self.bodymodel.add_edge(str(self.gui.comboBox_nodesForPrecessor.currentText()), str(self.gui.comboBox_newnode.currentText()), weight=self.gui.doubleSpinBox_weight.value())
        self.redraw()

    def updatenodeinfo(self,qstr):
        currentnode=self.bodymodel.node[str(qstr)]
        self.gui.doubleSpinBox_loc.setValue(currentnode['distpars'][0])
        self.gui.doubleSpinBox_scale.setValue(currentnode['distpars'][1])
        self.gui.doubleSpinBox_smth.setValue(currentnode['distpars'][2])
        self.gui.comboBox_distribution.setCurrentIndex(self.distribution(currentnode['distribution'],idx=False))


    def removenode(self):
        ctext=self.gui.comboBox_newnode.currentText()
        self.bodymodel.remove_node(str(ctext))
        self.gui.comboBox_newnode.removeItem(self.gui.comboBox_newnode.findText (ctext, flags = QtCore.Qt.MatchExactly))
        self.redraw()

    def setgraphtime(self):
        self.bodymodel.graph['time']=np.arange(0,self.gui.spinBox_time.value(),self.gui.doubleSpinBox_timeres.value())
        # this will update time dependent nodes parametrs
        self.bodymodel.add_nodes_from( self.bodymodel.nodes() )

    def updatenode(self):

        if not str(self.gui.comboBox_newnode.currentText())=="New node":
            self.bodymodel.add_node(str(self.gui.comboBox_newnode.currentText()),
                distribution=self.distribution( self.gui.comboBox_distribution.currentIndex()),
                distpars=[self.gui.doubleSpinBox_loc.value(),self.gui.doubleSpinBox_scale.value(),self.gui.doubleSpinBox_smth.value()])





    def update_cbox(self,cboxes):
        for cb in cboxes:
            for i in self.bodymodel.nodes():
                if cb.findText (i, flags = QtCore.Qt.MatchExactly)==-1:
                    cb.addItem(i)

    def redraw(self):
        layout=self.graph_layouts[str(self.gui.comboBox_graphlayout.currentText())]
        nx.draw_networkx(self.bodymodel,ax=self.canvas.ax,pos=layout(self.bodymodel))
        self.canvas.draw()

    def distribution(self,i,idx=True):
        distributionlist=['norm','gamma']
        if idx:
            return distributionlist[i]
        else:
            return distributionlist.index(i)

class CurrentQt(Editor2.Ui_MainWindow):
    def __init__(self,Form):
        self.gui=Editor2.Ui_MainWindow()
        self.gui.setupUi(Form)

        self.bodymodel=qmodels.QBodyModel()
        self.edgemodel=qmodels.QEdgeModel(self.bodymodel)

        self.gui.comboBox_nodesForPrecessor.setModel(self.bodymodel)
        self.gui.listView_nodestodraw.setModel(self.bodymodel)
        self.gui.listView_profilestodraw.setModel(self.bodymodel)
        self.gui.tableView_nodes.setModel(self.bodymodel)
        self.gui.tableView_edges.setModel(self.edgemodel)

        #----BUTTONS------------------------
        self.gui.pushButton_addNode.clicked.connect(self.addnode)
        self.gui.pushButton_removeNode.clicked.connect(self.removenode)
        self.gui.pushButton_simulate.clicked.connect(self.simulation)
        self.gui.pushButton_addPrecessor.clicked.connect(self.add_predecessor)
        self.gui.pushButton_removePred.clicked.connect(self.remove_edge)
        self.gui.pushButton_redraw.clicked.connect(self.draw_graph)
        #----------------------------

        #-----Actions with views-----------------------
        self.gui.tableView_nodes.clicked.connect(self.show_attributes)
        self.gui.tableView_nodes.clicked.connect(self.edgemodel.change_nodename)
        self.gui.listView_profilestodraw.clicked.connect(self.draw_profiles)
        self.gui.listView_nodestodraw.clicked.connect(self.draw_concs)
        #----------------------------
        self.gui.tabWidget.currentChanged.connect(self.choosecanvas)


        #--------_Defaults--------------------------
        [self.gui.comboBox_distribution.addItem(i,ii) for i,ii in {'Normal':'norm','Gamma':'gamma','Delta':'delta'}.items()]
        self.choosecanvas(self.gui.tabWidget.currentIndex())

    def choosecanvas(self,i):
        if i ==0:
            self.canvas=self.gui.mpl_graph.canvas
            self.draw_graph()
        if i==1:
            self.canvas=self.gui.mpl_concentration.canvas
            self.draw_concs()
        if i == 2:
            self.canvas=self.gui.mpl_profiles.canvas
            self.draw_profiles()

    def draw_graph(self):
        print self.bodymodel.nodes()
        self.canvas.ax.hold(False)
        nx.draw_networkx(self.bodymodel,ax=self.canvas.ax)
        self.canvas.draw()

    def draw_profiles(self):
        self.canvas.ax.hold(False)
        for i in self.gui.listView_profilestodraw.selectedIndexes():
            nodetodraw=self.bodymodel.nodes()[i.row()]
            try:
                self.canvas.ax.plot(self.bodymodel.graph['time'],self.bodymodel.node[nodetodraw]['profile'])
                self.canvas.ax.hold(True)
                self.canvas.draw()

            except KeyError:
                continue

    def draw_concs(self):
        self.canvas.ax.hold(False)
        for i in self.gui.listView_nodestodraw.selectedIndexes():
            nodetodraw=self.bodymodel.nodes()[i.row()]
            try:
                self.canvas.ax.plot(self.bodymodel.graph['time'],self.bodymodel.node[nodetodraw]['conc'])
                self.canvas.ax.hold(True)
                self.canvas.draw()
            except KeyError:
                continue

    def simulation(self):
        self.bodymodel.set_time(self.gui.spinBox_time.value(),self.gui.doubleSpinBox_timeres.value())
        self.bodymodel.update_profiles()
        self.bodymodel.flow( 'RV' )
        self.draw_concs()

    def remove_edge(self):
        for i in self.gui.tableView_edges.selectedIndexes():
            self.edgemodel.removeRow(i.row())

    def add_predecessor(self):
        for i in self.gui.tableView_nodes.selectedIndexes():
            self.edgemodel.insertRow(0,node=str(self.gui.comboBox_nodesForPrecessor.currentText()),
                                    weight=self.gui.doubleSpinBox_weight.value())

    def show_attributes(self,i):

        node_attrs=self.bodymodel.node[self.bodymodel.nodes()[i.row()]]



        for i in range(3):
            if node_attrs['distribution']==self.gui.comboBox_distribution.itemData(i).toString():
                self.gui.comboBox_distribution.setCurrentIndex(i)

        self.gui.doubleSpinBox_loc.setValue(node_attrs['loc'])
        self.gui.doubleSpinBox_scale.setValue(node_attrs['scale'])
        self.gui.doubleSpinBox_smth.setValue(node_attrs['smth'])

    def addnode(self):

        attrs=dict(distribution= str(self.gui.comboBox_distribution.itemData( self.gui.comboBox_distribution.currentIndex() ).toString()),
                    loc= self.gui.doubleSpinBox_loc.value(),
                    scale= self.gui.doubleSpinBox_scale.value(),
                    smth= self.gui.doubleSpinBox_smth.value())
        nodename= str(self.gui.lineEdit_newnode.text())
        if nodename in self.bodymodel.nodes():
            self.bodymodel.add_node(nodename,attr_dict=attrs)
        else:
            self.bodymodel.insertRow(nodename=nodename,attrs= attrs)
        self.gui.tableView_nodes.resizeColumnsToContents()

    def removenode(self):
        for nodeidx in self.gui.tableView_nodes.selectedIndexes():
            self.bodymodel.removeRow(nodeidx)
        self.gui.tableView_nodes.resizeColumnsToContents()











