Summary:	Display birthdays
Name:		birthday
Version:	1.5
Release:	1
License:	Gnu GPL
Group:		qq
Vendor:		Andy Mortimer <andy.mortimer@zetnet.co.uk>
Source:	%{name}-%{version}.tar.gz
#URL:		
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup  -q

%build


%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT SHARE=/share

%pre

%preun

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/usr/bin/birthday
/usr/share/man/man1/*
