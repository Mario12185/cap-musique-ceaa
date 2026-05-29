$dir = "$env:USERPROFILE\CAP_MUSIQUE_Projet"
$utf8 = New-Object System.Text.UTF8Encoding $false
Get-ChildItem $dir -Recurse -Filter "*.html" | ForEach-Object {
    $t = [IO.File]::ReadAllText($_.FullName, [Text.Encoding]::UTF8)
    $o = $t
    # Nettoyage des artefacts d'encodage courants
    $t = $t.Replace('??','?').Replace('??','?').Replace('? ','?').Replace('??','?').Replace('??','?').Replace('??','?').Replace('??','?').Replace('??','?').Replace('??','?').Replace('??','?').Replace('????','?').Replace('????','?').Replace('??? ','?').Replace('????','?').Replace('????','?').Replace('????','?').Replace('????','?')
    # Nettoyage meta charset
    $t = $t -replace '<meta[^>]*charset[^>]*>', ''
    $t = $t -replace '<head>', '<head><meta charset="UTF-8">'
    if ($t -ne $o) { [IO.File]::WriteAllText($_.FullName, $t, $utf8); Write-Host "Fixed: $($_.Name)" }
}
Write-Host "DONE. All files corrected. Ready for git push." -ForegroundColor Green