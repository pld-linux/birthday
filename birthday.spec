Summary:	Display birthdays
Summary(pl):	Wi¶wietlanie urodzin
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
To jest ma³y program napisany oryginalnie wtedy, gdy autor uczy³ siê
C, jaki¶ czas temu. Od tamtego czasu zosta³ wiele razy przepisany od
nowa, ostatni raz jakie¶ cztery czy piêæ lat temu - ale nadal
pozostaje u¿yteczny wed³ug autora.

Program wy¶wietla listê zdarzeñ, które maj± nast±piæ w najbli¿szej
przysz³o¶ci, w oparciu o plik konfiguracyjny (~/.birthdays) w katalogu
domowym u¿ytkownika. Program mo¿e byæ w³±czony do .profile, dziêki
czemu u¿ytkownik widzi listê przy ka¿dym logowaniu. Szczegó³owy opis
formatu pliku znajduje siê w manualu.

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
