def score_counter(
        standard_completion_time_sec,
        percentage,
        minutes_elapsed,
        seconds_elapsed,
        correct,
        incorrect,
        k=10):
    calc_time = minutes_elapsed * 60
    calc_time += seconds_elapsed
    calc_time += 1
    speed_impact = standard_completion_time_sec * correct / calc_time

    work = correct ** 2
    bad_work = incorrect ** 2
    correctness = (percentage / 100) ** 2

    score = work
    score -= bad_work
    score *= correctness
    score *= speed_impact
    score *= k  # purely cosmetic adjustment
    score = int(round(score, 0))

    return score
