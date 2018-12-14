import turtle
import json

with open("import.geojson", encoding='utf-8') as f:
    file = json.loads(f.read())
    features = file['features']
    print(features)

def get_x_half(data):
    """ Rozdeli data na pul podle souradnice

    Vraci = souradnici, podle ktere data rozdelit"""
    #rozdridime dvourozmerna data
    # trid podle x-ove souradnice
    data = sorted(data, key=lambda x: x[0])
    half = len(data)//2
    return (data[half][0]+data[half-1][0])/2

def get_y_half(data):
    data = sorted(data, key=lambda y: y[1])
    half = len(data)//2
    return (data[half][1]+data[half-1][1])/2
def bbox(data):
    minx = float("inf")
    miny = float("inf")
    maxx = float("inf")
    maxy = float("inf")

    if p[0] > maxx:
        maxx = p[0]
    if p[0] < minx:
        minx = p[0]
    if p[1] > maxy:
        maxy = p[1]
    if p[1] < miny:
        miny = p[1]

def split_x(data, x):
    p = []
    q = []
    for pt in data:
        if pt[0] < x:
            p.append()
    for pt in data:
        if pt[0] > x:
            q.append()
    return p,q


def split_y(data, y):
    p = []
    q = []
    for pt in data:
        if pt[1] < y:
            p.append()
    for pt in data:
        if pt[1] > y:
            q.append()
    return p,q

def draw(data,x,y,dir):
    bbox = calc_bbox(data)
    turtle.setposition(x*300,y*300)
    if x:
        turtle.setposition(x*300,bbox[1]*300)
        turtle.pendown()
        turtle.setposition(x*300,bbox[3]*300)
    if y:
        turtle.setposition(bbox[0]*300,y*300)
        turtle.pendown()
        turtle.setposition(bboy[2]*300,y*300)
    turtle.penup()

turtle.speed(0)





data = generate_data()
show_data(data)
# Sem vlozte kod pro clusterovani
x = get_x_half(data)
y = get_y_half(data)

turtle.setposition(x*300, 0)
turtle.pendown()
turtle.setposition(x*300, 300)
turtle.setposition(300*x, 300*y)
turtle.setposition(0,300*y)
turtle.setposition(300, 300*y)
turtle.exitonclick()





