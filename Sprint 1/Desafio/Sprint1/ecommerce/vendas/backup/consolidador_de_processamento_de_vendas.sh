#!/bin/bash

awk 'NR>0' relatorio20241022.txt >  relatorio_final.txt
echo "=========================================================================" >> relatorio_final.txt
awk 'NR>0' relatorio20241023.txt >> relatorio_final.txt
echo "=========================================================================" >> relatorio_final.txt
awk 'NR>0' relatorio20241024.txt >> relatorio_final.txt
echo "=========================================================================" >> relatorio_final.txt
awk 'NR>0' relatorio20241025.txt >> relatorio_final.txt
echo "=========================================================================" >> relatorio_final.txt
awk 'NR>0' relatorio20241026.txt >> relatorio_final.txt

