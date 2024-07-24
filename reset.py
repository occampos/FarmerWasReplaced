def reset():
	while True:
		if get_pos_x() == 0 and get_pos_y() == 0:
			break
		sweep_field()