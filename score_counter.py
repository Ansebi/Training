def score_counter(score,percentage,minutes_elapsed,seconds_elapsed,correct,incorrect):
    

    
    calc_time=minutes_elapsed*60
    calc_time+=seconds_elapsed
    calc_time=1+calc_time
    
    speed_impact=correct/calc_time
    speed_impact*=100 #so that 100 sec turns into 1
    #it gives 10 correct 5 sec each the perfect score of 100
  
    
    work=correct**2
    bad_work=incorrect**2
     

    correctness=(percentage/100)**2
    

    score=work
    score-=bad_work
    score*=correctness
    score*=speed_impact
    score/=10
    score=int(round(score,0))

    diag_mode='OFF'
    if diag_mode=='ON':
        print('minutes',minutes_elapsed)
        print('seconds',seconds_elapsed)
        print('time',calc_time)
        print('speed',speed_impact)
        print('correct',correct)
        print('work',work)
        print('bad work',bad_work)
        print('correctness',correctness)
    
    
    
    score_counter.score=score
