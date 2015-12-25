DESTDIR =

all:
	DESTDIR=$(DESTDIR) python setup.py build
	DESTDIR=$(DESTDIR) python3 setup.py build

clean:
	find . -name __PYCACHE__ -o -name "*.pyc" | xargs rm -rf
	rm -rf build

install:
	python setup.py install --install-layout=deb \
	         --root=$(DESTDIR)/ --prefix=/usr
	python3 setup.py install --install-layout=deb \
	         --root=$(DESTDIR)/ --prefix=/usr

.PHONY: all clean install
