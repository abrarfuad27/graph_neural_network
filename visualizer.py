import matplotlib.pyplot as plt

#tiny values = [4.365864121744253e-05,4.219837155310169e-05,0.01513452,1.5e-06]
values = []
labels = ['graph_init', 'loading dataset','training','evaluation']

plt.bar(labels, values)
plt.ylabel('Energy Consumption (kilowatt hour)')
plt.title('GNN Power Usage Components')
plt.savefig('gnn_components.png')


