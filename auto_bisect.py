import numpy as np
import subprocess

if __name__ == "__main__":
	subprocess.run(["git bisect start"])
	subprocess.run(["git bisect bad HEAD"])
	subprocess.run(["git bisect good master"])
	subprocess.run(["git bisect run python unit_test.py 2"])
