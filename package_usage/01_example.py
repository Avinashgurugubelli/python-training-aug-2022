# importing module from a package
import my_package.json_util as json_util

# importing a function from a package
from my_package.json_util import convertJsonToStr


def abc():
    json_util.convertJsonToStr()
