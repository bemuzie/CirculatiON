__author__ = 'denest'
import numpy as np
import matplotlib.pyplot as plt

import random
from scipy import stats
try:
    import bottleneck as bn
except ImportError:
    pass

class GenneticFit:
    def __init__(self,values_intervals,aimresult,fenotype_function,population_size,selection_ratio,
                fittness_function='ssd',
                selection_method='truncation',
                crossover_method='average',
                loops_treshold = 5000,
                output = None,

                ):
        """
        values_intervals - low and up tale of values range in chromosome.Should be list of lists or tuples
        aimresult - target array 
        population_size - size 
        selection_size - amount of best chromosomes in population wich will be choosen 
        fenotype_function - some function that take chromosome and time as arguments and return result like aim
        fittness_function:
            'ssd' - sum of squared differences
            'max' - maximum difference
        
        average_population_size - amount of new averaged cromosomes which are adding in each loop
        mutation_prob - probability of mutation
        loops - number of loops to estimate curve
        output - some function that defines output information
        """
        self.val_intervals=values_intervals
        self.aim = aimresult
        self.fenotype_function = fenotype_function
        self.fittness_function = fittness_function # 
        self.population_size=population_size
        self.randomfunc=np.random.uniform
        self.selection_method = selection_method #rank, tournament,truncation,proportional
        self.crossover_method = crossover_method #shuffle,average
        self.loops_treshold = loops_treshold
        self.output=output
        #------------------Defaults-------------------------------------
        self.mutation_prob=0.04
        self.selection_ratio=population_size/2
        self.tournament_ratio=2
        self.parent_ratio=1

        self.selection_strategy='best'

        self.outputrate=1

        
    def fit(self):
        self.generate_population()
        for i in range(self.loops_treshold):
            #print self.parents.shape
            self.crossover()
            self.mutation(self.mutation_prob,low=0.8,up=1.2)
            if self.output and i%self.outputrate==0:
                self.output(self.children,self.parents)
            self.selection(selection_method=self.selection_method,
                            strategy=self.selection_strategy,
                            ratio=self.selection_ratio,
                            tournament_ratio=self.tournament_ratio,
                            parent_ratio=self.parent_ratio)


    def generate_population(self):
        generatedpop = np.hstack([ self.randomfunc(low, up, self.population_size)[:, np.newaxis] 
                                               for low, up in self.val_intervals ])
        try:
            self.parents=np.vstack((self.children,generatedpop))
        except AttributeError:
            self.parents=generatedpop

    def selection(self,selection_method,
                    strategy,
                    ratio,
                    tournament_ratio,
                    parent_ratio):
        """
        We should have 2 generations to begin selection: parents and children.
        strategy:
            elit - new population consist of n best parents and all children
            full - new population consist of children
            best - new population consist of n best from parents and children
        selection strategy:
            truncation - 
            rank - 
            tournament - 
        """

        self.fenotype_ch = self.fenotype_function(self.children)
        self.fitness_ch = self.fitness(self.aim, self.fenotype_ch)
        
        if strategy == 'best':
            try:
                
                self.fitness_ch = np.concatenate((self.fitness_ch,self.fitness_p))
                self.children = np.vstack ((self.children,self.parents))
                
            except AttributeError,e:
                print e
                pass

        self.children_sorted = self.children[ np.argsort(self.fitness_ch)]
        #print 'self.children_sorted.shape',self.children_sorted.shape


        if selection_method=='truncation':
            self.children = self.children_sorted[:ratio]
            self.fitness_ch = self.fitness_ch[:ratio]
        elif selection_method=='rank':
            amount = self.children_sorted.shape[0]
            mask = np.random.binomial(1,np.linspace(1,0,amount),amount)
            self.children = self.children_sorted[mask==1]
        elif selection_method=='tournament':
            """
            We should random take n individuals from population 
            and put the best from them to the new population N times
            n - tournament_ratio
            N is ratio
            """
            bestones=[]
            amount = self.children_sorted.shape[0]
            for i in ratio:
                bestones.append( np.min (np.random.randint(0,amount,tournament_ratio)))
            self.children = self.children_sorted[bestones]
        else:
            raise AttributeError('Incorrect selection method used')

        if strategy == 'full' or strategy == 'best':
            self.parents = self.children
            
        elif strategy == 'elite':
            try:
                self.parents = np.vstack((self.parents_sorted[:parent_ratio], self.children))
            except AttributeError,e:
                print e
                self.parents = self.children
        else:
            raise AttributeError('Incorrect selection strategy used')

        self.fitness_p=self.fitness_ch
        self.parents_sorted=self.children_sorted

    def crossover(self):
        if self.crossover_method == 'shuffle':
            self.children=self.parents.copy()
            for chromosome in self.children.swapaxes(0,1):
                np.random.shuffle(chromosome)
        elif self.crossover_method == 'average':
            #pairs_index = np.random.randint(0,self.parents.shape[0],self.parents.shape[0]) #several to one
            pairs_index = np.arange(self.parents.shape[0])
            np.random.shuffle (pairs_index) #one to one
            
            self.children= (self.parents + self.parents[pairs_index])/2.
            #print self.parents[0]
            #print self.children[0]



    def mutation(self, prob, low=0.8,up=1.2):
        mask = np.random.binomial(1, prob, self.children.shape)
        self.children[mask == 1] *= np.random.uniform(low, up, self.children[mask==1].shape)

    def addaverage(self,amount):
        avpop_average = np.average(self.parents, axis = 0)
        avpop_sigma = np.std(self.parents, axis = 0)
        avpop = np.random.normal(loc = avpop_average, scale = avpop_sigma/2, size = (amount, avpop_average.shape[0]))
        self.parents = np.vstack((self.parents, avpop))

    def fitness(self, aim, a):
        if self.fittness_function=='ssd':
            diff=a-aim[np.newaxis,:]
            return np.sum(diff*diff,axis = 1)
        elif self.fittness_function=='ssd_bn':
            return bn.ss(a-aim[np.newaxis,:])
        elif self.fittness_function=='max':
            diff=a-aim[np.newaxis,:]
            #seems it faster then - np.max(np.abs(diff),axis=1)
            mx=np.max(diff, axis=1)
            mn=np.abs(np.min(diff, axis=1))
            return np.max((mx,mn), axis=0)
        elif self.fittness_function=='abs':
            return np.sum( np.abs(a-aim[np.newaxis,:]), axis=1)
            
                
        

    def stats(self, infotype=None):
        """
        infotype - type of returned info:
                            population - return all chromosomes
                            best - the best chromosome
                            average - the average chromosome
                            sd - the SD of values in chromosomes
        """
        if infotype == 'population':
            return self.parents
        elif infotype == 'best':
            return self.parents[0]
        elif infotype == 'average':
            print np.average(self.parents,0).shape
            return np.average(self.parents,0)
        elif infotype == 'sd':
            return np.std(self.parents,0)

    def plot(self):
        time = np.arange(0,100,2)
        plt.plot(time,self.aim)
        plt.hold(True)
        for i in self.fitting_function(self.parents):
            plt.plot(time,i,alpha=0.3)
        plt.hold(False)
        plt.draw()
