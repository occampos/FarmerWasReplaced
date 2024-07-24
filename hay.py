def hay():
    while True:
        if can_harvest():
			harvest()
			plant(Entities.Grass)
		if get_entity_type() != Entities.Grass:
            plant(Entities.Grass) 
		sweep_field()