Summary:	KDbg - a KDE Graphical Debugger Interface
Summary(pl):	Interfejs KDE do gdb
Name:		kdbg
Version:	1.1.2
Release:	2
License:	GPL
Group:		X11/KDE/Applications
Group(de):	X11/KDE/Applikationen
Group(pl):	X11/KDE/Aplikacje
Vendor:		Johannes Sixt <Johannes.Sixt@telecom.at>
Source0:	ftp://download.sourceforge.net/pub/sourceforge/kdbg/%{name}-%{version}.tar.gz
BuildRequires:	qt-devel
URL:		http://members.nextra.at/johsixt/kdbg.html
BuildRequires:	kdelibs-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_kde_icondir	%{_pixmapsdir}
%define		_kde_minidir	%{_kde_icondir}/mini

%description
KDbg is a graphical user interface to gdb, the GNU debugger. It
provides an intuitive interface for setting breakpoints, inspecting
variables, and stepping through code. Here's a screenshot.

Features:
- Variable inspection in a tree structure.
- Shows importent member variables of class types without the need to
  "open" the variable. For example, you don't need to go into a variable
  of type QString to view the string value - it's shown next to the
  string variable.
- See for yourself. (This is, of course, configurable, not
  hardcoded!).
- Debugger at your finger tips: The important debugger functions
  (step, next, finish, until, run/continue, enable/disable/set/remove
  breakpoint) are bound to the function keys F5 through F10. It's fast
  and easy!.
- Everthing you need to debug a program: View source code, Search
  text, set program arguments.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -Wall"
kde_icondir=%{_kde_icondir}
kde_minidir=%{_kde_minidir}
export kde_icondir kde_minidir
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf BUGS ChangeLog TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Development/*
%{_datadir}/apps/kdbg
%{_kde_icondir}/*.xpm
%{_kde_minidir}/*.xpm

%lang(de) %{_datadir}/doc/HTML/de/*
%lang(en) %{_datadir}/doc/HTML/en/*
%lang(ru) %{_datadir}/doc/HTML/ru/*
