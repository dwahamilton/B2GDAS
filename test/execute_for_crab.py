import sys
import PSet
files = []
outfile = file( 'filesToProcess.txt', 'w')
for ifile in PSet.process.source.fileNames :    
    outfile.write( ifile + '\n' )


outfile.close()

sys.argv.append('--files')
sys.argv.append('filesToProcess.txt')

print sys.argv

from b2gdas_fwlite import b2gdas_fwlite

b2gdas_fwlite(sys.argv)

