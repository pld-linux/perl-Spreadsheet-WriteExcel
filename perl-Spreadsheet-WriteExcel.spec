#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Spreadsheet
%define		pnam	WriteExcel
Summary:	Spreadsheet::WriteExcel perl module
Summary(cs.UTF-8):	Modul Spreadsheet::WriteExcel pro Perl
Summary(da.UTF-8):	Perlmodul Spreadsheet::WriteExcel
Summary(de.UTF-8):	Spreadsheet::WriteExcel Perl Modul
Summary(es.UTF-8):	Módulo de Perl Spreadsheet::WriteExcel
Summary(fr.UTF-8):	Module Perl Spreadsheet::WriteExcel
Summary(it.UTF-8):	Modulo di Perl Spreadsheet::WriteExcel
Summary(ja.UTF-8):	Spreadsheet::WriteExcel Perl モジュール
Summary(ko.UTF-8):	Spreadsheet::WriteExcel 펄 모줄
Summary(nb.UTF-8):	Perlmodul Spreadsheet::WriteExcel
Summary(pl.UTF-8):	Moduł Perla Spreadsheet::WriteExcel
Summary(pt.UTF-8):	Módulo de Perl Spreadsheet::WriteExcel
Summary(pt_BR.UTF-8):	Módulo Perl Spreadsheet::WriteExcel
Summary(ru.UTF-8):	Модуль для Perl Spreadsheet::WriteExcel
Summary(sv.UTF-8):	Spreadsheet::WriteExcel Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Spreadsheet::WriteExcel
Summary(zh_CN.UTF-8):	Spreadsheet::WriteExcel Perl 模块
Name:		perl-Spreadsheet-WriteExcel
Version:	2.17
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	996967698c8c24bda236ada8f06e0214
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Moduł Spreadsheet::WriteExcel może być używany do tworzenia
międzyplatformowych plików binarnych Excela. Wiele arkuszy może być
dodanych do jednej księgi, a w komórkach można używać formatowania.
Tekst, liczby, formuły, odnośniki i obrazki mogą być wpisywane do
komórek.

Pliki Excela produkowane przez ten moduł są kompatybilne z Excelem 5,
95, 97, 2000 i 2002.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv doc html

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/{README,*.pl,*.bmp} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
gzip -9 $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README html
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
