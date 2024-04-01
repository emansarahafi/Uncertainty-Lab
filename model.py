from pomegranate import *

# Burglar node has no parents
burglar = Node(DiscreteDistribution({
    "yes": 0.001,
    "no": 0.999 
}), name="burglar")

# Earthquake node has no parents
earthquake = Node(DiscreteDistribution({
    "yes": 0.002,
    "no": 0.998
}), name="earthquake")

# Alarm node is conditional on Burglar and Earthquake
alarm = Node(ConditionalProbabilityTable([
    ["yes", "yes", "yes", 0.95],
    ["yes", "yes", "no", 0.05],
    ["yes", "no", "yes", 0.94],
    ["yes", "no", "no", 0.06],
    ["no", "yes", "yes", 0.29],
    ["no", "yes", "no", 0.71],
    ["no", "no", "yes", 0.001],
    ["no", "no", "no", 0.999],
], [burglar.distribution, earthquake.distribution]), name="alarm")

# John node is conditional on Alarm
john = Node(ConditionalProbabilityTable([
    ["yes", "yes", 0.9],
    ["yes", "no", 0.1],
    ["no", "yes", 0.05],
    ["no", "no", 0.95],
], [alarm.distribution]), name="john")

# Mary node is conditional on Alarm
mary = Node(ConditionalProbabilityTable([
    ["yes", "yes", 0.7],
    ["yes", "no", 0.3],
    ["no", "yes", 0.01],
    ["no", "no", 0.99],
], [alarm.distribution]), name="mary")

# Create a Bayesian Network and add states (nodes)
model = BayesianNetwork()
model.add_states(burglar, earthquake, alarm, john, mary)

# Add edges connecting nodes
model.add_edge(burglar, alarm)
model.add_edge(earthquake, alarm)
model.add_edge(alarm, john)
model.add_edge(alarm, mary)

# Finalize model
model.bake()
