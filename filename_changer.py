import os
import re
import shutil

# loading files
root = os.path.dirname(os.path.realpath(__file__)) + '/'
filenames = os.listdir(root)

for filename in filenames:
	m = re.match(r'(?is)BW_s9_1.62_(\d)', filename)
	if m != None and len(m.groups()):
		test = re.sub(r'(?is)BW_s9_1.62_(\d)', 'BW_s9_1.62_try' + m.group(1), filename)
		shutil.move(root + filename, root + test)
