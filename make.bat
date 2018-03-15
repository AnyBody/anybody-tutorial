@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=python -msphinx
)
set SOURCEDIR=.
set BUILDDIR=_build
set SPHINXPROJ=AnyBodyTutorials

if "%1" == "" goto help

if "%1" == "html-da" goto da

if "%1" == "html-ja" goto ja

if "%1" == "clean" goto clean


%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The Sphinx module was not found. Make sure you have Sphinx installed,
	echo.then set the SPHINXBUILD environment variable to point to the full
	echo.path of the 'sphinx-build' executable. Alternatively you may add the
	echo.Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% -n %SPHINXOPTS% 
goto end

:da
%SPHINXBUILD% -M html %SOURCEDIR% _build_da -D language=da
goto end

:ja
%SPHINXBUILD% -M html %SOURCEDIR% _build_ja -D language=ja
goto end

:clean
%SPHINXBUILD% -M %1 %SOURCEDIR% _build %SPHINXOPTS%
%SPHINXBUILD% -M %1 %SOURCEDIR% _build_ja %SPHINXOPTS%
%SPHINXBUILD% -M %1 %SOURCEDIR% _build_da %SPHINXOPTS%
goto end

goto end



:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

:end
popd
