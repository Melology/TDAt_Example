import persim
import tadasets
import ripser
import matplotlib.pyplot as plt

#data sets
data_clean = tadasets.dsphere(d=1, n=100, noise=0.0)
data_noisy = tadasets.dsphere(d=1, n=100, noise=0.1)

#Gencerate H_1 diagrams for each of the data sets
plt.scatter(data_clean[:,0], data_clean[:,1], label="clean data")
plt.scatter(data_noisy[:,0], data_noisy[:,1], label="noisy data")
plt.axis('equal')
plt.legend()
plt.show()

dgm_clean = ripser.ripser(data_clean)['dgms'][1]
dgm_noisy = ripser.ripser(data_noisy)['dgms'][1]

persim.plot_diagrams([dgm_clean, dgm_noisy] , labels=['Clean $H_1$', 'Noisy $H_1$'])
plt.show()

#Compute and visualize Bottleneck distance
distance_bottleneck, matching = persim.bottleneck(dgm_clean, dgm_noisy, matching=True)
persim.bottleneck_matching(dgm_clean, dgm_noisy, matching, labels=['Clean $H_1$', 'Noisy $H_1$'])
plt.show()
print(distance_bottleneck)
persim.bottleneck(dgm_clean, dgm_noisy)