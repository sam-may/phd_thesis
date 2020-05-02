for fig in `ls -1 -d *.png`; do convert $fig -trim $fig; done
for fig in `ls -1 -d */*.png`; do convert $fig -trim $fig; done
