# Switched from plotly.px to io due to rendering issues on pi
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "png"
from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#print(results)

# Analyse the results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visialize the results.
fig = px.bar(x=poss_results, y=frequencies)
#png renderring issue workaround
fig.write_image("die_visual.png")
fig.show()