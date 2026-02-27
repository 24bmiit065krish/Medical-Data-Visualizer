from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Generate and save categorical plot
fig1 = draw_cat_plot()
fig1.savefig("catplot.png")

# Generate and save heatmap
fig2 = draw_heat_map()
fig2.savefig("heatmap.png")

print("Plots generated successfully!")