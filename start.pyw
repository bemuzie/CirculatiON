import sys
from PyQt4 import QtGui
#from View import sim
from Controller import controller

def main():
    app = QtGui.QApplication( sys.argv )
    MainWindow =  QtGui.QMainWindow()
    ww=controller.CurrentQt(MainWindow)

    for n,a in {"Injection":dict(distribution= 'delta',loc= 2,scale= 16,smth= 200),
                "RV":       dict(distribution= 'norm',loc= 10, scale= 2,smth= 0),
                "LV":       dict(distribution= 'norm',loc= 8,scale= 1,smth= 0),}.items():
        ww.bodymodel.insertRow(nodename= n,attrs= a)

    ww.bodymodel.add_weighted_edges_from([('Injection','RV',0.1),
                                        ('RV',"LV",1),
                                        ('LV','RV',1)])
    ww.simulation()



    MainWindow.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(  main() )

