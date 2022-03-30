#
# Conditional build:
# we are missing the 'expects' library to run the tests
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	dockerpty
Summary:	Python library to use the pseudo-tty of a docker container
Name:		python-%{module}
Version:	0.4.1
Release:	10
License:	Apache v2.0
Group:		Development/Libraries
Source0:	https://github.com/d11wtq/%{module}/archive/98c85b13/%{module}-98c85b13.tar.gz
# Source0-md5:	076876e830e29135214a2091b4b69c00
URL:		https://github.com/d11wtq/dockerpty
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-six
%endif
%if %{with python3}
BuildRequires:	python3-six
%endif
Requires:	python-docker
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides the functionality needed to operate the pseudo-tty (PTY)
allocated to a docker container, using the Python client

%package -n python3-%{module}
Summary:	Python library to use the pseudo-tty of a docker container
Group:		Development/Languages
Requires:	python3-docker

%description -n python3-%{module}
Provides the functionality needed to operate the pseudo-tty (PTY)
allocated to a docker container, using the Python client

%prep
%setup -qc
mv %{module}-*/* .

%build
%if %{with python3}
%py_build
%if %{with tests}
LANG=en_US.utf8 py.test-%{py_ver} -vv tests
%endif
%endif

%if %{with python3}
%py3_build
%if %{with tests}
LANG=en_US.utf8 py.test-%{py3_ver} -vv tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md LICENSE.txt MANIFEST.in
%{py_sitescriptdir}/dockerpty
%{py_sitescriptdir}/dockerpty-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.md LICENSE.txt MANIFEST.in
%{py3_sitescriptdir}/dockerpty
%{py3_sitescriptdir}/dockerpty-%{version}-py*.egg-info
%endif
