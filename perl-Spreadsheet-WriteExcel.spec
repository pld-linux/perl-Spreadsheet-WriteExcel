#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Spreadsheet
%define		pnam	WriteExcel
Summary:	Spreadsheet::WriteExcel perl module
Summary(cs):	Modul Spreadsheet::WriteExcel pro Perl
Summary(da):	Perlmodul Spreadsheet::WriteExcel
Summary(de):	Spreadsheet::WriteExcel Perl Modul
Summary(es):	Módulo de Perl Spreadsheet::WriteExcel
Summary(fr):	Module Perl Spreadsheet::WriteExcel
Summary(it):	Modulo di Perl Spreadsheet::WriteExcel
Summary(ja):	Spreadsheet::WriteExcel Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Spreadsheet::WriteExcel ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Spreadsheet::WriteExcel
Summary(pl):	Modu³ Perla Spreadsheet::WriteExcel
Summary(pt):	Módulo de Perl Spreadsheet::WriteExcel
Summary(pt_BR):	Módulo Perl Spreadsheet::WriteExcel
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Spreadsheet::WriteExcel
Summary(sv):	Spreadsheet::WriteExcel Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Spreadsheet::WriteExcel
Summary(zh_CN):	Spreadsheet::WriteExcel Perl Ä£¿é
Name:		perl-Spreadsheet-WriteExcel
Version:	0.42
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	164e6d454132c86c33168b45456c3e0b
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-modules >= 5.6.1
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Spreadsheet::WriteExcel module can be used to create a cross-
platform Excel binary file. Multiple worksheets can be added to a
workbook and formatting can be applied to cells. Text, numbers,
formulas, hyperlinks and images can be written to the cells.

The Excel file produced by this module is compatible with Excel 5, 95,
97, 2000 and 2002.

%description -l pl
Modu³ Spreadsheet::WriteExcel mo¿e byæ u¿ywany do tworzenia
miêdzyplatformowych plików binarnych Excela. Wiele arkuszy mo¿e byæ
dodanych do jednej ksiêgi, a w komórkach mo¿na u¿ywaæ formatowania.
Tekst, liczby, formu³y, odno¶niki i obrazki mog± byæ wpisywane do
komórek.

Pliki Excela produkowane przez ten modu³ s± kompatybilne z Excelem 5,
95, 97, 2000 i 2002.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv WriteExcel/examples .
mv WriteExcel/doc html

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install examples/{README,*.pl,*.bmp} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
gzip -9 $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README html
%{perl_vendorlib}/Spreadsheet/WriteExcel.pm
%dir %{perl_vendorlib}/Spreadsheet/WriteExcel
%{perl_vendorlib}/Spreadsheet/WriteExcel/*.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/README*
%{_examplesdir}/%{name}-%{version}/*.bmp
%{_examplesdir}/%{name}-%{version}/mo*.pl
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/m[^o]*.pl
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/[^m]*.pl
