Summary:	KDbg - a KDE Graphical Debugger Interface
Summary(pl):	Interfejs KDE do gdb
Name:		kdbg
Version:	1.2.5
Release:	2
License:	GPL
Group:		X11/Development/Tools
Vendor:		Johannes Sixt <Johannes.Sixt@telecom.at>
Source0:	ftp://download.sourceforge.net/pub/sourceforge/kdbg/%{name}-%{version}.tar.gz
URL:		http://members.nextra.at/johsixt/kdbg.html
BuildRequires:	XFree86-devel
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_kde_icondir	%{_pixmapsdir}
%define		_kde_minidir	%{_kde_icondir}/mini

%description
KDbg is a graphical user interface to gdb, the GNU debugger. It
provides an intuitive interface for setting breakpoints, inspecting
variables, and stepping through code.

Features:
- Variable inspection in a tree structure.
- Shows important member variables of class types without the need to
  "open" the variable. For example, you don't need to go into a variable
  of type QString to view the string value - it's shown next to the
  string variable.
- See for yourself. (This is, of course, configurable, not
  hardcoded!).
- Debugger at your finger tips: The important debugger functions
  (step, next, finish, until, run/continue, enable/disable/set/remove
  breakpoint) are bound to the function keys F5 through F10. It's fast
  and easy!.
- Everything you need to debug a program: View source code, Search
  text, set program arguments.

%description -l pl
KDbg to graficzny interfejs u¿ytkownika do gdb, debuggera GNU. Daje
intuicyjny interfejs do ustawiania breakpointów, przegl±dania
zmiennych, ¶ledzienia kodu.

Mo¿liwo¶ci:
- przegl±danie zmiennych w strukturze drzewiastej
- wy¶wietlanie istotnych zmiennych z klas bez potrzeby "otwierania"
  zmiennej. Na przyk³ad, nie potrzebujesz wchodziæ do zmiennej typu
  QString aby zobaczyæ zawarto¶æ stringa - jest wy¶wietlana zaraz za
  zmienn±
- debugger pod palcami - najwa¿niejsze funkcje (krok, nastêpny,
  koniec, do miejsca, uruchomienie/kontynuacja, w³±czenie/wy³±czenie/
  dodanie/usuniêcie brekpointu) s± przypisane klawiszom F5 do F10.
- Wszystko co potrzebne do odpluskwiania programu: przegl±danie kodu
  ¼ród³owego, wyszukiwanie tekstu, ustawianie parametrów programu.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -Wall"
kde_icondir=%{_kde_icondir}
kde_minidir=%{_kde_minidir}
export kde_icondir kde_minidir
%configure2_13  --with-kde-version=3

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
%doc BUGS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Development/*
%{_datadir}/apps/kdbg
%{_pixmapsdir}/*/*/*/*

%{_datadir}/doc/HTML/en/*
%lang(de) %{_datadir}/doc/HTML/de/*
%lang(ru) %{_datadir}/doc/HTML/ru/*
