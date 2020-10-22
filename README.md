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

## Install in a venv
Download and run bash script
[`make-cds-wrap-venv`](https://github.com/gregorydulin/cds-wrap/blob/gmd-update-readme/make-cds-wrap-venv)

This will create a folder `cds-wrap-venv` in the current directory

## Create package
```
# linux
./cds-wrap-venv/bin/cds-wrap file [file...]

# windows, e.g. git bash
./cds-wrap-venv/Scripts/cds-wrap file [file...]
```

## Reconstruct files from package
(i.e. on the other side of the CDS)

Run the file through a quoted-printable decoder (produces .tar file)
`tar -xf <file>`

TODO: add this functionality natively
