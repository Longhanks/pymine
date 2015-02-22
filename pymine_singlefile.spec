# -*- mode: python -*-
#pyinstaller pymine_singlefile.spec [-y] [--clean]

a = Analysis(['pymine.py'],
             pathex=['.'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

ui = Tree('ui', 'ui')

resources = Tree('resources', 'resources', excludes=['*.pyc'])

pyz = PYZ(a.pure)

exe = EXE(pyz,
          ui,
          resources,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Pymine.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
