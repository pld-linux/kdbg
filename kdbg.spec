Summary:     KDbg - a Graphical Debugger Interface
Name:        kdbg
Version:     0.2.2
Release:     3
Group:       X11/KDE/Applications
Source:      ftp://cronus.eudaptics.co.at/pub/people/jsixt/%{name}-%{version}.tar.gz
Patch:       kdbg-pl.po.patch
Copyright:   GPL
Requires:    qt >= 1.40
Vendor:      Johannes Sixt <Johannes.Sixt@telecom.at>
BuildRoot:   /tmp/%{name}-%{version}-root

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
./configure --prefix=$KDEDIR \
	--with-install-root=$RPM_BUILD_ROOT
make

%install
rm -rf $RPM_BUILD_ROOT

make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/X11R6/bin/*
/usr/X11R6/share/applnk/Applications/*
/usr/X11R6/share/apps/kdbg
/usr/X11R6/share/icons/kdbg.xpm
/usr/X11R6/share/icons/mini/kdbg.xpm

%lang(de) /usr/X11R6/share/doc/HTML/de/*
%lang(en) /usr/X11R6/share/doc/HTML/en/*

%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kdbg.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kdbg.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kdbg.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kdbg.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kdbg.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kdbg.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kdbg.mo
%lang(ln) /usr/X11R6/share/locale/nl/LC_MESSAGES/kdbg.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kdbg.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kdbg.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/kdbg.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kdbg.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kdbg.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kdbg.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kdbg.mo

%changelog
* Tue Sep 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.2-3]
- KDEDIR changed to /usr/X11R6,
- qt is now placed in /usr/X11R6 also.

* Thu Sep  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.2-2]
- added patch with polish translation
  (Adam Kozubowicz <tapir@interdata.com.pl>).

* Mon Aug 31 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.2-1]
- first release in rpm package.
