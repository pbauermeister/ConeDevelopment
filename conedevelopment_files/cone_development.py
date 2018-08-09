
cone_development_lengths = []
cone_development_total_angle = 0

def set(lengths, total_angle):
    global cone_development_lengths
    global cone_development_total_angle
    cone_development_lengths = lengths
    cone_development_total_angle = total_angle

def get():
    return cone_development_lengths, cone_development_total_angle
