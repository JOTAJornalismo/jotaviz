rm -r dist ;
python3 --version
python3 setup.py sdist bdist_wheel ;
python3 setup.py install;
if twine check dist/* ; then
  if [ "$1" = "--test" ] ; then
    twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
  else
    twine upload dist/* ;
  fi
fi