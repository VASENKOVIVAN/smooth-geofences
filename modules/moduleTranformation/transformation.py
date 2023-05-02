""" docstring """
import traceback
import math
import numpy as np
from modules.moduleTranformation.converter import mercator_to_wgs84, wgs84_to_mercator
from config import VALUE_ROUNDED, VALUE_ROUND_PARAMETR, REVERSE_LAT_LON


point_of_center_circle_arr = []


def where_is_point_of_short_side_h(short_side, arr_point, i):
    """ docstring """
    if short_side == "prev":
        if arr_point[i - 1][0] < arr_point[i][0]:
            return "left"
        else:
            return "right"
    else:
        if arr_point[i + 1][0] < arr_point[i][0]:
            return "left"
        else:
            return "right"


def where_is_point_of_short_side_v(short_side, arr_point, i):
    """ docstring """
    if short_side == "prev":
        if arr_point[i - 1][1] < arr_point[i][1]:
            return "down"
        else:
            return "up"
    else:
        if arr_point[i + 1][1] < arr_point[i][1]:
            return "down"
        else:
            return "up"


def where_is_point_of_long_side_h(short_side, arr_point, i):
    """ docstring """
    if short_side == "prev":
        if arr_point[i + 1][0] < arr_point[i][0]:
            return "left"
        else:
            return "right"
    else:
        if arr_point[i - 1][0] < arr_point[i][0]:
            return "left"
        else:
            return "right"


def where_is_point_of_long_side_v(short_side, arr_point, i):
    """ docstring """
    if short_side == "prev":
        if arr_point[i + 1][1] < arr_point[i][1]:
            return "down"
        else:
            return "up"
    else:
        if arr_point[i - 1][1] < arr_point[i][1]:
            return "down"
        else:
            return "up"


def point_of_short_side(short_side, arr_point, i):
    """ docstring """
    x = 0
    y = 0
    if short_side == "prev":
        if where_is_point_of_short_side_h(short_side, arr_point, i) == "left":
            x = (
                arr_point[i][0]
                - abs(arr_point[i][0] - arr_point[i - 1][0])
                * VALUE_ROUNDED
            )
        else:
            x = (
                arr_point[i][0]
                + abs(arr_point[i][0] - arr_point[i - 1][0])
                * VALUE_ROUNDED
            )
        if where_is_point_of_short_side_v(short_side, arr_point, i) == "down":
            y = (
                arr_point[i][1]
                - abs(arr_point[i][1] - arr_point[i - 1][1])
                * VALUE_ROUNDED
            )
        else:
            y = (
                arr_point[i][1]
                + abs(arr_point[i][1] - arr_point[i - 1][1])
                * VALUE_ROUNDED
            )
    else:
        if where_is_point_of_short_side_h(short_side, arr_point, i) == "left":
            x = (
                arr_point[i][0]
                - abs(arr_point[i][0] - arr_point[i + 1][0])
                * VALUE_ROUNDED
            )
        else:
            x = (
                arr_point[i][0]
                + abs(arr_point[i][0] - arr_point[i + 1][0])
                * VALUE_ROUNDED
            )
        if where_is_point_of_short_side_v(short_side, arr_point, i) == "down":
            y = (
                arr_point[i][1]
                - abs(arr_point[i][1] - arr_point[i + 1][1])
                * VALUE_ROUNDED
            )
        else:
            y = (
                arr_point[i][1]
                + abs(arr_point[i][1] - arr_point[i + 1][1])
                * VALUE_ROUNDED
            )

    return [x, y]


def lenght_from_now_point_to_procent_point_of_short_side(now_x, now_y, short_point):
    """ docstring """
    return (
        (now_x - short_point[0]) ** 2 +
        (now_y - short_point[1]) ** 2
    ) ** 0.5


