much harder to solve than system of linear equations. we usually resort to approximating it by linear equations (linearization).

searching for roots algorithmically:
recall fixed point iteration, newton, etc. for finding roots in one dimension. newton was following down the slope until intersection with the x-axis and continuing from that evalualted point again down the slope.
now for multivariate/multidimensional steps towards the roots we calculate a delta and add it to the position vector. we want to avoid computing the inverse of the jacobian. rather solve an equation directly for delta.
