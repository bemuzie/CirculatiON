import networkx as nx

t={"Injection":dict(distribution= 'delta',loc= 2,scale= 16,smth= 200),
                "RV":       dict(distribution= 'norm',loc= 10, scale= 2,smth= 0),
                "LV":       dict(distribution= 'norm',loc= 8,scale= 1,smth= 0)}

def add_node(*args, **kwargs):
	a=nx.DiGraph()
	a.add_node(kwargs['nodename'],kwargs['attrs'])
	return a


g=add_node(1,2,3)
