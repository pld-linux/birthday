Summary:	Display birthdays
Summary(pl):	Wi�wietlanie urodzin
Name:		birthday
Version:	1.5
Release:	1
License:	GPL
Vendor:		Andy Mortimer <andy.mortimer@zetnet.co.uk>
Group:		Applications
Source:		%{name}-%{version}.tar.gz
#URL:		
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a little program which was originally written when the author
was learning C, some time ago now. It has gone through a couple of total
re-writes, the last of which was four or five years ago now, but he
still finds it a useful program.

It displays a list of events which are coming up in the near future,
based on a config file (~/.birthdays) in the user's home directory.
It can be included it in .profile, so user gets the list every time he
logs on. See the manpage for more details of this format.

%description -l pl
To jest ma�y program napisany oryginalnie wtedy, gdy autor uczy� si�
C, jaki� czas temu. Od tamtego czasu zosta� wiele razy przepisany od
nowa, ostatni raz jakie� cztery czy pi�� lat temu - ale nadal
pozostaje u�yteczny wed�ug autora.

Program wy�wietla list� zdarze�, kt�re maj� nast�pi� w najbli�szej
przysz�o�ci, w oparciu o plik konfiguracyjny (~/.birthdays) w katalogu
domowym u�ytkownika. Program mo�e by� w��czony do .profile, dzi�ki
czemu u�ytkownik widzi list� przy ka�dym logowaniu. Szczeg�owy opis
formatu pliku znajduje si� w manualu.

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	SHARE=/share

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/birthday
%{_mandir}/man1/*
