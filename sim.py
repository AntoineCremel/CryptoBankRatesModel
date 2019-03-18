# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:35:06 2019

@author: Charles
"""

# This line configures matplotlib to show figures embedded in the notebook, 
# instead of opening a new window for each figure. More about that later. 
# If you are using an old version of IPython, try using '%pylab inline' instead.
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
"""
from pysolve.model import Model
from pysolve.utils import is_close,round_solution



model = Model()
model.set_var_default(0)
model.var('Cd', desc='Consumption goods demand by households')
model.var('Cs', desc='Consumption goods supply')
model.var('Gs', desc='Government goods, supply')
model.var('Hh', desc='Cash money held by households')
model.var('Hs', desc='Cash money supplied by the government')
model.var('Nd', desc='Demand for labor')
model.var('Ns', desc='Supply of labor')
model.var('Td', desc='Taxes, demand')
model.var('Ts', desc='Taxes, supply')
model.var('Y', desc='Income = GDP')
model.var('YD', desc='Disposable income of households');


model.param('Gd', desc='Government goods, demand', default=20.)
model.param('W', desc='Wage rate', default=1.)
model.param('alpha1', desc='Propensity to consume out of income', default=0.6)
model.param('alpha2', desc='Propensity to consume o of wealth', default=0.4)
model.param('theta', desc='Tax rate', default=0.2);


model.add('Cs = Cd')
model.add('Gs = Gd')
model.add('Ts = Td')
model.add('Ns = Nd');


model.add('YD = (W*Ns) - Ts');

model.add('Td = theta * W * Ns');

model.add('Cd = alpha1*YD + alpha2*Hh(-1)');

model.add('Hs - Hs(-1) =  Gd - Td');

model.add('Hh - Hh(-1) = YD - Cd');

model.add('Y = Cs + Gs');

model.add('Nd = Y/W');

model.solve(iterations=100, threshold=1e-4);


prev = round_solution(model.solutions[-2], decimals=1)
solution = round_solution(model.solutions[-1], decimals=1)
print ("Y         : " + str(solution['Y']))
print ("T         : " + str(solution['Ts']))
print ("YD        : " + str(solution['YD']))
print ("C         : " + str(solution['Cs']))
print ("Hs-Hs(-1) : " + str(solution['Hs'] - prev['Hs']))
print ("Hh-Hh(-1) : " + str(solution['Hh'] - prev['Hh']))
print ("H         : " + str(solution['Hh']))


