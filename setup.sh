rm -rf ./build ./dist ./utils_S.egg-info
py setup.py sdist
twine upload -u TheSal -p gaU7WQp4q7srwQG  dist/*

