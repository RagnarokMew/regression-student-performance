all:
	pandoc README \
  	-o my.pdf \
  	-f markdown-implicit_figures
