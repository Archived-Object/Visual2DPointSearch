import pygame

#graphical definition variables
MARGINS = Point(20,20)
WINDOW = (Point(0,0),Point(800,600))

POINT_RADIUS = 5

COLOR_BACKGROUND = pygame.color.Color(20,20,20)
COLOR_POINT = pygame.color.Color(220,221,216)
COLOR_POINT_HILIGHT = pygame.color.Color(215,75,75)


class Point(object):

	def __init__ (self, x ,y):
		self.x, self.y = x,y
		self.hilighted = False

	def render(surface, zoom, offset):
		pygame.gfxdraw.aacircle(surface,
				int(zoom*(x-offset.x)),
				int(zoom*(y-offset.y)),
				POINT_RADIUS,
				(COLOR_POINT_HILIGHT if self.hilighted else COLOR_POINT)
				)


def resize_window(points):
	'''
	Takes a list of points and finds the new dimensions of the window.
	Margin defined in global variable MARGINS
	'''
	upper_left = Point(point[0].x, point[0].y)
	lower_right = Point(point[0].x, point[0].y)
	for point in points:
		if(point.x< upper_left.x):
			upper_left.x = point.x
		if(point.x>lower_right.x):
			upper_left.x = point.x
		if(point.y< upper_left.y):
			upper_left.y = point.y
		if(point.y>lower_right.y):
			upper_left.y = point.y

	upper_left.x = upper_left.x-MARGINS.x
	upper_left.y = upper_left.y-MARGINS.y
	lower_right.x = lower_right.x-MARGINS.x
	lower_right.y = lower_right.y-MARGINS.y


def recursive_visual_search(points):
	pass


def main():
	points = collect_points(window)


if __name__ == "__main__":
	main()