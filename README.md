# 자주 찾아보는 것들 정리

### prevent master commit & merge & push
- link: https://stackoverflow.com/questions/40462111/git-prevent-commits-in-master-branch

1. .git/hooks/pre-commit
```bash
#!/bin/sh
branch="$(git rev-parse --abbrev-ref HEAD)"

if [ "$branch" = "master" ]; then
  echo "You can't commit directly to master branch"
  exit 1
fi
```

2. .git/config
```bash
[branch "master"]
    mergeoptions = --no-ff
```

3. .git/hooks/pre-push
```
#!/bin/bash
protected_branch='master'
current_branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')

if [ $protected_branch = $current_branch ]
then
    read -p "You're about to push master, is that what you intended? [y|n] " -n 1 -r < /dev/tty
    echo
    if echo $REPLY | grep -E '^[Yy]$' > /dev/null
    then
        exit 0 # push will execute
    fi
    exit 1 # push will not execute
else
    exit 0 # push will execute
fi
```

4. Make it executable
```bash
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-push
```
