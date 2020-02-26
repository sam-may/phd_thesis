pdflatex template

if [[ $1 == 'l' ]]
then
  pdflatex template
  bibtex template
  pdflatex template
  pdflatex template 
else
  echo "Bibliography not updated"
fi
