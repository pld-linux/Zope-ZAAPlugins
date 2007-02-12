%define		zope_subname	ZAAPlugins
Summary:	A set of plugins for use with ZAttachmentAttribute
Summary(pl.UTF-8):	Zestaw wtyczek do wykorzystania z ZAttachmentAttribute
Name:		Zope-%{zope_subname}
Version:	2.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/ingeniweb/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	64f6476d8ae6f2a572a8a2662fa5ec7c
URL:		http://sourceforge.net/projects/ingeniweb/
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of plugins for use with ZAttachmentAttribute.

%description -l pl.UTF-8
Zestaw wtyczek do wykorzystania z ZAttachmentAttribute.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af Audio Autocad Extensions HTML Image \
	MS{Access,Excel,PowerPoint,Project,Word} PDF Zip skins text visio *.py *.txt \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc doc/* CHANGES ChangeLog README
%{_datadir}/%{name}
