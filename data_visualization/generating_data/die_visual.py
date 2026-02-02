# Switched from plotly.px to io due to rendering issues on pi
import plotly.express as px
#pi work around
import plotly.io as pio
pio.renderers.default = "png"

from die import Die

# Create 2 D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store the results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(1000)]

# Analyse the results.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]

# Visialize the results.
title = "Results of Rolling two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.write_image("die_visual.png")
#proposed line for rendering in browser
#fig.write_html('dice_visual_d6d10.html')
