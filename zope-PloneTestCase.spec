%define Product PloneTestCase
%define product plonetestcase
%define name    zope-%{Product}
%define version 0.9.7
%define release %mkrel 3

%define zope_minver	2.7
%define plone_minver	2.0
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	PloneTestCase sits on top of the ZopeTestCase package
License:	GPL
Group:		System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
Requires:	zope >= %{zope_minver}
Requires:	zope-Plone >= %{plone_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
PloneTestCase sits on top of the ZopeTestCase package. It has been developed to
simplify testing of Plone and Plone-based applications and products.
The PloneTestCase package provides:
- The function installProduct to install a Zope product into the test
  environment.
- The function setupPloneSite to create a Plone portal in the test db.
  Note: setupPloneSite accepts an optional products argument, which allows you
  to specify a list of products that will be added to the portal using the
  quickinstaller tool.
- The class PloneTestCase of which to derive your test cases.
- The class FunctionalTestCase of which to derive your test cases for
  functional unit testing.
- The classes Sandboxed and Functional to mix-in with your own test cases.
- The constants portal_name, portal_owner, default_policy, default_products,
  default_user, and default_password.
- The constant PLONE21 which evaluates to true for Plone versions >= 2.1.
- The constant PLONE25 which evaluates to true for Plone versions >= 2.5.
- The module utils from the ZopeTestCase package.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a %{Product} %{buildroot}%{software_home}/Products


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
