from scipy.spatial.transform import Rotation as R
import numpy as np

r = R.from_quat([0.295, 0.404, -0.137, 0.855])
print(r.as_matrix())