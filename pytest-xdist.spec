Name:           python-pytest-xdist
Version:        %{major_version}
Release:        %{minor_version}%{?dist}
Url:            https://bitbucket.org/pytest-dev/pytest-xdist
Summary:        pytest 2 distributed testing plugin
License:        MIT
Source0:        rpmpkg-src.tar
Requires:	python-execnet
BuildArch:      noarch

%description
The pytest-xdist plugin extends py.test with some unique test execution
modes:

 * test run parallelization: if you have multiple CPUs or hosts you can use
   those for a combined test run.  This allows to speed up development or to
   use special resources of remote machines.
 * --boxed: (not available on Windows) run each test in a boxed subprocess
   to survive SEGFAULTS or otherwise dying processes
 * --looponfail: run your tests repeatedly in a subprocess.  After each run
   py.test waits until a file in your project changes and then re-runs the
   previously failing tests.  This is repeated until all tests pass after
   which again a full run is performed.
 * Multi-Platform coverage: you can specify different Python interpreters or
   different platforms and run tests in parallel on all of them.

Before running tests remotely, py.test efficiently "rsyncs" your program
source code to the remote place.  All test results are reported back and
displayed to your local terminal.  You may specify different Python versions
and interpreters.


%if %{?python3_sitelib:1}0
%package -n     python3-pytest-xdist
Summary:        pytest 3 distributed testing plugin
Requires:	python3-execnet
BuildArch:      noarch

%description -n python3-pytest-xdist
The pytest-xdist plugin extends py.test with some unique test execution
modes:

 * test run parallelization: if you have multiple CPUs or hosts you can use
   those for a combined test run.  This allows to speed up development or to
   use special resources of remote machines.
 * --boxed: (not available on Windows) run each test in a boxed subprocess
   to survive SEGFAULTS or otherwise dying processes
 * --looponfail: run your tests repeatedly in a subprocess.  After each run
   py.test waits until a file in your project changes and then re-runs the
   previously failing tests.  This is repeated until all tests pass after
   which again a full run is performed.
 * Multi-Platform coverage: you can specify different Python interpreters or
   different platforms and run tests in parallel on all of them.

Before running tests remotely, py.test efficiently "rsyncs" your program
source code to the remote place.  All test results are reported back and
displayed to your local terminal.  You may specify different Python versions
and interpreters.
%endif


%prep
%setup -q -n pytest-xdist


%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%if %{?python3_sitelib:1}0
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%endif


%check
#python2 -m pytest -vvv  -c /dev/null
%if %{?python3_sitelib:1}0
#python3 -m pytest -vvv  -c /dev/null
%endif


%files
%defattr(-,root,root,-)
%doc CHANGELOG  ISSUES.txt LICENSE README.txt
%{python_sitelib}/*

%if %{?python3_sitelib:1}0
%files -n python3-pytest-xdist
%defattr(-,root,root,-)
%doc CHANGELOG  ISSUES.txt LICENSE README.txt
%{python3_sitelib}/*
%endif


%changelog
* Mon Oct 26 2015 Oskari Saarenmaa <os@ohmu.fi> - 1.13.1-0
- Initial
