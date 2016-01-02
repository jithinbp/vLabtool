DESTDIR =

all:    docs
	DESTDIR=$(DESTDIR) python setup.py build
	DESTDIR=$(DESTDIR) python3 setup.py build

docs:
	make -C docs html

clean:
	find . -name __PYCACHE__ -o -name "*.pyc" -o -name *~ | xargs rm -rf
	rm -rf build vLabtool.egg-info
	make -C docs clean

IMAGEDIR=$(DESTDIR)/usr/share/docs/vlabtool/images

install:
	python setup.py install --install-layout=deb \
	         --root=$(DESTDIR)/ --prefix=/usr
	python3 setup.py install --install-layout=deb \
	         --root=$(DESTDIR)/ --prefix=/usr
	mkdir -p $(IMAGEDIR)
	mv $(DESTDIR)/usr/lib/python2.7/dist-packages/vLabtool/stylesheets/*.png $(IMAGEDIR)
	rm -f $(DESTDIR)/usr/lib/python3/dist-packages/vLabtool/stylesheets/*.png
	for f in $(IMAGEDIR)/*.png; do \
	  ln -rs $$f $(DESTDIR)/usr/lib/python2.7/dist-packages/vLabtool/stylesheets/ ; \
	  ln -rs $$f $(DESTDIR)/usr/lib/python3/dist-packages/vLabtool/stylesheets/ ; \
	done

.PHONY: all docs clean install
