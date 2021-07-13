from CLI.cmd import CMD
from factory import Factory

array = [1, 2, 3]
print(array[0::2])
factory = Factory()
cmd = CMD()
cmd.attach(factory)
cmd.run()