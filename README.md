## Move Windows 11 Start Menu to the Left and Enable Dark Theme

```powershell
# Enable dark theme for apps
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" -Name "AppsUseLightTheme" -Value 0

# Move Windows 11 taskbar (Start menu) to the left
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name "TaskbarAl" -Value 0

# (Optional) Restart Explorer to apply changes immediately
Stop-Process -Name explorer -Force
```

**Instructions:**
- Run the above commands in powershell_ise
---
