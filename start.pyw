import sys
from PyQt4 import QtGui,uic
#from View import sim
from Controller import controller
import os
newwindow=os.path.join('./View/Editor2.py')
os.remove(newwindow)
uic.compileUi(os.path.join('./View/Editor2.ui'),file(newwindow,'w'))
def main():
    app = QtGui.QApplication( sys.argv )
    MainWindow =  QtGui.QMainWindow()
    ww=controller.CurrentQt(MainWindow)

    for n,a in {"Injection":dict(distribution= 'delta',loc= 2,scale= 16,smth= 200),
                'Legs':       dict(distribution= 'gamma',loc= 7, scale= 10,smth= 6),
                'GI':       dict(distribution= 'gamma',loc= 7,scale= 5,smth= 4),
                'SVC':       dict(distribution= 'gamma',loc= 3,scale= 3,smth= 6),
                'Lungs':       dict(distribution= 'gamma',loc= 2,scale= 5,smth= 3),
                'Kidneys':       dict(distribution= 'gamma',loc= 4,scale= 2,smth= 2),
                }.items():
        ww.bodymodel.insertRow(nodename= n,attrs= a)

    ww.bodymodel.add_weighted_edges_from([('Legs','Lungs',0.3),
                                        ('Kidneys',"Lungs",0.2),
                                        ('GI',"Lungs", 0.2),
                                        ('Injection',"Lungs", 0.1),
                                        ('SVC',"Lungs", 0.3),
                                        ('Lungs',"Legs",1),
                                        ('Lungs',"GI",1),
                                        ('Lungs',"Kidneys",0.9),
                                        ('Lungs','SVC',1)])
    print 1
    ww.simulation()
    


    MainWindow.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(  main() )

