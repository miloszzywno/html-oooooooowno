from math import sqrt, ceil

def f(x):
    return (500 / 4) - (200 / 2) * x - x**2

def g(x):
    return (30 / 3) - (20 / 2) + x + x**3

x_start = 2
x_end = 10
y_bottom = -32
y_top = 19

def calculate_area():
    rectangle_area = (x_end - x_start) * (y_top - y_bottom)
    def integrate(func):
        step = 0.001
        total = 0
        x = x_start
        while x < x_end:
            total += func(x) * step
            x += step
        return total
    area_f = integrate(f)
    area_g = integrate(g)
    curtain_area = area_f - area_g
    return round(rectangle_area - curtain_area, 3)

def calculate_perimeter():
    n = 1000
    step = (x_end - x_start) / n
    length_f = 0
    length_g = 0
    x = x_start
    while x < x_end:
        x_next = x + step
        length_f += sqrt((x_next - x)**2 + (f(x_next) - f(x))**2)
        length_g += sqrt((x_next - x)**2 + (g(x_next) - g(x))**2)
        x = x_next
    top_side = x_end - x_start
    bottom_side = x_end - x_start
    left_side = f(x_start) - g(x_start)
    return ceil(length_f + length_g + top_side + bottom_side + abs(left_side))

def calculate_strip_length(remaining_area):
    strip_width = 0.25
    strip_count = remaining_area // strip_width
    return int(strip_count * (x_end - x_start))

if __name__ == "__main__":
    remaining_area = calculate_area()
    print(f"70.1. {remaining_area}")
    perimeter = calculate_perimeter()
    print(f"70.2. {perimeter}")
    strip_length = calculate_strip_length(remaining_area)
    print(f"70.3. {strip_length}")
