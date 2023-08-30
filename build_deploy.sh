rm -r dist ;
python --version
python setup.py sdist bdist_wheel ;
python setup.py install;
if twine check dist/* ; then
  if [ "$1" = "--test" ] ; then
    twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
  else
    twine upload dist/* ;
  fi
fi