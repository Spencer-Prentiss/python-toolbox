#region Script Info

#	File name:		merge-media.py
#	Description:	Python script to combine .ts and .aac files into .mp4 files.
#					Requires ffmpeg executable to handle the merger.

#	Author:			Spencer Prentiss

#endregion


#region Includes

from os import getcwd, system
from os.path import basename, dirname, exists, splitext
from glob import glob

#endregion

#region Defines

def clear(): system('cls')

#endregion

#region Variables

ffmpeg: str = getcwd() + '\\ffmpeg.exe'		#	Script requires ffmpeg to merge .ts and .aac files, needs to be downloaded separately
mediaGlob: str = getcwd() + '\**'
tsExt: str = '.ts'
aacExt: str = '.aac'
mp4Ext: str = '.mp4'

#endregion


#region Main Function

def Main():
	'''
	Main call for script work
	'''
	
	clear()
	if exists(ffmpeg):
		files = [f for f in glob(mediaGlob, recursive=True) if f.lower().endswith('.ts')]
		for f in files:
			parent: str = dirname(f)
			fileName: str = basename(f)
			tsFile: str = f
			title: str = splitext(fileName)[0].replace(' - ', ': ').replace('- ', ': ').replace('--', '/')
			if title.endswith('_'):
				title = title[:len(title) - 1] + '?'
			aacFile: str = parent + '\\' + fileName.replace(tsExt, aacExt)
			mp4File: str = parent + '\\' + fileName.replace(tsExt, mp4Ext).replace('--', '-')
			options: str = "-i \"{0}\" -i \"{1}\" -metadata title=\"{2}\" -c:v copy -c:a copy \"{3}\"".format(tsFile, aacFile, title, mp4File)
			if exists(aacFile) and not exists(mp4File):
				system("{0} {1}".format(ffmpeg, options))
	else:
		print('"ffmpeg.exe" missing, script cannot continue')

#endregion

#region Main Call and Exit

Main()
exit(0)

#endregion