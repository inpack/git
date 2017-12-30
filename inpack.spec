[project]
name = git
version = 2.15.1
vendor = git-scm.com
homepage = https://git-scm.com
groups = app/dev
description = distributed version control system


%build
PREFIX="{{.project__prefix}}"

cd {{.inpack__pack_dir}}/deps

if [ ! -f "git-{{.project__version}}.tar.gz" ]; then
    wget "https://www.kernel.org/pub/software/scm/git/git-2.15.1.tar.gz"
fi
if [ ! -d "git-{{.project__version}}" ]; then
    tar -zxf git-{{.project__version}}.tar.gz
fi

cd git-{{.project__version}}

./configure --prefix=/home/action/apps/git

make -j4

mkdir {{.inpack__pack_dir}}/make_install_temp

make install DESTDIR={{.inpack__pack_dir}}/make_install_temp

mkdir -p {{.buildroot}}/bin
install {{.inpack__pack_dir}}/make_install_temp/home/action/apps/git/bin/git {{.buildroot}}/bin/git
install {{.inpack__pack_dir}}/make_install_temp/home/action/apps/git/bin/git-receive-pack {{.buildroot}}/bin/git-receive-pack
install {{.inpack__pack_dir}}/make_install_temp/home/action/apps/git/bin/git-shell {{.buildroot}}/bin/git-shell
install {{.inpack__pack_dir}}/make_install_temp/home/action/apps/git/bin/git-upload-archive {{.buildroot}}/bin/git-upload-archive
install {{.inpack__pack_dir}}/make_install_temp/home/action/apps/git/bin/git-upload-pack {{.buildroot}}/bin/git-upload-pack

strip -s {{.buildroot}}/bin/git
strip -s {{.buildroot}}/bin/git-receive-pack
strip -s {{.buildroot}}/bin/git-shell
strip -s {{.buildroot}}/bin/git-upload-archive
strip -s {{.buildroot}}/bin/git-upload-pack


install {{.inpack__pack_dir}}/misc/init.sh {{.buildroot}}/init.sh

mkdir -p {{.buildroot}}/share/git-core/templates
rsync -av {{.inpack__pack_dir}}/make_install_temp/home/action/apps/git/share/git-core/templates/* {{.buildroot}}/share/git-core/templates/

rm -rf {{.inpack__pack_dir}}/make_install_temp

cd {{.inpack__pack_dir}}/deps
rm -rf git-{{.project__version}}

%files

