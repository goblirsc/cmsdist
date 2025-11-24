### RPM external millepede V04-18-00
## INCLUDE cpp-standard
## INCLUDE microarch_flags
## INCLUDE compilation_flags

Source: https://gitlab.desy.de/millepede/millepede-ii/-/archive/%{realversion}/%{n}-ii-%{realversion}.tar.gz
BuildRequires: cmake
Requires: zlib OpenBLAS root

%prep
%setup -n %{n}-ii-%{realversion}
sed -i "s;openblasp64;openblas;g" CMakeLists.txt

%build

%build
rm -rf build
mkdir build
cd build
cmake \
  -DCMAKE_CXX_STANDARD=%{cms_cxx_standard} \
  -DCMAKE_INSTALL_PREFIX="%{i}" \
  -DCMAKE_C_COMPILER=gcc \
  -DCMAKE_CXX_COMPILER=g++ \
  -DCMAKE_Fortran_COMPILER=gfortran \
  -DCMAKE_LINKER=ld \
  -DLAPACK_OPENBLAS=on \
  ../ 
make 

%install
cd build
make install PREFIX=%{i}

