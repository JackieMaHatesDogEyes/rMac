from random import randrange
import os

from sys import argv as args

def random(minimum, maximum, step=1) -> int:
	return randrange(minimum, maximum, step)

def r() -> str:
	return f":{random(0, 9)}{random(0, 9)}"


addr = f"0{random(0, 9, 2)}{r()}{r()}{r()}{r()}{r()}"

interface = "wlp4s0"

try:
	args.pop(0)
except:
	pass

if len(args) == 1:
	interface = args[0]

def cmd(command:str):
	print(command)
	os.system(command)


set = f"sudo ip link set {interface} addr {addr}"

cmd(f"sudo ip link set {interface} down")

cmd(set)

cmd(f"sudo ip link set {interface} up")




