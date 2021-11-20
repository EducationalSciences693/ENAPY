from plotnine import ggplot, geom_point, geom_label, geom_line, aes, stat_smooth, facet_wrap, coord_fixed
from pandas import DataFrame

def ena_plot(enaset, groupby=None, groupmode="facet"):
    if groupmode not in ["facet", "subtract"]:
        raise Exception("groupmode must be either 'facet' or 'subtract'")
    
    # Start the plot, using plotnine
    points = enaset.rx2("points")
    plot = ggplot(data=points)
    plot += coord_fixed(ratio=1, xlim=(-1, 1), ylim=(-1, 1))
    
    # Either show units as black (else) or colored by group (if)
    if groupby is not None:
        plot += geom_point(mapping=aes(x="SVD1", y="SVD2", color=groupby))
        if groupmode == "facet":
            plot += facet_wrap(groupby)
    else:
        plot += geom_point(mapping=aes(x="SVD1", y="SVD2"))
    
    # Prepare counts and nodes objects for below
    counts = enaset.rx2("line.weights")
    nodes = enaset.rx2("rotation").rx2("nodes")
    if groupby is not None:
        grouped_points = counts.groupby(groupby).mean()
        subbed = grouped_points.iloc[1] - grouped_points.iloc[0]
    else:
        mean_points = counts.select_dtypes(include="number").mean()

    # For each possible pair of nodes,
    # if that pairing is a valid connection in our model,
    # draw the network line. We draw the line slightly
    # differently depending on the groupby and groupmode.
    # Either way, the general strategy is to make a temp
    # dataframe and plot one line from it.
    for _, node1 in nodes.iterrows():
        for _, node2 in nodes.iterrows():
            connection = f"{node1.code} & {node2.code}"
            if connection in counts.columns:
                if groupby is not None:
                    if groupmode == "facet":
                        for group_name, group_points in grouped_points.iterrows():
                            xs = []
                            ys = []
                            sizes = []
                            groups = []
                            xs.append(node1.SVD1)
                            xs.append(node2.SVD1)
                            ys.append(node1.SVD2)
                            ys.append(node2.SVD2)
                            sizes.append(group_points[connection])
                            sizes.append(group_points[connection])
                            groups.append(group_name)
                            groups.append(group_name)
                            edges = DataFrame({"SVD1": xs, "SVD2": ys, groupby: groups, "size": sizes})
                            plot += geom_line(data=edges, mapping=aes(x="SVD1/3", y="SVD2/3", size="size", alpha="size", color=groupby))
                    else: # subtract
                        xs = []
                        ys = []
                        sizes = []
                        groups = []
                        xs.append(node1.SVD1)
                        xs.append(node2.SVD1)
                        ys.append(node1.SVD2)
                        ys.append(node2.SVD2)
                        sizes.append(subbed[connection])
                        sizes.append(subbed[connection])
                        if subbed[connection] < 0:
                            groups.append(grouped_points.index[0])
                            groups.append(grouped_points.index[0])
                        else:
                            groups.append(grouped_points.index[1])
                            groups.append(grouped_points.index[1])
                                
                        edges = DataFrame({"SVD1": xs, "SVD2": ys, groupby: groups, "size": sizes})
                        plot += geom_line(data=edges, mapping=aes(x="SVD1/3", y="SVD2/3", size="size", alpha="size", color=groupby))
                else:
                    xs = []
                    ys = []
                    sizes = []
                    xs.append(node1.SVD1)
                    xs.append(node2.SVD1)
                    ys.append(node1.SVD2)
                    ys.append(node2.SVD2)
                    sizes.append(mean_points[connection])
                    sizes.append(mean_points[connection])
                    edges = DataFrame({"SVD1": xs, "SVD2": ys, "size": sizes})
                    plot += geom_line(data=edges, mapping=aes(x="SVD1/3", y="SVD2/3", size="size", alpha="size"))

    # Finally, draw the node points and labels and we're done
    plot += geom_point(data=nodes, mapping=aes(x="SVD1/3", y="SVD2/3"))
    plot += geom_label(data=nodes, mapping=aes(x="SVD1/3", y="SVD2/3", label="code", size=8))
    return plot