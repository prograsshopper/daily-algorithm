def solution(a, b):
    from datetime import date
    date_dict = {0 : "MON",1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN"}
    return date_dict[date(2016, a, b).weekday()]