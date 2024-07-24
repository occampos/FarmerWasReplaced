def plant_sunflower():
	if num_items(Items.Sunflower_seed) == 0:
		trade(Items.Sunflower_seed)
	plant(Entities.Sunflower)
		
def sunflower():
	while True:
		if (get_pos_x() == 0 and get_pos_y() == 0) and (can_harvest() == False):
			while True:
				if get_entity_type() == None:
					plant_sunflower()
				if measure() != 15:
					till()
					plant_sunflower()
				if measure() == 15:
					sweep_field()
				if (get_pos_x() == 0 and get_pos_y() == 0) and (can_harvest() == True):
					break
		if (get_pos_x() == 0 and get_pos_y() == 0) and (can_harvest() == True):
			while True:
				harvest()
				sweep_field()
				if (get_pos_x() == 0 and get_pos_y() == 0) and can_harvest() == False:
					break
		elif get_pos_x() != 0 or get_pos_y() != 0:
			reset()