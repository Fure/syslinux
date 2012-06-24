Summary:	Simple bootloader
Summary(pl):	Prosty bootloader
Summary(pt_BR):	Carregador de boot simples
Summary(zh_CN):	Linux����ϵͳ������������
Name:		syslinux
Version:	2.11
Release:	2
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{version}.tar.bz2
# Source0-md5:	38a30cc790265f19f80330330ffaa527
Patch0:		%{name}-nowin32.patch
URL:		http://syslinux.zytor.com/
BuildRequires:	perl
BuildRequires:	nasm
Requires:	mtools
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SYSLINUX is a boot loader for the Linux operating system which
operates off MS-DOS floppies. It is intended to simplify first-time
installation of Linux, rescue disks, and other uses for boot floppies.
A SYSLINUX floppy can be manipulated using standard MS-DOS (or any
other OS that can access an MS-DOS filesystem) tools once it has been
created, and requires only a ~ 7K DOS program or ~ 13K Linux program
to create it in the first place. It also includes PXELINUX, a program
to boot off a network server using a boot PROM compatible with the
Intel PXE (Pre-Execution Environment) specification.

%description -l pl
SYSLINUX jest boot-loaderem dla Linux'a, kt�ry operuje na dyskietkach
z systemem plik�w MS-DOS. Jego przeznaczeniem jest uproszczenie
pierwszej instalacji Linux'a, dyskietki ratunkowe oraz inne rzeczy
zwi�zane z dyskietkami. Dyskietka SYSLINX'owa mo�e by� modyfikowana w
systemie MS-DOS (a tak�e ka�dym innym systemie z dost�pem do systemu
plik�w MS-DOS) gdy narz�dzia sa ju� stworzone, a tak�e potrzebuje
tylko ~7K programu DOS'owego lub ~13K programu Linux'owego do
stworzenia ich po raz pierwszy. Zawiera tak�e program PXELINUX -
program s�u��cy do bootowania servera sieciowego poprzez Boot-PROM
kompatybilny ze specyfikacj� Intel PXE (Pre-Execution Environment).

%description -l pt_BR
SYSLINUX � um carregador de boot para o linux, operando em disquetes
com formata��o DOS. Sua inten��o � simplificar instala��es do Linux,
discos de recupera��o, e outros usos para disquetes de boot. Um
disquete SYSLINUX pode ser manipulado usando ferramentas padr�o do DOS
(ou qualquer sistema que possa acessar um filesystem DOS) e requer
somente um programa DOS de aproximadamente 7K ou linux de 13K para
cri�-lo na primeira vez.

Tamb�m inclui o PXELINUX, um programa para boot remoto a partir de um
servidor de rede usando um boot PROM compat�vel com a especifica��o
Intel PXE (Pre-Execution Environment).

%package libs
Summary:	syslinux shared libraries
Summary(pl):	Biblioteki wsp�dzielone syslinux
Group:		Libraries

%description libs
syslinux shared libraries.

%description libs -l pl
Biblioteki wsp�dzielone syslinux.

%package devel
Summary:	Header files for syslinux libraries
Summary(pl):	Pliki nag��wkowe bibliotek syslinux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description devel
This package includes the header files needed for compilation of
applications that are making use of the syslinux internals. Install
this package only if you plan to develop or will need to compile
customized syslinux clients.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe potrzebne do kompilowania
aplikacji wykorzystuj�cych kod syslinuksa. Nale�y go instalowa�
tylko je�li chcemy tworzy� lub kompilowa� w�asnych klient�w
syslinuksa.

%package static
Summary:	syslinux static libraries
Summary(pl):	Biblioteki statyczne syslinux
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com syslinux
Summary(ru):	����������� ���������� syslinux
Summary(uk):	������Φ ¦�̦����� syslinux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
syslinux static libraries.

%description static -l pl
Biblioteki statyczne syslinux.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com syslinux.

%prep
%setup -q
%patch0 -p1

%build
rm -f ldlinux.{bin,bss,lst,sys}
%{__make} installer \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_includedir}}
install ldlinux.sys $RPM_BUILD_ROOT/%{_libdir}/%{name}

%{__make} install install-lib \
	INSTALLROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README *.doc */*.doc
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
