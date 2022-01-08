import distutils
from distutils.util import strtobool

positive = bool(distutils.util.strtobool('Yes'))
negative = bool(distutils.util.strtobool('No'))
# distutils.util.strtobool("Yes")

print(positive)
print(negative)