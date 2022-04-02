# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys

sys.path.append('../')
# End of fix

from niapy.algorithms.basic import BatAlgorithm
from niapy.task import Task


# we will run Bat Algorithm for 20 independent runs
for i in range(20):
    task = Task(problem="pinter", max_iters=100)
    algo = BatAlgorithm(population_size=25, loudness=1.0, pulse_rate=1.0, alpha=0.97, gamma=0.1, min_frequency=0.0,
                        max_frequency=2.0,)
    best = algo.run(task)
    print('%s -> %s' % (best[0], best[1]))