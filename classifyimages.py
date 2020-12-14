from Tools import tools_v000 as tools
import os
from os.path import dirname


# -14 for the name of this project ClassifyImages
# save_path = dirname(__file__)[ : -14]
save_path = os.path.dirname(os.path.abspath("__file__"))[ : -14]
propertiesFolder_path = save_path + "\\"+ "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'ClassifyImages', 'user_text=')
