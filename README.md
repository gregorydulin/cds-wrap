# cds-wrap
Wraps arbitrary files/folders into a package for transfer across a Cross-Domain
Solution (CDS)

The goal of this project is to make as much text as possible readable by both
humans and automated processes looking for security labels and/or "dirty 
words".  To that end, we use
[Quoted-Printable](https://en.wikipedia.org/wiki/Quoted-printable) encoding,
rather than, e.g., base64.

In it's current state, only text that is stored in the original file as native
ASCII or UTF-8 will be readable.  Later, we hope to extract text from common
files for plain-text audit.  Eventually, we'd like to perform OCR on images as
well.

## Quick Start (Linux)

### Install

#### Install in a venv
Download and run bash script
[`make-cds-wrap-venv`](./make-cds-wrap-venv)

This will create a folder `cds-wrap-venv` in the current directory

#### Install system-wide (Linux)
* Clone this repo
* execute `install` with root privileges (e.g. `sudo install`)

### Create package
```
# linux
./cds-wrap-venv/bin/cds-wrap file [file...]

# windows, e.g. git bash
./cds-wrap-venv/Scripts/cds-wrap file [file...]
```

### Reconstruct files from package
(i.e. on the other side of the CDS)

If cds-wrap is unavailable:
* Run the file through a quoted-printable decoder (produces .tar file)
  * `cat <cds-wrap package> | perl -MMIME::QuotedPrint=decode_qp -e 'print decode_qp join "",<>' > package.tar`
* Untar the tar file
  * `tar -xf package.tar`

If cds-wrap is available:
* `cds-wrap --unwrap <cds-wrap package>`

## "Quick" Start (Windows)
All commands should be run in PowerShell
* Click the "Windows" button in the lower-left corner
* Type "PowerShell"
* Click "Windows PowerShell"

### Install Dependencies

* Install Python
```
Invoke-WebRequest `
  -Uri https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe `
  -OutFile python-3.9.5-amd64.exe

.\python-3.9.5-amd64.exe /passive PrependPath=1
```

* Install Git for Windows (Git bash)
```
Invoke-WebRequest `
  -Uri https://github.com/git-for-windows/git/releases/download/v2.31.1.windows.1/Git-2.31.1-64-bit.exe `
  -OutFile Git-2.31.1-64-bit.exe

@'
[Setup]
Lang=default
Dir=C:\Program Files\Git
Group=Git
NoIcons=0
SetupType=default
Components=ext,ext\shellhere,ext\guihere,gitlfs,assoc,assoc_sh,autoupdate
Tasks=
EditorOption=VIM
CustomEditorPath=
DefaultBranchOption= 
PathOption=Cmd
SSHOption=OpenSSH
TortoiseOption=false
CURLOption=WinSSL
CRLFOption=CRLFCommitAsIs
BashTerminalOption=MinTTY
GitPullBehaviorOption=FFOnly
UseCredentialManager=Core
PerformanceTweaksFSCache=Enabled
EnableSymlinks=Enabled
EnablePseudoConsoleSupport=Enabled
'@ > gitforwindows.inf

./Git-2.31.1-64-bit.exe /SILENT /LOADINF=gitforwindows.inf
```

