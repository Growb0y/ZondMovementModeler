import numpy as np


def make_points_list(v0=10, v_plane=0, g=9.8):

    print(9)
    points_list = []
    t = 0

    time_to_open_parachute = v0/abs(g)
    moving_down = False
    moving_down_speed = v0/7

    # Максимальная высота
    H = v0*v0 / (2 * abs(g))
    print("H: ", H)

    time = time_to_open_parachute + H / moving_down_speed
    print("sum_time: ", time)

    points_count = 200
    time_delta = time / points_count

    if v_plane == 0:
        alpha = 0
    else:
        alpha = np.arctan(v0/v_plane)
    print("alpha: ", alpha)

    # Дальность полёта
    L = v0 * v0 * np.sin(2 * alpha) / abs(g) / 2
    print("L: ", L)

    x = 0
    y = 0
    i = 0

    while True:

        if t > time_to_open_parachute * 1.05:
            moving_down = True

        if moving_down:
            y -= moving_down_speed * time_delta
        else:
            x += v_plane * time_delta
            y = v0 * t - abs(g) * t*t / 2
        i += 1
        print(x, ' ', y, ' ', i)
        points_list.append((x, y, t))
        if y < 0:
            break
        t += time_delta

    print("Real times passes (in seconds): ", t)
    return points_list, time, H, L
