buster generate --domain="http://localhost:2369/" --dir="docs/"
sh deploy_after.sh
git add -A
git commit -a -m "Updated changes $(date +"%D %T")"
git push origin master
