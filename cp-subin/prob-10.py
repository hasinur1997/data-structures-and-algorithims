T = int(input())

def format_number(number):
    return "{:.2f}".format(number)


while T > 0:
    r1 = int(input())
    r2 = int(input())
    B = int(input())

    total_over = 50
    total_left_over = B / 6
    total_playing_over = total_over - total_left_over
    total_required_run = (r1 + 1) - r2

    current_run_rate = r2 / total_playing_over
    required_run_rate = total_required_run / total_left_over

    print(f"{format_number(current_run_rate)} {format_number(required_run_rate)}")

    T -= 1