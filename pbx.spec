#
#
Summary:	Phone billing system
Summary(pl):	 System bilingowy po³±czeñ telefonicznych.
Name:		pbx
Version:	20050222
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
#Icon:		-
Source0:	http://duch.mimuw.edu.pl/~hunter/%{name}-%{version}.tar.gz
# Source0-md5:	df997f519b7088b327aa612ef12e0fdb
#Patch0:		%{name}-what.patch
URL:		http://pbx.sf.net
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pbx Accounting / Billing is a call accounting/billing software which
uses SMDR (Station Message Detailed Recording) facility from modern
phone centrals.

The billing part of that package is written in PHP and can calculate
call cost based on a set of "cost configuration parameters":
currencies, cos, time (on-peak,off-peak), dialed number, etc.

%description -l pl
Pbx jest systemem ksiêgowania bilingowania po³±czeñ telefonicznych. 
Wykorzystuje on funkcjê SMDR (Station Message Detailed Recording) któr± 
posiadaj± wszystkie wspó³czesne centrale telefoniczne.

System bilingowo-prezentacyjny wykonany jest w PHP.

%package php
Summary: Phone billing system	
Summary(pl):	System bilingowy po³±czeñ telefonicznych. 
Group:		Applications/Communications

%description php
This is php part of PBX. 

%description php -l pl
To jest czê¶æ systemu PBX u¿ywaj±ca PHP. 

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/rc.d/init.d/pbx,%{_datadir}/pbx/{css,img,tpl}}
install util/pbx $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/pbx
install html/css/styles.css  $RPM_BUILD_ROOT%{_datadir}/pbx/css/styles.css
install html/img/*.gif  $RPM_BUILD_ROOT%{_datadir}/pbx/img/
install html/tpl/*.tpl  $RPM_BUILD_ROOT%{_datadir}/pbx/tpl/
install html/*.php  $RPM_BUILD_ROOT%{_datadir}/pbx/

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%doc docs/*

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%attr(755,root,root) %{_bindir}/*

%{_datadir}/%{name}

# initscript and it's config
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

%files php
%defattr(644,root,root,755)
#%{_datadir}/%{name}-e
