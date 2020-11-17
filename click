def setup():
    size(400,400)
def draw():
    fill(value)
    fill("#9EB712")
    if mousePressed and (mouseButton == LEFT):
        fill(0)
    elif mousePressed and (mouseButton == RIGHT):
        fill(255)
    else:
        fill(126)
    ellipse(200,200,100,100)
