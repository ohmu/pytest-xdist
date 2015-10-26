all:
	: try "make rpm"

rpm:
	git archive --output=rpmpkg-src.tar --prefix=pytest-xdist/ HEAD
	# create xdist/_version.py and add it to the tar, it's not in git repository
	echo "version = '$(shell git describe --tags --long)'" > xdist/_version.py
	tar -r -f rpmpkg-src.tar --transform=s,xdist,pytest-xdist/xdist, xdist/_version.py
	rpmbuild -bb pytest-xdist.spec \
		--define '_rpmdir $(shell pwd)' \
		--define '_sourcedir $(shell pwd)' \
		--define 'major_version $(shell git describe --tags --abbrev=0 | cut -c2-)' \
		--define 'minor_version $(subst -,.,$(shell git describe --tags --long | cut -f2- -d-))'
	$(RM) rpmpkg-src.tar
