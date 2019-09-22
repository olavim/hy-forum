import os
import sys
import sass
from application.main import manager, start_server

sass_map = {'application/static/scss/default.scss': 'application/static/css/default.css'}

def compile_sass_to_css(sass_map):
	print("Compiling scss to css:")

	for source, dest in sass_map.items():
		if not os.path.exists(os.path.dirname(dest)):
			os.makedirs(os.path.dirname(dest))

		with open(dest, 'w') as outfile:
			outfile.write(sass.compile(filename=source, output_style='compressed'))

		print('%s compiled to %s' % (source, dest))

def build_styles():
	compile_sass_to_css(sass_map)

if __name__ == '__main__':
	# If first command line argument is 'db', we are working with migrations
	if len(sys.argv) > 1 and sys.argv[1] == 'db':
		manager.run()
	else:
		build_styles()
		start_server()
