def plant_pumpkin():
	if num_items(Items.Pumpkin_Seed) == 0:
		trade(Items.Pumpkin_Seed)
	plant(Entities.Pumpkin)

def pumpkin():
	p = 0
	while True:
		if num_items(Items.Carrot) < 100:
			break
	
		if get_entity_type() != Entities.Pumpkin and get_entity_type() != None:
			if can_harvest():
				harvest()
			while True:
				if get_entity_type() == None:
					plant_pumpkin()
					break
				else:
					till()
		if get_entity_type() == None:
			plant_pumpkin()
	
		if get_pos_x() == 0 and get_pos_y() == 0:
			p = 0
		if can_harvest() == True:
			p = p + 1
		if p == grid_width ** 2:
			harvest()
	        
		sweep_field()