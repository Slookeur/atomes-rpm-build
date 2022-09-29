Name:           atomes
Version:        1.1.5
Release:        1%{?dist}
Summary:        An atomistic toolbox
Group:          Productivity/Scientific/Physics
License:        AGPL-3.0-or-later
Source0:        https://github.com/Slookeur/Atomes-rpm-build/raw/main/%{name}-%{version}.tar.gz
Source1:        https://github.com/Slookeur/Atomes-rpm-build/raw/main/%{name}-%{version}.tar.gz.asc
Source2:        https://github.com/Slookeur/Atomes-rpm-build/raw/main/atomes.gpg
URL:            https://atomes.ipcms.fr/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires: gnupg2
BuildRequires: make
BuildRequires: autoconf
BuildRequires: gcc
BuildRequires: gcc-gfortran
BuildRequires: libgfortran
BuildRequires: gtk3-devel
BuildRequires: libxml2-devel
BuildRequires: freeglut-devel
BuildRequires: libgfortran
BuildRequires: mesa-libGLU-devel
BuildRequires: libepoxy-devel
BuildRequires: libavutil-free-devel
BuildRequires: libavcodec-free-devel
BuildRequires: libavformat-free-devel
BuildRequires: libswscale-free-devel
BuildRequires: desktop-file-utils

Requires: gtk3
Requires: libgfortran
Requires: libxml2
Requires: libavutil-free
Requires: libavcodec-free
Requires: libavformat-free
Requires: libswscale-free
Requires: mesa-libGLU
Requires: libepoxy
Requires: desktop-file-utils
Requires: bash-completion

Provides: %{name}-%{version}

%description
Atomes: a toolbox to analyze, to visualize 
and to edit/create three-dimensional atomistic models.
It oﬀers a workspace that allows to have many projects opened simultaneously.
The different projects in the workspace can exchange data: 
analysis results, atomic coordinates ...
Atomes also provides an advanced input preparation system 
for further calculations using well known molecular dynamics codes:

    Classical MD : DLPOLY and LAMMPS
    ab-initio MD : CPMD and CP2K
    QM-MM MD : CPMD and CP2K

To prepare the input ﬁlles for these calculations is likely to be the key, 
and most complicated step towards MD simulations.
Atomes offers a user-friendly assistant to help 
and guide the scientist step by step to achieve this crucial step.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%configure --prefix=/usr
make `%{? smp_flags}`

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
%{_bindir}/atomes
%{_datadir}/doc/atomes/
%{_datadir}/atomes/
%{_datadir}/bash-completion/completions/atomes
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/atomes.1.gz

%changelog
* Fri Sep 23 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.5
- Bug correction:
 w_search.c: selection not to crash if atom_win is closed

* Thu Sep 22 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.4
- Bug correction: 
 read_coord.c: Windows to handle properly EOL symbols
 m_curve.c: Windows to not crash when destroying label widget
 glview.c: correct GWARNING messages on widget scale

* Thu Sep 15 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.3
- Bug correction: 
 read_opengl.c: correct 'read_atom_b'
 initring.c: coorect 'send_rings_opengl_'

* Wed Sep 14 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.2
- Bug correction: 
 atom_action.c: recompute bonding on passivate
 bdcall.c: do not trigger menu init on passivate

* Tue Sep 13 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.1
- Bug correction: double click on workspace

* Mon Aug 29 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.0
- Initial release of the Atomes program v1.1.0
 Enjoy !
