import discord
import os
import sys
import subprocess
import datetime
import re

mainCommandColors = discord.Color.red()

def p_bar(health: int, max_up: int = 2500):
  bars = 10
  percent = (health / max_up) * 100
  green_bars = round((percent / 100) * bars)

  progress_bar = "🟩" * green_bars + "🟥" * (bars - green_bars)

  return progress_bar

async def parse_time(time_str):
  time_units = {
    's': 'seconds',
    'm': 'minutes',
    'h': 'hours',
    'd': 'days'
  }
  match = re.match(r"(\d+)([smhd])", time_str)
  if not match:
    return None
  
  value, unit = match.groups()
  kwargs = {time_units[unit]: int(value)}
  return datetime.datetime.now() + datetime.timedelta(**kwargs)
  
def restartbot():
  subprocess.Popen([sys.executable] + sys.argv)
  os._exit(0)