Summary:	KDbg - a KDE Graphical Debugger Interface
Summary(es):	Interfaz gr�fica KDE para gdb
Summary(pl):	Interfejs KDE do gdb
Summary(pt_BR):	Interface gr�fica KDE para o gdb
Name:		kdbg
Version:	1.2.6
Release:	3
Epoch:		1
License:	GPL
Vendor:		Johannes Sixt <Johannes.Sixt@telecom.at>
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/kdbg/%{name}-%{version}.tar.gz
# Source0-md5: dc460350ff5f8c371f81f260b69d78ad
Patch0:		%{name}-desktop.patch
URL:		http://members.nextra.at/johsixt/kdbg.html
BuildRequires:	kdelibs-devel >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_kde_icondir	%{_pixmapsdir}
%define		_kde_minidir	%{_kde_icondir}/mini
%define		_htmldir	/usr/share/doc/kde/HTML

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

%description -l es
Interfaz gr�fica KDE para gdb.

%description -l pl
KDbg to graficzny interfejs u�ytkownika do gdb, debuggera GNU. Daje
intuicyjny interfejs do ustawiania breakpoint�w, przegl�dania
zmiennych, �ledzienia kodu.

Mo�liwo�ci:
- przegl�danie zmiennych w strukturze drzewiastej
- wy�wietlanie istotnych zmiennych z klas bez potrzeby "otwierania"
  zmiennej. Na przyk�ad, nie potrzeba wchodzi� do zmiennej typu
  QString aby zobaczy� zawarto�� stringa - jest wy�wietlana zaraz za
  zmienn�
- debugger pod palcami - najwa�niejsze funkcje (krok, nast�pny,
  koniec, do miejsca, uruchomienie/kontynuacja, w��czenie/wy��czenie/
  dodanie/usuni�cie brekpointu) s� przypisane klawiszom F5 do F10.
- Wszystko co potrzebne do odpluskwiania programu: przegl�danie kodu
  �r�d�owego, wyszukiwanie tekstu, ustawianie parametr�w programu.

%description -l pt_BR
Interface gr�fica KDE para o gdb.

%prep
%setup -q
%patch0 -p1

%build
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -Wall"
kde_icondir=%{_kde_icondir}
kde_minidir=%{_kde_minidir}
export kde_icondir kde_minidir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_appsdir="%{_applnkdir}"; export kde_appsdir 
%configure2_13 \
	--disable-rpath \
	--enable-final \
	--with-kde-version=3

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/zh_CN{.GB2312,}
mv -f $RPM_BUILD_ROOT%{_pixmapsdir}{/hicolor/48x48/apps,}/kdbg.png

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Development/*
%{_datadir}/apps/kdbg
%{_pixmapsdir}/*.png
