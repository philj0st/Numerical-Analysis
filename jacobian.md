assume in 3d space. z shall be the evaluation of a multivariate f(x,y).
we can model this as surface plots. we define a vector-in, scalar-out, function [x,y] |-> z.
We can linearize / approximate in neighbourhood of a given point by calculating the slope in every direction and then following the slopes of the tangent hyperplane instead of evaluating f. we receive z' that has smaller errors in closer neighbourhoods of z. the slopes in every direction needed to arrive at the tangent hyperplane equation can be calculated via the partial differentials inside the jacobian.
