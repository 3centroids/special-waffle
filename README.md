# local-test

Portable local testing software and test case generator written in Python for competitive programming in C++.
Aims to use only standard library.

## Platform support

Unix-like (e.g. macOS, Linux) uses bash and Windows uses Command Prompt.

| platform | Unix-like | Windows |
|:---:|:---:|:---:|
| support | :heavy_check_mark: | :heavy_check_mark: |
| shell | bash | cmd |

## Usage

It's recommended to add local-test directory to PATH.

```
usage: lt.py [-h] -p PROGRAM [-c]

optional arguments:
  -h, --help            show this help message and exit
  -p PROGRAM, --program PROGRAM
                        program pathname
  -c, --compile         compile program (default=False)
```

### Windows
```python %lt%\lt.py -p bar.cpp -c```\
Unless local-test directory is an environment variable ("lt"), replace "%lt%\lt.py" with its pathname.
System Properties > Environment Variables > System variables > New

### Unix-like
```python3 $LT/lt.py -p bar.cpp -c```\
You'll probably also want to setup an environment variable for your local-test directory.
In bash type ```export VARIABLE_NAME=value``` with proper VARIABLE_NAME and value.

### Writing test cases

> **IMPORTANT**
> Make sure to have matching newlines, otherwise correct output might flag your program as defective. Example below.

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

> **WARNING**
> Specified compiler will be used in shell.

### Keys

```json
"platform": ["Unix", "Windows"]
"compiler": ("clang++", "clang", "g++", "gcc", etc.)
"generator-prefix": ("gen", "g", etc.)
```

## TODO

[Known issues and future improvements](docs/TODO.md)

## Contributing

[Contribution guidelines for this project](docs/CONTRIBUTING.md)