def study_schedule(permanence_period, target_time):
    try:
        float(target_time)
        contador = 0
        for entry, study_exit in permanence_period:
            if entry <= target_time <= study_exit:
                contador += 1
        return contador
    except TypeError:
        return None
