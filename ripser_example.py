import numpy as np
from ripser import Rips

rips = Rips()

data = np.random.random((100, 2))

diagrams = rips.fit_transform(data)

rips.plot(diagrams, show=True)
