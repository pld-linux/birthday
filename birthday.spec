Summary:	Display birthdays
Summary(pl.UTF-8):   Wyświetlanie urodzin
Name:		birthday
Version:	1.5
Release:	1
License:	GPL
Vendor:		Andy Mortimer <andy.mortimer@zetnet.co.uk>
Group:		Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	d2ceb7ca58d998645a4bdc04d986139c
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

%description -l pl.UTF-8
To jest mały program napisany oryginalnie wtedy, gdy autor uczył się
C, jakiś czas temu. Od tamtego czasu został wiele razy przepisany od
nowa, ostatni raz jakieś cztery czy pięć lat temu - ale nadal
pozostaje użyteczny według autora.

Program wyświetla listę zdarzeń, które mają nastąpić w najbliższej
przyszłości, w oparciu o plik konfiguracyjny (~/.birthdays) w katalogu
domowym użytkownika. Program może być włączony do .profile, dzięki
czemu użytkownik widzi listę przy każdym logowaniu. Szczegółowy opis
formatu pliku znajduje się w manualu.

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
