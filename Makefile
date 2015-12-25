DESTDIR =

all:    docs
	DESTDIR=$(DESTDIR) python setup.py build
	DESTDIR=$(DESTDIR) python3 setup.py build

docs:
	make -C docs dirhtml

clean:
	find . -name __PYCACHE__ -o -name "*.pyc" | xargs rm -rf
	rm -rf build
	make -C docs clean

install:
	python setup.py install --install-layout=deb \
	         --root=$(DESTDIR)/ --prefix=/usr
	python3 setup.py install --install-layout=deb \
	         --root=$(DESTDIR)/ --prefix=/usr

.PHONY: all docs clean install
