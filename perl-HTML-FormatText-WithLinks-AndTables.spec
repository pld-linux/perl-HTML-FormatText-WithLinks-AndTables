#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	FormatText-WithLinks-AndTables
%include	/usr/lib/rpm/macros.perl
Summary:	HTML::FormatText::WithLinks::AndTables - Converts HTML to Text with tables in tact
Summary(pl.UTF-8):	HTML::FormatText::WithLinks::AndTables - konwersja HTML-a do tekstu z tabelkami
Name:		perl-HTML-FormatText-WithLinks-AndTables
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bd214ca080379cc09f0b2eef62bf3d0f
URL:		http://search.cpan.org/dist/HTML-FormatText-WithLinks-AndTables/
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-FormatText-WithLinks
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module was inspired by HTML::FormatText::WithLinks which has
proven to be a useful `lynx -dump` work-alike. However one frustration
was that no other HTML converters had the ability to deal affectively
with HTML <TABLE>s. This module can in a rudimentary sense do so. The
aim was to provide facility to take a simple HTML based email
template, and to also convert it to text with the <TABLE> structure in
tact for inclusion as "multipart/alternative" content. Further, it
will preserve both the formatting specified by the <TD> tag's "align"
attribute, and will also preserve multiline text inside of a <TD>
element provided it is broken using <BR/> tags.

%description -l pl.UTF-8
Ten moduł jest zainspirowany modułem HTML::FormatText::WithLinks,
który okazał się przydatnym odpowiednikiem polecenia "lynx -dump".
Jednak żaden dotychczasowy konwerter HTML-a nie mógł efektywnie
poradzić sobie z elementami HTML <TABLE>. Ten moduł potrafi to w
podstawowym zakresie. Celem była możliwość przekazania prostego
szablonu wiadomości elektronicznej w HTML-u i przekształcenie jej do
tekstu wraz ze strukturą <TABLE>, aby można ją było umieścić w treści
multipart/alternative. Co więcej, moduł zachowuje formatowanie
określone atrybutem "align" znacznika <TD> oraz wieloliniowy tekst
wewnątrz elementu <TD> - pod warunkiem, że jest złamany przy użyciu
znaczników <BR/>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

# duplicate of HTML::FormatText::WithLinks::AndTables docs (already included pm and man)
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/HTML/FormatText/WithLinks/README.pod \
	$RPM_BUILD_ROOT%{_mandir}/man3/HTML::FormatText::WithLinks::README.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/HTML/FormatText/WithLinks
%{perl_vendorlib}/HTML/FormatText/WithLinks/AndTables.pm
%{_mandir}/man3/HTML::FormatText::WithLinks::AndTables.3pm*
