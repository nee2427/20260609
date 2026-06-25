const { app, BrowserWindow, dialog } = require('electron')
const path = require('path')

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    minWidth: 900,
    minHeight: 600,
    title: '配課系統',
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false
    }
  })

  win.loadFile(path.join(__dirname, 'allocation.html'))
  win.on('page-title-updated', e => e.preventDefault())
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => app.quit())
