Summary:	KDbg - a Graphical Debugger Interface
Name:		kdbg
Version:	1.0.1
Release:	1
Copyright:	GPL
Group:		X11/KDE/Applications
Vendor:		Johannes Sixt <Johannes.Sixt@telecom.at>
Source:		ftp://cronus.eudaptics.co.at/pub/people/jsixt/%{name}-%{version}.tar.gz
BuildRequires:	qt-devel
URL:		http://members.telecom.at/~johsixt/kdbg.html
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%description
KDbg is a graphical user interface to gdb, the GNU debugger. It provides an
intuitive interface for setting breakpoints, inspecting variables, and
stepping through code. Here's a screenshot. 

Features: 
o Variable inspection in a tree structure.
o Shows importent member variables of class types without the need to "open"
  the variable. For example, you don't need to go into a variable of type
  QString to view the string value - it's shown next to the string variable.
o See for yourself. (This is, of course, configurable, not hardcoded!).
o Debugger at your finger tips: The important debugger functions (step,
  next, finish, until, run/continue, enable/disable/set/remove breakpoint)
  are bound to the function keys F5 through F10. It's fast and easy!.
o Everthing you need to debug a program: View source code, Search text, set
  program arguments.

%prep
%setup -q

%build
KDEDIR=%{_prefix}
LDFLAGS="-s"
CXXFLAGS="$RPM_OPT_FLAGS -Wall"
export KDEDIR LDFLAGS CXXFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/*
/etc/X11/kde/applnk/Applications/*
%{_datadir}/kde/apps/kdbg
%{_datadir}/kde/icons/kdbg.xpm
%{_datadir}/kde/icons/mini/kdbg.xpm

%{_datadir}/kde/doc/HTML/en/*
