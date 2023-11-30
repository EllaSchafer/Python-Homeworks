import math as m
class Point:
    """
    represents a point in space
    attribures: x and y
    """
class Circle:
    """
    represents a circle
    attributes: center (point), radius
    """
class Rectangle:
    """
    represents a rectangle, 
    attributes: width, height, lower left corner

    """

circle_1 = Circle()
circle_1.radius = 5

circle_1.center = Point()
circle_1.center.x = 4
circle_1.center.y = 4

point_check = Point()
point_check.x = 3
point_check.y = 3

rectangle_1 = Rectangle
rectangle_1.height = 1
rectangle_1.width  = 1
rectangle_1.corner = Point()
rectangle_1.corner.x = 40
rectangle_1.corner.y = 40

def point_in_circle(circle,point):
    """
    if distance from pt to center is shorter than radius it is in the circle
    distance btwn 2 points = sqrt((x-x)^2+(y-y)^2)
    """
    x_diff = circle.center.x - point.x
    y_diff = circle.center.y - point.y
    dist = m.sqrt(x_diff**2+y_diff**2)
    return dist < circle.radius


def rect_in_circle(circle, rectangle):
    """
    checks if an entire rectangle is in a circle
    r_bl = bottom left corner
    r_br = bottom right corner
    r_tl = top left corner
    r_tr = top right corner
    """
    # initializes points
    r_bl = Point()
    r_br = Point()
    r_tl = Point()
    r_tr = Point()

    # gets numbers for bl
    r_bl.x = rectangle.corner.x
    r_bl.y = rectangle.corner.y

    # gets numbers for br
    r_br.x = rectangle.corner.x + rectangle.width
    r_br.y = rectangle.corner.y

    # gets numbers for tl
    r_tl.x = rectangle.corner.x
    r_tl.y = rectangle.corner.y + rectangle.height

    # gets numbers for tr
    r_tr.x = rectangle.corner.x + rectangle.width
    r_tr.y = rectangle.corner.y + rectangle.height
    
    
    list_points = [r_bl,r_br,r_tl,r_tr]
    bool_check = []
    b = 0
    for point in list_points:
        if not point_in_circle(circle,point):
            b = 1
            return False
    if b == 0:
        return True
    

def rect_circle_overlap_1(circle, rectangle):
    """
    checks if an entire rectangle is in a circle
    r_bl = bottom left corner
    r_br = bottom right corner
    r_tl = top left corner
    r_tr = top right corner
    """
    # initializes points
    r_bl = Point()
    r_br = Point()
    r_tl = Point()
    r_tr = Point()

    # gets numbers for bl
    r_bl.x = rectangle.corner.x
    r_bl.y = rectangle.corner.y

    # gets numbers for br
    r_br.x = rectangle.corner.x + rectangle.width
    r_br.y = rectangle.corner.y

    # gets numbers for tl
    r_tl.x = rectangle.corner.x
    r_tl.y = rectangle.corner.y + rectangle.height

    # gets numbers for tr
    r_tr.x = rectangle.corner.x + rectangle.width
    r_tr.y = rectangle.corner.y + rectangle.height
    
    list_points = [r_bl,r_br,r_tl,r_tr]
    b = 0
    for point in list_points:
        if point_in_circle(circle,point):
            b = 1
            return True
    if b == 0:
        return False

def side_overlap(side,center, radius):
    dist = abs(side-center)
    return dist < radius
def rect_circle_overlap_2(circle, rectangle):
    """
    r_x_l = left side
    r_x_r = right side
    r_y_b = bottom side
    r_y_t = top side
    """
    point_check = rect_in_circle(circle,rectangle)
    if point_check:
        return True
    else:
        r_x_l = rectangle.corner.x
        r_x_r = rectangle.corner.x + rectangle.width
        r_y_b = rectangle.corner.y 
        r_y_t = rectangle.corner.y + rectangle.height
        return side_overlap(r_x_l, circle.center.x, circle.radius) or \
            side_overlap(r_x_r, circle.center.x, circle.radius) or \
            side_overlap(r_y_t, circle.center.y, circle.radius) or \
            side_overlap(r_y_b, circle.center.y, circle.radius)
    


        
print(point_in_circle(circle_1,point_check))
print(rect_in_circle(circle_1,rectangle_1))
print(rect_circle_overlap_1(circle_1,rectangle_1))
print(rect_circle_overlap_2(circle_1,rectangle_1))