def procent_lenght_for_long_side(short_side, arr_point, i, len_to_next, len_to_prew):
    """ docstring """
    if short_side == "prev":
        return len_to_next / lenght_from_now_point_to_procent_point_of_short_side(
            arr_point[i][0], arr_point[i][1], point_of_short_side(
                short_side, arr_point, i)
        )
    else:
        return len_to_prew / lenght_from_now_point_to_procent_point_of_short_side(
            arr_point[i][0], arr_point[i][1], point_of_short_side(
                short_side, arr_point, i)
        )


def procent_lenght_for_short_side(short_side, arr_point, i, len_to_next, len_to_prew):
    """ docstring """
    if short_side == "prev":
        return len_to_prew / lenght_from_now_point_to_procent_point_of_short_side(
            arr_point[i][0], arr_point[i][1], point_of_short_side(
                short_side, arr_point, i)
        )
    else:
        return len_to_next / lenght_from_now_point_to_procent_point_of_short_side(
            arr_point[i][0], arr_point[i][1], point_of_short_side(
                short_side, arr_point, i)
        )


def point_of_long_side(short_side, arr_point, i, len_to_next, len_to_prew):
    """ docstring """
    x = 0
    y = 0
    if short_side == "prev":
        if where_is_point_of_long_side_h(short_side, arr_point, i) == "left":
            x = (
                arr_point[i][0]
                - abs(arr_point[i + 1][0] - arr_point[i][0])
                / procent_lenght_for_long_side(short_side, arr_point, i, len_to_next, len_to_prew)
            )
        else:
            x = (
                arr_point[i][0]
                + abs(arr_point[i + 1][0] - arr_point[i][0])
                / procent_lenght_for_long_side(short_side, arr_point, i, len_to_next, len_to_prew)
            )
        if where_is_point_of_long_side_v(short_side, arr_point, i) == "down":
            y = (
                arr_point[i][1]
                - abs(arr_point[i + 1][1] - arr_point[i][1])
                / procent_lenght_for_long_side(short_side, arr_point, i, len_to_next, len_to_prew)
            )
        else:
            y = (
                arr_point[i][1]
                + abs(arr_point[i + 1][1] - arr_point[i][1])
                / procent_lenght_for_long_side(short_side, arr_point, i, len_to_next, len_to_prew)
            )
    else:
        if where_is_point_of_long_side_h(short_side, arr_point, i) == "left":
            x = (
                arr_point[i][0]
                - abs(arr_point[i][0] - arr_point[i - 1][0])
                / procent_lenght_for_long_side(short_side, arr_point, i, len_to_next, len_to_prew)
            )
        else:
            x = (
                arr_point[i][0]
                + abs(arr_point[i - 1][0] - arr_point[i][0])
                / procent_lenght_for_long_side(short_side, arr_point, i, len_to_next, len_to_prew)
            )
        if where_is_point_of_long_side_v(short_side, arr_point, i) == "down":
            y = (
                arr_point[i][1]
                - abs(arr_point[i][1] - arr_point[i - 1][1])
                / procent_lenght_for_long_side(short_side, arr_point, i, len_to_next, len_to_prew)
            )
        else:
            y = (
                arr_point[i][1]
                + abs(arr_point[i - 1][1] - arr_point[i][1])
                / procent_lenght_for_long_side(short_side, arr_point, i, len_to_next, len_to_prew)
            )
    return [x, y]


def equation_of_short_side(short_side, arr_point, i):
    """ docstring """
    if short_side == "prev":
        ABx = (arr_point[i - 1][1] - arr_point[i][1]) / (
            arr_point[i - 1][0] - arr_point[i][0]
        )
        ABc = arr_point[i][1] - ABx * arr_point[i][0]
        return (ABx, ABc)
    else:
        ABx = (arr_point[i + 1][1] - arr_point[i][1]) / (
            arr_point[i + 1][0] - arr_point[i][0]
        )
        ABc = arr_point[i][1] - ABx * arr_point[i][0]
        return (ABx, ABc)


