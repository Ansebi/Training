def score_counter(percentage, minutes_elapsed, seconds_elapsed, correct, incorrect):
    calc_time = minutes_elapsed * 60
    calc_time += seconds_elapsed
    calc_time += 1
    speed_impact = correct / calc_time
    speed_impact *= 100  # so that 100 sec turns into 1
    # it gives 10 correct 5 sec each the perfect score of 100

    work = correct ** 2
    bad_work = incorrect ** 2
    correctness = (percentage / 100) ** 2

    score = work
    score -= bad_work
    score *= correctness
    score *= speed_impact
    score = int(round(score, 0))

    return score
