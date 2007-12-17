%define modname gtkmvc
%define pyver %(python -V 2>&1 | cut -f2 -d" " | cut -f1,2 -d".")

Name:           python-%{modname}
URL:            http://pygtkmvc.sourceforge.net/
Summary:        Pygtk MVC is a multiplatform implementation of a dialect of the Model-View-Controller and Observer patterns for the PyGTK2
Version:        1.2.1
Release:        %mkrel 3
License:        BSD
Group:          Development/Python
Source:         http://ovh.dl.sourceforge.net/sourceforge/pygtkmvc/python-%{modname}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python pygtk2.0 libglade2.0

BuildRequires:  python-devel libglade2-devel pygtk2.0-devel

%description
Pygtk MVC is a multiplatform implementation of a dialect
of the Model-View-Controller and Observer patterns for the
PyGTK2 toolkit.

MVC is a pattern that can be successfully used to design
and develop well structured GUI applications.
The MVC pattern basically helps in separating sematics
and data of the application, from their representation.

Within Pygtk MVC the Observer pattern is also embedded.
This pattern allows making separated parts independent,
but still connected each other.

%prep
%setup -q -n python-%{modname}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
%{__python} setup.py build

export PYTHONPATH="$RPM_BUILD_ROOT%{_libdir}/python%{pyver}/site-packages"

%install
# -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf  %{buildroot}
%{__python} setup.py install --root=$RPM_BUILD_ROOT

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf  %{buildroot}

%files
%defattr(-,root,root)
%doc docs examples AUTHORS COPYING INSTALL NEWS README PKG-INFO
%{_bindir}/gtkmvc-progen
%py_purelibdir/*
