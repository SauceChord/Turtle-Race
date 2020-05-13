from Race import *

# create a race with 10 legs
# (a leg is a section of a track)
race = Race(legs = 10)

# enter competitors
race.join('red', name = 'Red Baron')
race.join('blue', name = 'Blue Pearl')
race.join('green', name = 'Green Witch')
race.join('orange', name = 'Orange Ninja')

# draw lanes and legs for track
# if more participants have entered, the
# track will adjust height.
race.draw_track()

# continue racing forever
while True:
  race.ready_set_go()
  race.honour_winner()
  race.clear_racers()