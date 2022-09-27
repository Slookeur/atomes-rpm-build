Name:           atomes
Version:        1.1.5
Release:        1
Summary:        An atomistic toolbox
Group:          Productivity/Scientific/Physics
License:        AGPLv3+
Source:         https://github.com/Slookeur/Atomes-rpm-build/blob/main/%name-%version.tar.gz
URL:            http://atomes.ipcms.fr/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libgfortran
BuildRequires:  gtk3-devel
BuildRequires:  libxml2-devel
BuildRequires:  libgfortran
BuildRequires:  libepoxy-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  desktop-file-utils

# For Suse-based linux
%if 0%{?suse_version}
BuildRequires:  gcc-fortran
BuildRequires:  update-desktop-files
%endif
 
# For RedHat-based linux
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  gcc-gfortran
%endif

Requires: gtk3
Requires: desktop-file-utils
Requires: bash-completion

Provides: atomes = %{version}

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
%autosetup

%build
%configure --prefix=/usr
make

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

* Mon Aug 28 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.0
- Initial release of the Atomes program v1.1.0
 Enjoy !
