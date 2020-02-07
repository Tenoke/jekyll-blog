JEKYLL_ENV=production jekyll build
python3.7 -m http.server -d ../_site/ &
python3.7 add_images.py
cd ..
cp -rn _site/static/previews/* static/previews/
git add .	
git commit -m "$1"
git push
cp -ru _site/* ../Tenoke.github.io/
cd ../Tenoke.github.io/
git add .
git commit -m "$1"
git push 
cd ../jekyll-blog
pkill -9 python3.7