def equation_of_long_side(short_side, arr_point, i):
    """ docstring """
    if short_side == "next":
        ABx = (arr_point[i - 1][1] - arr_point[i][1]) / (
            arr_point[i - 1][0] - arr_point[i][0]
        )
        ABc = arr_point[i][1] - ABx * arr_point[i][0]
        return (ABx, ABc)
    else:
        ABx = (arr_point[i + 1][1] - arr_point[i][1]) / (
            arr_point[i + 1][0] - arr_point[i][0]
        )
        ABc = arr_point[i][1] - ABx * arr_point[i][0]
        return (ABx, ABc)


def perpendicular_of_short_side(short_side, arr_point, i):
    """ docstring """
    if short_side == "prev":
        xk = arr_point[i][0] - arr_point[i - 1][0]
        yk = arr_point[i][1] - arr_point[i - 1][1]
        ck = xk * (-point_of_short_side(short_side, arr_point, i)[0]) + yk * (
            -point_of_short_side(short_side, arr_point, i)[1]
        )
        return (xk, yk, ck)
    else:
        xk = arr_point[i][0] - arr_point[i + 1][0]
        yk = arr_point[i][1] - arr_point[i + 1][1]
        ck = xk * (-point_of_short_side(short_side, arr_point, i)[0]) + yk * (
            -point_of_short_side(short_side, arr_point, i)[1]
        )
        return (xk, yk, ck)


def perpendicular_of_long_side(short_side, arr_point, i, len_to_next, len_to_prew):
    """ docstring """
    if short_side == "next":
        xk = arr_point[i][0] - arr_point[i - 1][0]
        yk = arr_point[i][1] - arr_point[i - 1][1]
        ck = xk * (-point_of_long_side(short_side, arr_point, i, len_to_next, len_to_prew)
                   [0]) + yk * \
            (-point_of_long_side(short_side, arr_point,
             i, len_to_next, len_to_prew)[1])
        return (xk, yk, ck)
    else:
        xk = arr_point[i][0] - arr_point[i + 1][0]
        yk = arr_point[i][1] - arr_point[i + 1][1]
        ck = xk * (-point_of_long_side(short_side, arr_point, i, len_to_next, len_to_prew)
                   [0]) + yk * \
            (-point_of_long_side(short_side, arr_point,
             i, len_to_next, len_to_prew)[1])
        return (xk, yk, ck)


def point_of_center_circle(short_x, short_y, short_c, long_x, long_y, long_c):
    """ docstring """
    global point_of_center_circle_arr
    A = np.array([[short_x, short_y], [long_x, long_y]])
    B = np.array([-short_c, -long_c])
    X = np.linalg.solve(A, B)
    point_of_center_circle_arr = [X[0], X[1]]
    return [X[0], X[1]]


def radius_circle(short_side, arr_point, i):
    """ docstring """
    return (
        (point_of_center_circle_arr[0] -
            point_of_short_side(short_side, arr_point, i)[0]) ** 2
        + (point_of_center_circle_arr[1] -
            point_of_short_side(short_side, arr_point, i)[1]) ** 2
    ) ** 0.5


def corner_zero(short_side, arr_point, i, len_to_next, len_to_prew):
    """ docstring """
    if short_side == "prev":
        if point_of_center_circle_arr[1] < point_of_long_side(
                short_side, arr_point, i, len_to_next, len_to_prew)[1]:
            return math.acos(
                point_of_long_side(short_side, arr_point, i, len_to_next, len_to_prew)[
                    0] / radius_circle(short_side, arr_point, i)
                - point_of_center_circle_arr[0] /
                radius_circle(short_side, arr_point, i)
            ) / (math.pi / 180)
        return -math.acos(
            point_of_long_side(short_side, arr_point, i, len_to_next, len_to_prew)[
                0] / radius_circle(short_side, arr_point, i)
            - point_of_center_circle_arr[0] /
            radius_circle(short_side, arr_point, i)
        ) / (math.pi / 180)
    else:
        if point_of_center_circle_arr[1] < point_of_short_side(short_side, arr_point, i)[1]:
            return math.acos(
                point_of_short_side(short_side, arr_point, i)[
                    0] / radius_circle(short_side, arr_point, i)
                - point_of_center_circle_arr[0] /
                radius_circle(short_side, arr_point, i)
            ) / (math.pi / 180)
        else:
            return -math.acos(
                point_of_short_side(short_side, arr_point, i)[
                    0] / radius_circle(short_side, arr_point, i)
                - point_of_center_circle_arr[0] /
                radius_circle(short_side, arr_point, i)
            ) / (math.pi / 180)


