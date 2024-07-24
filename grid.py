def grid():
	while True:
		x_pos_before = get_pos_x()
		move(East)
		x_pos_after = get_pos_x()
		
		if x_pos_before - x_pos_after > 1:
			return(x_pos_before + 1)