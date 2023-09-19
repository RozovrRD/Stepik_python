from math import sqrt, acos, degrees

# Direction = 0 means down_start_direction
# Direction = 1 means up_start_direction
# position = 1 means right_end_direction
# position = 2 means left_end_direction
# position = 3 means down_end_direction
# position = 4 means up_end_direction

def direction_angle(angle, direction, position):
    if direction == 0:
        if position == 1:
            pass
        elif position == 2:
            pass
        elif position == 3:
            pass
        elif position == 4:
            pass
        else:
            print('Value error: input position doesnt exist')




def bag_coord_and_angles(x, y, lenght, width, height, direction, first_bag_pos, another_bag_pos):
    delta_for_balance = abs((lenght - 2*width))/3 if width < lenght/2 else 0
    Yx, Yy = 0, 1
    first_bag_angle = round(degrees(acos((Yx*x+Yy*y) / (sqrt(Yx * Yx + Yy * Yy)) / (sqrt(x * x + y * y)))), 2)

    M = [x, y, first_bag_angle]
    M1 = [round(float(x-delta_for_balance/2 - width/2), 2), round(float(y+lenght/2 + width/2), 2)]
    M2 = [round(float(x + delta_for_balance / 2 + width / 2), 2), round(float(y + lenght / 2 + width / 2), 2)]
    N = [round(float(x), 2), round(float(y + lenght), 2)]
    N1 = [round(float(x - delta_for_balance / 2 - width / 2), 2), round(float(y + lenght / 2 - width / 2), 2)]
    N2 = [round(float(x + delta_for_balance / 2 + width / 2), 2), round(float(y + lenght / 2 - width / 2), 2)]

    for i in [M1, M2, N, N1, N2]:
        bag_angle = round(degrees(acos((Yx*i[0]+Yy*i[1]) / (sqrt(Yx * Yx + Yy * Yy)) / (sqrt(i[0]**2 + i[1]**2)))), 2)
        i.append(bag_angle)
    return M, M1, M2, N, N1, N2

print(*bag_coord_and_angles(200, 50, 500, 300, 150))
1