def corner_angel(short_side, arr_point, i, len_to_next, len_to_prew):
    """ docstring """
    result = (
        abs(
            math.atan2(
                point_of_long_side(short_side, arr_point, i, len_to_next, len_to_prew)[1] -
                point_of_center_circle_arr[1],
                point_of_long_side(short_side, arr_point, i, len_to_next, len_to_prew)[0] -
                point_of_center_circle_arr[0],
            )
            - math.atan2(
                point_of_short_side(short_side, arr_point, i)[1] -
                point_of_center_circle_arr[1],
                point_of_short_side(short_side, arr_point, i)[0] -
                point_of_center_circle_arr[0],
            )
        )
        * 180
        / math.pi
    )
    if result > 180:
        return 360 - result
    else:
        return result


def where_is_point_to_center_circle_h(arr_point, i):
    """ docstring """
    if arr_point[i][0] < point_of_center_circle_arr[0]:
        return "left"
    else:
        return "right"


def where_is_point_to_center_circle_v(arr_point, i):
    """ docstring """
    if arr_point[i][1] < point_of_center_circle_arr[1]:
        return "down"
    else:
        return "up"


def point_of_circle_2(short_side, arr_point, i, len_to_next, len_to_prew, step):
    """ docstring """
    angel_rad = 0
    if short_side == "prev":
        point_next_side = point_of_long_side(
            short_side, arr_point, i, len_to_next, len_to_prew)
    else:
        point_next_side = point_of_short_side(
            short_side, arr_point, i)
    if arr_point[i][1] > point_next_side[1]:
        if arr_point[i][0] > point_next_side[0]:
            if corner_zero(short_side, arr_point, i, len_to_next, len_to_prew) > 0:
                angel_rad = (
                    (
                        corner_zero(
                            short_side, arr_point, i, len_to_next, len_to_prew)
                        - corner_angel(short_side, arr_point, i, len_to_next,
                                       len_to_prew) / VALUE_ROUND_PARAMETR * step
                    )
                    * math.pi
                    / 180
                )
            else:
                angel_rad = (
                    (
                        corner_zero(
                            short_side, arr_point, i, len_to_next, len_to_prew)
                        + corner_angel(short_side, arr_point, i, len_to_next,
                                       len_to_prew) / VALUE_ROUND_PARAMETR * step
                    )
                    * math.pi
                    / 180
                )
        else:
            if corner_zero(short_side, arr_point, i, len_to_next, len_to_prew) > 0:
                angel_rad = (
                    (
                        corner_zero(
                            short_side, arr_point, i, len_to_next, len_to_prew)
                        + corner_angel(short_side, arr_point, i, len_to_next,
                                       len_to_prew) / VALUE_ROUND_PARAMETR * step
                    )
                    * math.pi
                    / 180
                )
            else:
                angel_rad = (
                    (
                        corner_zero(
                            short_side, arr_point, i, len_to_next, len_to_prew)
                        - corner_angel(short_side, arr_point, i, len_to_next,
                                       len_to_prew) / VALUE_ROUND_PARAMETR * step
                    )
                    * math.pi
                    / 180
                )
    else:
        if arr_point[i][0] > point_next_side[0]:
            if corner_zero(short_side, arr_point, i, len_to_next, len_to_prew) > 0:
                angel_rad = (
                    (
                        corner_zero(
                            short_side, arr_point, i, len_to_next, len_to_prew)
                        - corner_angel(short_side, arr_point, i, len_to_next,
                                       len_to_prew) / VALUE_ROUND_PARAMETR * step
                    )
                    * math.pi
                    / 180
                )
            else:
                angel_rad = (
                    (
                        corner_zero(
                            short_side, arr_point, i, len_to_next, len_to_prew)
                        + corner_angel(short_side, arr_point, i, len_to_next,
                                       len_to_prew) / VALUE_ROUND_PARAMETR * step
                    )
                    * math.pi
                    / 180
                )
        else:
            if corner_zero(short_side, arr_point, i, len_to_next, len_to_prew) > 0:
                angel_rad = (
                    (
                        corner_zero(
                            short_side, arr_point, i, len_to_next, len_to_prew)
                        + corner_angel(short_side, arr_point, i, len_to_next,
                                       len_to_prew) / VALUE_ROUND_PARAMETR * step
                    )
                    * math.pi
                    / 180
                )
            else:
                angel_rad = (
                    (
                        corner_zero(
                            short_side, arr_point, i, len_to_next, len_to_prew)
                        - corner_angel(short_side, arr_point, i, len_to_next,
                                       len_to_prew) / VALUE_ROUND_PARAMETR * step
                    )
                    * math.pi
                    / 180
                )

    return [
        point_of_center_circle_arr[0] +
        radius_circle(short_side, arr_point, i) *
        math.cos(angel_rad),
        point_of_center_circle_arr[1] +
        radius_circle(short_side, arr_point, i) *
        math.sin(angel_rad),
    ]


