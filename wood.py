def reset():
	while True:
		if get_pos_x() == 0 and get_pos_y() == 0:
			break
		sweep_field()
			
def harvest_tree():
	if can_harvest():
		harvest()
		plant(Entities.Tree)
	if get_entity_type() == None:
		plant(Entities.Tree)

def harvest_bush():
	if can_harvest():
		harvest()
	if get_entity_type() == None:
		plant(Entities.Bush)

def move_drone(move_1, move_2):
	move(move_1)
	move(move_2)
	
def trees():
	while True:
		if get_pos_x() == 9 and get_pos_y() == 9:
			harvest_tree()
			return
		elif get_pos_x() == 8:
			harvest_tree()
			move_drone(East, North)
			while get_pos_y() != 9:
				harvest_tree()
				move_drone(North, West)
		elif (get_pos_x() == 0 or get_pos_x() % 2 == 0) and get_pos_y() == 0:
			harvest_tree()
			move_drone(East, East)
			while get_pos_x() != 0:
				harvest_tree()
				move_drone(North, West)
		elif get_pos_x() == 0:
			harvest_tree()
			move_drone(North, North)
			while get_pos_y() != 0:
				harvest_tree()
				move_drone(East, South)
		elif get_pos_x() == 8:
			harvest_tree()
			move_drone(East, North)
			break
		elif get_pos_x() % 2 != 0 and get_pos_y() == 9:
			harvest_tree()
			move_drone(East, East)
			while get_pos_x() != 9:
				harvest_tree()
				move_drone(South, East)
		elif get_pos_x() == 9:
			harvest_tree()
			move_drone(North, North)
			while get_pos_y() != 9:
				harvest_tree()
				move_drone(North, West)				
		else:
			reset()
			
def harvest_all():
	while True:
		if get_entity_type() != Entities.Tree or get_entity_type() == Entities.Bush or get_entity_type() == None:
			harvest_bush()
		elif get_entity_type() == Entities.Tree:
			harvest_tree()
		sweep_field()
		
def wood():
	while True:
		if get_pos_x() == 0 and get_pos_y() == 0 or ((get_pos_x() == 9 and get_pos_y() == 9) and can_harvest() == True):
			reset()
            trees()
		elif (get_pos_x() == 9 and get_pos_y() == 9) and can_harvest() == False:
			harvest_all()
        else:
			reset()
			
wood()