#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Annotate AST trees with source code positions
Summary(pl.UTF-8):	Oznaczanie drzew AST lokalizacją w kodzie źródłowym
Name:		python3-asttokens
Version:	3.0.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/asttokens/
Source0:	https://files.pythonhosted.org/packages/source/a/asttokens/asttokens-%{version}.tar.gz
# Source0-md5:	7d99c4c80190c3ba64839138ea827970
URL:		https://pypi.org/project/asttokens/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools >= 1:44
BuildRequires:	python3-setuptools_scm >= 3.4.3
%if %{with tests}
BuildRequires:	python3-astroid >= 2
BuildRequires:	python3-astroid < 4
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.8
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
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/asttokens
%{py3_sitescriptdir}/asttokens-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