def transformation(arr_data):
    """ docstring """
    try:
        if REVERSE_LAT_LON:
            arr_data = [[i[1], i[0]] for i in arr_data]

        if arr_data[0] != arr_data[-1]:
            arr_data.append(arr_data[0])

        arr_point = wgs84_to_mercator(arr_data)
        result_arr_points = []

        for i in range(len(arr_point) - 1):
            if i > 0:
                len_to_prew = (
                    (arr_point[i][0] - arr_point[i - 1][0]) ** 2 +
                    (arr_point[i][1] - arr_point[i - 1][1]) ** 2
                ) ** 0.5
                len_to_next = (
                    (arr_point[i][0] - arr_point[i + 1][0]) ** 2 +
                    (arr_point[i][1] - arr_point[i + 1][1]) ** 2
                ) ** 0.5

                short_side = "prev" if len_to_prew < len_to_next else "next"

                point_of_center_circle(
                    perpendicular_of_short_side(short_side, arr_point, i)[0],
                    perpendicular_of_short_side(short_side, arr_point, i)[1],
                    perpendicular_of_short_side(short_side, arr_point, i)[2],
                    perpendicular_of_long_side(
                        short_side, arr_point, i, len_to_next, len_to_prew)[0],
                    perpendicular_of_long_side(
                        short_side, arr_point, i, len_to_next, len_to_prew)[1],
                    perpendicular_of_long_side(
                        short_side, arr_point, i, len_to_next, len_to_prew)[2],
                )

                if short_side == "prev":
                    result_arr_points.append(point_of_short_side(
                        short_side, arr_point, i)[::-1])

                    for j in range(VALUE_ROUND_PARAMETR, 1, -1):
                        result_arr_points.append(point_of_circle_2(
                            short_side, arr_point, i, len_to_next, len_to_prew, j)[::-1])

                    result_arr_points.append(point_of_long_side(
                        short_side, arr_point, i, len_to_next, len_to_prew)[::-1])

                else:
                    result_arr_points.append(point_of_long_side(
                        short_side, arr_point, i, len_to_next, len_to_prew)[::-1])

                    for j in range(VALUE_ROUND_PARAMETR, 1, -1):
                        result_arr_points.append(point_of_circle_2(
                            short_side, arr_point, i, len_to_next, len_to_prew, j)[::-1])

                    result_arr_points.append(point_of_short_side(
                        short_side, arr_point, i)[::-1])

            else:
                result_arr_points.append(arr_point[0][::-1])

        get_back = mercator_to_wgs84(result_arr_points)
        print("\n2) Зона была успешно преобразована")
        return get_back
    except Exception:
        print("Ошибка:\n", traceback.format_exc())
