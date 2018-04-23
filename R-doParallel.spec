#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-doParallel
Version  : 1.0.11
Release  : 4
URL      : https://cran.r-project.org/src/contrib/doParallel_1.0.11.tar.gz
Source0  : https://cran.r-project.org/src/contrib/doParallel_1.0.11.tar.gz
Summary  : Foreach Parallel Adaptor for the 'parallel' Package
Group    : Development/Tools
License  : GPL-2.0
Requires: R-RUnit
Requires: R-foreach
Requires: R-iterators
BuildRequires : R-RUnit
BuildRequires : R-foreach
BuildRequires : R-iterators
BuildRequires : clr-R-helpers

%description
the parallel package.

%prep
%setup -q -c -n doParallel

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523302773

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523302773
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doParallel
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doParallel
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doParallel
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library doParallel|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/doParallel/DESCRIPTION
/usr/lib64/R/library/doParallel/INDEX
/usr/lib64/R/library/doParallel/Meta/Rd.rds
/usr/lib64/R/library/doParallel/Meta/demo.rds
/usr/lib64/R/library/doParallel/Meta/features.rds
/usr/lib64/R/library/doParallel/Meta/hsearch.rds
/usr/lib64/R/library/doParallel/Meta/links.rds
/usr/lib64/R/library/doParallel/Meta/nsInfo.rds
/usr/lib64/R/library/doParallel/Meta/package.rds
/usr/lib64/R/library/doParallel/Meta/vignette.rds
/usr/lib64/R/library/doParallel/NAMESPACE
/usr/lib64/R/library/doParallel/NEWS
/usr/lib64/R/library/doParallel/R/doParallel
/usr/lib64/R/library/doParallel/R/doParallel.rdb
/usr/lib64/R/library/doParallel/R/doParallel.rdx
/usr/lib64/R/library/doParallel/demo/sincParallel.R
/usr/lib64/R/library/doParallel/doc/gettingstartedParallel.R
/usr/lib64/R/library/doParallel/doc/gettingstartedParallel.Rnw
/usr/lib64/R/library/doParallel/doc/gettingstartedParallel.pdf
/usr/lib64/R/library/doParallel/doc/index.html
/usr/lib64/R/library/doParallel/examples/bootParallel.R
/usr/lib64/R/library/doParallel/help/AnIndex
/usr/lib64/R/library/doParallel/help/aliases.rds
/usr/lib64/R/library/doParallel/help/doParallel.rdb
/usr/lib64/R/library/doParallel/help/doParallel.rdx
/usr/lib64/R/library/doParallel/help/paths.rds
/usr/lib64/R/library/doParallel/html/00Index.html
/usr/lib64/R/library/doParallel/html/R.css
/usr/lib64/R/library/doParallel/unitTests/options.R
/usr/lib64/R/library/doParallel/unitTests/report.html
/usr/lib64/R/library/doParallel/unitTests/report.txt
/usr/lib64/R/library/doParallel/unitTests/reportSummary.txt
/usr/lib64/R/library/doParallel/unitTests/runTestSuite.sh
