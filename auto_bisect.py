import numpy as np
import subprocess

if __name__ == "__main__":
	subprocess.run(["git","bisect","start"])
	subprocess.run(["git","bisect","bad","HEAD"])
	subprocess.run(["git","bisect","good","4042fcf5"])
	subprocess.run(["git","bisect","run","python3","unit_test.py","2"])
