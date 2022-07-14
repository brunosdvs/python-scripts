# COPIANDO CONTEÚDO DE UM ARQUIVO PARA OUTRO

outfile = 'diretorio'
infile = 'diretorio'

# Método 1  
with open(outfile,'r') as outfile:
        text = outfile.read()
        with open(infile, 'w') as infile:
            infile.write(text)
            
# Método 2
open(infile,'w').write(open(outfile,'r').read()) 