Summary:	KDbg - a Graphical Debugger Interface
Name:		kdbg
Version:	0.2.3
Release:	1
Group:		X11/KDE/Applications
Source:		ftp://cronus.eudaptics.co.at/pub/people/jsixt/%{name}-%{version}.tar.gz
Patch:		kdbg-pl.po.patch
Copyright:	GPL
Requires:	qt >= 1.40
Vendor:		Johannes Sixt <Johannes.Sixt@telecom.at>
BuildRoot:	/tmp/%{name}-%{version}-root

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
%patch -p1

%build
export KDEDIR=/usr/X11R6
CFLAGS="$RPM_OPT_FLAGS -Wall" CXXFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
	--with-install-root=$RPM_BUILD_ROOT
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
/usr/X11R6/share/kde/apps/kdbg
/usr/X11R6/share/kde/icons/kdbg.xpm
/usr/X11R6/share/kde/icons/mini/kdbg.xpm

%lang(en) /usr/X11R6/share/kde/doc/HTML/en/*
