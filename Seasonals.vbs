Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")

Dim objShell
Set objShell = WScript.CreateObject("WScript.Shell")

CurrentDirectory = fso.GetAbsolutePathName("Y:\RatesProd\stathis_sheets\rjs\Sheets\")
Dim strXLSheet
strXLSheet = fso.BuildPath(CurrentDirectory,"Seasonals.xlsb")

Dim strHomeFolder, strLogFolder
strHomeFolder = objShell.ExpandEnvironmentStrings("%USERPROFILE%")
strLogFolder = strHomeFolder & "\Logs\"

if (fso.FolderExists(strLogFolder))=False Then
  fso.CreateFolder(strLogFolder)
end if

Set fso = Nothing

Dim Excel
Set Excel = CreateObject("Excel.Application")

'Loop through the addins and explicitly uninstall dlx
For Each objAddin In Excel.AddIns2
  strAN = objAddin.name
  if objAddin.name = "DLX.XLA" or objAddin.name = "Dlx" or objAddin.name = "dlx" then
    objAddin.installed = false
  end if
next

Excel.Application.Visible = True
Call Excel.WorkBooks.Open("C:\blp\API\Office Tools\BloombergUI.xla")
Call Excel.RegisterXLL("C:\Suite\ALib30build3_9-ss\Libs\Excel7\nt.msvc9\ifexcel32.xll")
Call Excel.RegisterXLL("C:\Suite\ALib30build3_9-ss\Libs\Excel7\nt.msvc9\swaps32.xll")
Call Excel.RegisterXLL("C:\Suite\ALib30build3_9-ss\Libs\Excel7\nt.msvc9\credit32.xll")
Call Excel.RegisterXLL("C:\Suite\ALib30build3_9-ss\Libs\Excel7\nt.msvc9\exotics32.xll")

Call Excel.Workbooks.Open("\\clndata01\shared\RatesProd\Sheets\Tools\McKeever_Models\MILLER\Barr\Barr.xlam")

Call Excel.WorkBooks.Open(strXLSheet , True, True)

'Call Excel.Workbooks.Open("\\clndata01\shared\RatesProd\Sheets\Tools\McKeever_Models\MILLER\Barr\Barr.xlam")

objShell.AppActivate(Excel.Name)

Set objShell = Nothing
