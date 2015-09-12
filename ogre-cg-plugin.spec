%define	oname ogre
%define	filever %(echo v%{version}| tr . -)

Name:		%{oname}-cg-plugin
Version:	1.8.0
Release:	3
Summary:	CgProgramManager plugin for OGRE
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.ogre3d.org/
Source0:	http://downloads.sourceforge.net/ogre/%{oname}_src_%{filever}.tar.bz2
BuildRequires:	cmake
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
%__cp build/lib/Plugin_CgProgramManager.so.%{version} %{buildroot}%{_libdir}/OGRE/
pushd %{buildroot}%{_libdir}/OGRE/
%__ln_s Plugin_CgProgramManager.so.%{version} Plugin_CgProgramManager.so
popd

%files
%{_libdir}/OGRE/Plugin_CgProgramManager.so.%{version}
%{_libdir}/OGRE/Plugin_CgProgramManager.so
