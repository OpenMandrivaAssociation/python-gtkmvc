%define modname gtkmvc
%define pyver %(python -V 2>&1 | cut -f2 -d" " | cut -f1,2 -d".")

Name:           python-%{modname}
URL:            https://pygtkmvc.sourceforge.net/
Summary:        Model-View-Controller and Observer patterns for the PyGTK2
Version:        1.99.1
Release:        2
License:        BSD
Group:          Development/Python
Source0:        https://sourceforge.net/projects/pygtkmvc/files/pygtkmvc/1.99.1/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python pygtk2.0 libglade2.0

BuildRequires:  pkgconfig(python) pkgconfig(libglade-2.0) pygtk2.0-devel

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
%{__python} setup.py install --root=$RPM_BUILD_ROOT

%files
%doc docs examples AUTHORS COPYING INSTALL NEWS README PKG-INFO
%{_bindir}/gtkmvc-progen
%py_purelibdir/*


