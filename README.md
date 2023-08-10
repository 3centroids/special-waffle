# local-test

Portable local testing software and test case generator written in Python for competitive programming in C++.
Aims to use only standard library.

## Platform support

Unix-like (e.g. macOS, Linux) uses bash and Windows uses cmd.

| platform | Unix-like | Windows |
|:---:|:---:|:---:|
| support | :heavy_check_mark: | :heavy_check_mark: |
| shell | bash | cmd |

[!NOTE]
Colorful output may not work on Windows Command Prompt (but it does in Visual Studio Code and Windows Terminal).

## Usage

It's recommended to add local-test directory to PATH.

```python lt.py -h```
```
usage: lt.py [-h] -p PROGRAM [-c]

optional arguments:
  -h, --help            show this help message and exit
  -p PROGRAM, --program PROGRAM
                        program pathname
  -c, --compile         compile program (default=False)
```

Example usage: ```python lt.py -p bar.cpp -c```\
Unless local-test directory is added to PATH, replace "lt.py" with its pathname. On Unix-like systems do ```python3``` instead of ```python``` in the above command.

### Writing test cases

[!IMPORTANT]
Make sure to have matching newlines, otherwise correct output might flag your program as defective. Example below.

```bar.cpp```
```cpp
#include <cstdio>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", n);
}
```

^ Newline character present

```0.in```
```
66

```

^ Would work without newline

```0.out```
```
66

```

^ Newline present

## Why Python?

[SIO2](https://github.com/sio2project) (used by [POI](https://oi.edu.pl) ([POI's SIO2 link](https://sio2.mimuw.edu.pl/))) itself is partially written in Python. Honestly, I found joy writing Python for a change.
BTW check out similar testing program written in bash shell ([link](https://example.com)).

## Configuration - ```config.json```

### Decyphering what the author meant

[] - value must be one of the options provided\
() - literally anything

[!WARNING]
Specified compiler will be used in shell.

### Keys

"platform": ["Unix", "Windows"]\
"compiler": ("clang++", "clang", "g++", "gcc", etc.)\
"generator-prefix": ("gen", "g", etc.)

## TODO

[Known issues and future improvements](docs/TODO.md)

## Contributing

[Contribution guidelines for this project](docs/CONTRIBUTING.md)