%define	oname ogre
%define	version 1.7.4
%define	filever %(echo v%{version}| tr . -)

Name:		ogre-cg-plugin
Version:	%{version}
Release:	%mkrel 1
Summary:	CgProgramManager plugin for OGRE
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.ogre3d.org/
Source0:	http://downloads.sourceforge.net/ogre/%{oname}_src_%{filever}.tar.bz2
BuildRequires:	libx11-devel
BuildRequires:	libxaw-devel
BuildRequires:	libxrandr-devel
BuildRequires:	libxt-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	ois-devel
BuildRequires:	boost-devel
BuildRequires:	freeimage-devel
BuildRequires:	freetype2-devel
BuildRequires:	zziplib-devel
BuildRequires:	cppunit-devel
BuildRequires:	cmake
BuildRequires:	cg-devel

%description
This package contains CgProgramManager plugin for OGRE.

%prep
%setup -qn %{oname}_src_%{filever}

%build
%cmake
%make

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_libdir}/OGRE
%__cp build/lib/Plugin_CgProgramManager.so %{buildroot}%{_libdir}/OGRE/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/OGRE/Plugin_CgProgramManager.so
