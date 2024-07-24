def sweep_field():
    x = get_pos_x()
    y = get_pos_y()
    
    wrap_around = (grid_width - 1) - x
    
    if y == wrap_around:
        move(East)
    else:
        move(North)