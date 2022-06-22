shopt -s expand_aliases

alias yo='find . -type f -name "*.py" | wc -l'

alias completion_rate='expr $(expr $(yo) \*  100) / 150'

alias progress_bar='echo "![Progress](https:\/\/progress-bar.dev\/$(completion_rate)\/)"'

sed -i "5s/.*/$(progress_bar)/" README.md
