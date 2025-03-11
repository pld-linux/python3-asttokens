#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Annotate AST trees with source code positions
Summary(pl.UTF-8):	Oznaczanie drzew AST lokalizacją w kodzie źródłowym
Name:		python-asttokens
Version:	2.4.1
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/asttokens/
Source0:	https://files.pythonhosted.org/packages/source/a/asttokens/asttokens-%{version}.tar.gz
# Source0-md5:	c353679585a40f43c24ca60fca33bbf6
URL:		https://pypi.org/project/asttokens/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:44
BuildRequires:	python-setuptools_scm >= 3.4.3
BuildRequires:	python-toml
%if %{with tests}
BuildRequires:	python-astroid >= 1
BuildRequires:	python-pytest
BuildRequires:	python-six >= 1.12.0
BuildRequires:	python-typing
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools >= 1:44
BuildRequires:	python3-setuptools_scm >= 3.4.3
BuildRequires:	python3-tomli
%if %{with tests}
BuildRequires:	python3-astroid >= 2
BuildRequires:	python3-pytest
BuildRequires:	python3-six >= 1.12.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The asttokens module annotates Python abstract syntax trees (ASTs)
with the positions of tokens and text in the source code that
generated them.

%description -l pl.UTF-8
Moduł asttokens oznacza abstrakcyjne drzewa składniowe (AST) Pythona
lokalizacjami tokenów i tekstu w kodzie źródłowym, który je
wygenerował.

%package -n python3-asttokens
Summary:	Annotate AST trees with source code positions
Summary(pl.UTF-8):	Oznaczanie drzew AST lokalizacją w kodzie źródłowym
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-asttokens
The asttokens module annotates Python abstract syntax trees (ASTs)
with the positions of tokens and text in the source code that
generated them.

%description -n python3-asttokens -l pl.UTF-8
Moduł asttokens oznacza abstrakcyjne drzewa składniowe (AST) Pythona
lokalizacjami tokenów i tekstu w kodzie źródłowym, który je
wygenerował.

%package apidocs
Summary:	API documentation for Python asttokens module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona asttokens
Group:		Documentation

%description apidocs
API documentation for Python asttokens module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona asttokens.

%prep
%setup -q -n asttokens-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/asttokens
%{py_sitescriptdir}/asttokens-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-asttokens
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/asttokens
%{py3_sitescriptdir}/asttokens-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
