# **Install Library**
import subprocess
import sys

# Define the packages you want to install
packages = ['pandas', 'streamlit', 'pydeck', 'diskcache', 'memory_profiler', 'import_ipynb', 'matplotlib', 'seaborn', 'babel']
            
# Use subprocess to call pip install for each package
for package in packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
