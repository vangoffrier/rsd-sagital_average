import numpy as np
import subprocess

if __name__ == "__main__":
	subprocess.run(["python","sagital_brain.py","-o","ut_out.csv"])

	result = np.loadtxt('ut_out.csv', dtype=float,  delimiter=',')

	expected = np.zeros(20)
	expected[-1] = 1

	np.testing.assert_array_equal(result,expected)
