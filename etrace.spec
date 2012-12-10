Name:		etrace
Version:	1.1
Release:	%mkrel 8
URL:		http://www.bindshell.net/tools/etrace
Source:		http://www.bindshell.net/tools/etrace/%{name}.%{version}.tgz
Patch0:		etrace-1.1-fix-str-fmt.patch
License:	BSD
Group:		Monitoring
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:	Network tracing tool
BuildRequires:	libpcap-devel libdnet-devel
%description
etrace is a configurable static port network tracing tool, similar to
traceroute, but supporting ICMP, TCP, UDP and other IP protocols.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall

%clean
rm -rf %{buildroot}

%files
%doc LICENSE README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/dns
%{_datadir}/%{name}/ike
%{_datadir}/%{name}/profile
%{_mandir}/man8/%{name}.8.*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-8mdv2011.0
+ Revision: 610392
- rebuild

* Mon Mar 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.1-7mdv2010.1
+ Revision: 512933
- Add clean section
- fix mixed-use-of-spaces-and-tabs
- Use %%configure2_5x
- Specifiy version in the patch and fix name

* Tue Nov 10 2009 Michael Scherer <misc@mandriva.org> 1.1-6mdv2010.1
+ Revision: 463875
- fix format string problem, and rebuild it

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1-4mdv2009.1
+ Revision: 298251
- rebuilt against libpcap-1.0.0

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.1-3mdv2009.0
+ Revision: 240689
- rebuild
- fix summary-not-capitalized
- fix no-buildroot-tag

* Fri Aug 17 2007 Nicolas Vigier <nvigier@mandriva.com> 1.1-1mdv2008.0
+ Revision: 65086
- Import etrace

