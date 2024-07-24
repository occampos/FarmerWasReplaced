def plant_carrot():
	if num_items(Items.Carrot_Seed) == 0:
		trade(Items.Carrot_Seed)
	plant(Entities.Carrots)
			
def carrot():
	while True:
		if get_entity_type() != Entities.Carrots and get_entity_type() != None:
			if can_harvest():
				harvest()
			while True:
				if get_entity_type() == None:
					plant_carrot()
					break
				else:
					till()
		if get_entity_type() == None:
			plant_carrot()
		else:
			if can_harvest():
				harvest()
				plant_carrot()
			
		sweep_field()
	