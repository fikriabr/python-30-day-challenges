# Step-by-step Python installation using pyenv

## 1. Install pyenv using Homebrew
```sh
brew install pyenv
```

## 2. Install Python version 3.13.5 using pyenv
```sh
pyenv install 3.13.5
```

## 3. Set Python 3.13.5 as the global version
```sh
pyenv global 3.13.5
```

## 4. Update your shell configuration (.zshrc) for pyenv
```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

## 5. Reload your shell configuration
```sh
source ~/.zshrc
```

## 6. Verify your Python installation
```sh
python --version
python3 --version
```

## 7. Run Hello World file
```sh
python helloworld.py
```

### Output
```
Hello, World!
```