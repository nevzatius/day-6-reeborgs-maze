def turn_right():
  turn_left()
  turn_left()
  turn_left()
def parkour():
  if right_is_clear():
      turn_right()
      move()
  elif wall_in_front() and right_is_clear():
      turn_right()
  elif front_is_clear():
      move()
  elif wall_on_right() and wall_in_front():
      turn_left()

while not at_goal():
  if wall_in_front():
      parkour()
  else: 
      move()





