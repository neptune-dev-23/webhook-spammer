if (-not (Get-Command python.exe -ErrorAction SilentlyContinue)) {
    # If not, download and install Python
    $url = "https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe"
    $outfile = "$PWD\python_installer.exe"
    Invoke-WebRequest -Uri $url -OutFile $outfile
    Start-Process -Wait $outfile -ArgumentList "/quiet", "TargetDir=$PWD\Python"
}


$folder = './venv'
"Test to see if $folder exists"
if (-not (Test-Path -Path $folder -PathType Container)) {
	& virtualenv venv
}


& "$PWD\venv\Scripts\Activate.ps1"
& python -m pip install -r requirements.txt
