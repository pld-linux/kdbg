
%define         kde4ver 4.6.0
%define         qtver   4.7.1
%define         orgname	kdbg

Summary:	KDbg - a KDE Graphical Debugger Interface
Summary(es.UTF-8):	Interfaz gráfica KDE para gdb
Summary(pl.UTF-8):	Interfejs KDE do gdb
Summary(pt_BR.UTF-8):	Interface gráfica KDE para o gdb
Name:		kdbg
Version:	2.5.1
Release:	1
Epoch:		2
License:	GPL
Group:		X11/Development/Tools
Source0:	http://downloads.sourceforge.net/kdbg/%{name}-%{version}.tar.gz
# Source0-md5:	a19095dce4cb5df0dbaa9368d400fc30
URL:		http://www.kdbg.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{kde4ver}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l es.UTF-8
Interfaz gráfica KDE para gdb.

%description -l pl.UTF-8
KDbg to graficzny interfejs użytkownika do gdb, debuggera GNU. Daje
intuicyjny interfejs do ustawiania breakpointów, przeglądania
zmiennych, śledzenia kodu.

Możliwości:
- przeglądanie zmiennych w strukturze drzewiastej
- wyświetlanie istotnych zmiennych z klas bez potrzeby "otwierania"
  zmiennej. Na przykład, nie potrzeba wchodzić do zmiennej typu QString
  aby zobaczyć zawartość stringa - jest wyświetlana zaraz za zmienną
- debugger pod palcami - najważniejsze funkcje (krok, następny,
  koniec, do miejsca, uruchomienie/kontynuacja, włączenie/wyłączenie/
  dodanie/usunięcie breakpointa) są przypisane klawiszom F5 do F10.
- Wszystko co potrzebne do odpluskwiania programu: przeglądanie kodu
  źródłowego, wyszukiwanie tekstu, ustawianie parametrów programu.

%description -l pt_BR.UTF-8
Interface gráfica KDE para o gdb.

%prep
%setup -q

mv -f po/sr{,@latin}.po

%build
install -d build
cd build
%cmake \
		../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kdbg
%{_desktopdir}/kde4/*.desktop
%{_datadir}/config/*
