shopt -s expand_aliases

alias yo='find . -type f -name "*.py" | wc -l'

alias completion_rate='rate=$(expr $(expr $(yo) \*  100) / 150); if [ "$rate" -gt 100 ]; then echo 100; else echo "$rate"; fi'

alias progress_bar='echo "![Progress](https:\/\/geps.dev\/progress\/$(completion_rate)\/)"'


if [[ "$OSTYPE" == "darwin"* ]]; then
  sed -i '' "5s/.*/$(progress_bar)/" README.md
else
  sed -i "5s/.*/$(progress_bar)/" README.md
fi