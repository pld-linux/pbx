Summary:	Phone billing system
Summary(pl):	System bilingowy po³±czeñ telefonicznych
Name:		pbx
Version:	20050222
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://duch.mimuw.edu.pl/~hunter/%{name}-%{version}.tar.gz
# Source0-md5:	df997f519b7088b327aa612ef12e0fdb
Source1:	%{name}.sysconfig
URL:		http://pbx.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pbx Accounting / Billing is a call accounting/billing software which
uses SMDR (Station Message Detailed Recording) facility from modern
phone centrals.

The billing part of that package is written in PHP and can calculate
call cost based on a set of "cost configuration parameters":
currencies, cost, time (on-peak, off-peak), dialed number, etc.

%description -l pl
Pbx jest systemem ksiêgowania/bilingowania po³±czeñ telefonicznych.
Wykorzystuje on funkcjê SMDR (Station Message Detailed Recording)
któr± posiadaj± wszystkie wspó³czesne centrale telefoniczne.

System bilingowo-prezentacyjny wykonany jest w PHP i mo¿e obliczaæ
koszt po³±czeñ w oparciu o zbiór "parametrów konfiguruj±cych koszty":
walut, cen, czasu (w szczycie, poza szczytem), wybieranego numeru itp.

%package php
Summary:	Phone billing system	
Summary(pl):	System bilingowy po³±czeñ telefonicznych.
Group:		Applications/Communications

%description php
This is PHP part of PBX. 

%description php -l pl
To jest czê¶æ systemu PBX u¿ywaj±ca PHP. 

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_datadir}/pbx/{css,img,tpl}}
install -d $RPM_BUILD_ROOT/etc/sysconfig
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT/var/lib/%{name}/{log,run,scripts}

install util/pbx $RPM_BUILD_ROOT/etc/rc.d/init.d/pbx
install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/pbx

install html/css/styles.css $RPM_BUILD_ROOT%{_datadir}/pbx/css/styles.css
install html/img/*.gif $RPM_BUILD_ROOT%{_datadir}/pbx/img
install html/tpl/*.tpl $RPM_BUILD_ROOT%{_datadir}/pbx/tpl
install html/*.php $RPM_BUILD_ROOT%{_datadir}/pbx

install util/pbx.cron $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install sql/{user,pbx}.sql $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install workerhome/capture.log			$RPM_BUILD_ROOT/var/lib/%{name}
install workerhome/fix-rights.sh		$RPM_BUILD_ROOT/var/lib/%{name}
install workerhome/log/execution.log	$RPM_BUILD_ROOT/var/lib/%{name}/log
install workerhome/log/pbxerr.log		$RPM_BUILD_ROOT/var/lib/%{name}/log
install workerhome/run/pbx.pid			$RPM_BUILD_ROOT/var/lib/%{name}/run
install workerhome/scripts/processfile	$RPM_BUILD_ROOT/var/lib/%{name}/scripts
install workerhome/scripts/sed_script	$RPM_BUILD_ROOT/var/lib/%{name}/scripts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO docs/*

%{_datadir}/%{name}

%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

%{_examplesdir}/%{name}-%{version}
/var/lib/%{name}

%files php
%defattr(644,root,root,755)
#%{_datadir}/%{name}-e
