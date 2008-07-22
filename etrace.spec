Name:		etrace
Version:	1.1
Release:	%mkrel 3
URL:		http://www.bindshell.net/tools/etrace
Source:		http://www.bindshell.net/tools/etrace/%{name}.%{version}.tgz
License:	BSD
Group:		Monitoring
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:	Network tracing tool
BuildRequires:	libpcap-devel libdnet-devel
%description
etrace is a configurable static port network tracing tool, similar to
traceroute, but supporting ICMP, TCP, UDP and other IP protocols.

%prep
%setup -q -n %{name}

%build
%configure
%make

%install
%makeinstall

%files
%doc LICENSE README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/dns
%{_datadir}/%{name}/ike
%{_datadir}/%{name}/profile
%{_mandir}/man8/%{name}.8.*

