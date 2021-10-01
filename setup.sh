echo "Removing old distribution files"
rm -rf ./build ./dist ./utils_S.egg-info

echo "Preparing to creat distribution"
py setup.py sdist

echo "Preparing to upload distribution"
twine upload -u TheSal -p gaU7WQp4q7srwQG  dist/*

echo "Upload Completed"

