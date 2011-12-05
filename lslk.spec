Summary: A lock file lister
Name: lslk
Version: 1.29
Release: 23%{?dist}
License: zlib
Group: Development/Debuggers

# upstream is not active any more
URL: ftp://vic.cc.purdue.edu/pub/tools/unix/lslk
Source: lslk_%{version}_W.tar.gz

Patch0: lslk_1.29_W-misc.patch
Patch1: lslk_1.29_W-readlink.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Lslk is a lock file lister.  Lslk attempts to list all of the locks on
the executing system's local files (i.e., on the active inodes).

Install lslk if you need a utility for listing file locks.

%prep
%setup -q -c -n lslk
tar xf lslk_%{version}.tar
[ -d lslk_%{version} ] && cd lslk_%{version}
%patch0 -p2 -b .misc
%patch1 -p2 -b .readlink

%build
[ -d lslk_%{version} ] && cd lslk_%{version}
./Configure -n linux
make CFGF="-DLINUXV=21131" CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf ${RPM_BUILD_ROOT}

mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8

[ -d lslk_%{version} ] && cd lslk_%{version}
install -m 755 lslk ${RPM_BUILD_ROOT}%{_sbindir}
install lslk.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
# XXX should be mode 4755, but for now leave the setuid off
%attr(0755,root,kmem) %{_sbindir}/lslk
%{_mandir}/man*/*

%changelog
* Thu Jan  7 2010 Karel Zak <kzak@redhat.com> - 1.29-23
- remove obsolete URL to usptream tarball

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.29-22.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.29-20
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.29-19
- Autorebuild for GCC 4.3

* Thu Apr 12 2007 Karel Zak <kzak@redhat.com> 1.29-18
- fix according to rmplint

* Wed Jul 19 2006 Karel Zak <kzak@redhat.com> 1.29-17
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.29-16.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.29-16.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.29-16.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 21 2005 Karel Zak <kzak@redhat.com> 1.29-16
- rebuilt

* Fri Mar  4 2005 Jindrich Novy <jnovy@redhat.com> 1.29-15
- rebuilt with gcc4

* Wed Feb 10 2005 Jindrich Novy <jnovy@redhat.com> 1.29-14
- remove -D_FORTIFY_SOURCE=2 from CFLAGS, present in RPM_OPT_FLAGS

* Wed Feb  9 2005 Jindrich Novy <jnovy@redhat.com> 1.29-13
- add -D_FORTIFY_SOURCE=2 to CFLAGS

* Fri Sep 10 2004 Jindrich Novy <jnovy@redhat.com>
- fixed segfault #60866 - readlink patch

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.29-7
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Than Ngo <than@redhat.com> 1.29-5
- don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 1.29-3
- rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Dec 19 2001 Than Ngo <than@redhat.com> 1.28-2
- update to 1.29
- it displays list local locks correct (bug #56611)
- Copyright->License

* Mon May 07 2001 Than Ngo <than@redhat.com>
- update to 1.28
- use RPM_OPT_FLAGS

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed Jun 14 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Wed Dec 22 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.25.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- remove setgid kmem "just in case".

* Tue Nov 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.19.

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- create.
- leave the setuid root off.
