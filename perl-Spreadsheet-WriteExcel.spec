#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Spreadsheet
%define	pnam	WriteExcel
Summary:	Spreadsheet::WriteExcel perl module
Summary(pl):	Modu³ perla Spreadsheet::WriteExcel
Name:		perl-%{pdir}-%{pnam}
Version:	0.38
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-56
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-modules >= 5.6.1
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Spreadsheet::WriteExcel module can be used to create a cross-
platform Excel binary file. Multiple worksheets can be added to a
workbook and formatting can be applied to cells. Text, numbers,
formulas, hyperlinks and images can be written to the cells.

The Excel file produced by this module is compatible with Excel 5,
95, 97, 2000 and 2002.
												
%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv WriteExcel/examples .
mv WriteExcel/doc html

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install examples/{README,*.pl,*.bmp} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README html
%{perl_sitelib}/Spreadsheet/WriteExcel.pm
%{perl_sitelib}/Spreadsheet/WriteExcel/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
