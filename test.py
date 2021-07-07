from cmd import CMD
from factory import Factory

factory = Factory()
cmd = CMD()
cmd.attach(factory)
cmd.run()